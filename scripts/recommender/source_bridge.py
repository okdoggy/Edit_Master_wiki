"""Bridge graphify's source graph to the scene-first recommender graph.

The graphify graph is useful for source/wiki exploration. The scene graph is
useful for product recommendations. This module connects them by `source_file`
so the runtime can answer: "which raw evidence supports this recommendation?"
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .graph_loader import DEFAULT_GRAPH_PATH, REPO_ROOT, Node, SceneGraph


DEFAULT_SOURCE_GRAPH_PATH = REPO_ROOT / "graphify-out" / "graph.json"
DEFAULT_BRIDGE_JSON_PATH = REPO_ROOT / "graphify-out" / "source_recommender_bridge.json"
DEFAULT_BRIDGE_REPORT_PATH = REPO_ROOT / "graphify-out" / "SOURCE_RECOMMENDER_BRIDGE_REPORT.md"


@dataclass
class SourceNode:
    id: str
    label: str
    kind: str
    source_file: str
    properties: dict[str, Any] = field(default_factory=dict)

    @property
    def url(self) -> str:
        return str(self.properties.get("url", ""))

    @property
    def domain(self) -> str:
        return str(self.properties.get("domain", ""))

    @property
    def source_files(self) -> list[str]:
        values = [self.source_file]
        values.extend(str(self.properties.get("source_files", "")).split("|"))
        return sorted({normalize_path(value) for value in values if normalize_path(value)})


@dataclass
class SourceEdge:
    source: str
    target: str
    relation: str
    source_file: str
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExternalEvidence:
    id: str
    label: str
    url: str
    domain: str
    source_file: str

    @classmethod
    def from_node(cls, node: SourceNode, source_file: str | None = None) -> "ExternalEvidence":
        return cls(
            id=node.id,
            label=node.label,
            url=node.url,
            domain=node.domain,
            source_file=normalize_path(source_file or node.source_file),
        )


@dataclass
class BridgeRecord:
    scenario_id: str
    scenario_name: str
    source_file: str
    source_node_ids: list[str]
    external_evidence: list[ExternalEvidence]
    recommendation_ids: list[str]
    scene_evidence_ids: list[str]

    @property
    def has_source_graph_link(self) -> bool:
        return bool(self.source_node_ids)

    @property
    def has_external_evidence(self) -> bool:
        return bool(self.external_evidence)


class SourceGraph:
    def __init__(self, nodes: dict[str, SourceNode], edges: list[SourceEdge]):
        self.nodes = nodes
        self.edges = edges
        self.by_source_file: dict[str, list[SourceNode]] = {}
        self.outgoing: dict[str, list[SourceEdge]] = {}
        for node in nodes.values():
            for source_file in node.source_files:
                self.by_source_file.setdefault(source_file, []).append(node)
        for edge in edges:
            self.outgoing.setdefault(edge.source, []).append(edge)

    @classmethod
    def load(cls, path: Path = DEFAULT_SOURCE_GRAPH_PATH) -> "SourceGraph":
        raw = json.loads(path.read_text(encoding="utf-8"))
        nodes = {
            item["id"]: SourceNode(
                id=item["id"],
                label=str(item.get("label") or item["id"]),
                kind=str(item.get("kind") or item.get("file_type") or "Concept"),
                source_file=normalize_path(str(item.get("source_file", ""))),
                properties=dict(item),
            )
            for item in raw.get("nodes", [])
        }
        edge_items = raw.get("links", raw.get("edges", []))
        edges = [
            SourceEdge(
                source=item.get("source") or item.get("_src"),
                target=item.get("target") or item.get("_tgt"),
                relation=str(item.get("relation", item.get("type", "RELATES_TO"))),
                source_file=normalize_path(str(item.get("source_file", ""))),
                properties=dict(item),
            )
            for item in edge_items
            if item.get("source") or item.get("_src")
        ]
        return cls(nodes=nodes, edges=edges)

    def nodes_for_file(self, source_file: str, *, kind: str | None = None) -> list[SourceNode]:
        nodes = self.by_source_file.get(normalize_path(source_file), [])
        if kind is None:
            return list(nodes)
        return [node for node in nodes if node.kind == kind]

    def evidence_for_file(self, source_file: str, limit: int = 8) -> list[ExternalEvidence]:
        evidence_nodes = self.nodes_for_file(source_file, kind="Evidence")
        evidence_nodes.sort(key=lambda node: (node.domain, node.label, node.id))
        deduped: list[ExternalEvidence] = []
        seen: set[str] = set()
        for node in evidence_nodes:
            key = node.url or node.id
            if key in seen:
                continue
            seen.add(key)
            deduped.append(ExternalEvidence.from_node(node, source_file=source_file))
            if len(deduped) >= limit:
                break
        return deduped


class SourceRecommenderBridge:
    def __init__(self, scene_graph: SceneGraph, source_graph: SourceGraph):
        self.scene_graph = scene_graph
        self.source_graph = source_graph
        self.records = self._build_records()
        self.by_scenario_id = {record.scenario_id: record for record in self.records}
        self.by_source_file = {normalize_path(record.source_file): record for record in self.records}

    @classmethod
    def load(
        cls,
        scene_graph_path: Path = DEFAULT_GRAPH_PATH,
        source_graph_path: Path = DEFAULT_SOURCE_GRAPH_PATH,
    ) -> "SourceRecommenderBridge":
        return cls(SceneGraph.load(scene_graph_path), SourceGraph.load(source_graph_path))

    def _build_records(self) -> list[BridgeRecord]:
        records: list[BridgeRecord] = []
        for scenario in sorted(self.scene_graph.scenarios(), key=lambda node: node.id):
            source_file = normalize_path(str(scenario.properties.get("source_file", "")))
            source_nodes = self.source_graph.nodes_for_file(source_file)
            recs = self.scene_graph.recommendations_for(scenario.id)
            scene_evidence_ids = sorted(
                {
                    edge.target
                    for node in [scenario, *recs]
                    for edge in self.scene_graph.outgoing.get(node.id, [])
                    if edge.type == "SUPPORTED_BY"
                }
            )
            records.append(
                BridgeRecord(
                    scenario_id=scenario.id,
                    scenario_name=scenario.name,
                    source_file=source_file,
                    source_node_ids=sorted(node.id for node in source_nodes),
                    external_evidence=self.source_graph.evidence_for_file(source_file),
                    recommendation_ids=[node.id for node in recs],
                    scene_evidence_ids=scene_evidence_ids,
                )
            )
        return records

    def record_for_node(self, node: Node | str) -> BridgeRecord | None:
        node_id = node if isinstance(node, str) else node.id
        scene_node = self.scene_graph.nodes.get(node_id)
        if not scene_node:
            return None
        if scene_node.labels == ["Scenario"]:
            return self.by_scenario_id.get(scene_node.id)
        source_file = normalize_path(str(scene_node.properties.get("source_file", "")))
        return self.by_source_file.get(source_file)

    def evidence_for_node(self, node: Node | str, limit: int = 5) -> list[ExternalEvidence]:
        record = self.record_for_node(node)
        if not record:
            return []
        return record.external_evidence[:limit]

    def validate(self) -> dict[str, Any]:
        scenarios_without_source = [record.scenario_id for record in self.records if not record.has_source_graph_link]
        scenarios_without_external_evidence = [record.scenario_id for record in self.records if not record.has_external_evidence]

        recommendations = [node for node in self.scene_graph.nodes.values() if node.labels == ["Recommendation"]]
        recs_without_supported_by = [
            node.id
            for node in recommendations
            if not any(edge.type == "SUPPORTED_BY" for edge in self.scene_graph.outgoing.get(node.id, []))
        ]
        recs_without_source_file = [
            node.id for node in recommendations if not normalize_path(str(node.properties.get("source_file", "")))
        ]
        recs_without_source_graph_evidence = [
            node.id
            for node in recommendations
            if not self.source_graph.evidence_for_file(str(node.properties.get("source_file", "")), limit=1)
        ]

        scenario_count = len(self.records)
        linked_scenario_count = scenario_count - len(scenarios_without_source)
        external_evidence_count = sum(len(record.external_evidence) for record in self.records)
        ok = not scenarios_without_source and not recs_without_supported_by and not recs_without_source_file
        return {
            "ok": ok,
            "scenario_count": scenario_count,
            "linked_scenario_count": linked_scenario_count,
            "link_coverage": round(linked_scenario_count / scenario_count, 4) if scenario_count else 0,
            "recommendation_count": len(recommendations),
            "external_evidence_count": external_evidence_count,
            "scenarios_without_source": scenarios_without_source,
            "scenarios_without_external_evidence": scenarios_without_external_evidence,
            "recommendations_without_supported_by": recs_without_supported_by,
            "recommendations_without_source_file": recs_without_source_file,
            "recommendations_without_source_graph_evidence": recs_without_source_graph_evidence,
        }

    def as_dict(self) -> dict[str, Any]:
        return {
            "validation": self.validate(),
            "records": [
                {
                    **asdict(record),
                    "external_evidence": [asdict(item) for item in record.external_evidence],
                }
                for record in self.records
            ],
        }


def normalize_path(value: str) -> str:
    return value.replace("\\", "/").strip()


def render_report(bridge: SourceRecommenderBridge) -> str:
    validation = bridge.validate()
    lines = [
        "# Source-Recommender Bridge Report",
        "",
        "This report checks whether the graphify source graph can support the scene-first recommendation graph.",
        "",
        "## Summary",
        "",
        f"- OK: {validation['ok']}",
        f"- Scenario link coverage: {validation['linked_scenario_count']} / {validation['scenario_count']}",
        f"- Recommendations: {validation['recommendation_count']}",
        f"- External evidence links: {validation['external_evidence_count']}",
        "",
        "## Gaps",
        "",
        f"- Scenarios without source graph link: {len(validation['scenarios_without_source'])}",
        f"- Scenarios without external evidence: {len(validation['scenarios_without_external_evidence'])}",
        f"- Recommendations without SUPPORTED_BY: {len(validation['recommendations_without_supported_by'])}",
        f"- Recommendations without source_file: {len(validation['recommendations_without_source_file'])}",
        f"- Recommendations without source graph evidence: {len(validation['recommendations_without_source_graph_evidence'])}",
        "",
        "## Scenario Samples",
        "",
    ]
    for record in bridge.records[:10]:
        domains = sorted({item.domain for item in record.external_evidence if item.domain})
        domain_text = ", ".join(domains[:5]) if domains else "none"
        lines.extend(
            [
                f"### {record.scenario_name}",
                "",
                f"- Scenario: `{record.scenario_id}`",
                f"- Source file: `{record.source_file}`",
                f"- Recommendations: {len(record.recommendation_ids)}",
                f"- External evidence: {len(record.external_evidence)} ({domain_text})",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(
    bridge: SourceRecommenderBridge,
    bridge_json_path: Path = DEFAULT_BRIDGE_JSON_PATH,
    report_path: Path = DEFAULT_BRIDGE_REPORT_PATH,
) -> None:
    bridge_json_path.parent.mkdir(parents=True, exist_ok=True)
    bridge_json_path.write_text(json.dumps(bridge.as_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_path.write_text(render_report(bridge), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Validate source graph to recommender graph linkage.")
    parser.add_argument("--scene-graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--source-graph", type=Path, default=DEFAULT_SOURCE_GRAPH_PATH)
    parser.add_argument("--write", action="store_true", help="Write bridge JSON and Markdown report.")
    parser.add_argument("--json", action="store_true", help="Print full bridge JSON.")
    args = parser.parse_args(argv)

    bridge = SourceRecommenderBridge.load(args.scene_graph, args.source_graph)
    if args.write:
        write_outputs(bridge)
    if args.json:
        print(json.dumps(bridge.as_dict(), ensure_ascii=False, indent=2))
    else:
        validation = bridge.validate()
        print(f"ok: {validation['ok']}")
        print(f"scenario link coverage: {validation['linked_scenario_count']} / {validation['scenario_count']}")
        print(f"recommendations: {validation['recommendation_count']}")
        print(f"external evidence links: {validation['external_evidence_count']}")
        print(f"scenarios without external evidence: {len(validation['scenarios_without_external_evidence'])}")
    return 0 if bridge.validate()["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
