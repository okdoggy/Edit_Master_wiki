# daylight or golden hour

- id: `light_daylight_or_golden_hour`
- graph: scene-first
- labels: Light, SceneFacet
- source_file: raw/scenarios/crowded_landmark_portrait.md
- source_url: 

## Properties
- **id**: light_daylight_or_golden_hour
- **key**: light
- **value**: daylight_or_golden_hour
- **name**: daylight or golden hour
- **source_file**: raw/scenarios/crowded_landmark_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__busy background__issue_busy_background|busy background]]
- [[source_nodes/source__scale lost__issue_scale_lost|scale lost]]
- [[source_nodes/source__travel carousel with place + person__trend_travel_carousel|travel carousel with place + person]]
- [[source_nodes/source__place-centric__pref_place_centric|place-centric]]
- [[source_nodes/source__person-centric__pref_person_centric|person-centric]]
- [[source_nodes/source__background separation__outcome_background_separation|background separation]]
- [[source_nodes/source__scale + story__outcome_scale_story|scale + story]]
- [[source_nodes/source__remove _ heal__tech_remove_heal|remove / heal]]
- [[source_nodes/source__Background Saturation -5 to -20__param_background_saturation_minus_5_to_20|Background Saturation -5 to -20]]
- [[source_nodes/source__Adobe smartphone photography__evidence_adobe_smartphone_photography|Adobe smartphone photography]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_trend_crowded_landmark_portrait|Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_general_crowded_landmark_portrait|General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]

## Incoming
- [[scene_nodes/scene__관광지 랜드마크 인물 — 사람 많은 배경 정리__scenario_crowded_landmark_portrait|관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `HAS_LIGHT`
- [[scene_nodes/scene__Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_trend_crowded_landmark_portrait|Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_general_crowded_landmark_portrait|General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `USES_FACET`
