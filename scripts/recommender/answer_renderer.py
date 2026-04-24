"""Render scene-graph recommendations as a natural photo-coach answer."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .graph_loader import DEFAULT_GRAPH_PATH, Node, SceneGraph
from .image_facets import ImageObservation, observation_from_vision_json
from .normalization import extract_slots
from .personalization import UserPreferenceProfile
from .scenario_matcher import MatchResult, ScenarioMatcher
from .source_bridge import DEFAULT_SOURCE_GRAPH_PATH, ExternalEvidence, SourceRecommenderBridge


CHANNEL_LABELS = {
    "trend": "트렌드",
    "general": "기본",
    "personalized": "개인화",
}

DISPLAY_NAME_MAP = {
    "Natural skin tone": "자연스러운 피부톤",
    "Background separation": "배경 분리",
    "Highlight preservation": "하이라이트 보존",
    "Face clarity": "얼굴 선명도",
    "Social-ready crop/export": "SNS에 바로 쓰기 좋은 크롭/내보내기",
    "Prefers warm tone": "따뜻한 톤",
    "Prefers cinematic look": "시네마틱 무드",
    "Prefers natural edit": "자연스러운 보정",
    "Prefers natural color": "자연스러운 색",
    "Prefers film texture": "필름 질감",
    "Prefers film grain": "필름 입자감",
    "Prefers bright tone": "밝고 산뜻한 톤",
    "Low retouch preference": "낮은 피부 보정 강도",
}


@dataclass
class RecommendationView:
    id: str
    channel: str
    name: str
    score: float
    techniques: list[str] = field(default_factory=list)
    parameters: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    outcomes: list[str] = field(default_factory=list)
    preferences: list[str] = field(default_factory=list)
    evidence: list[ExternalEvidence] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "channel": self.channel,
            "name": self.name,
            "score": self.score,
            "techniques": self.techniques,
            "parameters": self.parameters,
            "risks": self.risks,
            "outcomes": self.outcomes,
            "preferences": self.preferences,
            "evidence": [asdict(item) for item in self.evidence],
        }


@dataclass
class RenderedAnswer:
    text: str
    matcher_query: str
    match: dict[str, Any]
    recommendations: list[RecommendationView]
    evidence: list[ExternalEvidence]

    def as_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "matcher_query": self.matcher_query,
            "match": self.match,
            "recommendations": [item.as_dict() for item in self.recommendations],
            "evidence": [asdict(item) for item in self.evidence],
        }


class NaturalAnswerRenderer:
    def __init__(
        self,
        graph: SceneGraph,
        matcher: ScenarioMatcher,
        bridge: SourceRecommenderBridge | None = None,
    ):
        self.graph = graph
        self.matcher = matcher
        self.bridge = bridge

    @classmethod
    def load(
        cls,
        graph_path: Path = DEFAULT_GRAPH_PATH,
        source_graph_path: Path = DEFAULT_SOURCE_GRAPH_PATH,
    ) -> "NaturalAnswerRenderer":
        graph = SceneGraph.load(graph_path)
        matcher = ScenarioMatcher(graph)
        bridge = None
        if source_graph_path.exists():
            bridge = SourceRecommenderBridge(graph, SourceRecommenderBridge.load(graph_path, source_graph_path).source_graph)
        return cls(graph, matcher, bridge)

    def render(
        self,
        query: str,
        *,
        top_k: int = 3,
        observation: ImageObservation | None = None,
        profile: UserPreferenceProfile | None = None,
    ) -> RenderedAnswer:
        matcher_query = observation.to_matcher_query(query) if observation else query
        matches = self.matcher.match(matcher_query, top_k=top_k)
        if not matches:
            return RenderedAnswer(
                text="지금 쿼리로는 확실한 촬영 상황을 찾지 못했어요. 장소, 피사체, 빛, 원하는 분위기 중 두세 가지를 더 알려주면 추천을 좁힐 수 있습니다.",
                matcher_query=matcher_query,
                match={},
                recommendations=[],
                evidence=[],
            )

        best = matches[0]
        scenario = self.graph.nodes[best.scenario_id]
        rec_views = self._recommendation_views(scenario, profile)
        evidence = self._dedupe_evidence([item for rec in rec_views for item in rec.evidence])
        text = self._render_text(query, best, scenario, rec_views, evidence, profile)
        return RenderedAnswer(
            text=text,
            matcher_query=matcher_query,
            match=best.as_dict(),
            recommendations=rec_views,
            evidence=evidence,
        )

    def _recommendation_views(self, scenario: Node, profile: UserPreferenceProfile | None) -> list[RecommendationView]:
        recs = self.graph.recommendations_for(scenario.id)
        views = [self._build_recommendation_view(rec) for rec in recs]
        if profile:
            for view in views:
                view.score = round(
                    view.score * profile.channel_multiplier(view.channel) * profile.scenario_multiplier(scenario.id),
                    4,
                )
            views.sort(key=lambda item: item.score, reverse=True)
        return views

    def _build_recommendation_view(self, rec: Node) -> RecommendationView:
        channel = str(rec.properties.get("channel", "general"))
        evidence = self.bridge.evidence_for_node(rec, limit=5) if self.bridge else []
        return RecommendationView(
            id=rec.id,
            channel=channel,
            name=rec.name,
            score=float(rec.properties.get("rank_score", 0)),
            techniques=self._connected_names(rec.id, {"USES_TECHNIQUE"}, limit=4),
            parameters=self._connected_names(rec.id, {"SETS_PARAMETER"}, limit=4),
            risks=self._connected_names(rec.id, {"AVOIDS", "CONSTRAINED_BY", "ADJUSTS"}, limit=3),
            outcomes=self._connected_names(rec.id, {"OPTIMIZES"}, limit=3),
            preferences=self._connected_names(rec.id, {"ADAPTS_TO"}, limit=4),
            evidence=evidence,
        )

    def _connected_names(self, node_id: str, edge_types: set[str], limit: int) -> list[str]:
        names: list[str] = []
        seen: set[str] = set()
        for edge in self.graph.outgoing.get(node_id, []):
            if edge.type not in edge_types:
                continue
            node = self.graph.nodes.get(edge.target)
            if not node:
                continue
            name = clean_name(node.name)
            if name and name not in seen:
                seen.add(name)
                names.append(name)
            if len(names) >= limit:
                break
        return names

    def _render_text(
        self,
        query: str,
        match: MatchResult,
        scenario: Node,
        recs: list[RecommendationView],
        evidence: list[ExternalEvidence],
        profile: UserPreferenceProfile | None,
    ) -> str:
        general = first_channel(recs, "general") or (recs[0] if recs else None)
        trend = first_channel(recs, "trend")
        personalized = first_channel(recs, "personalized")

        diagnosis = self._diagnosis(match, scenario, general)
        query_slots = extract_slots(query)
        reshoot = select_items((general.techniques if general else []) + (trend.techniques if trend else []), limit=4)
        edit = select_items(
            issue_adjustments_for(query_slots)
            + (general.parameters if general else [])
            + (personalized.parameters if personalized else []),
            limit=4,
        )
        risks = select_items((general.risks if general else []) + (trend.risks if trend else []), limit=2)

        lines = [diagnosis, ""]

        if reshoot:
            lines.append("다시 찍는다면:")
            lines.extend(f"- {item}" for item in reshoot)
            lines.append("")

        if edit:
            lines.append("편집한다면:")
            lines.extend(f"- {item}" for item in edit)
            lines.append("")

        if risks:
            lines.append("주의할 점:")
            lines.extend(f"- {item}" for item in risks)
            lines.append("")

        variants = self._style_variants(recs, profile)
        if variants:
            lines.append("스타일 변형:")
            lines.extend(f"- {item}" for item in variants)
            lines.append("")

        if evidence:
            lines.append("근거:")
            for item in evidence[:3]:
                label = item.domain or item.label
                lines.append(f"- {label}: {item.url or item.source_file}")

        return "\n".join(lines).strip()

    @staticmethod
    def _diagnosis(match: MatchResult, scenario: Node, rec: RecommendationView | None) -> str:
        core = scenario.name
        if rec and rec.outcomes:
            return f"이 사진은 '{core}' 상황에 가깝고, 핵심은 {join_natural(rec.outcomes[:2])}를 살리면서 촬영/보정 강도를 안정적으로 잡는 것입니다."
        return f"이 사진은 '{core}' 상황에 가깝고, 핵심은 장면에 맞는 렌즈, 빛, 보정 강도를 먼저 정하는 것입니다."

    @staticmethod
    def _style_variants(recs: list[RecommendationView], profile: UserPreferenceProfile | None) -> list[str]:
        lines: list[str] = []
        for channel in ("trend", "general", "personalized"):
            rec = first_channel(recs, channel)
            if not rec:
                continue
            label = CHANNEL_LABELS.get(channel, channel)
            focus_parts = rec.outcomes[:2] or rec.preferences[:2] or rec.techniques[:1]
            focus = join_natural(focus_parts) if focus_parts else "기본 보정 안정성"
            lines.append(f"{label}: {focus} 중심으로 적용")
        if profile:
            for hint in profile.parameter_hints()[:2]:
                lines.append(f"개인 취향 반영: {hint}")
        return lines

    @staticmethod
    def _dedupe_evidence(items: list[ExternalEvidence]) -> list[ExternalEvidence]:
        deduped: list[ExternalEvidence] = []
        seen: set[str] = set()
        for item in items:
            key = item.url or item.id
            if key in seen:
                continue
            seen.add(key)
            deduped.append(item)
        return deduped


def first_channel(recs: list[RecommendationView], channel: str) -> RecommendationView | None:
    for rec in recs:
        if rec.channel == channel:
            return rec
    return None


def select_items(items: list[str], limit: int) -> list[str]:
    selected: list[str] = []
    seen: set[str] = set()
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        selected.append(item)
        if len(selected) >= limit:
            break
    return selected


def issue_adjustments_for(slots) -> list[str]:
    adjustments: list[str] = []
    if "issue:hair_highlight_clipping" in slots.issues:
        adjustments.append("머리카락/테두리 빛은 작은 마스크로 Highlights -25~-50, Whites -10~-30부터 낮춘다.")
    elif "issue:blown_highlights" in slots.issues:
        adjustments.append("날아간 밝은 영역은 전체 노출보다 Highlights/Whites를 먼저 낮추고 필요한 곳만 마스크로 보정한다.")
    if "light:backlight" in slots.how and "issue:underexposed_face" in slots.issues:
        adjustments.append("얼굴은 Subject mask로 Exposure/Shadows만 살리고 배경 하이라이트와 분리한다.")
    return adjustments


def clean_name(value: str) -> str:
    value = value.replace("_", " ").strip()
    while "  " in value:
        value = value.replace("  ", " ")
    value = value.rstrip()
    return DISPLAY_NAME_MAP.get(value, value)


def join_natural(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + f", {items[-1]}"


def load_observation(path: Path | None) -> ImageObservation | None:
    if not path:
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    payload = data.get("observation", data)
    return observation_from_vision_json(payload)


def load_profile(path: Path | None, user_id: str) -> UserPreferenceProfile | None:
    if not path:
        return None
    return UserPreferenceProfile.load(path, user_id)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Render a natural photo-coach answer from the scene graph.")
    parser.add_argument("query", help="User query or caption.")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--source-graph", type=Path, default=DEFAULT_SOURCE_GRAPH_PATH)
    parser.add_argument("--observation-json", type=Path, help="Optional client-provided image analysis/facet JSON.")
    parser.add_argument("--profile", type=Path, help="Optional user preference profile JSON.")
    parser.add_argument("--user-id", default="default")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    renderer = NaturalAnswerRenderer.load(args.graph, args.source_graph)
    answer = renderer.render(
        args.query,
        top_k=args.top_k,
        observation=load_observation(args.observation_json),
        profile=load_profile(args.profile, args.user_id),
    )
    if args.json:
        print(json.dumps(answer.as_dict(), ensure_ascii=False, indent=2))
    else:
        print(answer.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
