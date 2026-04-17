# backlight golden hour

- id: `light_backlight_golden_hour`
- graph: scene-first
- labels: Light, SceneFacet
- source_file: raw/scenarios/beach_backlit_portrait.md
- source_url: 

## Properties
- **id**: light_backlight_golden_hour
- **key**: light
- **value**: backlight_golden_hour
- **name**: backlight golden hour
- **source_file**: raw/scenarios/beach_backlit_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Blue Travel__edit_style_warm_blue_travel|Warm Blue Travel]]
- [[source_nodes/source__Beach__environment_beach|Beach]]
- [[source_nodes/source__2x Portrait__lens_2x_portrait|2x Portrait]]
- [[source_nodes/source__2x Portrait__tok_2x_portrait|2x Portrait]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 해변 역광 인물 — 여름_휴양지 SNS 스타일__rec_trend_beach_backlit_portrait|Trend recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 해변 역광 인물 — 여름_휴양지 SNS 스타일__rec_general_beach_backlit_portrait|General recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일]]

## Incoming
- [[scene_nodes/scene__해변 역광 인물 — 여름_휴양지 SNS 스타일__scenario_beach_backlit_portrait|해변 역광 인물 — 여름/휴양지 SNS 스타일]] → `HAS_LIGHT`
- [[scene_nodes/scene__Trend recommendation — 해변 역광 인물 — 여름_휴양지 SNS 스타일__rec_trend_beach_backlit_portrait|Trend recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 해변 역광 인물 — 여름_휴양지 SNS 스타일__rec_general_beach_backlit_portrait|General recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일]] → `USES_FACET`
