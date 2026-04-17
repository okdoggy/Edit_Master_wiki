# clean product

- id: `editstyle_clean_product`
- graph: scene-first
- labels: EditStyle, SceneFacet
- source_file: raw/scenarios/small_product_listing_photo.md
- source_url: 

## Properties
- **id**: editstyle_clean_product
- **key**: edit_style
- **value**: clean_product
- **name**: clean product
- **source_file**: raw/scenarios/small_product_listing_photo.md

## Source-oriented graph 연결
- [[source_nodes/source__color inaccuracy__issue_color_inaccuracy|color inaccuracy]]
- [[source_nodes/source__trustworthy listing photo__trend_trustworthy_listing|trustworthy listing photo]]
- [[source_nodes/source__color accuracy__pref_color_accuracy|color accuracy]]
- [[source_nodes/source__aesthetic thumbnail__pref_aesthetic_thumbnail|aesthetic thumbnail]]
- [[source_nodes/source__trustworthy listing__outcome_trustworthy_listing|trustworthy listing]]
- [[source_nodes/source__white background__tech_white_background|white background]]
- [[source_nodes/source__background cleanup__tech_background_cleanup|background cleanup]]
- [[source_nodes/source__Background Saturation -10 to -30__param_background_saturation_minus_10_to_30|Background Saturation -10 to -30]]
- [[source_nodes/source__Shopify product photography help__evidence_shopify_product_photography|Shopify product photography help]]
- [[source_nodes/source__Shopify smartphone product photography article__evidence_shopify_smartphone_product_photography|Shopify smartphone product photography article]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__rec_trend_small_product_listing_photo|Trend recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__rec_personalized_small_product_listing_photo|Personalized recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]]

## Incoming
- [[scene_nodes/scene__집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__scenario_small_product_listing_photo|집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__rec_trend_small_product_listing_photo|Trend recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__rec_personalized_small_product_listing_photo|Personalized recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]] → `USES_FACET`
