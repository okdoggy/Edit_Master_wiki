from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
GRAPHIFY_DEPS = ROOT / ".graphify-deps"
if GRAPHIFY_DEPS.exists():
    sys.path.insert(0, str(GRAPHIFY_DEPS))

try:
    from graphify.analyze import god_nodes, suggest_questions, surprising_connections
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.detect import detect, save_manifest
    from graphify.export import to_canvas, to_cypher, to_html, to_json, to_obsidian
    from graphify.report import generate
except ImportError as exc:  # pragma: no cover - guidance path
    raise SystemExit(
        "graphify is not installed. Run:\n"
        "  python -m pip install --target .graphify-deps graphifyy"
    ) from exc


NODE_RELATIONS = {
    "subject": "HAS_SUBJECT",
    "environment": "IN_ENVIRONMENT",
    "light": "USES_LIGHT",
    "lens": "USES_LENS",
    "lens_mode": "USES_LENS",
    "mode": "USES_MODE",
    "edit_style": "SUPPORTS_STYLE",
    "style_recipe": "USES_STYLE_RECIPE",
    "personal_signal": "PERSONALIZES_BY",
    "personalization_signal": "PERSONALIZES_BY",
    "preference": "MATCHES_PREFERENCE",
    "trend_signal": "FOLLOWS_TREND",
    "platform": "TARGETS_PLATFORM",
    "season": "FITS_SEASON",
    "device": "USES_DEVICE",
    "tech": "USES_TECHNIQUE",
    "technique": "USES_TECHNIQUE",
    "param": "SETS_PARAMETER",
    "parameter": "SETS_PARAMETER",
    "out": "TARGETS_OUTCOME",
    "outcome": "TARGETS_OUTCOME",
    "issue": "ADJUSTED_BY_ISSUE",
    "risk": "CONSTRAINED_BY_RISK",
    "satisfaction_signal": "OPTIMIZES_FOR",
}

NODE_KINDS = {
    "subject": "SceneFacet",
    "environment": "SceneFacet",
    "light": "SceneFacet",
    "lens": "LensMode",
    "lens_mode": "LensMode",
    "mode": "LensMode",
    "edit_style": "EditStyle",
    "style_recipe": "StyleRecipe",
    "personal_signal": "PersonalizationSignal",
    "personalization_signal": "PersonalizationSignal",
    "preference": "Preference",
    "trend_signal": "TrendSignal",
    "platform": "Platform",
    "season": "Season",
    "device": "Device",
    "tech": "Technique",
    "technique": "Technique",
    "param": "Parameter",
    "parameter": "Parameter",
    "out": "Outcome",
    "outcome": "Outcome",
    "issue": "ImageIssue",
    "risk": "Risk",
    "satisfaction_signal": "SatisfactionSignal",
}

CORE_KIND_ORDER = [
    "TrendSignal",
    "Preference",
    "PersonalizationSignal",
    "EditStyle",
    "StyleRecipe",
    "Scenario",
    "RecommendationVariant",
    "Technique",
    "Parameter",
    "Evidence",
]

EXCLUDED_GRAPH_SOURCE_DIRS = {"manifests"}
EXCLUDED_GRAPH_SOURCE_FILES = {"README.md"}


def should_include_graph_source(path: Path, input_root: Path) -> bool:
    """Keep operational metadata out of the source knowledge graph."""
    try:
        rel_path = path.resolve().relative_to(input_root.resolve())
    except ValueError:
        return True
    if rel_path.name in EXCLUDED_GRAPH_SOURCE_FILES and len(rel_path.parts) == 1:
        return False
    return not (rel_path.parts and rel_path.parts[0] in EXCLUDED_GRAPH_SOURCE_DIRS)


def filter_detection_sources(detection: dict[str, object], input_root: Path) -> dict[str, object]:
    file_groups = detection.get("files", {})
    if not isinstance(file_groups, dict):
        return detection
    filtered_groups: dict[str, list[str]] = {}
    for group, paths in file_groups.items():
        if not isinstance(paths, list):
            filtered_groups[str(group)] = []
            continue
        filtered_groups[str(group)] = [
            str(path)
            for path in paths
            if should_include_graph_source(Path(str(path)), input_root)
        ]
    detection = dict(detection)
    detection["files"] = filtered_groups
    return detection


def stable_hash(text: str, length: int = 10) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:length]


def slug(text: str, fallback: str = "node", max_len: int = 72) -> str:
    normalized = text.lower().strip()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = normalized.strip("_")
    if not normalized:
        normalized = fallback
    return normalized[:max_len].strip("_") or fallback


def node_id(prefix: str, value: str) -> str:
    return f"{prefix}_{slug(value, prefix)}_{stable_hash(prefix + ':' + value, 8)}"


def short_label(value: str, max_len: int = 100) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= max_len:
        return value
    return f"{value[: max_len - 12].rstrip()}...{stable_hash(value, 8)}"


def clean_scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if (value[0], value[-1:]) in {('"', '"'), ("'", "'")}:
        value = value[1:-1]
    return value.strip()


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not match:
        return {}, text

    data: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", raw_line)
        if key_match:
            current_key = key_match.group(1)
            value = key_match.group(2).strip()
            data[current_key] = [] if value == "" else clean_scalar(value)
            continue
        item_match = re.match(r"^\s*-\s*(.*)$", raw_line)
        if item_match and current_key:
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(clean_scalar(item_match.group(1)))

    return data, text[match.end() :]


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        match = re.match(r"^#\s+(.+)$", line.strip())
        if match:
            return match.group(1).strip()
    return None


def section_headings(body: str, limit: int = 8) -> list[str]:
    headings: list[str] = []
    for line in body.splitlines():
        match = re.match(r"^##+\s+(.+)$", line.strip())
        if not match:
            continue
        heading = re.sub(r"\s+", " ", match.group(1)).strip()
        if heading and heading not in headings:
            headings.append(heading)
        if len(headings) >= limit:
            break
    return headings


def list_value(meta: dict[str, object], key: str) -> list[str]:
    value = meta.get(key)
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def add_node(
    nodes: dict[str, dict[str, object]],
    node_id_: str,
    label: str,
    source_file: str,
    *,
    kind: str,
    file_type: str = "document",
    **attrs: object,
) -> dict[str, object]:
    original_label = label
    label = short_label(label)
    if original_label != label:
        attrs.setdefault("full_label", original_label)
    if node_id_ in nodes:
        existing = nodes[node_id_]
        source_files = set(str(existing.get("source_files", "")).split("|"))
        source_files.add(source_file)
        existing["source_files"] = "|".join(sorted(s for s in source_files if s))
        return existing
    node = {
        "id": node_id_,
        "label": label,
        "file_type": file_type,
        "source_file": source_file,
        "kind": kind,
        **attrs,
    }
    nodes[node_id_] = node
    return node


def add_edge(
    edges_seen: set[tuple[str, str, str, str]],
    edges: list[dict[str, object]],
    source: str,
    target: str,
    relation: str,
    source_file: str,
    *,
    confidence: str = "EXTRACTED",
    **attrs: object,
) -> None:
    relation = re.sub(r"[^A-Za-z0-9_]+", "_", relation.upper()).strip("_") or "RELATES_TO"
    key = (source, target, relation, source_file)
    if key in edges_seen:
        return
    edges_seen.add(key)
    edges.append(
        {
            "source": source,
            "target": target,
            "relation": relation,
            "confidence": confidence,
            "source_file": source_file,
            **attrs,
        }
    )


def concept_from_graph_node(raw: str) -> tuple[str, str, str]:
    if ":" in raw:
        prefix, value = raw.split(":", 1)
        prefix = prefix.strip().lower()
        value = value.strip()
    else:
        prefix, value = "concept", raw.strip()
    kind = NODE_KINDS.get(prefix, "Concept")
    label = value.replace("_", " ").strip() or raw.strip()
    return prefix, label, kind


def infer_loose_kind(value: str) -> str:
    lower = value.lower()
    if any(token in lower for token in ("exposure", "highlight", "shadow", "saturation", "clarity", "dehaze", "crop")):
        return "Parameter"
    if any(token in lower for token in ("risk", "blur", "distortion", "blown", "busy", "underexpose")):
        return "Risk"
    if any(token in lower for token in ("2x", "3x", "0.5x", "portrait", "macro", "night")):
        return "Technique"
    if any(token in lower for token in ("skin", "bokeh", "separation", "texture", "glow", "readability")):
        return "Outcome"
    return "Concept"


def parse_relation(raw: str) -> tuple[str, str, str] | None:
    tokens = raw.split()
    if len(tokens) >= 3:
        return tokens[0], tokens[1], " ".join(tokens[2:])
    if len(tokens) == 2:
        source, rel_target = tokens
        if "_" in rel_target:
            relation, target = rel_target.split("_", 1)
            return source, relation, target
        return source, "RELATES_TO", rel_target
    return None


def evidence_label(url: str) -> str:
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    path = parsed.path.strip("/")
    if path:
        path = path.split("/")[-1] or path.split("/")[-2]
    return f"{domain}/{path}" if path else domain


def source_category(rel_path: Path, meta: dict[str, object]) -> str:
    category = str(meta.get("category") or "").strip()
    if category:
        return category
    return rel_path.parts[0] if rel_path.parts else "raw"


def collect_urls(meta: dict[str, object], body: str) -> list[str]:
    urls = list_value(meta, "urls")
    urls.extend(re.findall(r"https?://[^\s)>\]]+", body))
    cleaned: list[str] = []
    seen: set[str] = set()
    for url in urls:
        url = url.rstrip(".,")
        if url and url not in seen:
            seen.add(url)
            cleaned.append(url)
    return cleaned


def build_extraction(input_root: Path) -> tuple[dict[str, object], dict[str, object]]:
    detection = filter_detection_sources(detect(input_root), input_root)
    nodes: dict[str, dict[str, object]] = {}
    edges: list[dict[str, object]] = []
    edges_seen: set[tuple[str, str, str, str]] = set()

    file_groups = detection.get("files", {})
    source_files = sorted(file_groups.get("document", []))
    skipped = set(detection.get("skipped_sensitive", []))

    for absolute in source_files:
        path = Path(absolute)
        if str(path) in skipped:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="replace")

        rel_path = path.relative_to(ROOT)
        rel = rel_path.as_posix()
        raw_rel = path.relative_to(input_root).as_posix()
        meta, body = parse_frontmatter(text)
        title = str(meta.get("title") or first_heading(body) or path.stem).strip()
        category = source_category(path.relative_to(input_root), meta)
        content_type = str(meta.get("content_type") or "").strip()

        doc_id = node_id("doc", rel)
        add_node(
            nodes,
            doc_id,
            title,
            rel,
            kind="SourceDocument",
            category=category,
            content_type=content_type,
            raw_path=raw_rel,
        )

        category_id = node_id("category", category)
        add_node(nodes, category_id, category, rel, kind="SourceCategory")
        add_edge(edges_seen, edges, doc_id, category_id, "IN_CATEGORY", rel)

        if content_type:
            ctype_id = node_id("content_type", content_type)
            add_node(nodes, ctype_id, content_type, rel, kind="ContentType")
            add_edge(edges_seen, edges, doc_id, ctype_id, "HAS_CONTENT_TYPE", rel)

        anchor_id = doc_id
        if category == "scenarios":
            anchor_id = node_id("scenario", path.stem)
            add_node(
                nodes,
                anchor_id,
                title,
                rel,
                kind="Scenario",
                aliases=list_value(meta, "aliases"),
                scenario_tags=list_value(meta, "scenario_tags"),
                raw_path=raw_rel,
            )
            add_edge(edges_seen, edges, doc_id, anchor_id, "DESCRIBES_SCENARIO", rel)

        tag_keys = ("scenario_tags", "practical_tags", "query_aliases")
        for key in tag_keys:
            for tag in list_value(meta, key):
                kind = "TrendSignal" if category in {"trends", "sns"} else "SceneFacet"
                if key == "query_aliases":
                    kind = "QueryAlias"
                tag_id = node_id(key, tag)
                add_node(nodes, tag_id, tag, rel, kind=kind)
                relation = "HAS_SCENE_TAG" if key == "scenario_tags" else "MENTIONS_TAG"
                if key == "query_aliases":
                    relation = "MATCHES_QUERY_ALIAS"
                add_edge(edges_seen, edges, anchor_id, tag_id, relation, rel)

        for graph_node in list_value(meta, "graph_nodes"):
            prefix, label, kind = concept_from_graph_node(graph_node)
            concept_id = node_id(prefix, label)
            add_node(nodes, concept_id, label, rel, kind=kind, graph_prefix=prefix)
            relation = NODE_RELATIONS.get(prefix, "USES_CONCEPT")
            add_edge(edges_seen, edges, anchor_id, concept_id, relation, rel)

        for raw_edge in list_value(meta, "graph_edges"):
            parsed = parse_relation(raw_edge)
            if not parsed:
                continue
            source_label, relation, target_label = parsed
            src_kind = infer_loose_kind(source_label)
            tgt_kind = infer_loose_kind(target_label)
            src_id = node_id("concept", source_label)
            tgt_id = node_id("concept", target_label)
            add_node(nodes, src_id, source_label.replace("_", " "), rel, kind=src_kind)
            add_node(nodes, tgt_id, target_label.replace("_", " "), rel, kind=tgt_kind)
            add_edge(edges_seen, edges, anchor_id, src_id, "USES_CONCEPT", rel)
            add_edge(edges_seen, edges, anchor_id, tgt_id, "TARGETS_CONCEPT", rel)
            add_edge(edges_seen, edges, src_id, tgt_id, relation, rel, confidence="EXTRACTED", raw_relation=raw_edge)

        for heading in section_headings(body):
            heading_id = node_id("section", f"{rel}:{heading}")
            add_node(nodes, heading_id, heading, rel, kind="DocumentSection")
            add_edge(edges_seen, edges, doc_id, heading_id, "HAS_SECTION", rel)

        for url in collect_urls(meta, body):
            evid_id = node_id("evidence", url)
            add_node(
                nodes,
                evid_id,
                evidence_label(url),
                rel,
                kind="Evidence",
                url=url,
                domain=urlparse(url).netloc.replace("www.", ""),
            )
            add_edge(edges_seen, edges, anchor_id, evid_id, "SUPPORTED_BY", rel)

    extraction = {
        "nodes": list(nodes.values()),
        "edges": edges,
        "hyperedges": [],
        "input_tokens": 0,
        "output_tokens": 0,
    }
    return extraction, detection


def auto_label_communities(G, communities: dict[int, list[str]]) -> dict[int, str]:
    labels: dict[int, str] = {}
    for cid, members in communities.items():
        kinds = Counter(str(G.nodes[n].get("kind", "Concept")) for n in members)
        categories = Counter(str(G.nodes[n].get("category", "")) for n in members if G.nodes[n].get("category"))

        for kind in CORE_KIND_ORDER:
            if kinds.get(kind):
                top_kind = kind
                break
        else:
            top_kind = kinds.most_common(1)[0][0] if kinds else "Concepts"

        if top_kind == "Scenario":
            labels[cid] = "Scenarios & Styles"
        elif top_kind in {"TrendSignal", "EditStyle", "StyleRecipe"}:
            labels[cid] = "Trends & Recipes"
        elif top_kind in {"Preference", "PersonalizationSignal"}:
            labels[cid] = "Personalization Signals"
        elif top_kind in {"Technique", "Parameter"}:
            labels[cid] = "Techniques & Parameters"
        elif top_kind == "Evidence":
            labels[cid] = "Evidence Sources"
        elif categories:
            labels[cid] = f"{categories.most_common(1)[0][0].title()} Sources"
        else:
            labels[cid] = top_kind.replace("_", " ")

    seen: defaultdict[str, int] = defaultdict(int)
    for cid in sorted(labels):
        base = labels[cid]
        seen[base] += 1
        if seen[base] > 1:
            labels[cid] = f"{base} {seen[base]}"
    return labels


def clean_wiki_dir(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    root = ROOT.resolve()
    if resolved == root or root not in resolved.parents:
        raise RuntimeError(f"Refusing to remove path outside workspace: {resolved}")
    shutil.rmtree(resolved)


def obsidian_safe_name(label: str) -> str:
    cleaned = re.sub(r'[\\/*?:"<>|#^[\]]', "", label.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")).strip()
    cleaned = re.sub(r"\.(md|mdx|markdown)$", "", cleaned, flags=re.IGNORECASE)
    return cleaned or "unnamed"


def disambiguate_wiki_labels(G) -> None:
    buckets: defaultdict[str, list[str]] = defaultdict(list)
    for node_id_, data in G.nodes(data=True):
        buckets[obsidian_safe_name(str(data.get("label", node_id_))).casefold()].append(node_id_)

    for node_ids in buckets.values():
        if len(node_ids) <= 1:
            continue
        for node_id_ in node_ids:
            data = G.nodes[node_id_]
            original = str(data.get("label", node_id_))
            data.setdefault("full_label", original)
            data["label"] = short_label(f"{original} [{stable_hash(node_id_, 6)}]")


def write_summary(output_root: Path, extraction: dict[str, object], communities: dict[int, list[str]]) -> None:
    kinds = Counter(str(n.get("kind", "Concept")) for n in extraction["nodes"])
    lines = [
        "# graphify-out",
        "",
        "Generated from `raw/` with `scripts/run_graphify_raw.py` and the `graphifyy` package.",
        "",
        "## Outputs",
        "",
        "- `graph.json`: graphify JSON export",
        "- `graph.html`: interactive graph visualization",
        "- `cypher.txt`: Neo4j import script generated by graphify",
        "- `wiki/`: Obsidian vault generated by graphify",
        "- `GRAPH_REPORT.md`: graphify audit report",
        "",
        "## Run Stats",
        "",
        f"- Nodes: {len(extraction['nodes'])}",
        f"- Edges: {len(extraction['edges'])}",
        f"- Communities: {len(communities)}",
        "",
        "## Top Kinds",
        "",
    ]
    for kind, count in kinds.most_common(12):
        lines.append(f"- {kind}: {count}")
    lines.append("")
    (output_root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def run(input_root: Path, output_root: Path, *, clean_wiki: bool = True) -> None:
    input_root = input_root.resolve()
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    extraction, detection = build_extraction(input_root)
    if not extraction["nodes"]:
        raise SystemExit("No nodes extracted from raw input.")

    (ROOT / ".graphify_detect.json").write_text(json.dumps(detection, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / ".graphify_semantic.json").write_text(
        json.dumps(extraction, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (ROOT / ".graphify_extract.json").write_text(
        json.dumps(extraction, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    G = build_from_json(extraction)
    disambiguate_wiki_labels(G)
    communities = cluster(G)
    cohesion = score_all(G, communities)
    labels = auto_label_communities(G, communities)
    gods = god_nodes(G)
    surprises = surprising_connections(G, communities)
    questions = suggest_questions(G, communities, labels)

    analysis = {
        "communities": {str(k): v for k, v in communities.items()},
        "cohesion": {str(k): v for k, v in cohesion.items()},
        "labels": {str(k): v for k, v in labels.items()},
        "gods": gods,
        "surprises": surprises,
        "questions": questions,
    }
    (ROOT / ".graphify_analysis.json").write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / ".graphify_labels.json").write_text(
        json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    report = generate(
        G,
        communities,
        cohesion,
        labels,
        gods,
        surprises,
        detection,
        {"input": 0, "output": 0},
        str(input_root),
        suggested_questions=questions,
    )
    (output_root / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(G, communities, str(output_root / "graph.json"), force=True)
    to_html(G, communities, str(output_root / "graph.html"), community_labels=labels)
    to_cypher(G, str(output_root / "cypher.txt"))

    wiki_root = output_root / "wiki"
    if clean_wiki:
        clean_wiki_dir(wiki_root)
    note_count = to_obsidian(G, communities, str(wiki_root), community_labels=labels, cohesion=cohesion)
    to_canvas(G, communities, str(wiki_root / "graph.canvas"), community_labels=labels)
    save_manifest(detection.get("files", {}), str(output_root / "manifest.json"))
    write_summary(output_root, extraction, communities)

    print(f"Graphify raw rebuild complete: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"Communities: {len(communities)}")
    print(f"Wiki notes: {note_count}")
    print(f"Output: {output_root}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate graphify-out from raw/ using graphify internals.")
    parser.add_argument("--input", default="raw", help="Input raw directory")
    parser.add_argument("--output", default="graphify-out", help="Output graphify directory")
    parser.add_argument("--no-clean-wiki", action="store_true", help="Do not remove graphify-out/wiki before export")
    args = parser.parse_args()

    run(ROOT / args.input, ROOT / args.output, clean_wiki=not args.no_clean_wiki)


if __name__ == "__main__":
    main()
