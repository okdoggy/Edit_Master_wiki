#!/usr/bin/env python3
"""Evaluate scenario matching against user-like queries."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.recommender.graph_loader import DEFAULT_GRAPH_PATH
from scripts.recommender.scenario_matcher import ScenarioMatcher


DEFAULT_EVAL_PATH = REPO_ROOT / "tests" / "eval_queries.json"
DEFAULT_REALISTIC_EVAL_PATH = REPO_ROOT / "tests" / "eval_queries_realistic.json"
DEFAULT_AMBIGUOUS_EVAL_PATH = REPO_ROOT / "tests" / "eval_queries_ambiguous.json"
DEFAULT_COVERAGE_GAP_MAX_SCORE = 2.0
GAP_BEHAVIORS = {"coverage_gap", "candidate_gap"}


def match_should_abstain(match) -> bool:
    if match.coverage_status == "gap" or match.confidence == "low":
        return True
    if getattr(match, "unknown_concepts", None):
        return True
    if match.coverage_status == "partial":
        return match.score < 3.0 or match.slot_coverage < 0.5
    return False


def expected_scenarios(case: dict) -> list[str]:
    if case.get("expected_behavior") in GAP_BEHAVIORS or (
        "expected_scenario" in case and case.get("expected_scenario") is None
    ):
        return []
    values = case.get("expected_scenarios") or case.get("acceptable_scenarios")
    if isinstance(values, list):
        return [str(value) for value in values if str(value)]
    return [str(case["expected_scenario"])]


def primary_expected_scenario(case: dict, expected: list[str]) -> str | None:
    value = case.get("primary_expected_scenario")
    if value:
        return str(value)
    return expected[0] if expected else None


def evaluate(eval_path: Path, graph_path: Path, top_k: int) -> dict:
    cases = json.loads(eval_path.read_text(encoding="utf-8"))
    matcher = ScenarioMatcher.from_path(graph_path)
    rows = []
    top1_hits = 0
    top3_hits = 0
    match_total = 0
    match_top1_hits = 0
    match_top3_hits = 0
    gap_total = 0
    gap_hits = 0

    for case in cases:
        matches = matcher.match(case["query"], top_k=top_k)
        best = matches[0] if matches else None
        predicted = best.scenario_id if best else None
        top_score = best.score if best else 0.0
        top_confidence = best.confidence if best else "none"
        coverage_status = best.coverage_status if best else "gap"
        score_gap = best.score_gap if best else 0.0
        slot_coverage = best.slot_coverage if best else 0.0
        unknown_concepts = best.unknown_concepts if best else []
        abstained = True if best is None else match_should_abstain(best)
        top_ids = [item.scenario_id for item in matches]
        expected = expected_scenarios(case)
        primary_expected = primary_expected_scenario(case, expected)
        expected_behavior = case.get("expected_behavior", "match")
        if not expected and case.get("expected_scenario") is None:
            expected_behavior = "candidate_gap"
        if expected_behavior in GAP_BEHAVIORS:
            max_top_score = float(case.get("max_top_score", DEFAULT_COVERAGE_GAP_MAX_SCORE))
            top1 = top_score <= max_top_score or abstained
            top3 = top1
            gap_total += 1
            gap_hits += int(top1)
        else:
            max_top_score = None
            top1 = predicted == primary_expected and not abstained
            top3 = bool(set(expected) & set(top_ids[:3])) and not abstained
            match_total += 1
            match_top1_hits += int(top1)
            match_top3_hits += int(top3)
        top1_hits += int(top1)
        top3_hits += int(top3)
        rows.append(
            {
                "id": case["id"],
                "expected": expected,
                "primary_expected": primary_expected,
                "expected_behavior": expected_behavior,
                "max_top_score": max_top_score,
                "candidate_scenario": case.get("candidate_scenario"),
                "predicted": predicted,
                "top_score": round(top_score, 4),
                "top_confidence": top_confidence,
                "coverage_status": coverage_status,
                "score_gap": round(score_gap, 4),
                "slot_coverage": round(slot_coverage, 4),
                "unknown_concepts": unknown_concepts,
                "abstained": abstained,
                "top1": top1,
                "top3": top3,
                "language": case.get("language"),
                "difficulty": case.get("difficulty"),
                "matches": [item.as_dict() for item in matches],
            }
        )

    total = len(cases)
    return {
        "total": total,
        "top1_accuracy": top1_hits / total if total else 0,
        "top3_accuracy": top3_hits / total if total else 0,
        "match_total": match_total,
        "gap_total": gap_total,
        "match_top1_accuracy": match_top1_hits / match_total if match_total else 0,
        "match_top3_accuracy": match_top3_hits / match_total if match_total else 0,
        "gap_abstain_accuracy": gap_hits / gap_total if gap_total else None,
        "rows": rows,
    }


def evaluate_suite(eval_paths: dict[str, Path], graph_path: Path, top_k: int) -> dict:
    sets = {
        name: evaluate(path, graph_path, top_k=top_k)
        for name, path in eval_paths.items()
    }
    total = sum(item["total"] for item in sets.values())
    match_total = sum(item["match_total"] for item in sets.values())
    gap_total = sum(item["gap_total"] for item in sets.values())
    weighted_top1 = (
        sum(item["top1_accuracy"] * item["total"] for item in sets.values()) / total if total else 0
    )
    weighted_top3 = (
        sum(item["top3_accuracy"] * item["total"] for item in sets.values()) / total if total else 0
    )
    weighted_match_top1 = (
        sum(item["match_top1_accuracy"] * item["match_total"] for item in sets.values()) / match_total
        if match_total else 0
    )
    weighted_match_top3 = (
        sum(item["match_top3_accuracy"] * item["match_total"] for item in sets.values()) / match_total
        if match_total else 0
    )
    weighted_gap_abstain = (
        sum((item["gap_abstain_accuracy"] or 0) * item["gap_total"] for item in sets.values()) / gap_total
        if gap_total else None
    )
    return {
        "total": total,
        "top1_accuracy": weighted_top1,
        "top3_accuracy": weighted_top3,
        "weighted_top1_accuracy": weighted_top1,
        "weighted_top3_accuracy": weighted_top3,
        "match_total": match_total,
        "gap_total": gap_total,
        "weighted_match_top1_accuracy": weighted_match_top1,
        "weighted_match_top3_accuracy": weighted_match_top3,
        "weighted_gap_abstain_accuracy": weighted_gap_abstain,
        "sets": sets,
    }


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Evaluate the scene scenario matcher.")
    parser.add_argument("--eval", type=Path, default=DEFAULT_EVAL_PATH)
    parser.add_argument("--realistic-eval", type=Path, default=DEFAULT_REALISTIC_EVAL_PATH)
    parser.add_argument("--ambiguous-eval", type=Path, default=DEFAULT_AMBIGUOUS_EVAL_PATH)
    parser.add_argument("--set", choices=["regression", "realistic", "ambiguous", "all"], default="regression")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="Print full JSON report.")
    parser.add_argument("--min-top1", type=float, default=0.8, help="Fail if top-1 accuracy is below this threshold.")
    args = parser.parse_args(argv)

    path_by_set = {
        "regression": args.eval,
        "realistic": args.realistic_eval,
        "ambiguous": args.ambiguous_eval,
    }
    if args.set == "all":
        result = evaluate_suite(path_by_set, args.graph, args.top_k)
        set_results = result["sets"]
    else:
        result = evaluate(path_by_set[args.set], args.graph, args.top_k)
        set_results = {args.set: result}

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for name, set_result in set_results.items():
            print(f"[{name}] cases: {set_result['total']}")
            print(f"[{name}] top1_accuracy: {set_result['top1_accuracy']:.3f}")
            print(f"[{name}] top3_accuracy: {set_result['top3_accuracy']:.3f}")
            print(
                f"[{name}] match_top1/top3: "
                f"{set_result['match_top1_accuracy']:.3f} / {set_result['match_top3_accuracy']:.3f} "
                f"(match cases: {set_result['match_total']})"
            )
            gap_value = set_result["gap_abstain_accuracy"]
            gap_text = "n/a" if gap_value is None else f"{gap_value:.3f}"
            print(f"[{name}] gap_abstain_accuracy: {gap_text} (gap cases: {set_result['gap_total']})")
            for row in set_result["rows"]:
                status = "OK" if row["top1"] else "MISS"
                expected = ",".join(row["expected"]) or row["expected_behavior"]
                print(
                    f"{status} {row['id']}: expected={expected} "
                    f"predicted={row['predicted']} score={row['top_score']} "
                    f"confidence={row['top_confidence']} status={row['coverage_status']} "
                    f"abstained={row['abstained']}"
                )
                if not row["top1"]:
                    for match in row["matches"][:3]:
                        unknown = ",".join(match.get("unknown_concepts", [])) or "-"
                        print(
                            f"  - {match['scenario_id']} score={match['score']} "
                            f"reasons={','.join(match['reasons'])} unknown={unknown}"
                        )
            print()

    return 0 if all(item["top1_accuracy"] >= args.min_top1 for item in set_results.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
