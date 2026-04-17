# overcast reflection

- id: `light_overcast_reflection`
- graph: scene-first
- labels: Light, SceneFacet
- source_file: raw/scenarios/snow_portrait_clean_winter.md
- source_url: 

## Properties
- **id**: light_overcast_reflection
- **key**: light
- **value**: overcast_reflection
- **name**: overcast reflection
- **source_file**: raw/scenarios/snow_portrait_clean_winter.md

## Source-oriented graph 연결
- [[source_nodes/source__Clean Winter__edit_style_clean_winter|Clean Winter]]
- [[source_nodes/source__Snow__environment_snow|Snow]]
- [[source_nodes/source__Person__subject_person|Person]]
- [[source_nodes/source__Blue Cast__tok_blue_cast|Blue Cast]]
- [[source_nodes/source__Camera Meter__tok_camera_meter|Camera Meter]]
- [[source_nodes/source__Light__tok_light|Light]]
- [[source_nodes/source__Subject Mask__tok_subject_mask|Subject Mask]]
- [[source_nodes/source__Underexpose Snow__tok_underexpose_snow|Underexpose Snow]]
- [[source_nodes/source__White Balance__tok_white_balance|White Balance]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__rec_trend_snow_portrait_clean_winter|Trend recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__rec_general_snow_portrait_clean_winter|General recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]]

## Incoming
- [[scene_nodes/scene__눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__scenario_snow_portrait_clean_winter|눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]] → `HAS_LIGHT`
- [[scene_nodes/scene__Trend recommendation — 눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__rec_trend_snow_portrait_clean_winter|Trend recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__rec_general_snow_portrait_clean_winter|General recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]] → `USES_FACET`
