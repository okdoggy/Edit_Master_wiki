"""Scenario matcher for the scene-first smartphone photo recommender."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from .graph_loader import DEFAULT_GRAPH_PATH, Node, SceneGraph
from .graph_loader import REPO_ROOT
from .normalization import QuerySlots, canonical_terms_for_text, extract_slots, normalize_text, tokenize


@dataclass(frozen=True)
class KnowledgeGapConcept:
    id: str
    phrases: tuple[str, ...]
    supported_scenarios: frozenset[str] = frozenset()


# These markers describe scenario intents that are common in real user queries
# but are not yet represented as first-class source-backed raw scenarios.
# They should be removed or given supported_scenarios once those raws exist.
KNOWLEDGE_GAP_CONCEPTS: tuple[KnowledgeGapConcept, ...] = (
    KnowledgeGapConcept(
        "photo_booth_rephoto",
        ("photo booth", "photobooth", "four-cut", "four cut", "printed strip", "네컷", "인생네컷", "포토부스"),
        frozenset({"scenario_photo_booth_flash_portrait"}),
    ),
    KnowledgeGapConcept(
        "airplane_window_travel",
        ("airplane window", "plane window", "aircraft window", "wing", "glare and haze from the glass", "비행기 창", "항공기 창", "항공기 창가", "날개"),
        frozenset({"scenario_airplane_window_travel_view"}),
    ),
    KnowledgeGapConcept(
        "gym_progress_photo",
        ("gym mirror", "fitness mirror", "progress photo", "workout progress", "fitness progress", "body line", "fluorescent light", "헬스장", "헬스장 거울", "운동 후", "몸 라인", "바디 프로그레스"),
        frozenset({"scenario_gym_mirror_fitness_progress"}),
    ),
    KnowledgeGapConcept(
        "car_dashboard_night",
        ("dashboard", "windshield", "parked car", "car interior", "차 안", "대시보드", "계기판", "자동차 실내", "앞유리"),
    ),
    KnowledgeGapConcept(
        "desk_setup_productivity",
        ("desk setup", "productivity thumbnail", "laptop desk", "laptop-and-keyboard", "keyboard", "cables", "책상 셋업", "책상샷", "노트북", "키보드", "생산성 콘텐츠", "생산성 브이로그"),
    ),
    KnowledgeGapConcept(
        "graduation_ceremony",
        ("graduation", "cap and gown", "졸업식", "학사모", "가운", "graduation ceremony"),
        frozenset({"scenario_graduation_ceremony_portrait"}),
    ),
    KnowledgeGapConcept(
        "hotel_morning_routine",
        ("hotel bed breakfast", "hotel breakfast tray", "breakfast tray", "morning routine", "pajamas", "호텔 침대", "호텔 조식", "조식 쟁반", "아침 루틴", "모닝 루틴", "파자마", "잠옷"),
    ),
    KnowledgeGapConcept(
        "hair_salon_color",
        ("hair salon", "color appointment", "new brown tone", "hair colored", "염색", "염색 후", "미용실", "머리색", "헤어 컬러"),
    ),
    KnowledgeGapConcept(
        "nail_art_closeup",
        ("nail art", "nails", "manicure", "네일아트", "네일 사진", "네일 색", "손톱"),
        frozenset({"scenario_beauty_makeup_nail_closeup"}),
    ),
    KnowledgeGapConcept(
        "bookstore_reading_portrait",
        ("bookstore", "book cafe", "bookshelves", "shelves", "reading portrait", "서점", "북카페", "책장", "독서 인물"),
        frozenset({"scenario_bookstore_library_reading_portrait"}),
    ),
    KnowledgeGapConcept(
        "train_window_travel",
        ("train window", "train seat", "기차 창", "기차 좌석", "열차 창", "창밖 풍경", "좌석 옆", "좌석 인물"),
    ),
    KnowledgeGapConcept(
        "picnic_blanket_flatlay",
        ("picnic blanket", "picnic flatlay", "sunglasses", "피크닉", "돗자리"),
    ),
    KnowledgeGapConcept(
        "linkedin_headshot",
        ("linkedin", "professional headshot", "business headshot", "headshot", "링크드인", "비즈니스 프로필", "헤드샷"),
    ),
    KnowledgeGapConcept(
        "birthday_balloon_party",
        ("birthday balloon", "balloons", "balloon party", "생일 풍선", "풍선 파티"),
    ),
)


SCENARIO_SLOT_HINTS: dict[str, dict[str, set[str]]] = {
    "scenario_window_light_cafe_portrait": {
        "where": {"place:cafe", "place:cafe_window"},
        "what": {"intent:portrait"},
        "how": {"lens_mode:2x", "mode:portrait", "edit:mask"},
        "issues": {"issue:underexposed_face", "issue:busy_background"},
        "preferences": {"pref:natural", "pref:clean"},
    },
    "scenario_rain_neon_street_portrait": {
        "when": {"time:night", "weather:rain"},
        "where": {"place:street", "place:rain_neon_street"},
        "what": {"intent:portrait", "intent:couple_portrait", "intent:trendy_style"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights", "issue:mixed_white_balance"},
        "preferences": {"pref:cinematic"},
    },
    "scenario_dim_restaurant_food": {
        "when": {"time:night"},
        "where": {"place:restaurant"},
        "what": {"intent:food"},
        "how": {"edit:white_balance", "lens_mode:1x", "lens_mode:2x"},
        "issues": {"issue:mixed_white_balance", "issue:motion_blur"},
        "preferences": {"pref:warm"},
    },
    "scenario_cafe_flatlay_dessert": {
        "where": {"place:cafe"},
        "what": {"intent:food", "intent:flatlay"},
        "how": {"lens_mode:1x", "edit:crop"},
        "issues": {"issue:tilted_horizon", "issue:edge_distortion"},
        "preferences": {"pref:clean"},
    },
    "scenario_harsh_noon_beach_portrait": {
        "when": {"time:noon", "time:day"},
        "where": {"place:beach"},
        "what": {"intent:portrait"},
        "how": {"lens_mode:2x", "mode:portrait", "light:harsh_light"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights"},
    },
    "scenario_backlit_silhouette_sunset": {
        "when": {"time:golden_hour"},
        "what": {"intent:portrait", "intent:couple_portrait"},
        "how": {"lens_mode:1x", "lens_mode:2x", "light:backlight", "light:rim_light"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights", "issue:hair_highlight_clipping"},
        "preferences": {"pref:warm", "pref:cinematic"},
    },
    "scenario_beach_backlit_portrait": {
        "when": {"time:golden_hour", "season:summer"},
        "where": {"place:beach"},
        "what": {"intent:portrait", "intent:trendy_style"},
        "how": {"lens_mode:2x", "mode:portrait", "light:backlight", "light:rim_light"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights", "issue:hair_highlight_clipping"},
    },
    "scenario_backlit_rim_light_portrait": {
        "when": {"time:golden_hour"},
        "what": {"intent:portrait"},
        "how": {"lens_mode:2x", "mode:portrait", "light:backlight", "light:rim_light", "edit:mask"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights", "issue:hair_highlight_clipping"},
        "preferences": {"pref:natural"},
    },
    "scenario_fashion_ootd_portrait": {
        "where": {"place:street"},
        "what": {"intent:ootd", "intent:portrait"},
        "how": {"lens_mode:1x", "lens_mode:2x"},
        "issues": {"issue:edge_distortion", "issue:busy_background"},
        "preferences": {"pref:clean"},
    },
    "scenario_concert_stage_low_light": {
        "when": {"time:night"},
        "where": {"place:stage"},
        "what": {"intent:portrait", "intent:trendy_style"},
        "how": {"lens_mode:3x_5x", "mode:night", "mode:pro"},
        "issues": {"issue:blown_highlights", "issue:motion_blur"},
        "preferences": {"pref:cinematic"},
    },
    "scenario_snow_portrait_clean_winter": {
        "when": {"season:winter", "time:day"},
        "where": {"place:snow"},
        "what": {"intent:portrait"},
        "issues": {"issue:underexposed_face", "issue:mixed_white_balance"},
        "preferences": {"pref:clean", "pref:natural"},
    },
    "scenario_pets_children_action": {
        "what": {"intent:pets_kids"},
        "how": {"mode:burst"},
        "issues": {"issue:motion_blur"},
    },
    "scenario_city_window_reflection": {
        "when": {"time:night"},
        "where": {"place:city_window"},
        "what": {"intent:city_lights", "intent:reflection"},
        "issues": {"issue:dirty_reflection", "issue:blown_highlights"},
        "preferences": {"pref:cinematic"},
    },
    "scenario_reflection_mirror_puddle_prism": {
        "where": {"place:street", "place:mirror"},
        "what": {"intent:reflection", "intent:trendy_style"},
        "issues": {"issue:dirty_reflection"},
        "preferences": {"pref:cinematic"},
    },
    "scenario_mirror_selfie_ootd": {
        "where": {"place:mirror"},
        "what": {"intent:selfie", "intent:ootd"},
        "issues": {"issue:edge_distortion", "issue:dirty_reflection"},
        "preferences": {"pref:clean"},
    },
    "scenario_small_product_listing_photo": {
        "where": {"place:home"},
        "what": {"intent:product_listing"},
        "issues": {"issue:busy_background", "issue:mixed_white_balance"},
        "preferences": {"pref:clean"},
    },
    "scenario_marketplace_street_food_story": {
        "where": {"place:market", "place:street"},
        "what": {"intent:food", "intent:story"},
        "how": {"lens_mode:1x", "lens_mode:2x"},
        "preferences": {"pref:warm", "pref:film"},
    },
    "scenario_cafe_drink_dessert_closeup": {
        "where": {"place:cafe"},
        "what": {"intent:food", "intent:drink_dessert_closeup"},
        "how": {"lens_mode:1x"},
        "issues": {"issue:macro_focus"},
        "preferences": {"pref:warm"},
    },
    "scenario_flower_macro_bokeh": {
        "what": {"intent:flower_macro", "intent:drink_dessert_closeup"},
        "issues": {"issue:macro_focus"},
        "preferences": {"pref:natural", "pref:clean"},
    },
    "scenario_group_travel_selfie": {
        "where": {"place:travel", "place:landmark"},
        "what": {"intent:selfie", "intent:group_photo", "intent:portrait"},
        "how": {"lens_mode:0_5x", "edit:crop"},
        "issues": {"issue:edge_distortion", "issue:busy_background"},
        "preferences": {"pref:clean", "pref:natural"},
    },
    "scenario_crowded_landmark_portrait": {
        "where": {"place:travel", "place:landmark"},
        "what": {"intent:portrait", "intent:ootd"},
        "how": {"lens_mode:1x", "lens_mode:2x", "edit:crop"},
        "issues": {"issue:busy_background", "issue:edge_distortion"},
        "preferences": {"pref:clean", "pref:natural"},
    },
    "scenario_action_pan_runner_cyclist": {
        "what": {"intent:action_motion"},
        "how": {"mode:panning", "mode:burst"},
        "issues": {"issue:motion_blur"},
        "preferences": {"pref:cinematic"},
    },
    "scenario_landscape_sky_dynamic_range_2026": {
        "where": {"place:mountain"},
        "what": {"intent:landscape"},
        "how": {"edit:mask"},
        "issues": {"issue:blown_highlights", "issue:dynamic_range"},
        "preferences": {"pref:natural"},
    },
    "scenario_museum_gallery_portrait": {
        "where": {"place:museum"},
        "what": {"intent:portrait"},
        "how": {"lens_mode:2x", "mode:no_flash", "edit:white_balance"},
        "issues": {"issue:mixed_white_balance", "issue:motion_blur"},
        "preferences": {"pref:natural", "pref:low_retouch"},
    },
    "scenario_indoor_party_group": {
        "when": {"time:night"},
        "where": {"place:home"},
        "what": {"intent:group_photo", "intent:portrait"},
        "how": {"mode:night", "mode:burst"},
        "issues": {"issue:mixed_white_balance", "issue:motion_blur"},
        "preferences": {"pref:warm"},
    },
    "scenario_candle_cake_low_light_party": {
        "when": {"time:night"},
        "what": {"intent:food", "intent:group_photo"},
        "how": {"mode:night"},
        "issues": {"issue:blown_highlights", "issue:mixed_white_balance"},
        "preferences": {"pref:warm"},
    },
    "scenario_document_scan_correction": {
        "where": {"place:desk_table"},
        "what": {"intent:document_scan", "intent:product_listing"},
        "how": {"edit:perspective", "edit:crop"},
        "issues": {"issue:document_skew", "issue:paper_shadow", "issue:tilted_horizon"},
        "preferences": {"pref:clean"},
    },
    "scenario_receipt_memory_flatlay": {
        "where": {"place:cafe", "place:desk_table", "place:travel"},
        "what": {"intent:receipt_flatlay", "intent:flatlay", "intent:story", "intent:food"},
        "how": {"lens_mode:1x", "edit:crop"},
        "issues": {"issue:busy_background", "issue:document_skew"},
        "preferences": {"pref:warm", "pref:film", "pref:clean", "pref:natural"},
    },
    "scenario_dating_profile_natural_portrait": {
        "where": {"place:cafe_window", "place:home"},
        "what": {"intent:dating_profile", "intent:portrait", "intent:selfie"},
        "how": {"lens_mode:2x", "mode:portrait", "edit:mask"},
        "issues": {"issue:busy_background", "issue:mixed_white_balance"},
        "preferences": {"pref:natural", "pref:clean", "pref:low_retouch"},
    },
    "scenario_trendy_aerial_beach_minimal": {
        "where": {"place:aerial_view", "place:beach", "place:travel"},
        "what": {"intent:aerial_shot", "intent:landscape", "intent:trendy_style"},
        "how": {"lens_mode:1x", "lens_mode:2x", "edit:crop"},
        "issues": {"issue:motion_blur", "issue:edge_distortion"},
        "preferences": {"pref:clean", "pref:natural"},
    },
    "scenario_cave_low_light_travel_portrait": {
        "when": {"time:night"},
        "where": {"place:cave", "place:travel"},
        "what": {"intent:cave_photo", "intent:portrait", "intent:group_photo", "intent:landscape"},
        "how": {"mode:night", "mode:burst", "mode:no_flash", "edit:white_balance"},
        "issues": {"issue:underexposed_face", "issue:mixed_white_balance", "issue:motion_blur"},
        "preferences": {"pref:cinematic", "pref:natural"},
    },
    "scenario_paparazzi_flash_candid": {
        "when": {"time:night"},
        "where": {"place:street"},
        "what": {"intent:paparazzi_candid", "intent:ootd", "intent:portrait", "intent:trendy_style"},
        "how": {"light:flash", "mode:burst", "lens_mode:1x", "lens_mode:2x"},
        "issues": {"issue:red_eye_flash_glare", "issue:motion_blur", "issue:busy_background"},
        "preferences": {"pref:cinematic", "pref:clean"},
    },
}


@dataclass
class ScenarioIndexEntry:
    id: str
    name: str
    source_file: str
    tags: set[str]
    aliases: set[str]
    terms: set[str]
    slot_hints: dict[str, set[str]]


@dataclass
class MatchResult:
    scenario_id: str
    scenario_name: str
    score: float
    source_file: str
    matched_terms: list[str]
    matched_slots: dict[str, list[str]]
    reasons: list[str]
    score_breakdown: dict[str, float] = field(default_factory=dict)
    unknown_concepts: list[str] = field(default_factory=list)
    confidence: str = "uncalibrated"
    coverage_status: str = "unknown"
    score_gap: float = 0.0
    slot_coverage: float = 0.0

    def as_dict(self) -> dict:
        return {
            "scenario_id": self.scenario_id,
            "scenario_name": self.scenario_name,
            "score": round(self.score, 4),
            "confidence": self.confidence,
            "coverage_status": self.coverage_status,
            "score_gap": round(self.score_gap, 4),
            "slot_coverage": round(self.slot_coverage, 4),
            "source_file": self.source_file,
            "matched_terms": self.matched_terms,
            "matched_slots": self.matched_slots,
            "reasons": self.reasons,
            "score_breakdown": {key: round(value, 4) for key, value in self.score_breakdown.items()},
            "unknown_concepts": self.unknown_concepts,
        }


class ScenarioMatcher:
    def __init__(self, graph: SceneGraph):
        self.graph = graph
        self.entries = [self._build_entry(node) for node in graph.scenarios()]

    @classmethod
    def from_path(cls, graph_path: Path = DEFAULT_GRAPH_PATH) -> "ScenarioMatcher":
        return cls(SceneGraph.load(graph_path))

    def _build_entry(self, node: Node) -> ScenarioIndexEntry:
        props = node.properties
        name = str(props.get("name", node.id))
        source_file = str(props.get("source_file", ""))
        tags = {str(tag) for tag in props.get("tags", [])}
        aliases = {alias.name for alias in self.graph.aliases_for(node.id)}
        aliases.update(self._aliases_from_source(source_file))
        neighbor_names = {
            neighbor.name
            for neighbor in self.graph.neighbors(
                node.id,
                {
                    "HAS_SUBJECT",
                    "HAS_ENVIRONMENT",
                    "HAS_LIGHT",
                    "HAS_FACET",
                    "USES_LENS",
                    "USES_MODE",
                    "HAS_EDIT_STYLE",
                    "HAS_RISK",
                    "USES_TECHNIQUE",
                },
            )
        }
        text_bits = {name, source_file, *tags, *aliases, *neighbor_names, node.id.replace("scenario_", "").replace("_", " ")}
        terms: set[str] = set()
        for bit in text_bits:
            terms.update(canonical_terms_for_text(bit))
        return ScenarioIndexEntry(
            id=node.id,
            name=name,
            source_file=source_file,
            tags=tags,
            aliases=aliases,
            terms=terms,
            slot_hints=SCENARIO_SLOT_HINTS.get(node.id, {}),
        )

    @staticmethod
    def _aliases_from_source(source_file: str) -> set[str]:
        if not source_file:
            return set()
        path = REPO_ROOT / source_file
        if not path.exists():
            return set()
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = re.match(r"---\s*\n(.*?)\n---", text, flags=re.S)
        if not match or "aliases:" not in match.group(1):
            return set()
        aliases: set[str] = set()
        in_aliases = False
        for line in match.group(1).splitlines():
            if line.startswith("aliases:"):
                in_aliases = True
                continue
            if in_aliases and re.match(r"^[a-zA-Z0-9_-]+:", line):
                break
            if in_aliases:
                item = line.strip()
                if item.startswith("- "):
                    aliases.add(item[2:].strip().strip('"').strip("'"))
        return {alias for alias in aliases if alias}

    def match(self, query: str, top_k: int = 5) -> list[MatchResult]:
        normalized = normalize_text(query)
        query_terms = canonical_terms_for_text(normalized)
        query_tokens = tokenize(normalized)
        query_slots = extract_slots(normalized)
        knowledge_gap_concepts = detect_knowledge_gap_concepts(normalized)

        results = [
            self._score_entry(entry, normalized, query_terms, query_tokens, query_slots, knowledge_gap_concepts)
            for entry in self.entries
        ]
        results.sort(key=lambda item: (item.score, len(item.matched_terms), item.scenario_name), reverse=True)
        filtered = [item for item in results if item.score > 0][:top_k]
        self._annotate_confidence(filtered, query_slots)
        return filtered

    @staticmethod
    def _annotate_confidence(results: list[MatchResult], query_slots: QuerySlots) -> None:
        core_slots = ("where", "what", "how", "issues")
        filled_core = {
            slot: set(getattr(query_slots, slot))
            for slot in core_slots
            if getattr(query_slots, slot)
        }
        core_count = len(filled_core)
        for index, result in enumerate(results):
            next_score = results[index + 1].score if index + 1 < len(results) else 0.0
            result.score_gap = max(result.score - next_score, 0.0)
            if core_count:
                matched_core = sum(1 for slot in filled_core if result.matched_slots.get(slot))
                result.slot_coverage = matched_core / core_count
            else:
                result.slot_coverage = 1.0 if result.score >= 3.0 else 0.0

            has_direct_alias = "direct_alias" in result.reasons
            if result.unknown_concepts:
                result.confidence = "low"
                result.coverage_status = "gap"
            elif result.score < 2.5 or (core_count >= 2 and result.slot_coverage < 0.34):
                result.confidence = "low"
                result.coverage_status = "gap"
            elif result.score_gap < 0.6 or result.score < 4.0 or (core_count >= 2 and result.slot_coverage < 0.5):
                result.confidence = "medium"
                result.coverage_status = "partial"
            else:
                result.confidence = "high"
                result.coverage_status = "supported"

            if (
                has_direct_alias
                and not result.unknown_concepts
                and result.score >= 5.0
                and (result.slot_coverage >= 0.5 or result.score_gap >= 1.0)
            ):
                result.confidence = "high"
                result.coverage_status = "supported"

    def _score_entry(
        self,
        entry: ScenarioIndexEntry,
        normalized_query: str,
        query_terms: set[str],
        query_tokens: set[str],
        query_slots: QuerySlots,
        knowledge_gap_concepts: set[str],
    ) -> MatchResult:
        score = 0.0
        reasons: list[str] = []
        score_breakdown: dict[str, float] = {}

        def add_score(key: str, amount: float, reason: str | None = None) -> None:
            nonlocal score
            if not amount:
                return
            score += amount
            score_breakdown[key] = score_breakdown.get(key, 0.0) + amount
            if reason:
                reasons.append(reason)

        def subtract_score(key: str, amount: float, reason: str | None = None) -> None:
            nonlocal score
            if not amount:
                return
            score -= amount
            score_breakdown[key] = score_breakdown.get(key, 0.0) - amount
            if reason:
                reasons.append(reason)

        direct_aliases = [alias for alias in entry.aliases if normalize_text(alias) and normalize_text(alias) in normalized_query]
        if direct_aliases:
            add_score("direct_alias", 5.0 + min(len(direct_aliases), 3), "direct_alias")

        name_tokens = tokenize(entry.name)
        name_overlap = query_tokens & name_tokens
        if name_overlap:
            add_score("scenario_name_overlap", len(name_overlap) * 0.45, "scenario_name_overlap")

        term_overlap = query_terms & entry.terms
        if term_overlap:
            add_score("graph_term_overlap", len(term_overlap) * 0.35, "graph_term_overlap")

        matched_slots: dict[str, list[str]] = {}
        slot_weights = {
            "when": 0.9,
            "who": 0.25,
            "where": 1.6,
            "what": 1.8,
            "how": 0.9,
            "issues": 0.55,
            "preferences": 0.35,
        }
        slot_values = query_slots.as_dict()
        for slot, query_values in slot_values.items():
            hints = entry.slot_hints.get(slot, set())
            overlap = set(query_values) & hints
            if overlap:
                matched_slots[slot] = sorted(overlap)
                add_score(f"{slot}_slot", slot_weights[slot] * len(overlap), f"{slot}_slot")

        specificity_bonus = self._specificity_bonus(entry, query_slots, matched_slots)
        add_score("specificity_bonus", specificity_bonus)
        conflict_penalty = self._conflict_penalty(entry, query_slots)
        subtract_score("conflict_penalty", conflict_penalty, "conflict_penalty" if conflict_penalty else None)
        unsupported_concepts = unsupported_knowledge_gap_concepts(entry, knowledge_gap_concepts)
        unknown_penalty = unknown_intent_penalty(unsupported_concepts)
        subtract_score("unknown_intent_penalty", unknown_penalty, "unsupported_intent" if unsupported_concepts else None)
        score_breakdown["final_score"] = score

        return MatchResult(
            scenario_id=entry.id,
            scenario_name=entry.name,
            score=score,
            source_file=entry.source_file,
            matched_terms=sorted(term_overlap)[:20],
            matched_slots=matched_slots,
            reasons=sorted(set(reasons)),
            score_breakdown=score_breakdown,
            unknown_concepts=sorted(unsupported_concepts),
        )

    @staticmethod
    def _specificity_bonus(entry: ScenarioIndexEntry, query_slots: QuerySlots, matched_slots: dict[str, list[str]]) -> float:
        bonus = 0.0
        if "where" in matched_slots and "what" in matched_slots:
            bonus += 1.2
        if "issues" in matched_slots and ("where" in matched_slots or "what" in matched_slots):
            bonus += 0.35
        if query_slots.filled_slot_count >= 3 and len(matched_slots) >= 3:
            bonus += 0.45
        if entry.id == "scenario_backlit_silhouette_sunset":
            if (
                "light:rim_light" in query_slots.how
                and "issue:hair_highlight_clipping" in query_slots.issues
                and "intent:portrait" not in query_slots.what
            ):
                bonus += 0.9
        if entry.id in {"scenario_backlit_rim_light_portrait", "scenario_backlit_silhouette_sunset"}:
            if "light:backlight" in query_slots.how and "intent:portrait" in query_slots.what:
                bonus += 1.0
            if "issue:hair_highlight_clipping" in query_slots.issues or "light:rim_light" in query_slots.how:
                bonus += 1.0
        if entry.id == "scenario_harsh_noon_beach_portrait":
            if "time:noon" in query_slots.when and "place:beach" in query_slots.where:
                bonus += 1.2
            if "intent:portrait" in query_slots.what and "issue:blown_highlights" in query_slots.issues:
                bonus += 0.6
        if entry.id == "scenario_museum_gallery_portrait":
            if "place:museum" in query_slots.where:
                bonus += 1.2
            if "mode:no_flash" in query_slots.how:
                bonus += 0.7
            if "issue:mixed_white_balance" in query_slots.issues:
                bonus += 0.5
        if entry.id == "scenario_crowded_landmark_portrait":
            if "place:landmark" in query_slots.where and "intent:ootd" in query_slots.what:
                bonus += 1.0
            if "issue:busy_background" in query_slots.issues:
                bonus += 0.5
        if entry.id == "scenario_action_pan_runner_cyclist":
            if "intent:action_motion" in query_slots.what and "intent:pets_kids" in query_slots.what:
                bonus += 0.9
            if "mode:panning" in query_slots.how:
                bonus += 0.7
        if entry.id == "scenario_pets_children_action":
            if "intent:pets_kids" in query_slots.what:
                bonus += 1.2
            if "issue:motion_blur" in query_slots.issues or "intent:action_motion" in query_slots.what:
                bonus += 0.5
        # Prevent broad story scenarios from swallowing concrete food/cafe queries.
        if entry.id == "scenario_marketplace_street_food_story":
            if "place:market" in set(query_slots.where):
                bonus += 0.8
            if "intent:story" in set(query_slots.what):
                bonus += 0.6
        return bonus

    @staticmethod
    def _conflict_penalty(entry: ScenarioIndexEntry, query_slots: QuerySlots) -> float:
        penalty = 0.0
        where = query_slots.where
        what = query_slots.what
        issues = query_slots.issues

        if entry.id == "scenario_marketplace_street_food_story":
            if "place:restaurant" in where:
                penalty += 2.6
            if "place:cafe" in where and "intent:flatlay" in what:
                penalty += 2.4
            if "intent:portrait" in what and not ({"intent:food", "intent:story"} & what or "place:market" in where):
                penalty += 1.2
            if {"issue:mixed_white_balance", "issue:motion_blur"} & issues and "place:market" not in where:
                penalty += 0.8

        if entry.id == "scenario_reflection_mirror_puddle_prism":
            if "place:city_window" in where:
                penalty += 2.3
            if "issue:blown_highlights" in issues and "place:city_window" in where:
                penalty += 0.8

        if entry.id == "scenario_beach_backlit_portrait" and "time:noon" in query_slots.when:
            penalty += 1.8

        if entry.id == "scenario_cafe_drink_dessert_closeup" and "intent:flatlay" in what:
            penalty += 1.2

        if entry.id == "scenario_cafe_drink_dessert_closeup" and "intent:flower_macro" in what:
            penalty += 2.0

        if entry.id == "scenario_concert_stage_low_light":
            if "intent:action_motion" in what and "place:stage" not in where:
                penalty += 2.0

        if entry.id in {"scenario_beach_backlit_portrait", "scenario_backlit_rim_light_portrait"}:
            if "intent:group_photo" in what and "place:beach" not in where:
                penalty += 1.4

        if entry.id == "scenario_group_travel_selfie":
            if "intent:group_photo" not in what and "intent:selfie" not in what:
                penalty += 1.8

        if entry.id == "scenario_landscape_sky_dynamic_range_2026":
            if "intent:portrait" in what:
                penalty += 2.6
            if "place:beach" in where or "time:noon" in query_slots.when:
                penalty += 0.8

        if entry.id == "scenario_harsh_noon_beach_portrait":
            if "light:backlight" in query_slots.how or "light:rim_light" in query_slots.how:
                penalty += 2.0
            if "issue:hair_highlight_clipping" in issues:
                penalty += 1.4

        if entry.id == "scenario_marketplace_street_food_story":
            if "place:museum" in where:
                penalty += 2.5

        if entry.id == "scenario_action_pan_runner_cyclist":
            if "intent:pets_kids" in what and not ({"mode:panning"} & query_slots.how):
                penalty += 1.2

        specific_routes = {
            "intent:document_scan": {"scenario_document_scan_correction", "scenario_small_product_listing_photo", "scenario_architecture_interior_wide"},
            "intent:receipt_flatlay": {"scenario_receipt_memory_flatlay", "scenario_cafe_flatlay_dessert", "scenario_cafe_drink_dessert_closeup", "scenario_marketplace_street_food_story"},
            "intent:dating_profile": {"scenario_dating_profile_natural_portrait", "scenario_selfie_profile_portrait", "scenario_portrait_skin_tone_2026", "scenario_window_light_cafe_portrait"},
            "intent:aerial_shot": {"scenario_trendy_aerial_beach_minimal", "scenario_landscape_sky_dynamic_range_2026", "scenario_golden_hour_travel_scale"},
            "intent:cave_photo": {"scenario_cave_low_light_travel_portrait", "scenario_backlit_silhouette_sunset", "scenario_concert_stage_low_light", "scenario_city_night_long_exposure"},
            "intent:paparazzi_candid": {"scenario_paparazzi_flash_candid", "scenario_rain_neon_street_portrait", "scenario_fashion_ootd_portrait", "scenario_city_night_long_exposure"},
        }
        for intent, allowed_ids in specific_routes.items():
            if intent in what and entry.id not in allowed_ids:
                penalty += 2.2

        return penalty


def detect_knowledge_gap_concepts(normalized_query: str) -> set[str]:
    concepts: set[str] = set()
    for concept in KNOWLEDGE_GAP_CONCEPTS:
        if any(_contains_marker(normalized_query, phrase) for phrase in concept.phrases):
            concepts.add(concept.id)
    return concepts


def unsupported_knowledge_gap_concepts(entry: ScenarioIndexEntry, concepts: set[str]) -> set[str]:
    if not concepts:
        return set()
    by_id = {concept.id: concept for concept in KNOWLEDGE_GAP_CONCEPTS}
    unsupported: set[str] = set()
    for concept_id in concepts:
        concept = by_id[concept_id]
        if entry.id in concept.supported_scenarios:
            continue
        if entry_has_concept_marker(entry, concept):
            continue
        unsupported.add(concept_id)
    return unsupported


def unknown_intent_penalty(concepts: set[str]) -> float:
    if not concepts:
        return 0.0
    return 4.0 + (0.9 * max(len(concepts) - 1, 0))


def entry_has_concept_marker(entry: ScenarioIndexEntry, concept: KnowledgeGapConcept) -> bool:
    entry_text = normalize_text(
        " ".join(
            [
                entry.name,
                entry.source_file,
                *entry.aliases,
                *entry.tags,
                *(term.replace(":", " ") for term in entry.terms),
            ]
        )
    )
    return any(_contains_marker(entry_text, phrase) for phrase in concept.phrases)


def _contains_marker(text: str, phrase: str) -> bool:
    marker = normalize_text(phrase)
    if not marker:
        return False
    return marker in text


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Match a natural-language photo query to scene-first scenarios.")
    parser.add_argument("query", help="User query to match.")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH_PATH)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    matcher = ScenarioMatcher.from_path(args.graph)
    print(json.dumps([item.as_dict() for item in matcher.match(args.query, args.top_k)], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
