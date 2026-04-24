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
    personalization_dir: Path
    min_top1: float
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

    return HarnessConfig(
        root=root,
        raw_dir=resolve_path(root, paths.get("raw", "raw")),
        graphify_out_dir=resolve_path(root, paths.get("graphify_out", "graphify-out")),
        scene_graph_path=resolve_path(root, paths.get("scene_graph", "graphify-out/scene_recommender_graph.json")),
        source_graph_path=resolve_path(root, paths.get("source_graph", "graphify-out/graph.json")),
        eval_path=resolve_path(root, paths.get("eval", "tests/eval_queries.json")),
        personalization_dir=resolve_path(root, paths.get("personalization", "data/personalization")),
        min_top1=float(quality.get("min_top1", 1.0)),
        answer_smoke_query=str(
            quality.get("answer_smoke_query", "카페 창가 인물 사진을 자연스럽게 보정하고 싶어요")
        ),
        default_user_id=str(user.get("default_user_id", "default")),
    )


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
