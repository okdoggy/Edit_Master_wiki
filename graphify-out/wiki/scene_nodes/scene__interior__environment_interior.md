# interior

- id: `environment_interior`
- graph: scene-first
- labels: Environment, SceneFacet
- source_file: raw/scenarios/architecture_interior_wide.md
- source_url: 

## Properties
- **id**: environment_interior
- **key**: environment
- **value**: interior
- **name**: interior
- **source_file**: raw/scenarios/architecture_interior_wide.md

## Source-oriented graph 연결
- [[source_nodes/source__0.5x 1x__lens_0_5x_1x|0.5x 1x]]
- [[source_nodes/source__Geometry Edit__tok_geometry_edit|Geometry Edit]]
- [[source_nodes/source__Lines__tok_lines|Lines]]
- [[source_nodes/source__Space__tok_space|Space]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 건축·실내 공간 — 초광각 왜곡 제어__rec_trend_architecture_interior_wide|Trend recommendation — 건축·실내 공간 — 초광각 왜곡 제어]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 건축·실내 공간 — 초광각 왜곡 제어__rec_general_architecture_interior_wide|General recommendation — 건축·실내 공간 — 초광각 왜곡 제어]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 건축·실내 공간 — 초광각 왜곡 제어__rec_personalized_architecture_interior_wide|Personalized recommendation — 건축·실내 공간 — 초광각 왜곡 제어]]

## Incoming
- [[scene_nodes/scene__건축·실내 공간 — 초광각 왜곡 제어__scenario_architecture_interior_wide|건축·실내 공간 — 초광각 왜곡 제어]] → `HAS_ENVIRONMENT`
- [[scene_nodes/scene__Trend recommendation — 건축·실내 공간 — 초광각 왜곡 제어__rec_trend_architecture_interior_wide|Trend recommendation — 건축·실내 공간 — 초광각 왜곡 제어]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 건축·실내 공간 — 초광각 왜곡 제어__rec_general_architecture_interior_wide|General recommendation — 건축·실내 공간 — 초광각 왜곡 제어]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 건축·실내 공간 — 초광각 왜곡 제어__rec_personalized_architecture_interior_wide|Personalized recommendation — 건축·실내 공간 — 초광각 왜곡 제어]] → `USES_FACET`
