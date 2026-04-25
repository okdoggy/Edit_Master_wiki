"""Configuration loading for the Edit Master harness."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CONFIG_NAME = "edit-master.toml"


@dataclass(frozen=True)
class HarnessConfig:
    root: Path
    raw_dir: Path
    graphify_out_dir: Path
    scene_graph_path: Path
    source_graph_path: Path
    eval_path: Path
    realistic_eval_path: Path
    ambiguous_eval_path: Path
    personalization_dir: Path
    raw_incoming_dir: Path
    raw_source_notes_dir: Path
    raw_intake_runs_dir: Path
    raw_min_sources: int
    raw_max_similarity: float
    min_top1: float
    eval_thresholds: dict[str, dict[str, float]]
    answer_smoke_query: str
    default_user_id: str

    @property
    def bridge_json_path(self) -> Path:
        return self.graphify_out_dir / "source_recommender_bridge.json"

    @property
    def bridge_report_path(self) -> Path:
        return self.graphify_out_dir / "SOURCE_RECOMMENDER_BRIDGE_REPORT.md"


def load_config(config_path: Path | None = None) -> HarnessConfig:
    config_file = config_path.resolve() if config_path else find_config_file()
    root = config_file.parent
    data = read_toml(config_file)

    paths = data.get("paths", {})
    quality = data.get("quality", {})
    user = data.get("user", {})
    raw_intake = data.get("raw_intake", {})

    return HarnessConfig(
        root=root,
        raw_dir=resolve_path(root, paths.get("raw", "raw")),
        graphify_out_dir=resolve_path(root, paths.get("graphify_out", "graphify-out")),
        scene_graph_path=resolve_path(root, paths.get("scene_graph", "graphify-out/scene_recommender_graph.json")),
        source_graph_path=resolve_path(root, paths.get("source_graph", "graphify-out/graph.json")),
        eval_path=resolve_path(root, paths.get("eval", "tests/eval_queries.json")),
        realistic_eval_path=resolve_path(root, paths.get("eval_realistic", "tests/eval_queries_realistic.json")),
        ambiguous_eval_path=resolve_path(root, paths.get("eval_ambiguous", "tests/eval_queries_ambiguous.json")),
        personalization_dir=resolve_path(root, paths.get("personalization", "data/personalization")),
        raw_incoming_dir=resolve_path(root, raw_intake.get("incoming", "raw/_incoming/scenarios")),
        raw_source_notes_dir=resolve_path(root, raw_intake.get("source_notes", "raw/_incoming/source_notes")),
        raw_intake_runs_dir=resolve_path(root, raw_intake.get("runs", "data/raw_intake_runs")),
        raw_min_sources=int(raw_intake.get("min_sources", 2)),
        raw_max_similarity=float(raw_intake.get("max_similarity", 0.72)),
        min_top1=float(quality.get("min_top1", 1.0)),
        eval_thresholds=eval_thresholds(quality),
        answer_smoke_query=str(
            quality.get("answer_smoke_query", "카페 창가 인물 사진을 자연스럽게 보정하고 싶어요")
        ),
        default_user_id=str(user.get("default_user_id", "default")),
    )


def eval_thresholds(quality: dict[str, Any]) -> dict[str, dict[str, float]]:
    raw_thresholds = quality.get("eval_thresholds", {})
    defaults = {
        "regression": {"top1": float(quality.get("min_top1", 1.0)), "top3": 1.0},
        "realistic": {"top1": 0.70, "top3": 0.85},
        "ambiguous": {"top1": 0.50, "top3": 0.85},
    }
    if not isinstance(raw_thresholds, dict):
        return defaults
    for name, values in raw_thresholds.items():
        if not isinstance(values, dict):
            continue
        thresholds = defaults.setdefault(str(name), {})
        for key in ("top1", "top3"):
            if key in values:
                thresholds[key] = float(values[key])
    return defaults


def find_config_file(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        config_file = candidate / CONFIG_NAME
        if config_file.exists():
            return config_file
    package_root = Path(__file__).resolve().parents[1]
    config_file = package_root / CONFIG_NAME
    if config_file.exists():
        return config_file
    raise SystemExit(f"Cannot find {CONFIG_NAME}. Run commands from the repository root or pass --config.")


def read_toml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Config file not found: {path}")
    return tomllib.loads(path.read_text(encoding="utf-8"))


def resolve_path(root: Path, value: object) -> Path:
    path = Path(str(value))
    if path.is_absolute():
        return path
    return root / path
