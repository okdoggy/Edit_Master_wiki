"""Scenario matcher for the scene-first smartphone photo recommender."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from .graph_loader import DEFAULT_GRAPH_PATH, Node, SceneGraph
from .graph_loader import REPO_ROOT
from .normalization import QuerySlots, canonical_terms_for_text, extract_slots, normalize_text, tokenize


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
        "how": {"lens_mode:2x", "mode:portrait"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights"},
    },
    "scenario_beach_backlit_portrait": {
        "when": {"time:golden_hour", "season:summer"},
        "where": {"place:beach"},
        "what": {"intent:portrait", "intent:trendy_style"},
        "how": {"lens_mode:2x", "mode:portrait"},
        "issues": {"issue:underexposed_face", "issue:blown_highlights"},
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

    def as_dict(self) -> dict:
        return {
            "scenario_id": self.scenario_id,
            "scenario_name": self.scenario_name,
            "score": round(self.score, 4),
            "source_file": self.source_file,
            "matched_terms": self.matched_terms,
            "matched_slots": self.matched_slots,
            "reasons": self.reasons,
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

        results = [self._score_entry(entry, normalized, query_terms, query_tokens, query_slots) for entry in self.entries]
        results.sort(key=lambda item: (item.score, len(item.matched_terms), item.scenario_name), reverse=True)
        return [item for item in results if item.score > 0][:top_k]

    def _score_entry(
        self,
        entry: ScenarioIndexEntry,
        normalized_query: str,
        query_terms: set[str],
        query_tokens: set[str],
        query_slots: QuerySlots,
    ) -> MatchResult:
        score = 0.0
        reasons: list[str] = []

        direct_aliases = [alias for alias in entry.aliases if normalize_text(alias) and normalize_text(alias) in normalized_query]
        if direct_aliases:
            score += 5.0 + min(len(direct_aliases), 3)
            reasons.append("direct_alias")

        name_tokens = tokenize(entry.name)
        name_overlap = query_tokens & name_tokens
        if name_overlap:
            score += len(name_overlap) * 0.45
            reasons.append("scenario_name_overlap")

        term_overlap = query_terms & entry.terms
        if term_overlap:
            score += len(term_overlap) * 0.35
            reasons.append("graph_term_overlap")

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
                score += slot_weights[slot] * len(overlap)
                reasons.append(f"{slot}_slot")

        score += self._specificity_bonus(entry, query_slots, matched_slots)
        score -= self._conflict_penalty(entry, query_slots)

        return MatchResult(
            scenario_id=entry.id,
            scenario_name=entry.name,
            score=score,
            source_file=entry.source_file,
            matched_terms=sorted(term_overlap)[:20],
            matched_slots=matched_slots,
            reasons=sorted(set(reasons)),
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

        return penalty


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
