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

from scripts.evaluate_scene_matcher import DEFAULT_EVAL_PATH, evaluate
from scripts.recommender.graph_loader import DEFAULT_GRAPH_PATH, SceneGraph
from scripts.recommender.learning_loop import PersonalizationMemory, build_feedback_event
from scripts.recommender.personalization import FeedbackEvent
from scripts.recommender.source_bridge import DEFAULT_SOURCE_GRAPH_PATH, SourceRecommenderBridge


REQUIRED_SCENARIO_KEYS = ("scenario_tags:", "graph_nodes:", "graph_edges:", "urls:")


def validate_raw() -> dict:
    scenario_files = sorted((REPO_ROOT / "raw" / "scenarios").glob("*.md"))
    missing_required: dict[str, list[str]] = {}
    missing_aliases: list[str] = []
    for path in scenario_files:
        text = path.read_text(encoding="utf-8")
        missing = [key.rstrip(":") for key in REQUIRED_SCENARIO_KEYS if key not in text]
        if missing:
            missing_required[str(path.relative_to(REPO_ROOT))] = missing
        if "aliases:" not in text:
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


def validate_graph(graph_path: Path = DEFAULT_GRAPH_PATH) -> dict:
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

    return {
        "node_count": len(graph.nodes),
        "edge_count": len(graph.edges),
        "scenario_count": len(scenarios),
        "recommendation_count": len(recommendations),
        "recommendation_channels": rec_channels,
        "isolates": isolates,
        "recommendations_missing_evidence": recs_missing_evidence,
        "ok": len(scenarios) > 0 and len(recommendations) > 0 and not recs_missing_evidence,
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


def run_pipeline(graph_path: Path, eval_path: Path, min_top1: float, source_graph_path: Path = DEFAULT_SOURCE_GRAPH_PATH) -> dict:
    raw = validate_raw()
    graph = validate_graph(graph_path)
    bridge = validate_bridge(graph_path, source_graph_path)
    learning = validate_learning_loop()
    matcher_eval = evaluate(eval_path, graph_path, top_k=5)
    ok = raw["ok"] and graph["ok"] and bridge["ok"] and learning["ok"] and matcher_eval["top1_accuracy"] >= min_top1
    return {
        "ok": ok,
        "raw": raw,
        "graph": graph,
        "bridge": bridge,
        "learning_loop": learning,
        "matcher_eval": {
            "total": matcher_eval["total"],
            "top1_accuracy": matcher_eval["top1_accuracy"],
            "top3_accuracy": matcher_eval["top3_accuracy"],
            "misses": [
                {
                    "id": row["id"],
                    "expected": row["expected"],
                    "predicted": row["predicted"],
                }
                for row in matcher_eval["rows"]
                if not row["top1"]
            ],
        },
    }


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Validate and evaluate Learnable Agent assets.")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--source-graph", type=Path, default=DEFAULT_SOURCE_GRAPH_PATH)
    parser.add_argument("--eval", type=Path, default=DEFAULT_EVAL_PATH)
    parser.add_argument("--min-top1", type=float, default=0.8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    report = run_pipeline(args.graph, args.eval, args.min_top1, args.source_graph)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"ok: {report['ok']}")
        print(f"raw scenarios: {report['raw']['scenario_count']}")
        print(f"raw missing required: {len(report['raw']['missing_required'])}")
        print(f"raw missing aliases: {len(report['raw']['missing_aliases'])}")
        print(f"graph nodes/edges: {report['graph']['node_count']} / {report['graph']['edge_count']}")
        print(f"graph recommendations: {report['graph']['recommendation_count']} {report['graph']['recommendation_channels']}")
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
        print(f"matcher top1/top3: {report['matcher_eval']['top1_accuracy']:.3f} / {report['matcher_eval']['top3_accuracy']:.3f}")
        if report["matcher_eval"]["misses"]:
            print("matcher misses:")
            for miss in report["matcher_eval"]["misses"]:
                print(f"  - {miss['id']}: expected={miss['expected']} predicted={miss['predicted']}")

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
