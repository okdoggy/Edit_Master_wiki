# mixed white balance

- id: `risk_mixed_white_balance`
- graph: scene-first
- labels: Risk, SceneFacet
- source_file: raw/scenarios/museum_gallery_portrait.md
- source_url: 

## Properties
- **id**: risk_mixed_white_balance
- **key**: risk
- **value**: mixed_white_balance
- **name**: mixed white balance
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
- [[scene_nodes/scene__어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기__scenario_dim_restaurant_food|어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기]] → `HAS_RISK`
- [[scene_nodes/scene__실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__scenario_indoor_party_group|실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]] → `HAS_RISK`
- [[scene_nodes/scene__미술관·전시회 인물 — 플래시 없이 차분하게__scenario_museum_gallery_portrait|미술관·전시회 인물 — 플래시 없이 차분하게]] → `HAS_RISK`
