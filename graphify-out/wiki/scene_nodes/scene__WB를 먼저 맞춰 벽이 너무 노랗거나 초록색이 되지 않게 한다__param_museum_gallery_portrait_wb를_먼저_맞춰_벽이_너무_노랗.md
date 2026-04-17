# WB를 먼저 맞춰 벽이 너무 노랗거나 초록색이 되지 않게 한다.

- id: `param_museum_gallery_portrait_wb를_먼저_맞춰_벽이_너무_노랗거나_초록색이_되지_않게_한다.`
- graph: scene-first
- labels: Parameter
- source_file: raw/scenarios/museum_gallery_portrait.md
- source_url: 

## Properties
- **id**: param_museum_gallery_portrait_wb를_먼저_맞춰_벽이_너무_노랗거나_초록색이_되지_않게_한다.
- **name**: WB를 먼저 맞춰 벽이 너무 노랗거나 초록색이 되지 않게 한다.
- **source_file**: raw/scenarios/museum_gallery_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__color cast__issue_color_cast|color cast]]
- [[source_nodes/source__minimal clean gallery__trend_minimal_clean_gallery|minimal clean gallery]]
- [[source_nodes/source__minimal clean__pref_minimal_clean|minimal clean]]
- [[source_nodes/source__art centered__pref_art_centered|art centered]]
- [[source_nodes/source__minimal clean__outcome_minimal_clean|minimal clean]]
- [[source_nodes/source__art context__outcome_art_context|art context]]
- [[source_nodes/source__no flash__tech_no_flash|no flash]]
- [[source_nodes/source__white balance correction__tech_white_balance|white balance correction]]
- [[source_nodes/source__negative space__tech_negative_space|negative space]]
- [[source_nodes/source__White balance control__param_wb_control|White balance control]]

## Outgoing

## Incoming
- [[scene_nodes/scene__Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_trend_museum_gallery_portrait|Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `SETS_PARAMETER`
- [[scene_nodes/scene__General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_general_museum_gallery_portrait|General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `SETS_PARAMETER`
- [[scene_nodes/scene__Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_personalized_museum_gallery_portrait|Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `SETS_PARAMETER`
