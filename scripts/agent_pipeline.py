#!/usr/bin/env python3
"""Validate and evaluate the scene-first agent assets.

This script is intentionally read-only by default. It checks whether the current
raw corpus and graph outputs are usable by the Learnable Agent runtime layer.
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.evaluate_scene_matcher import DEFAULT_AMBIGUOUS_EVAL_PATH, DEFAULT_EVAL_PATH, DEFAULT_REALISTIC_EVAL_PATH, evaluate_suite
from scripts.recommender.graph_loader import DEFAULT_GRAPH_PATH, SceneGraph
from scripts.recommender.learning_loop import PersonalizationMemory, build_feedback_event
from scripts.recommender.personalization import FeedbackEvent
from scripts.recommender.source_bridge import DEFAULT_SOURCE_GRAPH_PATH, SourceRecommenderBridge
from edit_master.raw_harness import MIN_ALIASES, REQUIRED_BODY_MARKERS, list_value, parse_frontmatter


REQUIRED_SCENARIO_KEYS = ("scenario_tags", "aliases", "graph_nodes", "graph_edges", "urls")


def validate_raw() -> dict:
    scenario_files = sorted((REPO_ROOT / "raw" / "scenarios").glob("*.md"))
    missing_required: dict[str, list[str]] = {}
    missing_aliases: list[str] = []
    for path in scenario_files:
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        missing = [key for key in REQUIRED_SCENARIO_KEYS if not list_value(meta, key)]
        missing.extend(marker for marker in REQUIRED_BODY_MARKERS if marker not in body)
        if missing:
            missing_required[str(path.relative_to(REPO_ROOT))] = missing
        if len(list_value(meta, "aliases")) < MIN_ALIASES:
            missing_aliases.append(str(path.relative_to(REPO_ROOT)))

    raw_files = sorted((REPO_ROOT / "raw").rglob("*.md"))
    raw_without_urls = []
    for path in raw_files:
        rel_path = path.relative_to(REPO_ROOT)
        rel = str(rel_path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        if rel_path.parts[1] in {"recommendation", "manifests"} or rel_path.name == "README.md":
            continue
        if "http://" not in text and "https://" not in text:
            raw_without_urls.append(rel)

    return {
        "scenario_count": len(scenario_files),
        "missing_required": missing_required,
        "missing_aliases": missing_aliases,
        "raw_without_urls": raw_without_urls,
        "ok": not missing_required and not raw_without_urls,
    }


def validate_graph(graph_path: Path = DEFAULT_GRAPH_PATH, expected_scenario_count: int | None = None) -> dict:
    graph = SceneGraph.load(graph_path)
    degree: dict[str, int] = {node_id: 0 for node_id in graph.nodes}
    for edge in graph.edges:
        degree[edge.source] = degree.get(edge.source, 0) + 1
        degree[edge.target] = degree.get(edge.target, 0) + 1
    isolates = [node_id for node_id, count in degree.items() if count == 0]
    scenarios = graph.scenarios()
    recommendations = [node for node in graph.nodes.values() if node.labels == ["Recommendation"]]
    rec_channels: dict[str, int] = {}
    for rec in recommendations:
        channel = str(rec.properties.get("channel", "unknown"))
        rec_channels[channel] = rec_channels.get(channel, 0) + 1

    recs_missing_evidence = []
    for rec in recommendations:
        if not any(edge.type == "SUPPORTED_BY" for edge in graph.outgoing.get(rec.id, [])):
            recs_missing_evidence.append(rec.id)

    scenario_count = len(scenarios)
    scenario_count_matches_raw = expected_scenario_count is None or scenario_count == expected_scenario_count
    channels_complete = all(rec_channels.get(channel, 0) == scenario_count for channel in ("trend", "general", "personalized"))

    return {
        "node_count": len(graph.nodes),
        "edge_count": len(graph.edges),
        "scenario_count": scenario_count,
        "expected_scenario_count": expected_scenario_count,
        "scenario_count_matches_raw": scenario_count_matches_raw,
        "recommendation_count": len(recommendations),
        "recommendation_channels": rec_channels,
        "recommendation_channels_complete": channels_complete,
        "isolates": isolates,
        "recommendations_missing_evidence": recs_missing_evidence,
        "ok": (
            scenario_count > 0
            and len(recommendations) > 0
            and not recs_missing_evidence
            and scenario_count_matches_raw
            and channels_complete
        ),
    }


def validate_bridge(graph_path: Path = DEFAULT_GRAPH_PATH, source_graph_path: Path = DEFAULT_SOURCE_GRAPH_PATH) -> dict:
    bridge = SourceRecommenderBridge.load(graph_path, source_graph_path)
    return bridge.validate()


def validate_learning_loop() -> dict:
    smoke_dir = REPO_ROOT / "data" / "personalization" / "_pipeline_smoke" / uuid.uuid4().hex
    memory = PersonalizationMemory(smoke_dir, "pipeline_smoke")
    event = FeedbackEvent(
        scenario_id="scenario_window_light_cafe_portrait",
        channel="personalized",
        rating=1.0,
        style_tags=["natural", "clean", "low_retouch"],
        issue_tags=["issue:busy_background"],
    )
    memory.record_feedback(event, action="accepted", query="cafe window portrait natural background cleanup")
    rejected = build_feedback_event(
        scenario_id="scenario_low_light_food_restaurant",
        channel="trend",
        action="rejected",
        style_tags=["cinematic", "strong_edit"],
    )
    memory.record_feedback(rejected, action="rejected", query="restaurant food cinematic strong edit")
    profile = memory.load_profile()
    hints = profile.parameter_hints()
    ok = (
        profile.event_count == 2
        and profile.channel_weights.get("personalized", 1.0) > 1.0
        and profile.channel_weights.get("trend", 1.0) < 1.0
        and profile.preferences.get("natural", 0.0) > 0.0
        and profile.preferences.get("cinematic", 0.0) < 0.0
        and bool(hints)
    )
    return {
        "ok": ok,
        "event_count": profile.event_count,
        "personalized_weight": profile.channel_weights.get("personalized", 1.0),
        "top_hints": hints[:3],
    }


DEFAULT_EVAL_THRESHOLDS = {
    "regression": {"top1": 1.0, "top3": 1.0, "match_top1": 1.0, "match_top3": 1.0},
    "realistic": {"match_top1": 0.85, "match_top3": 0.90, "gap_abstain": 0.60},
    "ambiguous": {"match_top1": 0.75, "match_top3": 0.85, "gap_abstain": 0.50},
}


def validate_matcher_eval(suite: dict, thresholds: dict[str, dict[str, float]]) -> dict:
    set_reports: dict[str, dict] = {}
    ok = True
    misses: list[dict] = []
    candidate_gaps: list[dict] = []
    for name, result in suite["sets"].items():
        threshold = thresholds.get(name, {})
        checks: dict[str, dict] = {}
        metric_map = {
            "top1": "top1_accuracy",
            "top3": "top3_accuracy",
            "match_top1": "match_top1_accuracy",
            "match_top3": "match_top3_accuracy",
            "gap_abstain": "gap_abstain_accuracy",
        }
        for threshold_key, metric_key in metric_map.items():
            if threshold_key not in threshold:
                continue
            value = result.get(metric_key)
            minimum = float(threshold[threshold_key])
            if value is None:
                passed = result.get("gap_total", 0) == 0 and threshold_key == "gap_abstain"
            else:
                passed = value >= minimum
            checks[threshold_key] = {"value": value, "min": minimum, "ok": passed}
        set_ok = all(item["ok"] for item in checks.values())
        ok = ok and set_ok
        set_reports[name] = {
            "total": result["total"],
            "top1_accuracy": result["top1_accuracy"],
            "top3_accuracy": result["top3_accuracy"],
            "match_total": result.get("match_total", result["total"]),
            "gap_total": result.get("gap_total", 0),
            "match_top1_accuracy": result.get("match_top1_accuracy", result["top1_accuracy"]),
            "match_top3_accuracy": result.get("match_top3_accuracy", result["top3_accuracy"]),
            "gap_abstain_accuracy": result.get("gap_abstain_accuracy"),
            "min_top1": threshold.get("top1"),
            "min_top3": threshold.get("top3"),
            "min_match_top1": threshold.get("match_top1"),
            "min_match_top3": threshold.get("match_top3"),
            "min_gap_abstain": threshold.get("gap_abstain"),
            "checks": checks,
            "ok": set_ok,
        }
        for row in result["rows"]:
            if row.get("candidate_scenario") or row.get("coverage_status") == "gap":
                candidate_gaps.append(
                    {
                        "set": name,
                        "id": row["id"],
                        "candidate_scenario": row.get("candidate_scenario"),
                        "expected": row["expected"],
                        "predicted": row["predicted"],
                        "top_score": row.get("top_score"),
                        "top_confidence": row.get("top_confidence"),
                        "coverage_status": row.get("coverage_status"),
                        "abstained": row.get("abstained"),
                        "score_gap": row.get("score_gap"),
                        "slot_coverage": row.get("slot_coverage"),
                        "unknown_concepts": row.get("unknown_concepts", []),
                    }
                )
            if not row["top1"]:
                misses.append(
                    {
                        "set": name,
                        "id": row["id"],
                        "expected": row["expected"],
                        "expected_behavior": row.get("expected_behavior", "match"),
                        "predicted": row["predicted"],
                        "top_score": row.get("top_score"),
                        "top_confidence": row.get("top_confidence"),
                        "coverage_status": row.get("coverage_status"),
                        "abstained": row.get("abstained"),
                        "score_gap": row.get("score_gap"),
                        "slot_coverage": row.get("slot_coverage"),
                        "unknown_concepts": row.get("unknown_concepts", []),
                        "max_top_score": row.get("max_top_score"),
                        "top3": row["top3"],
                    }
                )
    return {
        "ok": ok,
        "total": suite["total"],
        "top1_accuracy": suite["weighted_top1_accuracy"],
        "top3_accuracy": suite["weighted_top3_accuracy"],
        "weighted_top1_accuracy": suite["weighted_top1_accuracy"],
        "weighted_top3_accuracy": suite["weighted_top3_accuracy"],
        "weighted_match_top1_accuracy": suite.get("weighted_match_top1_accuracy", suite["weighted_top1_accuracy"]),
        "weighted_match_top3_accuracy": suite.get("weighted_match_top3_accuracy", suite["weighted_top3_accuracy"]),
        "weighted_gap_abstain_accuracy": suite.get("weighted_gap_abstain_accuracy"),
        "match_total": suite.get("match_total", suite["total"]),
        "gap_total": suite.get("gap_total", 0),
        "sets": set_reports,
        "misses": misses,
        "candidate_gaps": candidate_gaps,
    }


def run_pipeline(
    graph_path: Path,
    eval_path: Path | dict[str, Path],
    min_top1: float,
    source_graph_path: Path = DEFAULT_SOURCE_GRAPH_PATH,
    eval_thresholds: dict[str, dict[str, float]] | None = None,
) -> dict:
    raw = validate_raw()
    graph = validate_graph(graph_path, expected_scenario_count=raw["scenario_count"])
    bridge = validate_bridge(graph_path, source_graph_path)
    learning = validate_learning_loop()
    if isinstance(eval_path, dict):
        eval_paths = eval_path
    else:
        eval_paths = {
            "regression": eval_path,
            "realistic": DEFAULT_REALISTIC_EVAL_PATH,
            "ambiguous": DEFAULT_AMBIGUOUS_EVAL_PATH,
        }
    thresholds = dict(DEFAULT_EVAL_THRESHOLDS)
    thresholds["regression"] = {**thresholds["regression"], "top1": min_top1}
    if eval_thresholds:
        for name, values in eval_thresholds.items():
            thresholds[name] = {**thresholds.get(name, {}), **values}
    matcher_eval = validate_matcher_eval(evaluate_suite(eval_paths, graph_path, top_k=5), thresholds)
    ok = raw["ok"] and graph["ok"] and bridge["ok"] and learning["ok"] and matcher_eval["ok"]
    return {
        "ok": ok,
        "raw": raw,
        "graph": graph,
        "bridge": bridge,
        "learning_loop": learning,
        "matcher_eval": matcher_eval,
    }


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Validate and evaluate Learnable Agent assets.")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--source-graph", type=Path, default=DEFAULT_SOURCE_GRAPH_PATH)
    parser.add_argument("--eval", type=Path, default=DEFAULT_EVAL_PATH)
    parser.add_argument("--eval-realistic", type=Path, default=DEFAULT_REALISTIC_EVAL_PATH)
    parser.add_argument("--eval-ambiguous", type=Path, default=DEFAULT_AMBIGUOUS_EVAL_PATH)
    parser.add_argument("--min-top1", type=float, default=0.8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    report = run_pipeline(
        args.graph,
        {"regression": args.eval, "realistic": args.eval_realistic, "ambiguous": args.eval_ambiguous},
        args.min_top1,
        args.source_graph,
    )
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"ok: {report['ok']}")
        print(f"raw scenarios: {report['raw']['scenario_count']}")
        print(f"raw missing required: {len(report['raw']['missing_required'])}")
        print(f"raw missing aliases: {len(report['raw']['missing_aliases'])}")
        print(f"graph nodes/edges: {report['graph']['node_count']} / {report['graph']['edge_count']}")
        if not report["graph"].get("scenario_count_matches_raw", True):
            print(
                "graph/raw scenario mismatch: "
                f"{report['graph']['scenario_count']} / {report['graph'].get('expected_scenario_count')}"
            )
        print(f"graph recommendations: {report['graph']['recommendation_count']} {report['graph']['recommendation_channels']}")
        if not report["graph"].get("recommendation_channels_complete", True):
            print("graph recommendation channels incomplete")
        print(f"graph isolates: {len(report['graph']['isolates'])}")
        print(
            "bridge coverage: "
            f"{report['bridge']['linked_scenario_count']} / {report['bridge']['scenario_count']} "
            f"(external evidence: {report['bridge']['external_evidence_count']})"
        )
        print(
            "learning loop: "
            f"events={report['learning_loop']['event_count']} "
            f"personalized_weight={report['learning_loop']['personalized_weight']:.3f}"
        )
        print(
            "matcher weighted top1/top3: "
            f"{report['matcher_eval']['weighted_top1_accuracy']:.3f} / "
            f"{report['matcher_eval']['weighted_top3_accuracy']:.3f}"
        )
        gap_value = report["matcher_eval"].get("weighted_gap_abstain_accuracy")
        gap_text = "n/a" if gap_value is None else f"{gap_value:.3f}"
        print(
            "matcher match-only top1/top3: "
            f"{report['matcher_eval']['weighted_match_top1_accuracy']:.3f} / "
            f"{report['matcher_eval']['weighted_match_top3_accuracy']:.3f}"
        )
        print(f"matcher gap abstain: {gap_text}")
        for name, result in report["matcher_eval"]["sets"].items():
            gap_value = result.get("gap_abstain_accuracy")
            gap_text = "n/a" if gap_value is None else f"{gap_value:.3f}"
            print(
                f"matcher {name} top1/top3: {result['top1_accuracy']:.3f} / {result['top3_accuracy']:.3f} "
                f"(match {result.get('match_top1_accuracy', result['top1_accuracy']):.3f}/"
                f"{result.get('match_top3_accuracy', result['top3_accuracy']):.3f}, gap {gap_text})"
            )
        if report["matcher_eval"]["misses"]:
            print("matcher misses:")
            for miss in report["matcher_eval"]["misses"]:
                print(
                    f"  - [{miss['set']}] {miss['id']}: expected={miss['expected']} "
                    f"predicted={miss['predicted']} confidence={miss.get('top_confidence')} "
                    f"status={miss.get('coverage_status')}"
                )
        if report["matcher_eval"].get("candidate_gaps"):
            print("candidate gaps:")
            for gap in report["matcher_eval"]["candidate_gaps"]:
                print(
                    f"  - [{gap['set']}] {gap['id']}: candidate={gap.get('candidate_scenario')} "
                    f"predicted={gap['predicted']} confidence={gap.get('top_confidence')} "
                    f"status={gap.get('coverage_status')}"
                )

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
