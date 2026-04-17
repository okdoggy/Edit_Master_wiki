# cafe window

- id: `environment_cafe_window`
- graph: scene-first
- labels: Environment, SceneFacet
- source_file: raw/scenarios/window_light_cafe_portrait.md
- source_url: 

## Properties
- **id**: environment_cafe_window
- **key**: environment
- **value**: cafe_window
- **name**: cafe window
- **source_file**: raw/scenarios/window_light_cafe_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Diffused Window__light_diffused_window|Diffused Window]]
- [[source_nodes/source__Skin Retouch Strength__personal_signal_skin_retouch_strength|Skin Retouch Strength]]
- [[source_nodes/source__Background Distance__tok_background_distance|Background Distance]]
- [[source_nodes/source__Separation__tok_separation|Separation]]
- [[source_nodes/source__Window Light__tok_window_light|Window Light]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_trend_window_light_cafe_portrait|Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_general_window_light_cafe_portrait|General recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_personalized_window_light_cafe_portrait|Personalized recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]]

## Incoming
- [[scene_nodes/scene__카페 창가 인물 — 자연광_인플루언서 프로필__scenario_window_light_cafe_portrait|카페 창가 인물 — 자연광/인플루언서 프로필]] → `HAS_ENVIRONMENT`
- [[scene_nodes/scene__Trend recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_trend_window_light_cafe_portrait|Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_general_window_light_cafe_portrait|General recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_personalized_window_light_cafe_portrait|Personalized recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_FACET`
