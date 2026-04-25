"""Build the scene-first recommender graph from raw scenario Markdown files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_DIR = REPO_ROOT / "raw"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "graphify-out"
DEFAULT_GRAPH_PATH = DEFAULT_OUTPUT_DIR / "scene_recommender_graph.json"
DEFAULT_CYPHER_PATH = DEFAULT_OUTPUT_DIR / "cypher_scene_recommender.txt"
DEFAULT_REPORT_PATH = DEFAULT_OUTPUT_DIR / "SCENE_RECOMMENDER_REPORT.md"

RECOMMENDATION_CHANNELS = {
    "trend": 0.74,
    "general": 0.82,
    "personalized": 0.78,
}

PREFIX_RULES: dict[str, tuple[list[str], str, str]] = {
    "subject": (["SceneFacet", "Subject"], "HAS_SUBJECT", "subject"),
    "environment": (["SceneFacet", "Environment"], "HAS_ENVIRONMENT", "environment"),
    "light": (["SceneFacet", "Light"], "HAS_LIGHT", "light"),
    "lens": (["SceneFacet", "LensMode"], "USES_LENS", "lens"),
    "lens_mode": (["SceneFacet", "LensMode"], "USES_LENS", "lens"),
    "mode": (["SceneFacet", "LensMode"], "USES_MODE", "mode"),
    "camera": (["SceneFacet", "Device"], "HAS_FACET", "camera"),
    "composition": (["SceneFacet", "Composition"], "HAS_FACET", "composition"),
    "human_element": (["SceneFacet", "Subject"], "HAS_SUBJECT", "human_element"),
    "shot_set": (["SceneFacet", "ShotSet"], "HAS_FACET", "shot_set"),
    "motion": (["SceneFacet", "Motion"], "HAS_FACET", "motion"),
    "edit": (["SceneFacet", "Technique"], "USES_TECHNIQUE", "edit"),
    "edit_style": (["EditStyle", "SceneFacet"], "HAS_EDIT_STYLE", "editstyle"),
    "style_recipe": (["StyleRecipe", "SceneFacet"], "USES_STYLE_RECIPE", "stylerecipe"),
    "trend_signal": (["SceneFacet", "TrendSignal"], "HAS_TREND_SIGNAL", "trendsignal"),
    "personal_signal": (["SceneFacet", "PersonalizationSignal"], "HAS_PERSONALIZATION_SIGNAL", "preference"),
    "personalization_signal": (["SceneFacet", "PersonalizationSignal"], "HAS_PERSONALIZATION_SIGNAL", "preference"),
    "preference": (["SceneFacet", "Preference"], "HAS_PERSONALIZATION_SIGNAL", "preference"),
    "satisfaction_signal": (["SceneFacet", "SatisfactionSignal"], "HAS_SATISFACTION_SIGNAL", "satisfactionsignal"),
    "tech": (["Technique"], "USES_TECHNIQUE", "tech"),
    "technique": (["Technique"], "USES_TECHNIQUE", "tech"),
    "param": (["Parameter"], "SETS_PARAMETER", "param"),
    "parameter": (["Parameter"], "SETS_PARAMETER", "param"),
    "out": (["Outcome"], "OPTIMIZES", "out"),
    "outcome": (["Outcome"], "OPTIMIZES", "out"),
    "issue": (["ImageIssue", "Risk"], "HAS_RISK", "issue"),
    "risk": (["Risk", "ImageIssue"], "HAS_RISK", "risk"),
    "platform": (["Platform", "SceneFacet"], "HAS_FACET", "platform"),
    "season": (["Season", "SceneFacet"], "HAS_FACET", "season"),
    "device": (["Device", "SceneFacet"], "HAS_FACET", "device"),
}

GLOBAL_OUTCOMES = {
    "out_natural_skin_tone": "Natural skin tone",
    "out_background_separation": "Background separation",
    "out_highlight_preservation": "Highlight preservation",
    "out_face_clarity": "Face clarity",
    "out_texture_detail": "Texture detail",
    "out_geometry_control": "Geometry control",
    "out_motion_story": "Motion story",
    "out_color_accuracy": "Color accuracy",
    "out_storytelling": "Storytelling",
    "out_social_readiness": "Social-ready crop/export",
}


class SceneGraphBuilder:
    def __init__(self, raw_dir: Path):
        self.raw_dir = raw_dir
        self.nodes: dict[str, dict[str, object]] = {}
        self.edges: list[dict[str, object]] = []
        self.edge_keys: set[tuple[str, str, str]] = set()

    def build(self) -> dict[str, object]:
        self._add_global_nodes()
        for path in sorted((self.raw_dir / "scenarios").glob("*.md")):
            self._add_scenario(path)
        return {
            "nodes": list(self.nodes.values()),
            "edges": self.edges,
        }

    def _add_global_nodes(self) -> None:
        self.add_node(
            "answer_renderer_contract",
            ["RuntimeContract"],
            {
                "id": "answer_renderer_contract",
                "name": "Natural answer renderer contract",
                "source_file": "scripts/recommender/answer_renderer.py",
            },
        )
        for node_id, name in GLOBAL_OUTCOMES.items():
            self.add_node(node_id, ["Outcome"], {"id": node_id, "name": name})

    def _add_scenario(self, path: Path) -> None:
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        rel = path.relative_to(REPO_ROOT).as_posix()
        title = str(meta.get("title") or first_heading(body) or path.stem)
        scenario_id = f"scenario_{path.stem}"
        aliases = unique_list(list_value(meta, "aliases") + list_value(meta, "query_aliases"))
        tags = list_value(meta, "scenario_tags")
        urls = collect_urls(meta, body)

        self.add_node(
            scenario_id,
            ["Scenario"],
            {
                "id": scenario_id,
                "name": title,
                "source_file": rel,
                "tags": tags,
                "aliases": aliases,
            },
        )
        source_evidence_id = f"evidence_{rel.replace('/', '_')}"
        self.add_node(
            source_evidence_id,
            ["Evidence"],
            {
                "id": source_evidence_id,
                "name": title,
                "source_file": rel,
                "source_type": "raw_markdown",
            },
        )
        self.add_edge(scenario_id, source_evidence_id, "SUPPORTED_BY")
        self.add_edge(scenario_id, "answer_renderer_contract", "RENDERED_BY", confidence="INFERRED", weight=0.8)

        for alias in aliases:
            alias_id = f"alias_{stable_slug(alias)}"
            self.add_node(alias_id, ["QueryAlias"], {"id": alias_id, "name": alias, "source_file": rel})
            self.add_edge(alias_id, scenario_id, "MATCHES_SCENARIO")

        facet_nodes = self._add_graph_nodes(scenario_id, rel, meta)
        extracted_techniques = self._add_extracted_relation_techniques(scenario_id, path.stem, rel, meta)
        url_nodes = self._add_evidence_urls(scenario_id, rel, urls)

        shot_techniques = self._add_section_nodes(path.stem, rel, body, "촬영 레시피", "Technique", "tech")
        edit_parameters = self._add_section_nodes(path.stem, rel, body, "보정 레시피", "Parameter", "param")
        risks = self._add_section_nodes(path.stem, rel, body, "실패 방지 / 주의점", "Risk", "risk")
        outcomes = self._infer_outcomes(tags, list_value(meta, "graph_nodes"))
        preferences = [node_id for prefix, node_id in facet_nodes if prefix in {"preference", "personal_signal", "personalization_signal"}]

        for channel, score in RECOMMENDATION_CHANNELS.items():
            rec_id = f"rec_{channel}_{path.stem}"
            self.add_node(
                rec_id,
                ["Recommendation"],
                {
                    "id": rec_id,
                    "name": f"{channel.title()} recommendation — {title}",
                    "channel": channel,
                    "rank_score": score,
                    "source_file": rel,
                },
            )
            self.add_edge(scenario_id, rec_id, "HAS_RECOMMENDATION")
            self.add_edge(rec_id, source_evidence_id, "SUPPORTED_BY")
            self.add_edge(rec_id, "answer_renderer_contract", "RENDERED_BY", confidence="INFERRED", weight=0.8)
            for node_id in url_nodes:
                self.add_edge(rec_id, node_id, "SUPPORTED_BY", source_file=rel, source_url=self.nodes[node_id]["properties"]["url"])
            for _prefix, node_id in facet_nodes:
                self.add_edge(rec_id, node_id, "USES_FACET", confidence="INFERRED", weight=0.7)
            for node_id in shot_techniques:
                self.add_edge(rec_id, node_id, "USES_TECHNIQUE")
            for node_id in edit_parameters:
                self.add_edge(rec_id, node_id, "SETS_PARAMETER")
            for node_id in risks:
                self.add_edge(rec_id, node_id, "AVOIDS")
            for node_id in outcomes:
                self.add_edge(rec_id, node_id, "OPTIMIZES", confidence="INFERRED", weight=0.65)
            for node_id in preferences:
                self.add_edge(rec_id, node_id, "ADAPTS_TO", confidence="INFERRED", weight=0.7)

    def _add_graph_nodes(self, scenario_id: str, source_file: str, meta: dict[str, object]) -> list[tuple[str, str]]:
        result: list[tuple[str, str]] = []
        for raw in list_value(meta, "graph_nodes"):
            prefix, value = split_graph_node(raw)
            labels, relation, id_prefix = PREFIX_RULES.get(prefix, (["SceneFacet"], "HAS_FACET", prefix or "facet"))
            node_id = f"{id_prefix}_{stable_slug(value)}"
            self.add_node(
                node_id,
                labels,
                {
                    "id": node_id,
                    "key": prefix,
                    "value": value,
                    "name": value.replace("_", " "),
                    "source_file": source_file,
                },
            )
            self.add_edge(scenario_id, node_id, relation)
            result.append((prefix, node_id))
        return result

    def _add_extracted_relation_techniques(
        self,
        scenario_id: str,
        slug: str,
        source_file: str,
        meta: dict[str, object],
    ) -> list[str]:
        node_ids: list[str] = []
        for raw in list_value(meta, "graph_edges"):
            name = raw.strip()
            if not name:
                continue
            node_id = f"tech_{stable_slug(slug)}_{stable_slug(name)}"
            self.add_node(
                node_id,
                ["Technique"],
                {
                    "id": node_id,
                    "name": name,
                    "source_file": source_file,
                    "extracted_edge": True,
                },
            )
            self.add_edge(scenario_id, node_id, "USES_TECHNIQUE")
            node_ids.append(node_id)
        return node_ids

    def _add_evidence_urls(self, scenario_id: str, source_file: str, urls: list[str]) -> list[str]:
        node_ids: list[str] = []
        for url in urls:
            node_id = f"evidence_url_{stable_slug(url)}"
            parsed = urlparse(url)
            domain = parsed.netloc.lower().removeprefix("www.")
            self.add_node(
                node_id,
                ["Evidence"],
                {
                    "id": node_id,
                    "name": evidence_label(url),
                    "source_file": source_file,
                    "source_type": "external_url",
                    "url": url,
                    "domain": domain,
                },
            )
            self.add_edge(scenario_id, node_id, "SUPPORTED_BY", source_file=source_file, source_url=url)
            node_ids.append(node_id)
        return node_ids

    def _add_section_nodes(self, slug: str, source_file: str, body: str, heading: str, label: str, prefix: str) -> list[str]:
        node_ids: list[str] = []
        for bullet in section_bullets(body, heading):
            node_id = f"{prefix}_{stable_slug(slug)}_{stable_slug(bullet, max_len=96)}"
            self.add_node(
                node_id,
                [label],
                {
                    "id": node_id,
                    "name": bullet,
                    "source_file": source_file,
                    "section": heading,
                },
            )
            node_ids.append(node_id)
        return node_ids

    @staticmethod
    def _infer_outcomes(tags: list[str], graph_nodes: list[str]) -> list[str]:
        corpus = " ".join([*tags, *graph_nodes]).lower()
        outcomes = {"out_social_readiness"}
        if any(token in corpus for token in ("portrait", "person", "woman", "selfie", "group", "skin")):
            outcomes.update({"out_natural_skin_tone", "out_face_clarity", "out_background_separation"})
        if any(token in corpus for token in ("backlight", "highlight", "night", "stage", "snow", "beach", "sky")):
            outcomes.add("out_highlight_preservation")
        if any(token in corpus for token in ("food", "macro", "product", "texture", "dessert", "drink", "flower")):
            outcomes.update({"out_texture_detail", "out_color_accuracy"})
        if any(token in corpus for token in ("geometry", "wide", "architecture", "flatlay", "mirror")):
            outcomes.add("out_geometry_control")
        if any(token in corpus for token in ("travel", "market", "story", "documentary")):
            outcomes.add("out_storytelling")
        if any(token in corpus for token in ("action", "motion", "runner", "cyclist", "pets", "children")):
            outcomes.add("out_motion_story")
        return sorted(outcomes)

    def add_node(self, node_id: str, labels: list[str], properties: dict[str, object]) -> None:
        if node_id in self.nodes:
            node = self.nodes[node_id]
            props = node["properties"]
            if isinstance(props, dict):
                source_files = set(str(props.get("source_files", "")).split("|"))
                source_file = properties.get("source_file")
                if source_file:
                    source_files.add(str(source_file))
                props["source_files"] = "|".join(sorted(item for item in source_files if item))
            return
        self.nodes[node_id] = {
            "id": node_id,
            "labels": labels,
            "properties": properties,
        }

    def add_edge(
        self,
        source: str,
        target: str,
        edge_type: str,
        *,
        confidence: str = "EXTRACTED",
        weight: float = 1.0,
        **properties: object,
    ) -> None:
        key = (source, target, edge_type)
        if key in self.edge_keys:
            return
        self.edge_keys.add(key)
        self.edges.append(
            {
                "source": source,
                "target": target,
                "type": edge_type,
                "properties": {
                    "confidence": confidence,
                    "weight": weight,
                    **properties,
                },
            }
        )


def build_scene_graph(raw_dir: Path = DEFAULT_RAW_DIR) -> dict[str, object]:
    return SceneGraphBuilder(raw_dir).build()


def run(raw_dir: Path = DEFAULT_RAW_DIR, output_dir: Path = DEFAULT_OUTPUT_DIR) -> dict[str, object]:
    graph = build_scene_graph(raw_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    graph_path = output_dir / "scene_recommender_graph.json"
    cypher_path = output_dir / "cypher_scene_recommender.txt"
    report_path = output_dir / "SCENE_RECOMMENDER_REPORT.md"
    graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cypher_path.write_text(to_cypher(graph), encoding="utf-8")
    report_path.write_text(render_report(graph), encoding="utf-8")
    print(f"Scene recommender graph rebuilt: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    print(f"Output: {graph_path}")
    return graph


def render_report(graph: dict[str, object]) -> str:
    nodes = list(graph.get("nodes", []))
    edges = list(graph.get("edges", []))
    labels = Counter(label for node in nodes for label in node.get("labels", []))
    scenarios = [node for node in nodes if node.get("labels") == ["Scenario"]]
    recommendations = [node for node in nodes if node.get("labels") == ["Recommendation"]]
    channels = Counter(str(node.get("properties", {}).get("channel", "unknown")) for node in recommendations)
    lines = [
        "# Scene Recommender Graph Report",
        "",
        "Generated from `raw/scenarios/*.md` by `scripts/recommender/scene_graph_builder.py`.",
        "",
        "## Summary",
        "",
        f"- Nodes: {len(nodes)}",
        f"- Edges: {len(edges)}",
        f"- Scenarios: {len(scenarios)}",
        f"- Recommendations: {len(recommendations)}",
        "",
        "## Recommendation Channels",
        "",
    ]
    for channel, count in sorted(channels.items()):
        lines.append(f"- {channel}: {count}")
    lines.extend(["", "## Top Labels", ""])
    for label, count in labels.most_common(12):
        lines.append(f"- {label}: {count}")
    lines.extend(["", "## Scenario Files", ""])
    for node in sorted(scenarios, key=lambda item: str(item["id"])):
        props = node.get("properties", {})
        lines.append(f"- `{node['id']}`: {props.get('source_file')}")
    return "\n".join(lines).rstrip() + "\n"


def to_cypher(graph: dict[str, object]) -> str:
    lines = [
        "// Generated by scripts/recommender/scene_graph_builder.py",
        "CREATE CONSTRAINT scene_node_id IF NOT EXISTS FOR (n:SceneNode) REQUIRE n.id IS UNIQUE;",
        "",
    ]
    for node in graph.get("nodes", []):
        labels = [sanitize_label(label) for label in node.get("labels", [])]
        label_text = ":".join(["SceneNode", *labels])
        props = dict(node.get("properties", {}))
        props.setdefault("id", node["id"])
        lines.append(f"MERGE (n:{label_text} {{id: {cypher_value(node['id'])}}})")
        lines.append(f"SET n += {cypher_value(props)};")
    lines.append("")
    for edge in graph.get("edges", []):
        edge_type = sanitize_label(edge["type"]).upper()
        lines.append(f"MATCH (a:SceneNode {{id: {cypher_value(edge['source'])}}}), (b:SceneNode {{id: {cypher_value(edge['target'])}}})")
        lines.append(f"MERGE (a)-[r:{edge_type}]->(b)")
        lines.append(f"SET r += {cypher_value(edge.get('properties', {}))};")
    return "\n".join(lines) + "\n"


def cypher_value(value: object) -> str:
    if isinstance(value, dict):
        items = ", ".join(f"{sanitize_property_key(str(k))}: {cypher_value(v)}" for k, v in sorted(value.items()))
        return "{" + items + "}"
    if isinstance(value, list):
        return "[" + ", ".join(cypher_value(item) for item in value) + "]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if value is None:
        return "null"
    return json.dumps(str(value), ensure_ascii=False)


def sanitize_label(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", value).strip("_")
    return cleaned or "Concept"


def sanitize_property_key(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", value).strip("_")
    if not cleaned:
        return "value"
    if cleaned[0].isdigit():
        return f"p_{cleaned}"
    return cleaned


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.S)
    if not match:
        return {}, text
    meta: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in match.group(1).splitlines():
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
    return meta, text[match.end() :]


def collect_urls(meta: dict[str, object], body: str) -> list[str]:
    urls = list_value(meta, "urls")
    urls.extend(re.findall(r"https?://[^\s)>\]]+", body))
    return unique_list(url.strip().rstrip(".,") for url in urls if url.strip().startswith(("http://", "https://")))


def section_bullets(body: str, heading: str) -> list[str]:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", flags=re.M)
    match = pattern.search(body)
    if not match:
        return []
    rest = body[match.end() :]
    next_heading = re.search(r"^##\s+", rest, flags=re.M)
    section = rest[: next_heading.start()] if next_heading else rest
    bullets: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        value = clean_markdown(stripped[2:])
        if value:
            bullets.append(value)
    return bullets


def first_heading(body: str) -> str | None:
    match = re.search(r"^#\s+(.+)$", body, flags=re.M)
    return match.group(1).strip() if match else None


def split_graph_node(raw: str) -> tuple[str, str]:
    if ":" not in raw:
        return "facet", raw.strip()
    prefix, value = raw.split(":", 1)
    return prefix.strip().lower(), value.strip()


def list_value(meta: dict[str, object], key: str) -> list[str]:
    value = meta.get(key)
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def unique_list(values) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(text)
    return result


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")):
        value = value[1:-1]
    return value.strip()


def clean_markdown(value: str) -> str:
    value = re.sub(r"\*\*(.*?)\*\*", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return re.sub(r"\s+", " ", value).strip()


def evidence_label(url: str) -> str:
    parsed = urlparse(url)
    domain = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.strip("/")
    if path:
        path = path.split("/")[-1] or path.split("/")[-2]
    return f"{domain}/{path}" if path else domain


def stable_slug(value: str, max_len: int = 72) -> str:
    normalized = value.lower().strip()
    normalized = re.sub(r"[^a-z0-9가-힣]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
    if not normalized:
        normalized = "node"
    return f"{normalized[:max_len].strip('_')}_{digest}"


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Regenerate scene-first recommender graph from raw scenarios.")
    parser.add_argument("--input", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args(argv)
    run(args.input, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
