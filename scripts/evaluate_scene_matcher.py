#!/usr/bin/env python3
"""Evaluate scenario matching against user-like Korean queries."""

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


def evaluate(eval_path: Path, graph_path: Path, top_k: int) -> dict:
    cases = json.loads(eval_path.read_text(encoding="utf-8"))
    matcher = ScenarioMatcher.from_path(graph_path)
    rows = []
    top1_hits = 0
    top3_hits = 0

    for case in cases:
        matches = matcher.match(case["query"], top_k=top_k)
        predicted = matches[0].scenario_id if matches else None
        top_ids = [item.scenario_id for item in matches]
        expected = case["expected_scenario"]
        top1 = predicted == expected
        top3 = expected in top_ids[:3]
        top1_hits += int(top1)
        top3_hits += int(top3)
        rows.append(
            {
                "id": case["id"],
                "expected": expected,
                "predicted": predicted,
                "top1": top1,
                "top3": top3,
                "matches": [item.as_dict() for item in matches],
            }
        )

    total = len(cases)
    return {
        "total": total,
        "top1_accuracy": top1_hits / total if total else 0,
        "top3_accuracy": top3_hits / total if total else 0,
        "rows": rows,
    }


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Evaluate the scene scenario matcher.")
    parser.add_argument("--eval", type=Path, default=DEFAULT_EVAL_PATH)
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="Print full JSON report.")
    parser.add_argument("--min-top1", type=float, default=0.8, help="Fail if top-1 accuracy is below this threshold.")
    args = parser.parse_args(argv)

    result = evaluate(args.eval, args.graph, args.top_k)

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

    return 0 if result["top1_accuracy"] >= args.min_top1 else 1


if __name__ == "__main__":
    raise SystemExit(main())
