"""Single command-line harness for the Edit Master wiki runtime."""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from .config import HarnessConfig, load_config


INTERNAL_LABEL_MARKERS = (
    "SceneFacet",
    "TrendSignal",
    "UserPreference",
    "RecommendationVariant",
    "ImageIssue",
    "confidence_score",
    "rank_score",
)

MOJIBAKE_MARKERS = (
    "\ufffd",
    "?\uafa9",
    "?\u317b",
    "\uf9de\u0080",
    "\u6e72\uacd5",
    "\u7570\ubdbf",
    "\u5a9b\uc496",
)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    config = load_config(args.config)
    return args.func(args, config)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Edit Master wiki and recommender harness.")
    parser.add_argument("--config", type=Path, help="Path to edit-master.toml.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="Check local harness dependencies and required files.")
    doctor.add_argument("--json", action="store_true")
    doctor.set_defaults(func=command_doctor)

    build = subparsers.add_parser("build", help="Regenerate graphify-out from raw sources.")
    build.add_argument("--no-clean-wiki", action="store_true", help="Do not remove graphify-out/wiki before export.")
    build.set_defaults(func=command_build)

    bridge = subparsers.add_parser("bridge", help="Validate source graph to recommender graph linkage.")
    bridge.add_argument("--write", action="store_true", help="Write bridge JSON and Markdown report.")
    bridge.add_argument("--json", action="store_true", help="Print full bridge JSON.")
    bridge.set_defaults(func=command_bridge)

    validate = subparsers.add_parser("validate", help="Run the full read-only quality gate.")
    validate.add_argument("--json", action="store_true")
    validate.add_argument("--min-top1", type=float, help="Override the matcher top-1 threshold.")
    validate.set_defaults(func=command_validate)

    eval_parser = subparsers.add_parser("eval", help="Evaluate scenario matching only.")
    eval_parser.add_argument("--json", action="store_true", help="Print full JSON report.")
    eval_parser.add_argument("--top-k", type=int, default=5)
    eval_parser.add_argument("--min-top1", type=float, help="Override the matcher top-1 threshold.")
    eval_parser.add_argument("--set", choices=["all", "regression", "realistic", "ambiguous"], default="all")
    eval_parser.set_defaults(func=command_eval)

    add_raw_parser(subparsers)

    answer = subparsers.add_parser("answer", help="Render a natural photo-coach answer.")
    answer.add_argument("query")
    answer.add_argument("--observation-json", type=Path)
    answer.add_argument("--profile", type=Path, help="Override the user profile JSON path.")
    answer.add_argument("--user-id", help="User id for personalization memory.")
    answer.add_argument("--top-k", type=int, default=3)
    answer.add_argument("--json", action="store_true")
    answer.add_argument("--no-profile", action="store_true", help="Ignore personalization memory.")
    answer.set_defaults(func=command_answer)

    feedback = subparsers.add_parser("feedback", help="Record or inspect personalization feedback.")
    feedback.add_argument("--memory-dir", type=Path)
    feedback.add_argument("--user-id")
    feedback_sub = feedback.add_subparsers(dest="feedback_command", required=True)
    add_feedback_record_parser(feedback_sub)
    add_feedback_show_parser(feedback_sub)
    add_feedback_rebuild_parser(feedback_sub)
    add_feedback_render_parser(feedback_sub)
    feedback.set_defaults(func=command_feedback)

    all_parser = subparsers.add_parser("all", help="Run build, bridge --write, then validate.")
    all_parser.add_argument("--min-top1", type=float, help="Override the matcher top-1 threshold.")
    all_parser.set_defaults(func=command_all)

    return parser


def add_raw_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    raw = subparsers.add_parser("raw", help="Source-backed raw-data intake harness.")
    raw_sub = raw.add_subparsers(dest="raw_command", required=True)

    intake = raw_sub.add_parser("intake", help="Create briefs, run workers, and validate incoming candidates.")
    intake.add_argument("--topic", action="append", default=[], help="Research topic. Repeat for multiple parallel tasks.")
    intake.add_argument("--topics-file", type=Path, help="One research topic per line. Lines starting with # are ignored.")
    intake.add_argument("--count", type=int, default=5, help="Latest expert topic count when no --topic is supplied.")
    intake.add_argument("--run-id", help="Stable run id. Defaults to a timestamped id.")
    intake.add_argument("--engine", choices=["codex", "claude"], default="codex")
    intake.add_argument("--parallel", default="max", help='Worker count or "max".')
    intake.add_argument("--min-sources", type=int, help="Minimum external source URLs required per candidate.")
    intake.add_argument("--max-similarity", type=float)
    intake.add_argument("--strict-sources", action="store_true", help="Fail unknown source domains instead of warning.")
    intake.add_argument("--dry-run", action="store_true", help="Create briefs and print dispatch plan without launching workers.")
    intake.add_argument("--json", action="store_true")
    intake.set_defaults(func=command_raw)

    brief = raw_sub.add_parser("brief", help="Create parallel Codex/Claude task briefs for source-backed raw collection.")
    brief.add_argument("--topic", action="append", default=[], help="Research topic. Repeat for multiple parallel tasks.")
    brief.add_argument("--topics-file", type=Path, help="One research topic per line. Lines starting with # are ignored.")
    brief.add_argument("--count", type=int, default=5, help="Latest expert topic count when no --topic is supplied.")
    brief.add_argument("--run-id", help="Stable run id. Defaults to a timestamped id.")
    brief.add_argument("--engine", choices=["codex", "claude", "both"], default="both")
    brief.add_argument("--parallel", default="max", help='Worker count or "max". Task generation is one task per topic.')
    brief.add_argument("--min-sources", type=int, help="Minimum external source URLs required per candidate.")
    brief.add_argument("--json", action="store_true")
    brief.set_defaults(func=command_raw)

    validate = raw_sub.add_parser("validate", help="Validate incoming or existing raw scenario files.")
    validate.add_argument("--scope", choices=["incoming", "scenarios"], default="incoming")
    validate.add_argument("--path", type=Path, help="Specific candidate file or directory to validate.")
    validate.add_argument("--min-sources", type=int)
    validate.add_argument("--max-similarity", type=float)
    validate.add_argument("--strict-sources", action="store_true", help="Fail unknown source domains instead of warning.")
    validate.add_argument("--json", action="store_true")
    validate.set_defaults(func=command_raw)

    dispatch = raw_sub.add_parser("dispatch", help="Run generated Codex or Claude raw-intake tasks in parallel.")
    dispatch.add_argument("--run-id", default="latest", help='Run id from raw brief, or "latest".')
    dispatch.add_argument("--engine", choices=["codex", "claude"], default="codex")
    dispatch.add_argument("--parallel", default="max", help='Worker count or "max".')
    dispatch.add_argument("--dry-run", action="store_true", help="Print the execution plan without launching workers.")
    dispatch.add_argument("--json", action="store_true")
    dispatch.set_defaults(func=command_raw)

    promote = raw_sub.add_parser("promote", help="Promote validated incoming candidates into raw/scenarios.")
    promote.add_argument("--path", type=Path, help="Specific incoming file or directory to promote.")
    promote.add_argument("--min-sources", type=int)
    promote.add_argument("--max-similarity", type=float)
    promote.add_argument("--strict-sources", action="store_true")
    promote.add_argument("--passing-only", action="store_true", help="Promote only candidates that pass validation; leave failures in incoming.")
    promote.add_argument("--delete-incoming", action="store_true", help="Delete incoming files after successful promotion.")
    promote.add_argument("--delete-failed", action="store_true", help="With --passing-only, delete failed incoming candidates and source notes after validation.")
    promote.add_argument("--build", action="store_true", help="Run build, bridge --write, and validate after promotion.")
    promote.add_argument("--json", action="store_true")
    promote.set_defaults(func=command_raw)


def add_feedback_record_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    from scripts.recommender.learning_loop import ACTION_RATINGS

    record = subparsers.add_parser("record", help="Record one feedback event and update the user profile.")
    add_runtime_args(record)
    record.add_argument("--feedback-json", help="FeedbackEvent JSON string or path.")
    record.add_argument("--scenario-id", help="Scenario id. If omitted, inferred from --query.")
    record.add_argument("--query", default="", help="Original query used only for scenario inference and hashed audit.")
    record.add_argument("--action", default="accepted", choices=sorted(ACTION_RATINGS))
    record.add_argument("--channel", default="personalized", choices=["trend", "general", "personalized"])
    record.add_argument("--rating", type=float, help="Override action-derived rating in [-1, 1].")
    record.add_argument("--style-tags", nargs="*", default=[])
    record.add_argument("--rejected-tags", nargs="*", default=[])
    record.add_argument("--issue-tags", nargs="*", default=[])
    record.add_argument("--note", default="")
    record.add_argument("--learning-rate", type=float)


def add_feedback_show_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser("show", help="Show the current user profile and learned hints.")


def add_feedback_rebuild_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    rebuild = subparsers.add_parser("rebuild", help="Rebuild profile from the JSONL event log.")
    rebuild.add_argument("--learning-rate", type=float)


def add_feedback_render_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    render = subparsers.add_parser("render", help="Render an answer with the current user profile.")
    add_runtime_args(render)
    render.add_argument("query")
    render.add_argument("--top-k", type=int, default=3)
    render.add_argument("--json", action="store_true")


def add_runtime_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--observation-json", type=Path)


def command_doctor(args: argparse.Namespace, config: HarnessConfig) -> int:
    report = build_doctor_report(config)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"ok: {report['ok']}")
        print(f"python: {report['python']['version']}")
        print(f"uv: {report['uv']['path'] or 'not found'}")
        print(f"graphify: {'ok' if report['graphify']['ok'] else 'missing'}")
        print("paths:")
        for item in report["paths"]:
            print(f"  - {item['name']}: {'ok' if item['exists'] else 'missing'} ({item['path']})")
        if report["messages"]:
            print("messages:")
            for message in report["messages"]:
                print(f"  - {message}")
    return 0 if report["ok"] else 1


def build_doctor_report(config: HarnessConfig) -> dict[str, Any]:
    graphify_deps = config.root / ".graphify-deps"
    if graphify_deps.exists() and str(graphify_deps) not in sys.path:
        sys.path.insert(0, str(graphify_deps))

    path_checks = [
        path_status("config", config.root / "edit-master.toml"),
        path_status("raw", config.raw_dir),
        path_status("graphify_out", config.graphify_out_dir),
        path_status("scene_graph", config.scene_graph_path),
        path_status("source_graph", config.source_graph_path),
        path_status("eval_regression", config.eval_path),
        path_status("eval_realistic", config.realistic_eval_path),
        path_status("eval_ambiguous", config.ambiguous_eval_path),
        path_status("README", config.root / "README.md"),
    ]
    graphify_ok = importlib.util.find_spec("graphify") is not None
    uv_path = shutil.which("uv")
    messages: list[str] = []
    if not uv_path:
        messages.append("Install uv before using `uv run edit-master ...`.")
    if not graphify_ok:
        messages.append("Run `uv sync` to install graphifyy, or keep graphify available in .graphify-deps.")
    missing_paths = [item["name"] for item in path_checks if not item["exists"]]
    if missing_paths:
        messages.append(f"Missing required paths: {', '.join(missing_paths)}")

    return {
        "ok": bool(uv_path) and graphify_ok and not missing_paths,
        "python": {"version": sys.version.split()[0], "executable": sys.executable},
        "uv": {"path": uv_path},
        "graphify": {"ok": graphify_ok},
        "paths": path_checks,
        "messages": messages,
    }


def path_status(name: str, path: Path) -> dict[str, Any]:
    return {"name": name, "path": str(path), "exists": path.exists()}


def command_build(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.run_graphify_raw import run
    from scripts.recommender.scene_graph_builder import run as run_scene_graph_builder

    run(config.raw_dir, config.graphify_out_dir, clean_wiki=not args.no_clean_wiki)
    run_scene_graph_builder(config.raw_dir, config.graphify_out_dir)
    return 0


def command_bridge(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.recommender.source_bridge import SourceRecommenderBridge, write_outputs

    bridge = SourceRecommenderBridge.load(config.scene_graph_path, config.source_graph_path)
    if args.write:
        write_outputs(bridge, config.bridge_json_path, config.bridge_report_path)
    if args.json:
        print(json.dumps(bridge.as_dict(), ensure_ascii=False, indent=2))
    else:
        print_bridge_validation(bridge.validate())
    return 0 if bridge.validate()["ok"] else 1


def print_bridge_validation(validation: dict[str, Any]) -> None:
    print(f"ok: {validation['ok']}")
    print(f"scenario link coverage: {validation['linked_scenario_count']} / {validation['scenario_count']}")
    print(f"recommendations: {validation['recommendation_count']}")
    print(f"external evidence links: {validation['external_evidence_count']}")
    print(f"scenarios without external evidence: {len(validation['scenarios_without_external_evidence'])}")


def command_validate(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.agent_pipeline import run_pipeline

    min_top1 = args.min_top1 if args.min_top1 is not None else config.min_top1
    report = run_pipeline(
        config.scene_graph_path,
        eval_paths(config),
        min_top1,
        config.source_graph_path,
        config.eval_thresholds,
    )
    report["answer_smoke"] = validate_answer_smoke(config)
    report["ok"] = bool(report["ok"] and report["answer_smoke"]["ok"])
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_pipeline_report(report)
    return 0 if report["ok"] else 1


def validate_answer_smoke(config: HarnessConfig) -> dict[str, Any]:
    from scripts.recommender.answer_renderer import NaturalAnswerRenderer

    renderer = NaturalAnswerRenderer.load(config.scene_graph_path, config.source_graph_path)
    answer = renderer.render(config.answer_smoke_query)
    text = answer.text.strip()
    issues: list[str] = []
    if not text:
        issues.append("answer text is empty")
    leaked = [marker for marker in INTERNAL_LABEL_MARKERS if marker in text]
    if leaked:
        issues.append(f"internal graph labels leaked: {', '.join(leaked)}")
    garbled = [marker for marker in MOJIBAKE_MARKERS if marker in text]
    if garbled:
        issues.append(f"possible mojibake markers found: {', '.join(garbled)}")
    return {
        "ok": not issues,
        "query": config.answer_smoke_query,
        "issues": issues,
        "sample": text[:500],
    }


def print_pipeline_report(report: dict[str, Any]) -> None:
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
            f"matcher {name} top1/top3: "
            f"{result['top1_accuracy']:.3f} / {result['top3_accuracy']:.3f} "
            f"(match {result.get('match_top1_accuracy', result['top1_accuracy']):.3f}/"
            f"{result.get('match_top3_accuracy', result['top3_accuracy']):.3f}, gap {gap_text}) "
            f"({format_eval_checks(result)})"
        )
    print(f"answer smoke: {report['answer_smoke']['ok']}")
    for issue in report["answer_smoke"]["issues"]:
        print(f"  - {issue}")
    if report["matcher_eval"]["misses"]:
        print("matcher misses:")
        for miss in report["matcher_eval"]["misses"]:
            expected = miss["expected"] or miss.get("expected_behavior", "match")
            score = "" if miss.get("top_score") is None else f" score={miss['top_score']}"
            print(
                f"  - [{miss['set']}] {miss['id']}: expected={expected} "
                f"predicted={miss['predicted']}{score} "
                f"confidence={miss.get('top_confidence')} status={miss.get('coverage_status')} "
                f"abstained={miss.get('abstained')}"
            )
    if report["matcher_eval"].get("candidate_gaps"):
        print("candidate gaps:")
        for gap in report["matcher_eval"]["candidate_gaps"]:
            candidate = gap.get("candidate_scenario") or "-"
            score = "" if gap.get("top_score") is None else f" score={gap['top_score']}"
            print(
                f"  - [{gap['set']}] {gap['id']}: candidate={candidate} "
                f"predicted={gap['predicted']}{score} "
                f"confidence={gap.get('top_confidence')} status={gap.get('coverage_status')} "
                f"abstained={gap.get('abstained')}"
            )


def format_eval_checks(result: dict[str, Any]) -> str:
    checks = result.get("checks") or {}
    if not checks:
        return "no explicit thresholds"
    parts = []
    for key in ("top1", "top3", "match_top1", "match_top3", "gap_abstain"):
        item = checks.get(key)
        if not item:
            continue
        value = item.get("value")
        value_text = "n/a" if value is None else f"{value:.3f}"
        parts.append(f"{key}>={item['min']:.2f}:{value_text}")
    return "min " + ", ".join(parts)


def command_eval(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.agent_pipeline import validate_matcher_eval
    from scripts.evaluate_scene_matcher import evaluate_suite

    min_top1 = args.min_top1 if args.min_top1 is not None else config.min_top1
    selected_paths = eval_paths(config)
    if args.set != "all":
        selected_paths = {args.set: selected_paths[args.set]}
    thresholds = dict(config.eval_thresholds)
    thresholds["regression"] = {**thresholds.get("regression", {}), "top1": min_top1}
    result = validate_matcher_eval(evaluate_suite(selected_paths, config.scene_graph_path, top_k=args.top_k), thresholds)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"cases: {result['total']}")
        print(f"weighted_top1_accuracy: {result['weighted_top1_accuracy']:.3f}")
        print(f"weighted_top3_accuracy: {result['weighted_top3_accuracy']:.3f}")
        print(f"match_top1_accuracy: {result['weighted_match_top1_accuracy']:.3f}")
        print(f"match_top3_accuracy: {result['weighted_match_top3_accuracy']:.3f}")
        gap_value = result.get("weighted_gap_abstain_accuracy")
        gap_text = "n/a" if gap_value is None else f"{gap_value:.3f}"
        print(f"gap_abstain_accuracy: {gap_text}")
        print()
        for name, item in result["sets"].items():
            gap_value = item.get("gap_abstain_accuracy")
            gap_text = "n/a" if gap_value is None else f"{gap_value:.3f}"
            print(
                f"{name}: top1={item['top1_accuracy']:.3f} "
                f"top3={item['top3_accuracy']:.3f} "
                f"match={item.get('match_top1_accuracy', item['top1_accuracy']):.3f}/"
                f"{item.get('match_top3_accuracy', item['top3_accuracy']):.3f} "
                f"gap={gap_text} "
                f"cases={item['total']} "
                f"ok={item['ok']} "
                f"({format_eval_checks(item)})"
            )
        if result["misses"]:
            print()
            print("misses:")
            for miss in result["misses"]:
                expected = miss["expected"] or miss.get("expected_behavior", "match")
                score = "" if miss.get("top_score") is None else f" score={miss['top_score']}"
                print(
                    f"  - [{miss['set']}] {miss['id']}: expected={expected} "
                    f"predicted={miss['predicted']} top3={miss['top3']}{score} "
                    f"confidence={miss.get('top_confidence')} status={miss.get('coverage_status')} "
                    f"abstained={miss.get('abstained')}"
                )
        if result.get("candidate_gaps"):
            print()
            print("candidate gaps:")
            for gap in result["candidate_gaps"]:
                candidate = gap.get("candidate_scenario") or "-"
                score = "" if gap.get("top_score") is None else f" score={gap['top_score']}"
                print(
                    f"  - [{gap['set']}] {gap['id']}: candidate={candidate} "
                    f"predicted={gap['predicted']}{score} "
                    f"confidence={gap.get('top_confidence')} status={gap.get('coverage_status')} "
                    f"abstained={gap.get('abstained')}"
                )
    return 0 if result["ok"] else 1


def eval_paths(config: HarnessConfig) -> dict[str, Path]:
    return {
        "regression": config.eval_path,
        "realistic": config.realistic_eval_path,
        "ambiguous": config.ambiguous_eval_path,
    }


def command_raw(args: argparse.Namespace, config: HarnessConfig) -> int:
    from . import raw_harness

    if args.raw_command == "intake":
        if not args.dry_run:
            raw_harness.ensure_agent_engine_ready(args.engine)
        topics = collect_raw_topics(args)
        if not topics:
            topics = raw_harness.default_topics(args.count)
        min_sources = args.min_sources or config.raw_min_sources
        manifest = raw_harness.create_agent_briefs(
            root=config.root,
            raw_dir=config.raw_dir,
            incoming_dir=config.raw_incoming_dir,
            source_notes_dir=config.raw_source_notes_dir,
            runs_dir=config.raw_intake_runs_dir,
            topics=topics,
            run_id=args.run_id,
            engine=args.engine,
            parallel=args.parallel,
            min_sources=min_sources,
        )
        dispatch = raw_harness.dispatch_agent_tasks(
            root=config.root,
            runs_dir=config.raw_intake_runs_dir,
            run_id=str(manifest["run_id"]),
            engine=args.engine,
            parallel=args.parallel,
            dry_run=args.dry_run,
        )
        validation = None
        if not args.dry_run:
            candidate_paths = [Path(str(task["candidate_path"])) for task in manifest["tasks"]]
            validation = raw_harness.validate_raw_candidates(
                raw_dir=config.raw_dir,
                paths=candidate_paths,
                min_sources=min_sources,
                max_similarity=args.max_similarity or config.raw_max_similarity,
                strict_sources=args.strict_sources,
                source_notes_dir=config.raw_source_notes_dir,
            )
        result = {
            "ok": bool(dispatch["ok"] and (args.dry_run or (validation and validation["ok"] and validation["candidate_count"] > 0))),
            "run_id": manifest["run_id"],
            "manifest": manifest,
            "dispatch": dispatch,
            "validation": validation,
            "next_command": "uv run edit-master raw promote --build",
        }
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"ok: {result['ok']}")
            print(f"run_id: {manifest['run_id']}")
            print(f"tasks: {manifest['task_count']} (max_parallel={dispatch['max_parallel']})")
            print(f"manifest: {config.raw_intake_runs_dir / str(manifest['run_id']) / 'manifest.json'}")
            if args.dry_run:
                print("dispatch: dry-run")
                for item in dispatch["tasks"]:
                    suffix = f" < {item['stdin_path']}" if item.get("stdin_path") else ""
                    print(f"planned: {item['slug']} -> {' '.join(item['command'])}{suffix}")
                print("next:")
                print(f"  uv run edit-master raw dispatch --run-id {manifest['run_id']} --engine {args.engine} --parallel {args.parallel}")
            else:
                print(f"dispatch: {'ok' if dispatch['ok'] else 'failed'}")
                for item in dispatch["tasks"]:
                    print(f"done: {item['slug']} rc={item['returncode']}")
                print_raw_validation(validation)
                if result["ok"]:
                    print("next:")
                    print("  uv run edit-master raw promote --build")
        return 0 if result["ok"] else 1

    if args.raw_command == "brief":
        topics = collect_raw_topics(args)
        if not topics:
            topics = raw_harness.default_topics(args.count)
        manifest = raw_harness.create_agent_briefs(
            root=config.root,
            raw_dir=config.raw_dir,
            incoming_dir=config.raw_incoming_dir,
            source_notes_dir=config.raw_source_notes_dir,
            runs_dir=config.raw_intake_runs_dir,
            topics=topics,
            run_id=args.run_id,
            engine=args.engine,
            parallel=args.parallel,
            min_sources=args.min_sources or config.raw_min_sources,
        )
        if args.json:
            print(json.dumps(manifest, ensure_ascii=False, indent=2))
        else:
            print(f"run_id: {manifest['run_id']}")
            print(f"tasks: {manifest['task_count']} (max_parallel={manifest['max_parallel']})")
            print(f"manifest: {config.raw_intake_runs_dir / manifest['run_id'] / 'manifest.json'}")
            print(f"runner: {config.raw_intake_runs_dir / manifest['run_id'] / 'RUN_PARALLEL.md'}")
            print("next:")
            print("  uv run edit-master raw validate --scope incoming")
            print("  uv run edit-master raw promote --build")
        return 0

    if args.raw_command == "validate":
        paths = raw_harness.candidate_paths_for_scope(config.raw_incoming_dir, config.raw_dir, args.scope, args.path)
        source_notes_dir = raw_source_notes_dir_for_paths(paths, config.raw_incoming_dir, config.raw_source_notes_dir)
        result = raw_harness.validate_raw_candidates(
            raw_dir=config.raw_dir,
            paths=paths,
            min_sources=args.min_sources or config.raw_min_sources,
            max_similarity=args.max_similarity or config.raw_max_similarity,
            strict_sources=args.strict_sources,
            source_notes_dir=source_notes_dir,
        )
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print_raw_validation(result)
        return 0 if result["ok"] and result["candidate_count"] > 0 else 1

    if args.raw_command == "dispatch":
        result = raw_harness.dispatch_agent_tasks(
            root=config.root,
            runs_dir=config.raw_intake_runs_dir,
            run_id=args.run_id,
            engine=args.engine,
            parallel=args.parallel,
            dry_run=args.dry_run,
        )
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"ok: {result['ok']}")
            print(f"run_id: {result['run_id']}")
            print(f"engine: {result['engine']}")
            print(f"max_parallel: {result['max_parallel']}")
            for item in result["tasks"]:
                if result["dry_run"]:
                    suffix = f" < {item['stdin_path']}" if item.get("stdin_path") else ""
                    print(f"planned: {item['slug']} -> {' '.join(item['command'])}{suffix}")
                else:
                    print(f"done: {item['slug']} rc={item['returncode']}")
                    print(f"  stdout: {item['stdout_log']}")
                    print(f"  stderr: {item['stderr_log']}")
        return 0 if result["ok"] else 1

    if args.raw_command == "promote":
        if args.delete_failed and not args.passing_only:
            raise SystemExit("--delete-failed must be used with --passing-only.")
        paths = raw_harness.candidate_paths_for_scope(config.raw_incoming_dir, config.raw_dir, "incoming", args.path)
        result = raw_harness.promote_candidates(
            raw_dir=config.raw_dir,
            paths=paths,
            min_sources=args.min_sources or config.raw_min_sources,
            max_similarity=args.max_similarity or config.raw_max_similarity,
            strict_sources=args.strict_sources,
            delete_incoming=args.delete_incoming,
            passing_only=args.passing_only,
            delete_failed=args.delete_failed,
            source_notes_dir=config.raw_source_notes_dir,
        )
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            if not result["ok"]:
                print("ok: False")
                print_raw_validation(result["validation"])
            else:
                print("ok: True")
                for item in result["promoted"]:
                    print(f"promoted: {item['source']} -> {item['target']}")
                    if item.get("source_note"):
                        print(f"  source_note: {item['source_note']}")
                skipped = result.get("skipped") or []
                if skipped:
                    print(f"skipped: {len(skipped)} failed candidate(s)")
                    for item in skipped:
                        print(f"  - {item['slug']}: {'; '.join(item['errors'][:2])}")
                deleted_failed = result.get("deleted_failed") or []
                if deleted_failed:
                    print(f"deleted_failed: {len(deleted_failed)} file(s)")
                    for item in deleted_failed:
                        print(f"  - {item['type']}: {item['path']}")
        if not result["ok"]:
            return 1
        if args.build and result["promoted"]:
            print()
            return command_all(SimpleNamespace(min_top1=None), config)
        if args.build and not result["promoted"]:
            print("build: skipped (no candidates promoted)")
        return 0

    raise SystemExit(f"Unknown raw command: {args.raw_command}")


def collect_raw_topics(args: argparse.Namespace) -> list[str]:
    topics = list(args.topic or [])
    if args.topics_file:
        for line in args.topics_file.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                topics.append(stripped)
    return topics


def raw_source_notes_dir_for_paths(paths: list[Path], incoming_dir: Path, source_notes_dir: Path) -> Path | None:
    incoming = incoming_dir.resolve()
    for path in paths:
        try:
            if path.resolve().is_relative_to(incoming):
                return source_notes_dir
        except OSError:
            continue
    return None


def print_raw_validation(result: dict[str, Any]) -> None:
    print(f"ok: {result['ok']}")
    print(f"candidates: {result['candidate_count']}")
    if result["candidate_count"] == 0:
        print("  - no candidate files found")
        return
    for item in result["results"]:
        status = "OK" if item["ok"] else "FAIL"
        print(f"{status} {item['slug']}: {item['title']}")
        trusted = [
            source
            for source in item["source_report"]
            if source["source_class"] in {"official", "expert", "creator_social", "community"}
        ]
        print(f"  sources: {len(item['source_report'])} total, {len(trusted)} trusted/classified")
        source_note = item.get("source_note")
        if source_note:
            print(
                "  source_note: "
                f"{'ok' if source_note.get('ok') else 'missing/invalid'} "
                f"({source_note.get('path')})"
            )
        for error in item["errors"]:
            print(f"  error: {error}")
        for warning in item["warnings"]:
            print(f"  warning: {warning}")


def command_answer(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.recommender.answer_renderer import NaturalAnswerRenderer, load_observation
    from scripts.recommender.learning_loop import PersonalizationMemory
    from scripts.recommender.personalization import UserPreferenceProfile

    user_id = args.user_id or config.default_user_id
    profile = None
    if not args.no_profile:
        if args.profile:
            profile = UserPreferenceProfile.load(args.profile, user_id)
        else:
            profile = PersonalizationMemory(config.personalization_dir, user_id).load_profile()

    renderer = NaturalAnswerRenderer.load(config.scene_graph_path, config.source_graph_path)
    answer = renderer.render(
        args.query,
        top_k=args.top_k,
        observation=load_observation(args.observation_json),
        profile=profile,
    )
    if args.json:
        print(json.dumps(answer.as_dict(), ensure_ascii=False, indent=2))
    else:
        print(answer.text)
    return 0


def command_feedback(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.recommender import learning_loop

    memory_dir = args.memory_dir or config.personalization_dir
    user_id = args.user_id or config.default_user_id
    command = args.feedback_command

    if command == "record":
        namespace = SimpleNamespace(
            memory_dir=memory_dir,
            user_id=user_id,
            graph=config.scene_graph_path,
            source_graph=config.source_graph_path,
            observation_json=args.observation_json,
            feedback_json=args.feedback_json,
            scenario_id=args.scenario_id,
            query=args.query,
            action=args.action,
            channel=args.channel,
            rating=args.rating,
            style_tags=args.style_tags,
            rejected_tags=args.rejected_tags,
            issue_tags=args.issue_tags,
            note=args.note,
            learning_rate=args.learning_rate or learning_loop.DEFAULT_LEARNING_RATE,
        )
        return learning_loop.command_record(namespace)
    if command == "show":
        namespace = SimpleNamespace(memory_dir=memory_dir, user_id=user_id)
        return learning_loop.command_show(namespace)
    if command == "rebuild":
        namespace = SimpleNamespace(
            memory_dir=memory_dir,
            user_id=user_id,
            learning_rate=args.learning_rate or learning_loop.DEFAULT_LEARNING_RATE,
        )
        return learning_loop.command_rebuild(namespace)
    if command == "render":
        namespace = SimpleNamespace(
            memory_dir=memory_dir,
            user_id=user_id,
            graph=config.scene_graph_path,
            source_graph=config.source_graph_path,
            observation_json=args.observation_json,
            query=args.query,
            top_k=args.top_k,
            json=args.json,
        )
        return learning_loop.command_render(namespace)
    raise SystemExit(f"Unknown feedback command: {command}")


def command_all(args: argparse.Namespace, config: HarnessConfig) -> int:
    print("== build ==")
    build_code = command_build(SimpleNamespace(no_clean_wiki=False), config)
    if build_code:
        return build_code
    print()
    print("== bridge ==")
    bridge_code = command_bridge(SimpleNamespace(write=True, json=False), config)
    if bridge_code:
        return bridge_code
    print()
    print("== validate ==")
    return command_validate(SimpleNamespace(json=False, min_top1=args.min_top1), config)


if __name__ == "__main__":
    raise SystemExit(main())
