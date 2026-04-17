# landmark

- id: `environment_landmark`
- graph: scene-first
- labels: Environment, SceneFacet
- source_file: raw/scenarios/golden_hour_travel_scale.md
- source_url: 

## Properties
- **id**: environment_landmark
- **key**: environment
- **value**: landmark
- **name**: landmark
- **source_file**: raw/scenarios/golden_hour_travel_scale.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Travel__edit_style_warm_travel|Warm Travel]]
- [[source_nodes/source__Golden Hour__light_golden_hour|Golden Hour]]
- [[source_nodes/source__Traveler__subject_traveler|Traveler]]
- [[source_nodes/source__Detail__tok_detail|Detail]]
- [[source_nodes/source__Detail Shot__tok_detail_shot|Detail Shot]]
- [[source_nodes/source__Golden Hour__tok_golden_hour|Golden Hour]]
- [[source_nodes/source__Location__tok_location|Location]]
- [[source_nodes/source__Memory__tok_memory|Memory]]
- [[source_nodes/source__Scale Subject__tok_scale_subject|Scale Subject]]
- [[source_nodes/source__Size__tok_size|Size]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 여행 골든아워 — wide_detail_scale 3컷 추천__rec_trend_golden_hour_travel_scale|Trend recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 여행 골든아워 — wide_detail_scale 3컷 추천__rec_general_golden_hour_travel_scale|General recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 여행 골든아워 — wide_detail_scale 3컷__rec_personalized_golden_hour_travel_scale|Personalized recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]]

## Incoming
- [[scene_nodes/scene__여행 골든아워 — wide_detail_scale 3컷 추천__scenario_golden_hour_travel_scale|여행 골든아워 — wide/detail/scale 3컷 추천]] → `HAS_ENVIRONMENT`
- [[scene_nodes/scene__Trend recommendation — 여행 골든아워 — wide_detail_scale 3컷 추천__rec_trend_golden_hour_travel_scale|Trend recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 여행 골든아워 — wide_detail_scale 3컷 추천__rec_general_golden_hour_travel_scale|General recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 여행 골든아워 — wide_detail_scale 3컷__rec_personalized_golden_hour_travel_scale|Personalized recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]] → `USES_FACET`
