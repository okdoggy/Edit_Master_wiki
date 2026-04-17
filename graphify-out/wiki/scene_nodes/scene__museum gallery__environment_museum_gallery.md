# museum gallery

- id: `environment_museum_gallery`
- graph: scene-first
- labels: Environment, SceneFacet
- source_file: raw/scenarios/museum_gallery_portrait.md
- source_url: 

## Properties
- **id**: environment_museum_gallery
- **key**: environment
- **value**: museum_gallery
- **name**: museum gallery
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
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_trend_museum_gallery_portrait|Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_general_museum_gallery_portrait|General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_personalized_museum_gallery_portrait|Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]

## Incoming
- [[scene_nodes/scene__미술관·전시회 인물 — 플래시 없이 차분하게__scenario_museum_gallery_portrait|미술관·전시회 인물 — 플래시 없이 차분하게]] → `HAS_ENVIRONMENT`
- [[scene_nodes/scene__Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_trend_museum_gallery_portrait|Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_general_museum_gallery_portrait|General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_personalized_museum_gallery_portrait|Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `USES_FACET`
