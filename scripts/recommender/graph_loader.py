"""Load the scene-first graph into small Python indexes."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GRAPH_PATH = REPO_ROOT / "graphify-out" / "scene_recommender_graph.json"


@dataclass
class Node:
    id: str
    labels: list[str]
    properties: dict[str, Any]

    @property
    def name(self) -> str:
        return str(self.properties.get("name") or self.properties.get("id") or self.id)


@dataclass
class Edge:
    source: str
    target: str
    type: str
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass
class SceneGraph:
    nodes: dict[str, Node]
    edges: list[Edge]
    outgoing: dict[str, list[Edge]]
    incoming: dict[str, list[Edge]]

    @classmethod
    def load(cls, path: Path = DEFAULT_GRAPH_PATH) -> "SceneGraph":
        raw = json.loads(path.read_text(encoding="utf-8"))
        nodes = {
            item["id"]: Node(
                id=item["id"],
                labels=list(item.get("labels", [])),
                properties=dict(item.get("properties", {})),
            )
            for item in raw.get("nodes", [])
        }
        edges = [
            Edge(
                source=item["source"],
                target=item["target"],
                type=item["type"],
                properties=dict(item.get("properties", {})),
            )
            for item in raw.get("edges", [])
        ]
        outgoing: dict[str, list[Edge]] = {}
        incoming: dict[str, list[Edge]] = {}
        for edge in edges:
            outgoing.setdefault(edge.source, []).append(edge)
            incoming.setdefault(edge.target, []).append(edge)
        return cls(nodes=nodes, edges=edges, outgoing=outgoing, incoming=incoming)

    def scenarios(self) -> list[Node]:
        return [node for node in self.nodes.values() if node.labels == ["Scenario"]]

    def recommendations_for(self, scenario_id: str) -> list[Node]:
        recs: list[Node] = []
        for edge in self.outgoing.get(scenario_id, []):
            if edge.type == "HAS_RECOMMENDATION" and edge.target in self.nodes:
                recs.append(self.nodes[edge.target])
        return sorted(recs, key=lambda n: float(n.properties.get("rank_score", 0)), reverse=True)

    def neighbors(self, node_id: str, edge_types: set[str] | None = None) -> list[Node]:
        result: list[Node] = []
        for edge in self.outgoing.get(node_id, []):
            if edge_types is None or edge.type in edge_types:
                target = self.nodes.get(edge.target)
                if target:
                    result.append(target)
        return result

    def aliases_for(self, scenario_id: str) -> list[Node]:
        aliases: list[Node] = []
        for edge in self.incoming.get(scenario_id, []):
            if edge.type == "MATCHES_SCENARIO":
                source = self.nodes.get(edge.source)
                if source:
                    aliases.append(source)
        return aliases

