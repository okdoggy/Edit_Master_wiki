# photo or portrait

- id: `mode_photo_or_portrait`
- graph: scene-first
- labels: Mode, SceneFacet
- source_file: raw/scenarios/museum_gallery_portrait.md
- source_url: 

## Properties
- **id**: mode_photo_or_portrait
- **key**: mode
- **value**: photo_or_portrait
- **name**: photo or portrait
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
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_general_crowded_landmark_portrait|General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기__rec_general_harsh_noon_beach_portrait|General recommendation — 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_general_museum_gallery_portrait|General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]

## Incoming
- [[scene_nodes/scene__관광지 랜드마크 인물 — 사람 많은 배경 정리__scenario_crowded_landmark_portrait|관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `USES_MODE`
- [[scene_nodes/scene__General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_general_crowded_landmark_portrait|General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `USES_FACET`
- [[scene_nodes/scene__한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기__scenario_harsh_noon_beach_portrait|한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기]] → `USES_MODE`
- [[scene_nodes/scene__General recommendation — 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기__rec_general_harsh_noon_beach_portrait|General recommendation — 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기]] → `USES_FACET`
- [[scene_nodes/scene__미술관·전시회 인물 — 플래시 없이 차분하게__scenario_museum_gallery_portrait|미술관·전시회 인물 — 플래시 없이 차분하게]] → `USES_MODE`
- [[scene_nodes/scene__General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_general_museum_gallery_portrait|General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]] → `USES_FACET`
