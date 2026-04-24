"""Raw-data intake harness for source-backed scenario collection.

The harness intentionally separates research from promotion:

1. Generate parallel task briefs for Codex/Claude workers.
2. Workers create candidates under raw/_incoming.
3. Validate source quality, required format, and overlap.
4. Promote only validated candidates into raw/scenarios.
"""

from __future__ import annotations

import asyncio
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


REQUIRED_KEYS = ("scenario_tags", "aliases", "graph_nodes", "graph_edges", "urls")
REQUIRED_BODY_MARKERS = (
    "추천 시스템용 요약",
    "촬영 레시피",
    "보정 레시피",
    "근거",
    "Graphify 추출 힌트",
)

OFFICIAL_DOMAINS = {
    "adobe.com",
    "helpx.adobe.com",
    "support.apple.com",
    "apple.com",
    "support.google.com",
    "blog.google",
    "samsung.com",
    "help.shopify.com",
    "shopify.com",
}

EXPERT_DOMAINS = {
    "nationalgeographic.com",
    "masterclass.com",
    "bhphotovideo.com",
    "petapixel.com",
    "fstoppers.com",
    "photographylife.com",
    "digitalcameraworld.com",
    "dpreview.com",
    "time.com",
    "wired.com",
}

SOCIAL_DOMAINS = {
    "youtube.com",
    "youtu.be",
    "instagram.com",
    "tiktok.com",
    "x.com",
    "twitter.com",
    "threads.net",
}

COMMUNITY_DOMAINS = {
    "reddit.com",
    "community.adobe.com",
    "discussions.apple.com",
}

TRUSTED_CLASSES = {"official", "expert", "creator_social", "community"}

DEFAULT_TOPIC_SEEDS = (
    "스마트폰으로 기차나 버스 창가 여행 인물 사진을 찍고, 유리 반사와 얼굴 노출을 함께 제어하는 시나리오",
    "실내 식물과 작은 오브제를 창가 자연광으로 촬영하고 초록색/질감을 자연스럽게 보정하는 시나리오",
    "헬스장 거울 운동 기록 사진에서 형광등 색과 거울 얼룩, 몸 비율 왜곡을 제어하는 시나리오",
    "호텔 방 또는 에어비앤비 숙소를 넓고 깨끗하게 찍되 초광각 왜곡을 줄이는 시나리오",
    "박물관 유리 진열장 속 전시물을 반사와 저조도 없이 기록하는 시나리오",
    "홈 오피스/책상 셋업 사진을 깔끔한 생산성 스타일로 촬영하고 색을 정리하는 시나리오",
    "비 오는 날 차 안에서 창문 물방울과 바깥 네온을 함께 담는 감성 시나리오",
    "스마트폰으로 향수/주얼리 같은 작은 광택 제품을 매크로와 반사판으로 찍는 시나리오",
)


LATEST_EXPERT_TOPIC_THEMES = (
    "portrait_skin_tone_2026: 2026년 기준 전문가/공식 문서 기반 스마트폰 인물 촬영 및 보정 기법: 자연스러운 피부톤, 얼굴 노출, 배경 분리",
    "backlight_hdr_highlight_recovery_2026: 2026년 기준 전문가/공식 문서 기반 역광/하이라이트 제어 촬영 및 보정 기법: HDR, 마스크, highlight recovery",
    "low_light_noise_white_balance_2026: 2026년 기준 전문가 튜토리얼 기반 실내 저조도 스마트폰 촬영 및 보정 기법: 노이즈, 셔터, 화이트밸런스",
    "food_window_light_texture_2026: 2026년 기준 전문가 튜토리얼 기반 음식 사진 촬영 및 보정 기법: 창가광, 식감, 따뜻한 색, 과보정 방지",
    "travel_street_social_crop_2026: 2026년 기준 전문가/creator 기반 여행·거리 사진 촬영 및 보정 기법: 스토리텔링, 색감, vertical/social crop",
    "product_reflection_color_accuracy_2026: 2026년 기준 전문가/공식 문서 기반 제품/소품 사진 촬영 및 보정 기법: 반사 제어, 정확한 색, 커머스 썸네일",
    "landscape_sky_dynamic_range_2026: 2026년 기준 전문가 튜토리얼 기반 풍경·하늘 사진 촬영 및 보정 기법: dynamic range, dehaze, 자연스러운 색",
    "sns_no_filter_clean_edit_2026: 2026년 기준 전문가/creator 기반 SNS용 자연스러운 no-filter/clean edit 스타일 촬영 및 보정 기법",
    "motion_burst_panning_2026: 2026년 기준 전문가/공식 문서 기반 움직이는 피사체 촬영 및 보정 기법: burst, motion blur, panning, 선명도",
    "night_city_neon_noise_2026: 2026년 기준 전문가 튜토리얼 기반 야간 도시/네온 사진 촬영 및 보정 기법: 색 번짐, 노이즈, 분위기 보존",
    "seasonal_photo_styles_2026: 2026년 기준 전문가/creator 기반 계절성 사진 스타일 촬영 및 보정 기법: 봄꽃, 단풍, 눈, 여름 해변",
    "mobile_lightroom_workflow_2026: 2026년 기준 전문가/공식 문서 기반 모바일 Lightroom/Photos 편집 워크플로: masks, curves, HSL, preset 강도 조절",
    "group_family_best_face_2026: 2026년 기준 전문가 튜토리얼 기반 그룹/가족 사진 촬영 및 보정 기법: 표정 선택, 얼굴 균형, 왜곡 방지",
    "cafe_lifestyle_natural_light_2026: 2026년 기준 전문가/creator 기반 카페·라이프스타일 사진 촬영 및 보정 기법: 자연광, 따뜻한 톤, 과한 필터 방지",
    "mobile_raw_dng_editing_2026: 2026년 기준 전문가/공식 문서 기반 RAW/DNG 모바일 촬영 및 보정 기법: 노출 여유, 색 보정, 파일 관리",
    "editing_failure_guardrails_2026: 2026년 기준 전문가/커뮤니티 합의 기반 보정 실패 방지 기법: halo, oversharpening, orange skin, crushed blacks",
)


def default_topics(count: int) -> list[str]:
    """Return source-backed default topics for latest expert technique collection."""
    requested = max(0, count)
    if requested <= len(LATEST_EXPERT_TOPIC_THEMES):
        return list(LATEST_EXPERT_TOPIC_THEMES[:requested])
    topics = list(LATEST_EXPERT_TOPIC_THEMES)
    for index in range(len(topics) + 1, requested + 1):
        topics.append(
            f"2026년 기준 전문가/공식/creator 최신 사진 촬영 및 보정 기법 확장 조사 #{index}: "
            "기존 raw와 겹치지 않는 스마트폰 시나리오를 외부 근거로 발굴"
        )
    return topics


@dataclass(frozen=True)
class InventoryItem:
    slug: str
    title: str
    aliases: set[str]
    graph_nodes: set[str]
    path: Path


def load_inventory(raw_dir: Path) -> list[InventoryItem]:
    scenario_dir = raw_dir / "scenarios"
    items: list[InventoryItem] = []
    for path in sorted(scenario_dir.glob("*.md")):
        meta, _ = parse_markdown(path)
        aliases = set(list_value(meta, "aliases")) | set(list_value(meta, "query_aliases"))
        items.append(
            InventoryItem(
                slug=path.stem,
                title=str(meta.get("title") or path.stem),
                aliases={normalize_text(alias) for alias in aliases if alias},
                graph_nodes={normalize_text(node) for node in list_value(meta, "graph_nodes")},
                path=path,
            )
        )
    return items


def create_agent_briefs(
    *,
    root: Path,
    raw_dir: Path,
    incoming_dir: Path,
    source_notes_dir: Path,
    runs_dir: Path,
    topics: list[str],
    run_id: str | None,
    engine: str,
    parallel: str,
    min_sources: int,
) -> dict[str, Any]:
    inventory = load_inventory(raw_dir)
    selected_topics = topics or list(DEFAULT_TOPIC_SEEDS)
    if not selected_topics:
        raise SystemExit("No topics supplied and no default topic seeds available.")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    actual_run_id = run_id or f"raw-intake-{timestamp}"
    run_dir = runs_dir / actual_run_id
    task_dir = run_dir / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)
    incoming_dir.mkdir(parents=True, exist_ok=True)
    source_notes_dir.mkdir(parents=True, exist_ok=True)

    used_slugs = {item.slug for item in inventory}
    tasks: list[dict[str, Any]] = []
    for index, topic in enumerate(selected_topics, start=1):
        slug = unique_slug(suggest_slug(topic), used_slugs)
        used_slugs.add(slug)
        candidate_path = incoming_dir / f"{slug}.md"
        source_note_path = source_notes_dir / f"{slug}.json"
        task_path = task_dir / f"task_{index:02d}_{slug}.md"
        task_text = render_agent_task(
            root=root,
            topic=topic,
            slug=slug,
            candidate_path=candidate_path,
            source_note_path=source_note_path,
            inventory=inventory,
            min_sources=min_sources,
        )
        task_path.write_text(task_text, encoding="utf-8", newline="\n")
        tasks.append(
            {
                "index": index,
                "topic": topic,
                "slug": slug,
                "task_path": str(task_path),
                "candidate_path": str(candidate_path),
                "source_note_path": str(source_note_path),
            }
        )

    max_parallel = len(tasks) if parallel == "max" else max(1, int(parallel))
    manifest = {
        "run_id": actual_run_id,
        "created_at": timestamp,
        "engine": engine,
        "max_parallel": min(max_parallel, len(tasks)),
        "task_count": len(tasks),
        "tasks": tasks,
        "validate_command": "uv run edit-master raw validate --scope incoming",
        "promote_command": "uv run edit-master raw promote --build",
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    (run_dir / "RUN_PARALLEL.md").write_text(render_parallel_readme(root, tasks, engine), encoding="utf-8", newline="\n")
    return manifest


def render_agent_task(
    *,
    root: Path,
    topic: str,
    slug: str,
    candidate_path: Path,
    source_note_path: Path,
    inventory: list[InventoryItem],
    min_sources: int,
) -> str:
    inventory_lines = "\n".join(
        f"- {item.slug}: {item.title}; aliases={', '.join(sorted(item.aliases)[:8])}"
        for item in inventory
    )
    return f"""# Edit Master Raw Intake Task

You are one worker in a parallel raw-data intake run. Work only on this task.

## Topic
{topic}

## Write Scope
- Candidate raw scenario: `{candidate_path}`
- Source note JSON: `{source_note_path}`

Do not edit `raw/scenarios/`, `graphify-out/`, `scripts/`, or unrelated files.

## Non-Negotiable Rules
- Do not stitch together existing raw files. Use the inventory below only to avoid overlap.
- Browse or otherwise verify real external sources before writing the candidate.
- Prefer sources published/updated in 2025-2026, or current official documentation with a clear recency note.
- Use at least {min_sources} external URLs in `urls:`.
- At least one source must be official, expert/tutorial, recognized creator/SNS, or practical community consensus.
- Paraphrase. Do not copy long source passages.
- The scenario must follow this conceptual path:
  `TrendSignal + Preference -> EditStyle / StyleRecipe -> Scenario -> RecommendationVariant -> Technique / Parameter -> Evidence`.
- Image issues are only modifiers/guardrails.

## Candidate Markdown Contract

```markdown
---
title: "..."
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "YYYY-MM-DD"
scenario_tags:
  - "..."
aliases:
  - "..."
query_aliases:
  - "..."
graph_nodes:
  - "subject:..."
  - "trend_signal:..."
  - "preference:..."
  - "edit_style:..."
  - "style_recipe:..."
  - "technique:..."
  - "parameter:..."
  - "issue:..."
graph_edges:
  - "TrendSignal + Preference SELECTS ..."
  - "... CONSTRAINS ..."
urls:
  - "https://..."
---

# Same title

## 추천 시스템용 요약

- **트렌드 추천:** ...
- **일반 추천:** ...
- **개인화 추천 변수:** ...

## 촬영 레시피

...

## 보정 레시피

...

## 실패 방지 / 주의점

...

## 전문가/공식/SNS 근거 반영

### 반영한 외부 근거

- ...

### 시나리오 수정 포인트

- ...

## Graphify 추출 힌트

```yaml
entities:
  - ...
relationships:
  - ...
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://...
```

## Source Note JSON Contract

```json
{{
  "slug": "{slug}",
  "topic": "{topic}",
  "source_summary": [
    {{
      "url": "https://...",
      "source_type": "official|expert|creator_social|community",
      "published_or_updated_at": "YYYY-MM-DD or n/a",
      "recency_note": "...",
      "why_trustworthy": "...",
      "used_for": "..."
    }}
  ],
  "overlap_check": {{
    "closest_existing_scenario": "...",
    "why_distinct": "..."
  }}
}}
```

## Existing Scenario Inventory

{inventory_lines}

## Local Validation

After writing the two files, run:

```powershell
uv run edit-master raw validate --scope incoming
```
"""


def render_parallel_readme(root: Path, tasks: list[dict[str, Any]], engine: str) -> str:
    task_lines = "\n".join(f"- Task {task['index']:02d}: `{task['task_path']}`" for task in tasks)
    command_lines = []
    for task in tasks:
        task_path = task["task_path"]
        if engine in {"codex", "both"}:
            command_lines.append(
                f'Get-Content -Raw "{task_path}" | '
                f'codex --search --sandbox workspace-write --ask-for-approval never exec --cd "{root}" -'
            )
        if engine in {"claude", "both"}:
            command_lines.append(f'claude -p (Get-Content -Raw "{task_path}")')
    commands = "\n".join(command_lines)
    return f"""# Parallel Raw Intake Run

Open one Codex or Claude worker per task. The generated prompts are the source of truth; command syntax may need small adjustment for your local CLI.

## Tasks

{task_lines}

## Suggested Launch Commands

```powershell
{commands}
```

## Gate

```powershell
uv run edit-master raw validate --scope incoming
uv run edit-master raw promote --build
```
"""


def load_run_manifest(runs_dir: Path, run_id: str) -> tuple[Path, dict[str, Any]]:
    run_dir = latest_run_dir(runs_dir) if run_id == "latest" else runs_dir / run_id
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"Raw intake manifest not found: {manifest_path}")
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        raise SystemExit(f"Invalid raw intake manifest: {manifest_path}")
    return run_dir, data


def latest_run_dir(runs_dir: Path) -> Path:
    if not runs_dir.exists():
        raise SystemExit(f"Raw intake runs directory not found: {runs_dir}")
    candidates = [path for path in runs_dir.iterdir() if (path / "manifest.json").exists()]
    if not candidates:
        raise SystemExit(f"No raw intake manifests found under: {runs_dir}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def dispatch_agent_tasks(
    *,
    root: Path,
    runs_dir: Path,
    run_id: str,
    engine: str,
    parallel: str,
    dry_run: bool,
) -> dict[str, Any]:
    run_dir, manifest = load_run_manifest(runs_dir, run_id)
    tasks = list(manifest["tasks"])
    max_parallel = len(tasks) if parallel == "max" else max(1, int(parallel))
    max_parallel = min(max_parallel, len(tasks)) if tasks else 0
    planned = [
        {
            "index": task["index"],
            "slug": task["slug"],
            "task_path": task["task_path"],
            "command": agent_command(root, task, engine),
            "stdin_path": str(task["task_path"]) if engine == "codex" else None,
        }
        for task in tasks
    ]
    if dry_run:
        return {
            "ok": True,
            "run_id": manifest.get("run_id", run_dir.name),
            "engine": engine,
            "max_parallel": max_parallel,
            "dry_run": True,
            "tasks": planned,
        }

    executable = shutil.which(engine)
    if not executable:
        raise SystemExit(f"{engine} CLI not found on PATH. Install and authenticate it, or use --dry-run.")
    assert_engine_runnable(engine, executable)

    results = asyncio.run(run_agent_commands(root=root, run_dir=run_dir, planned=planned, max_parallel=max_parallel))
    return {
        "ok": all(item["returncode"] == 0 for item in results),
        "run_id": manifest.get("run_id", run_dir.name),
        "engine": engine,
        "max_parallel": max_parallel,
        "dry_run": False,
        "tasks": results,
    }


def ensure_agent_engine_ready(engine: str) -> None:
    executable = shutil.which(engine)
    if not executable:
        raise SystemExit(f"{engine} CLI not found on PATH. Install and authenticate it, or use --dry-run.")
    assert_engine_runnable(engine, executable)


def assert_engine_runnable(engine: str, executable: str) -> None:
    try:
        subprocess.run(
            platform_command(engine, ["--version"]),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=15,
            check=False,
        )
    except OSError as exc:
        raise SystemExit(
            f"{engine} CLI was found but could not be executed: {executable}\n"
            f"Reason: {exc}\n"
            "Fix the CLI installation/authentication, or run with --dry-run to only generate task briefs."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise SystemExit(
            f"{engine} CLI did not respond to --version within 15 seconds: {executable}\n"
            "Fix the CLI installation/authentication, or run with --dry-run to only generate task briefs."
        ) from exc


def agent_command(root: Path, task: dict[str, Any], engine: str) -> list[str]:
    task_path = Path(str(task["task_path"]))
    if engine == "codex":
        return platform_command(
            "codex",
            [
                "--search",
                "--sandbox",
                "workspace-write",
                "--ask-for-approval",
                "never",
                "exec",
                "--cd",
                str(root),
                "-",
            ],
        )
    if engine == "claude":
        prompt = task_path.read_text(encoding="utf-8")
        return platform_command("claude", ["-p", prompt])
    raise SystemExit(f"Unknown dispatch engine: {engine}")


def platform_command(command: str, args: list[str]) -> list[str]:
    if os.name == "nt":
        return ["cmd.exe", "/d", "/s", "/c", command, *args]
    return [command, *args]


async def run_agent_commands(
    *,
    root: Path,
    run_dir: Path,
    planned: list[dict[str, Any]],
    max_parallel: int,
) -> list[dict[str, Any]]:
    logs_dir = run_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    semaphore = asyncio.Semaphore(max_parallel or 1)

    async def run_one(item: dict[str, Any]) -> dict[str, Any]:
        async with semaphore:
            started_at = datetime.now(timezone.utc)
            proc = await asyncio.create_subprocess_exec(
                *item["command"],
                cwd=str(root),
                stdin=asyncio.subprocess.PIPE if item.get("stdin_path") else None,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdin_bytes = None
            if item.get("stdin_path"):
                stdin_bytes = Path(str(item["stdin_path"])).read_bytes()
            stdout, stderr = await proc.communicate(stdin_bytes)
            finished_at = datetime.now(timezone.utc)
            log_base = logs_dir / f"task_{int(item['index']):02d}_{item['slug']}"
            (log_base.with_suffix(".stdout.log")).write_bytes(stdout)
            (log_base.with_suffix(".stderr.log")).write_bytes(stderr)
            return {
                "index": item["index"],
                "slug": item["slug"],
                "task_path": item["task_path"],
                "returncode": proc.returncode,
                "started_at": started_at.isoformat(),
                "finished_at": finished_at.isoformat(),
                "stdout_log": str(log_base.with_suffix(".stdout.log")),
                "stderr_log": str(log_base.with_suffix(".stderr.log")),
            }

    return await asyncio.gather(*(run_one(item) for item in planned))


def validate_raw_candidates(
    *,
    raw_dir: Path,
    paths: list[Path],
    min_sources: int,
    max_similarity: float,
    strict_sources: bool = False,
    source_notes_dir: Path | None = None,
) -> dict[str, Any]:
    inventory = load_inventory(raw_dir)
    results = [
        validate_one_candidate(
            path=path,
            inventory=inventory,
            raw_dir=raw_dir,
            min_sources=min_sources,
            max_similarity=max_similarity,
            strict_sources=strict_sources,
            source_notes_dir=source_notes_dir,
        )
        for path in sorted(paths)
    ]
    return {
        "ok": all(item["ok"] for item in results),
        "candidate_count": len(results),
        "results": results,
    }


def validate_one_candidate(
    *,
    path: Path,
    inventory: list[InventoryItem],
    raw_dir: Path,
    min_sources: int,
    max_similarity: float,
    strict_sources: bool,
    source_notes_dir: Path | None,
) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return {
            "path": str(path),
            "slug": path.stem,
            "title": path.stem,
            "ok": False,
            "errors": [f"candidate file missing: {path}"],
            "warnings": [],
            "source_report": [],
            "source_note": None,
        }

    meta, body = parse_markdown(path)

    missing = [key for key in REQUIRED_KEYS if not list_value(meta, key)]
    if missing:
        errors.append(f"missing required frontmatter lists: {', '.join(missing)}")
    if meta.get("category") != "scenarios":
        errors.append('category must be "scenarios"')
    if meta.get("content_type") != "graphify_ready_actionable_recipe":
        errors.append('content_type must be "graphify_ready_actionable_recipe"')
    for marker in REQUIRED_BODY_MARKERS:
        if marker not in body:
            errors.append(f"missing body section marker: {marker}")

    title = str(meta.get("title") or path.stem)
    aliases = {normalize_text(value) for value in list_value(meta, "aliases") + list_value(meta, "query_aliases") if value}
    graph_nodes = {normalize_text(value) for value in list_value(meta, "graph_nodes") if value}
    urls = list_value(meta, "urls")
    source_report = classify_sources(urls)
    valid_source_count = sum(1 for item in source_report if item["source_class"] != "invalid")
    trusted_count = sum(1 for item in source_report if item["source_class"] in TRUSTED_CLASSES)
    if valid_source_count < min_sources:
        errors.append(f"not enough valid external source URLs: {valid_source_count} < {min_sources}")
    invalid = [item["url"] for item in source_report if item["source_class"] == "invalid"]
    if invalid:
        errors.append(f"invalid source URLs: {', '.join(invalid)}")
    if trusted_count < 1:
        errors.append("no trusted official/expert/creator/community source detected")
    if strict_sources:
        unknown = [item["domain"] for item in source_report if item["source_class"] == "unknown"]
        if unknown:
            errors.append(f"unknown source domains in strict mode: {', '.join(sorted(set(unknown)))}")
    else:
        unknown = [item["domain"] for item in source_report if item["source_class"] == "unknown"]
        if unknown:
            warnings.append(f"review unknown source domains: {', '.join(sorted(set(unknown)))}")

    source_note: dict[str, Any] | None = None
    if source_notes_dir is not None:
        source_note = validate_source_note(
            slug=path.stem,
            urls=urls,
            source_notes_dir=source_notes_dir,
            min_sources=min_sources,
            errors=errors,
            warnings=warnings,
        )

    destination = raw_dir / "scenarios" / path.name
    if destination.exists() and destination.resolve() != path.resolve():
        errors.append(f"scenario slug already exists: {path.stem}")

    normalized_title = normalize_text(title)
    for item in inventory:
        if item.path.resolve() == path.resolve():
            continue
        if normalize_text(item.title) == normalized_title:
            errors.append(f"title duplicates existing scenario: {item.slug}")
        alias_overlap = aliases & item.aliases
        if len(alias_overlap) >= 2:
            errors.append(f"aliases overlap existing scenario {item.slug}: {', '.join(sorted(alias_overlap)[:6])}")
        elif alias_overlap:
            warnings.append(f"one alias overlaps existing scenario {item.slug}: {', '.join(sorted(alias_overlap))}")
        similarity = jaccard(graph_nodes, item.graph_nodes)
        if graph_nodes and item.graph_nodes and similarity >= max_similarity:
            errors.append(f"graph_nodes too similar to {item.slug}: {similarity:.2f}")
        elif graph_nodes and item.graph_nodes and similarity >= 0.55:
            warnings.append(f"graph_nodes may overlap {item.slug}: {similarity:.2f}")

    return {
        "path": str(path),
        "slug": path.stem,
        "title": title,
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "source_report": source_report,
        "source_note": source_note,
    }


def promote_candidates(
    *,
    raw_dir: Path,
    paths: list[Path],
    min_sources: int,
    max_similarity: float,
    strict_sources: bool,
    delete_incoming: bool,
    passing_only: bool = False,
    delete_failed: bool = False,
    source_notes_dir: Path | None = None,
) -> dict[str, Any]:
    if not paths:
        return {
            "ok": False,
            "validation": {"ok": False, "candidate_count": 0, "results": []},
            "promoted": [],
            "skipped": [],
            "deleted_failed": [],
        }
    validation = validate_raw_candidates(
        raw_dir=raw_dir,
        paths=paths,
        min_sources=min_sources,
        max_similarity=max_similarity,
        strict_sources=strict_sources,
        source_notes_dir=source_notes_dir,
    )
    if not validation["ok"] and not passing_only:
        return {"ok": False, "validation": validation, "promoted": []}

    result_by_path = {Path(str(item["path"])).resolve(): item for item in validation["results"]}
    paths_to_promote = [path for path in paths if result_by_path.get(path.resolve(), {}).get("ok")]
    skipped = [
        item
        for item in validation["results"]
        if not item["ok"]
    ]
    failed_paths = [Path(str(item["path"])) for item in skipped]
    deleted_failed = delete_candidate_files(failed_paths, source_notes_dir) if delete_failed else []
    if passing_only and not paths_to_promote:
        return {
            "ok": bool(deleted_failed),
            "validation": validation,
            "promoted": [],
            "skipped": skipped,
            "deleted_failed": deleted_failed,
        }
    if not passing_only:
        paths_to_promote = paths

    scenario_dir = raw_dir / "scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    promoted: list[dict[str, str]] = []
    for path in paths_to_promote:
        target = scenario_dir / path.name
        if target.exists():
            raise SystemExit(f"Refusing to overwrite existing scenario: {target}")
        shutil.copyfile(path, target)
        if delete_incoming:
            path.unlink()
            if source_notes_dir is not None:
                note_path = source_notes_dir / f"{path.stem}.json"
                if note_path.exists():
                    note_path.unlink()
        promoted.append({"source": str(path), "target": str(target)})
    update_scenario_manifest(raw_dir, [Path(item["target"]) for item in promoted])
    return {
        "ok": True,
        "validation": validation,
        "promoted": promoted,
        "skipped": skipped,
        "deleted_failed": deleted_failed,
    }


def delete_candidate_files(paths: list[Path], source_notes_dir: Path | None) -> list[dict[str, str]]:
    deleted: list[dict[str, str]] = []
    for path in paths:
        if path.exists():
            path.unlink()
            deleted.append({"type": "candidate", "path": str(path)})
        if source_notes_dir is not None:
            note_path = source_notes_dir / f"{path.stem}.json"
            if note_path.exists():
                note_path.unlink()
                deleted.append({"type": "source_note", "path": str(note_path)})
    return deleted


def update_scenario_manifest(raw_dir: Path, scenario_paths: list[Path]) -> None:
    manifest_path = raw_dir / "manifests" / "scenario_files.csv"
    rows: list[dict[str, str]] = []
    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    by_file = {row["file"]: row for row in rows if row.get("file")}
    for path in scenario_paths:
        meta, _ = parse_markdown(path)
        try:
            rel = path.relative_to(raw_dir.parent).as_posix()
        except ValueError:
            rel = path.as_posix()
        aliases = " | ".join(list_value(meta, "aliases"))
        by_file[rel] = {
            "file": rel,
            "slug": path.stem,
            "title": str(meta.get("title") or path.stem),
            "aliases": aliases,
        }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "slug", "title", "aliases"], lineterminator="\n")
        writer.writeheader()
        for row in sorted(by_file.values(), key=lambda item: item["file"]):
            writer.writerow(row)


def candidate_paths_for_scope(incoming_dir: Path, raw_dir: Path, scope: str, explicit_path: Path | None) -> list[Path]:
    if explicit_path:
        if explicit_path.is_file():
            return [explicit_path]
        return sorted(explicit_path.glob("*.md"))
    if scope == "incoming":
        return sorted(incoming_dir.glob("*.md"))
    if scope == "scenarios":
        return sorted((raw_dir / "scenarios").glob("*.md"))
    raise SystemExit(f"Unknown raw validation scope: {scope}")


def validate_source_note(
    *,
    slug: str,
    urls: list[str],
    source_notes_dir: Path,
    min_sources: int,
    errors: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    note_path = source_notes_dir / f"{slug}.json"
    report: dict[str, Any] = {"path": str(note_path), "exists": note_path.exists(), "ok": False, "source_count": 0}
    local_errors: list[str] = []
    local_warnings: list[str] = []

    if not note_path.exists():
        errors.append(f"source note JSON missing: {note_path}")
        return report

    try:
        data = json.loads(note_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"source note JSON is invalid: {note_path} ({exc})")
        return report

    if not isinstance(data, dict):
        errors.append(f"source note JSON must be an object: {note_path}")
        return report

    if data.get("slug") != slug:
        local_errors.append(f"source note slug must match candidate slug: {slug}")

    summary = data.get("source_summary")
    if not isinstance(summary, list) or not summary:
        local_errors.append("source note requires non-empty source_summary list")
        summary = []

    note_urls: set[str] = set()
    for index, item in enumerate(summary, start=1):
        if not isinstance(item, dict):
            local_errors.append(f"source_summary[{index}] must be an object")
            continue
        url = normalize_url(str(item.get("url") or ""))
        if not url:
            local_errors.append(f"source_summary[{index}] is missing url")
        else:
            note_urls.add(url)
            source_class = classify_sources([url])[0]["source_class"]
            if source_class == "invalid":
                local_errors.append(f"source_summary[{index}] has invalid url: {url}")
        source_type = str(item.get("source_type") or "").strip()
        if source_type not in TRUSTED_CLASSES:
            local_errors.append(
                f"source_summary[{index}] source_type must be one of {', '.join(sorted(TRUSTED_CLASSES))}"
            )
        for key in ("why_trustworthy", "used_for"):
            if not str(item.get(key) or "").strip():
                local_errors.append(f"source_summary[{index}] is missing {key}")
        if not str(item.get("recency_note") or "").strip():
            local_warnings.append(f"source_summary[{index}] is missing recency_note")
        if not str(item.get("published_or_updated_at") or "").strip():
            local_warnings.append(f"source_summary[{index}] is missing published_or_updated_at")

    if len(note_urls) < min_sources:
        local_errors.append(f"source note has too few sources: {len(note_urls)} < {min_sources}")

    frontmatter_urls = {normalize_url(url) for url in urls if normalize_url(url)}
    missing_from_note = sorted(frontmatter_urls - note_urls)
    if missing_from_note:
        local_errors.append(f"source note does not explain frontmatter urls: {', '.join(missing_from_note[:5])}")

    overlap = data.get("overlap_check")
    if not isinstance(overlap, dict):
        local_errors.append("source note requires overlap_check object")
    else:
        if not str(overlap.get("closest_existing_scenario") or "").strip():
            local_warnings.append("source note overlap_check.closest_existing_scenario is empty")
        if not str(overlap.get("why_distinct") or "").strip():
            local_errors.append("source note overlap_check.why_distinct is required")

    errors.extend(local_errors)
    warnings.extend(local_warnings)
    report.update({"ok": not local_errors, "source_count": len(note_urls), "warnings": local_warnings})
    return report


def classify_sources(urls: list[str]) -> list[dict[str, str]]:
    report: list[dict[str, str]] = []
    seen: set[str] = set()
    for url in urls:
        normalized_url = normalize_url(url)
        parsed = urlparse(normalized_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            report.append({"url": url, "domain": "", "source_class": "invalid"})
            continue
        if normalized_url in seen:
            continue
        seen.add(normalized_url)
        domain = parsed.netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        report.append({"url": normalized_url, "domain": domain, "source_class": classify_domain(domain)})
    return report


def classify_domain(domain: str) -> str:
    if domain_matches(domain, OFFICIAL_DOMAINS):
        return "official"
    if domain_matches(domain, EXPERT_DOMAINS):
        return "expert"
    if domain_matches(domain, SOCIAL_DOMAINS):
        return "creator_social"
    if domain_matches(domain, COMMUNITY_DOMAINS):
        return "community"
    return "unknown"


def domain_matches(domain: str, suffixes: set[str]) -> bool:
    return any(domain == suffix or domain.endswith(f".{suffix}") for suffix in suffixes)


def normalize_url(url: str) -> str:
    return url.strip().rstrip(".,)")


def parse_markdown(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    return parse_frontmatter(text)


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.S)
    if not match:
        return {}, text
    meta_text = match.group(1)
    body = text[match.end() :]
    meta: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in meta_text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        key_match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if key_match:
            key, raw_value = key_match.groups()
            current_key = key
            value = clean_scalar(raw_value or "")
            meta[key] = value if value else []
            continue
        item = line.strip()
        if current_key and item.startswith("- "):
            values = meta.setdefault(current_key, [])
            if not isinstance(values, list):
                values = []
                meta[current_key] = values
            values.append(clean_scalar(item[2:]))
    return meta, body


def list_value(meta: dict[str, object], key: str) -> list[str]:
    value = meta.get(key)
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")):
        value = value[1:-1]
    return value.strip()


def normalize_text(value: str) -> str:
    lowered = value.lower().strip()
    lowered = re.sub(r"[\W_]+", " ", lowered, flags=re.UNICODE)
    return re.sub(r"\s+", " ", lowered).strip()


def suggest_slug(topic: str) -> str:
    slug_source = topic
    prefix_match = re.match(r"^([A-Za-z0-9_-]+):", topic)
    if prefix_match:
        slug_source = prefix_match.group(1)
    ascii_slug = re.sub(r"[^a-z0-9]+", "_", slug_source.lower()).strip("_")
    ascii_slug = re.sub(r"_+", "_", ascii_slug)
    if ascii_slug:
        return ascii_slug[:64].strip("_")
    return f"scenario_{short_hash(topic)}"


def unique_slug(slug: str, used: set[str]) -> str:
    candidate = slug or "scenario"
    if candidate not in used:
        return candidate
    base = candidate[:54].rstrip("_") or "scenario"
    counter = 2
    while f"{base}_{counter}" in used:
        counter += 1
    return f"{base}_{counter}"


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


def jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)
