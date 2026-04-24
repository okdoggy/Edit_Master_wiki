"""Image observation facet contract and a text/vision-output adapter.

This is not a computer-vision model. It is the stable interface between a future
vision analyzer and the scene-first graph matcher. Until a real image analyzer
is wired in, it can derive facets from a user caption/query or normalize a JSON
object produced by an external vision model.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .normalization import extract_slots


@dataclass
class ImageObservation:
    id: str
    source: str = "text_or_external_vision"
    subjects: list[str] = field(default_factory=list)
    environments: list[str] = field(default_factory=list)
    lights: list[str] = field(default_factory=list)
    composition: list[str] = field(default_factory=list)
    technical_issues: list[str] = field(default_factory=list)
    style_preferences: list[str] = field(default_factory=list)
    device_or_app: list[str] = field(default_factory=list)
    confidence: dict[str, float] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    def to_matcher_query(self, original_query: str = "") -> str:
        parts = [
            original_query,
            *self.subjects,
            *self.environments,
            *self.lights,
            *self.composition,
            *self.technical_issues,
            *self.style_preferences,
            *self.device_or_app,
        ]
        return " ".join(part for part in parts if part)

    def as_graph_seed(self) -> dict[str, Any]:
        return {
            "ImageObservation": {
                "id": self.id,
                "source": self.source,
            },
            "OBSERVED_AS": {
                "subject": self.subjects,
                "environment": self.environments,
                "light": self.lights,
                "composition": self.composition,
                "device_or_app": self.device_or_app,
            },
            "HAS_ISSUE": self.technical_issues,
            "HAS_PREFERENCE": self.style_preferences,
            "confidence": self.confidence,
        }


def observation_from_text(query: str, observation_id: str | None = None) -> ImageObservation:
    slots = extract_slots(query)
    observation = ImageObservation(id=observation_id or f"obs_{int(time.time())}", source="text_query")
    observation.environments.extend(sorted(slots.where))
    observation.subjects.extend(sorted(slots.what))
    observation.device_or_app.extend(sorted(slots.who | slots.how))
    observation.technical_issues.extend(sorted(slots.issues))
    observation.style_preferences.extend(sorted(slots.preferences))
    observation.confidence = {
        "text_slots": 0.65 if slots.filled_slot_count else 0.25,
        "issues": 0.7 if slots.issues else 0.2,
    }
    observation.raw = {"query_slots": slots.as_dict()}
    return observation


def observation_from_vision_json(data: dict[str, Any], observation_id: str | None = None) -> ImageObservation:
    """Normalize a future vision-model payload into the graph-facing contract.

    Accepted keys are intentionally broad:
    - subject / subjects
    - environment / environments
    - light / lighting
    - composition
    - issues / technical_issues
    - preferences / style_preferences
    - device / app
    """

    observation = ImageObservation(id=observation_id or str(data.get("id") or f"obs_{int(time.time())}"), source=str(data.get("source", "external_vision")))
    observation.subjects = as_list(data.get("subjects", data.get("subject")))
    observation.environments = as_list(data.get("environments", data.get("environment")))
    observation.lights = as_list(data.get("lights", data.get("lighting", data.get("light"))))
    observation.composition = as_list(data.get("composition"))
    observation.technical_issues = as_list(data.get("technical_issues", data.get("issues")))
    observation.style_preferences = as_list(data.get("style_preferences", data.get("preferences")))
    observation.device_or_app = as_list(data.get("device_or_app", data.get("device", data.get("app"))))
    observation.confidence = {str(k): float(v) for k, v in dict(data.get("confidence", {})).items()}
    observation.raw = data
    return observation


def merge_observations(*observations: ImageObservation) -> ImageObservation:
    if not observations:
        raise ValueError("At least one observation is required.")
    merged = ImageObservation(id=observations[0].id, source="+".join(obs.source for obs in observations))
    for field_name in ("subjects", "environments", "lights", "composition", "technical_issues", "style_preferences", "device_or_app"):
        values: list[str] = []
        for obs in observations:
            values.extend(getattr(obs, field_name))
        setattr(merged, field_name, sorted(set(values)))
    merged.confidence = {}
    for obs in observations:
        merged.confidence.update(obs.confidence)
    merged.raw = {"merged": [asdict(obs) for obs in observations]}
    return merged


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list | tuple | set):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Create a graph-ready ImageObservation facet payload.")
    parser.add_argument("--query", default="", help="User query/caption to derive facets from.")
    parser.add_argument("--vision-json", type=Path, help="Optional JSON payload from a vision analyzer.")
    parser.add_argument("--observation-id", default=None)
    args = parser.parse_args()

    observations: list[ImageObservation] = []
    if args.query:
        observations.append(observation_from_text(args.query, args.observation_id))
    if args.vision_json:
        observations.append(observation_from_vision_json(json.loads(args.vision_json.read_text(encoding="utf-8")), args.observation_id))
    if not observations:
        parser.error("Provide --query, --vision-json, or both.")

    observation = merge_observations(*observations) if len(observations) > 1 else observations[0]
    print(json.dumps({"observation": asdict(observation), "graph_seed": observation.as_graph_seed()}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
