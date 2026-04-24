"""Personalization primitives for a learnable photo-coach agent.

The module stores only compact preference signals. It does not store image files
or private conversation text; callers can keep those in an application database
and pass derived events here.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


PREFERENCE_KEYS = {
    "warmth",
    "brightness",
    "contrast",
    "saturation",
    "grain",
    "skin_retouch",
    "background_cleanup",
    "cinematic",
    "natural",
    "edit_strength",
}

TAG_TO_PREFERENCE = {
    "warm": {"warmth": 0.2},
    "cool": {"warmth": -0.2},
    "bright": {"brightness": 0.2},
    "airy": {"brightness": 0.2, "contrast": -0.1},
    "cinematic": {"cinematic": 0.25, "contrast": 0.15, "grain": 0.1},
    "natural": {"natural": 0.25, "edit_strength": -0.1, "skin_retouch": -0.1},
    "clean": {"background_cleanup": 0.2, "saturation": -0.05},
    "film": {"grain": 0.25, "contrast": -0.05},
    "low_retouch": {"skin_retouch": -0.25, "natural": 0.15},
    "strong_edit": {"edit_strength": 0.25, "contrast": 0.1, "saturation": 0.1},
    "soft": {"contrast": -0.15, "skin_retouch": 0.1},
}


@dataclass
class FeedbackEvent:
    scenario_id: str
    channel: str
    rating: float
    style_tags: list[str] = field(default_factory=list)
    rejected_tags: list[str] = field(default_factory=list)
    issue_tags: list[str] = field(default_factory=list)
    note: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "FeedbackEvent":
        return cls(
            scenario_id=str(data["scenario_id"]),
            channel=str(data.get("channel", "general")),
            rating=float(data.get("rating", 0)),
            style_tags=list(data.get("style_tags", [])),
            rejected_tags=list(data.get("rejected_tags", [])),
            issue_tags=list(data.get("issue_tags", [])),
            note=str(data.get("note", "")),
        )


@dataclass
class UserPreferenceProfile:
    user_id: str
    preferences: dict[str, float] = field(default_factory=lambda: {key: 0.0 for key in PREFERENCE_KEYS})
    channel_weights: dict[str, float] = field(default_factory=lambda: {"trend": 1.0, "general": 1.0, "personalized": 1.0})
    scenario_affinity: dict[str, float] = field(default_factory=dict)
    issue_sensitivity: dict[str, float] = field(default_factory=dict)
    event_count: int = 0

    @classmethod
    def empty(cls, user_id: str) -> "UserPreferenceProfile":
        return cls(user_id=user_id)

    @classmethod
    def load(cls, path: Path, user_id: str = "default") -> "UserPreferenceProfile":
        if not path.exists():
            return cls.empty(user_id)
        data = json.loads(path.read_text(encoding="utf-8"))
        profile = cls.empty(str(data.get("user_id", user_id)))
        profile.preferences.update({key: float(value) for key, value in data.get("preferences", {}).items() if key in PREFERENCE_KEYS})
        profile.channel_weights.update({key: float(value) for key, value in data.get("channel_weights", {}).items()})
        profile.scenario_affinity.update({key: float(value) for key, value in data.get("scenario_affinity", {}).items()})
        profile.issue_sensitivity.update({key: float(value) for key, value in data.get("issue_sensitivity", {}).items()})
        profile.event_count = int(data.get("event_count", 0))
        return profile

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def apply_feedback(self, event: FeedbackEvent, learning_rate: float = 0.18) -> None:
        rating = max(-1.0, min(1.0, event.rating))
        if rating == 0 and not event.style_tags and not event.rejected_tags:
            self.event_count += 1
            return

        self.channel_weights[event.channel] = clamp(
            self.channel_weights.get(event.channel, 1.0) + learning_rate * rating,
            0.4,
            1.8,
        )
        self.scenario_affinity[event.scenario_id] = clamp(
            self.scenario_affinity.get(event.scenario_id, 0.0) + learning_rate * rating,
            -1.0,
            1.0,
        )

        for tag in event.style_tags:
            self._apply_tag(tag, learning_rate * max(0.25, rating))
        for tag in event.rejected_tags:
            self._apply_tag(tag, -learning_rate * max(0.25, abs(rating) or 1.0))
        for issue in event.issue_tags:
            self.issue_sensitivity[issue] = clamp(
                self.issue_sensitivity.get(issue, 0.0) + learning_rate * max(0.25, rating),
                0.0,
                1.0,
            )
        self.event_count += 1

    def _apply_tag(self, tag: str, amount: float) -> None:
        for key, direction in TAG_TO_PREFERENCE.get(tag, {}).items():
            self.preferences[key] = clamp(self.preferences.get(key, 0.0) + amount * direction, -1.0, 1.0)

    def channel_multiplier(self, channel: str) -> float:
        return self.channel_weights.get(channel, 1.0)

    def scenario_multiplier(self, scenario_id: str) -> float:
        return 1.0 + self.scenario_affinity.get(scenario_id, 0.0) * 0.25

    def parameter_hints(self) -> list[str]:
        hints: list[str] = []
        prefs = self.preferences
        if prefs.get("warmth", 0) > 0.15:
            hints.append("따뜻한 색을 선호하므로 Temp/Tint는 과하지 않게 따뜻한 쪽에서 시작")
        if prefs.get("warmth", 0) < -0.15:
            hints.append("차분한 색을 선호하므로 노란 조명은 WB로 중립에 가깝게 정리")
        if prefs.get("natural", 0) > 0.15 or prefs.get("edit_strength", 0) < -0.15:
            hints.append("자연스러운 결과를 선호하므로 보정 강도는 기본값의 50~70%부터 적용")
        if prefs.get("cinematic", 0) > 0.15:
            hints.append("시네마틱 취향이 강하므로 shadows는 약간 차갑게, highlights는 따뜻하게 분리")
        if prefs.get("grain", 0) > 0.15:
            hints.append("필름/입자 취향이 있어 Grain +10~+25 범위를 후보로 유지")
        if prefs.get("skin_retouch", 0) < -0.15:
            hints.append("피부 보정 티를 싫어하므로 Texture 감소는 -5~-10 이내로 제한")
        if prefs.get("background_cleanup", 0) > 0.15:
            hints.append("깔끔한 배경 선호가 있어 배경 채도/선명도를 낮추는 variant를 우선")
        return hints


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def rerank_recommendations(recommendations: list[dict[str, Any]], profile: UserPreferenceProfile, scenario_id: str) -> list[dict[str, Any]]:
    reranked: list[dict[str, Any]] = []
    for rec in recommendations:
        props = rec.get("properties", rec)
        channel = str(props.get("channel", "general"))
        base_score = float(props.get("rank_score", rec.get("rank_score", 0.0)))
        personalized_score = base_score * profile.channel_multiplier(channel) * profile.scenario_multiplier(scenario_id)
        clone = dict(rec)
        clone["personalized_score"] = round(personalized_score, 4)
        clone["personalization_hints"] = profile.parameter_hints()
        reranked.append(clone)
    return sorted(reranked, key=lambda item: item["personalized_score"], reverse=True)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Update or inspect a compact user preference profile.")
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--user-id", default="default")
    parser.add_argument("--feedback-json", help="FeedbackEvent JSON object to apply.")
    parser.add_argument("--show-hints", action="store_true")
    args = parser.parse_args()

    profile = UserPreferenceProfile.load(args.profile, args.user_id)
    if args.feedback_json:
        profile.apply_feedback(FeedbackEvent.from_dict(json.loads(args.feedback_json)))
        profile.save(args.profile)
    if args.show_hints or not args.feedback_json:
        print(json.dumps({"profile": asdict(profile), "parameter_hints": profile.parameter_hints()}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
