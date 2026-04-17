# 2x portrait

- id: `lens_2x_portrait`
- graph: scene-first
- labels: Lens, SceneFacet
- source_file: raw/scenarios/window_light_cafe_portrait.md
- source_url: 

## Properties
- **id**: lens_2x_portrait
- **key**: lens
- **value**: 2x_portrait
- **name**: 2x portrait
- **source_file**: raw/scenarios/window_light_cafe_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Diffused Window__light_diffused_window|Diffused Window]]
- [[source_nodes/source__Skin Retouch Strength__personal_signal_skin_retouch_strength|Skin Retouch Strength]]
- [[source_nodes/source__Background Distance__tok_background_distance|Background Distance]]
- [[source_nodes/source__Separation__tok_separation|Separation]]
- [[source_nodes/source__Window Light__tok_window_light|Window Light]]
- [[source_nodes/source__2x Portrait__lens_2x_portrait|2x Portrait]]
- [[source_nodes/source__2x Portrait__tok_2x_portrait|2x Portrait]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 해변 역광 인물 — 여름_휴양지 SNS 스타일__rec_general_beach_backlit_portrait|General recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일__rec_general_cherry_blossom_flower_portrait|General recommendation — 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_general_window_light_cafe_portrait|General recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]]

## Incoming
- [[scene_nodes/scene__해변 역광 인물 — 여름_휴양지 SNS 스타일__scenario_beach_backlit_portrait|해변 역광 인물 — 여름/휴양지 SNS 스타일]] → `USES_LENS`
- [[scene_nodes/scene__General recommendation — 해변 역광 인물 — 여름_휴양지 SNS 스타일__rec_general_beach_backlit_portrait|General recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일]] → `USES_FACET`
- [[scene_nodes/scene__벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일__scenario_cherry_blossom_flower_portrait|벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일]] → `USES_LENS`
- [[scene_nodes/scene__General recommendation — 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일__rec_general_cherry_blossom_flower_portrait|General recommendation — 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일]] → `USES_FACET`
- [[scene_nodes/scene__카페 창가 인물 — 자연광_인플루언서 프로필__scenario_window_light_cafe_portrait|카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_LENS`
- [[scene_nodes/scene__General recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_general_window_light_cafe_portrait|General recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_FACET`
