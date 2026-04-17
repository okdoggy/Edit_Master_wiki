# warm travel

- id: `editstyle_warm_travel`
- graph: scene-first
- labels: EditStyle, SceneFacet
- source_file: raw/scenarios/golden_hour_travel_scale.md
- source_url: 

## Properties
- **id**: editstyle_warm_travel
- **key**: edit_style
- **value**: warm_travel
- **name**: warm travel
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
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_trend_crowded_landmark_portrait|Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_personalized_crowded_landmark_portrait|Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 여행 골든아워 — wide_detail_scale 3컷 추천__rec_trend_golden_hour_travel_scale|Trend recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 여행 골든아워 — wide_detail_scale 3컷__rec_personalized_golden_hour_travel_scale|Personalized recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]]

## Incoming
- [[scene_nodes/scene__관광지 랜드마크 인물 — 사람 많은 배경 정리__scenario_crowded_landmark_portrait|관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_trend_crowded_landmark_portrait|Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_personalized_crowded_landmark_portrait|Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `USES_FACET`
- [[scene_nodes/scene__여행 골든아워 — wide_detail_scale 3컷 추천__scenario_golden_hour_travel_scale|여행 골든아워 — wide/detail/scale 3컷 추천]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 여행 골든아워 — wide_detail_scale 3컷 추천__rec_trend_golden_hour_travel_scale|Trend recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 여행 골든아워 — wide_detail_scale 3컷__rec_personalized_golden_hour_travel_scale|Personalized recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천]] → `USES_FACET`
