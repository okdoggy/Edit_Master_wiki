# stage

- id: `environment_stage`
- graph: scene-first
- labels: Environment, SceneFacet
- source_file: raw/scenarios/concert_stage_low_light.md
- source_url: 

## Properties
- **id**: environment_stage
- **key**: environment
- **value**: stage
- **name**: stage
- **source_file**: raw/scenarios/concert_stage_low_light.md

## Source-oriented graph 연결
- [[source_nodes/source__Moody Stage__edit_style_moody_stage|Moody Stage]]
- [[source_nodes/source__3x 5x 10x__lens_3x_5x_10x|3x 5x 10x]]
- [[source_nodes/source__Spotlight__light_spotlight|Spotlight]]
- [[source_nodes/source__Photo Or Pro__mode_photo_or_pro|Photo Or Pro]]
- [[source_nodes/source__Performer__subject_performer|Performer]]
- [[source_nodes/source__Clipping__tok_clipping|Clipping]]
- [[source_nodes/source__Fast Shutter__tok_fast_shutter|Fast Shutter]]
- [[source_nodes/source__Motion__tok_motion|Motion]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_trend_concert_stage_low_light|Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_general_concert_stage_low_light|General recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_personalized_concert_stage_low_light|Personalized recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]]

## Incoming
- [[scene_nodes/scene__공연·무대 저조도 — 망원_하이라이트 보호__scenario_concert_stage_low_light|공연·무대 저조도 — 망원/하이라이트 보호]] → `HAS_ENVIRONMENT`
- [[scene_nodes/scene__Trend recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_trend_concert_stage_low_light|Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_general_concert_stage_low_light|General recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_personalized_concert_stage_low_light|Personalized recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]] → `USES_FACET`
