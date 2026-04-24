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
    eval_parser.set_defaults(func=command_eval)

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
        path_status("eval", config.eval_path),
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

    run(config.raw_dir, config.graphify_out_dir, clean_wiki=not args.no_clean_wiki)
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
    report = run_pipeline(config.scene_graph_path, config.eval_path, min_top1, config.source_graph_path)
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
    print(f"answer smoke: {report['answer_smoke']['ok']}")
    for issue in report["answer_smoke"]["issues"]:
        print(f"  - {issue}")
    if report["matcher_eval"]["misses"]:
        print("matcher misses:")
        for miss in report["matcher_eval"]["misses"]:
            print(f"  - {miss['id']}: expected={miss['expected']} predicted={miss['predicted']}")


def command_eval(args: argparse.Namespace, config: HarnessConfig) -> int:
    from scripts.evaluate_scene_matcher import evaluate

    min_top1 = args.min_top1 if args.min_top1 is not None else config.min_top1
    result = evaluate(config.eval_path, config.scene_graph_path, top_k=args.top_k)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"cases: {result['total']}")
        print(f"top1_accuracy: {result['top1_accuracy']:.3f}")
        print(f"top3_accuracy: {result['top3_accuracy']:.3f}")
        print()
        for row in result["rows"]:
            status = "OK" if row["top1"] else "MISS"
            print(f"{status} {row['id']}: expected={row['expected']} predicted={row['predicted']}")
            if not row["top1"]:
                for match in row["matches"][:3]:
                    print(f"  - {match['scenario_id']} score={match['score']} reasons={','.join(match['reasons'])}")
    return 0 if result["top1_accuracy"] >= min_top1 else 1


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
