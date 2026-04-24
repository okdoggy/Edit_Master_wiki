"""Persistent personalization loop for the photo-coach recommender.

The runtime stores compact derived feedback events, not source images or full
conversation text. A user's event log can be replayed to rebuild the current
UserPreferenceProfile at any time.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .answer_renderer import NaturalAnswerRenderer, load_observation
from .graph_loader import DEFAULT_GRAPH_PATH, REPO_ROOT, SceneGraph
from .image_facets import ImageObservation
from .personalization import FeedbackEvent, UserPreferenceProfile
from .scenario_matcher import ScenarioMatcher


DEFAULT_MEMORY_DIR = REPO_ROOT / "data" / "personalization"
DEFAULT_LEARNING_RATE = 0.18

ACTION_RATINGS = {
    "accepted": 1.0,
    "saved": 1.0,
    "copied": 0.85,
    "edited_again": -0.35,
    "rejected": -1.0,
    "toned_down": 0.45,
}

ACTION_STYLE_TAGS = {
    "toned_down": ["natural", "low_retouch"],
}

ACTION_REJECTED_TAGS = {
    "toned_down": ["strong_edit"],
}


@dataclass
class StoredFeedbackRecord:
    event_id: str
    created_at: str
    user_id: str
    action: str
    feedback: dict[str, Any]
    query_fingerprint: str = ""


class PersonalizationMemory:
    def __init__(self, memory_dir: Path = DEFAULT_MEMORY_DIR, user_id: str = "default"):
        self.memory_dir = memory_dir
        self.user_id = user_id

    @property
    def profile_path(self) -> Path:
        return self.memory_dir / f"{safe_user_id(self.user_id)}.profile.json"

    @property
    def events_path(self) -> Path:
        return self.memory_dir / f"{safe_user_id(self.user_id)}.events.jsonl"

    def load_profile(self) -> UserPreferenceProfile:
        return UserPreferenceProfile.load(self.profile_path, self.user_id)

    def save_profile(self, profile: UserPreferenceProfile) -> None:
        profile.save(self.profile_path)

    def iter_records(self) -> list[StoredFeedbackRecord]:
        if not self.events_path.exists():
            return []
        records: list[StoredFeedbackRecord] = []
        for line in self.events_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            data = json.loads(line)
            records.append(
                StoredFeedbackRecord(
                    event_id=str(data.get("event_id", "")),
                    created_at=str(data.get("created_at", "")),
                    user_id=str(data.get("user_id", self.user_id)),
                    action=str(data.get("action", "")),
                    feedback=dict(data.get("feedback", {})),
                    query_fingerprint=str(data.get("query_fingerprint", "")),
                )
            )
        return records

    def record_feedback(
        self,
        event: FeedbackEvent,
        *,
        action: str = "accepted",
        query: str = "",
        learning_rate: float = DEFAULT_LEARNING_RATE,
    ) -> tuple[StoredFeedbackRecord, UserPreferenceProfile]:
        profile = self.load_profile()
        profile.apply_feedback(event, learning_rate=learning_rate)
        self.save_profile(profile)

        record = StoredFeedbackRecord(
            event_id=uuid.uuid4().hex,
            created_at=datetime.now(timezone.utc).isoformat(),
            user_id=self.user_id,
            action=action,
            feedback=asdict(event),
            query_fingerprint=fingerprint(query) if query else "",
        )
        self.events_path.parent.mkdir(parents=True, exist_ok=True)
        with self.events_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")
        return record, profile

    def rebuild_profile(self, *, learning_rate: float = DEFAULT_LEARNING_RATE) -> UserPreferenceProfile:
        profile = UserPreferenceProfile.empty(self.user_id)
        for record in self.iter_records():
            profile.apply_feedback(FeedbackEvent.from_dict(record.feedback), learning_rate=learning_rate)
        self.save_profile(profile)
        return profile

    def summary(self) -> dict[str, Any]:
        profile = self.load_profile()
        records = self.iter_records()
        return {
            "user_id": self.user_id,
            "profile_path": str(self.profile_path),
            "events_path": str(self.events_path),
            "event_count": len(records),
            "profile_event_count": profile.event_count,
            "top_preferences": top_preferences(profile),
            "channel_weights": profile.channel_weights,
            "top_scenario_affinity": top_mapping(profile.scenario_affinity),
            "issue_sensitivity": top_mapping(profile.issue_sensitivity),
            "parameter_hints": profile.parameter_hints(),
        }


def build_feedback_event(
    *,
    scenario_id: str,
    channel: str,
    action: str,
    rating: float | None = None,
    style_tags: list[str] | None = None,
    rejected_tags: list[str] | None = None,
    issue_tags: list[str] | None = None,
    note: str = "",
) -> FeedbackEvent:
    action = action or "accepted"
    rating_value = rating if rating is not None else ACTION_RATINGS.get(action, 0.0)
    if rating_value < 0:
        merged_style_tags = [*ACTION_STYLE_TAGS.get(action, [])]
        merged_rejected_tags = [*ACTION_REJECTED_TAGS.get(action, []), *(style_tags or []), *(rejected_tags or [])]
    else:
        merged_style_tags = [*ACTION_STYLE_TAGS.get(action, []), *(style_tags or [])]
        merged_rejected_tags = [*ACTION_REJECTED_TAGS.get(action, []), *(rejected_tags or [])]
    return FeedbackEvent(
        scenario_id=scenario_id,
        channel=channel,
        rating=rating_value,
        style_tags=normalize_style_tags(merged_style_tags),
        rejected_tags=normalize_style_tags(merged_rejected_tags),
        issue_tags=normalize_issue_tags(issue_tags or []),
        note=note,
    )


def infer_scenario_id(query: str, observation: ImageObservation | None, graph_path: Path) -> str:
    matcher_query = observation.to_matcher_query(query) if observation else query
    matcher = ScenarioMatcher(SceneGraph.load(graph_path))
    matches = matcher.match(matcher_query, top_k=1)
    if not matches:
        raise SystemExit("No scenario matched. Provide --scenario-id explicitly.")
    return matches[0].scenario_id


def normalize_style_tags(tags: list[str]) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()
    for tag in tags:
        clean = str(tag).strip()
        if ":" in clean:
            clean = clean.split(":", 1)[1]
        clean = clean.replace("-", "_")
        if clean and clean not in seen:
            seen.add(clean)
            normalized.append(clean)
    return normalized


def normalize_issue_tags(tags: list[str]) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()
    for tag in tags:
        clean = str(tag).strip().replace("-", "_")
        if clean and not clean.startswith("issue:"):
            clean = f"issue:{clean}"
        if clean and clean not in seen:
            seen.add(clean)
            normalized.append(clean)
    return normalized


def top_preferences(profile: UserPreferenceProfile, limit: int = 8) -> list[dict[str, float]]:
    items = [
        {"key": key, "value": round(value, 4)}
        for key, value in profile.preferences.items()
        if abs(value) > 0.0001
    ]
    items.sort(key=lambda item: abs(item["value"]), reverse=True)
    return items[:limit]


def top_mapping(mapping: dict[str, float], limit: int = 8) -> list[dict[str, float]]:
    items = [{"key": key, "value": round(value, 4)} for key, value in mapping.items() if abs(value) > 0.0001]
    items.sort(key=lambda item: abs(item["value"]), reverse=True)
    return items[:limit]


def safe_user_id(user_id: str) -> str:
    return "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in user_id) or "default"


def fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def load_feedback_json(value: str) -> dict[str, Any]:
    try:
        candidate = Path(value)
        if len(value) < 260 and candidate.exists():
            return json.loads(candidate.read_text(encoding="utf-8"))
    except OSError:
        pass
    return json.loads(value)


def command_record(args: argparse.Namespace) -> int:
    observation = load_observation(args.observation_json)
    if args.feedback_json:
        feedback = FeedbackEvent.from_dict(load_feedback_json(args.feedback_json))
        action = args.action or "accepted"
    else:
        if not args.scenario_id and not args.query and not observation:
            raise SystemExit("Provide --scenario-id, --query, or --observation-json so feedback can be attached to a scenario.")
        scenario_id = args.scenario_id or infer_scenario_id(args.query, observation, args.graph)
        feedback = build_feedback_event(
            scenario_id=scenario_id,
            channel=args.channel,
            action=args.action,
            rating=args.rating,
            style_tags=args.style_tags,
            rejected_tags=args.rejected_tags,
            issue_tags=args.issue_tags,
            note=args.note,
        )
        action = args.action

    memory = PersonalizationMemory(args.memory_dir, args.user_id)
    record, profile = memory.record_feedback(
        feedback,
        action=action,
        query=args.query,
        learning_rate=args.learning_rate,
    )
    print(json.dumps({"record": asdict(record), "profile": asdict(profile), "summary": memory.summary()}, ensure_ascii=False, indent=2))
    return 0


def command_show(args: argparse.Namespace) -> int:
    memory = PersonalizationMemory(args.memory_dir, args.user_id)
    profile = memory.load_profile()
    print(json.dumps({"profile": asdict(profile), "summary": memory.summary()}, ensure_ascii=False, indent=2))
    return 0


def command_rebuild(args: argparse.Namespace) -> int:
    memory = PersonalizationMemory(args.memory_dir, args.user_id)
    profile = memory.rebuild_profile(learning_rate=args.learning_rate)
    print(json.dumps({"profile": asdict(profile), "summary": memory.summary()}, ensure_ascii=False, indent=2))
    return 0


def command_render(args: argparse.Namespace) -> int:
    memory = PersonalizationMemory(args.memory_dir, args.user_id)
    renderer = NaturalAnswerRenderer.load(args.graph, args.source_graph)
    answer = renderer.render(
        args.query,
        top_k=args.top_k,
        observation=load_observation(args.observation_json),
        profile=memory.load_profile(),
    )
    if args.json:
        print(json.dumps({"answer": answer.as_dict(), "summary": memory.summary()}, ensure_ascii=False, indent=2))
    else:
        print(answer.text)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Record feedback and apply personalization to future answers.")
    parser.add_argument("--memory-dir", type=Path, default=DEFAULT_MEMORY_DIR)
    parser.add_argument("--user-id", default="default")

    subparsers = parser.add_subparsers(dest="command", required=True)

    record = subparsers.add_parser("record", help="Record one feedback event and update the user profile.")
    add_common_runtime_args(record)
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
    record.add_argument("--learning-rate", type=float, default=DEFAULT_LEARNING_RATE)
    record.set_defaults(func=command_record)

    show = subparsers.add_parser("show", help="Show the current user profile and learned hints.")
    show.set_defaults(func=command_show)

    rebuild = subparsers.add_parser("rebuild", help="Rebuild profile from the JSONL event log.")
    rebuild.add_argument("--learning-rate", type=float, default=DEFAULT_LEARNING_RATE)
    rebuild.set_defaults(func=command_rebuild)

    render = subparsers.add_parser("render", help="Render an answer with the current user profile.")
    add_common_runtime_args(render)
    render.add_argument("query")
    render.add_argument("--top-k", type=int, default=3)
    render.add_argument("--json", action="store_true")
    render.set_defaults(func=command_render)

    return parser


def add_common_runtime_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--source-graph", type=Path, default=REPO_ROOT / "graphify-out" / "graph.json")
    parser.add_argument("--observation-json", type=Path)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
