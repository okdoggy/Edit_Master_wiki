# Trend recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기

- id: `rec_trend_small_product_listing_photo`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/small_product_listing_photo.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_small_product_listing_photo
- **name**: Trend recommendation — 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기
- **channel**: trend
- **rank_score**: 0.75
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
- `SUPPORTED_BY` → [[scene_nodes/scene__집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__evidence_raw_scenarios_small_product_listing_pho|집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__home table__environment_home_table|home table]]
- `USES_FACET` → [[scene_nodes/scene__window light__light_window_light|window light]]
- `USES_FACET` → [[scene_nodes/scene__clean product__editstyle_clean_product|clean product]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__창가 옆빛에 흰 종이_천_벽을 배경으로 둔다__tech_small_product_listing_photo_창가_옆빛에_흰_종이_천_벽|창가 옆빛에 흰 종이/천/벽을 배경으로 둔다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x로 전체, 2x로 로고_상태_질감 디테일__tech_small_product_listing_photo_1x로_전체_2x로_로고_상|1x로 전체, 2x로 로고/상태/질감 디테일.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__제품과 카메라를 평행하게 두어 형태 왜곡을 줄인다__tech_small_product_listing_photo_제품과_카메라를_평행하게_두|제품과 카메라를 평행하게 두어 형태 왜곡을 줄인다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__작은 제품은 macro보다 2x로 한 발 물러나 비교__tech_small_product_listing_photo_작은_제품은_macro보다|작은 제품은 macro보다 2x로 한 발 물러나 비교.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__WB를 정확히 맞춰 실제 색과 가깝게__param_small_product_listing_photo_wb를_정확히_맞춰_실제|WB를 정확히 맞춰 실제 색과 가깝게.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.1~+0.4, Highlights -10~-30, Shadows +10~+20__param_small_product_listing_photo_exposure_0_1_0|Exposure +0.1~+0.4, Highlights -10~-30, Shadows +10~+20.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture +5~+20, Clarity +3~+10__param_small_product_listing_photo_texture_5_20_c|Texture +5~+20, Clarity +3~+10.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__배경은 Saturation -10~-30 또는 Remove로 정리__param_small_product_listing_photo_배경은_saturation|배경은 Saturation -10~-30 또는 Remove로 정리.]]
- `AVOIDS` → [[scene_nodes/scene__색을 과하게 예쁘게 만들면 실제 상품과 달라 신뢰가 떨어진다__risk_small_product_listing_photo_색을_과하게_예쁘게_만들면|색을 과하게 예쁘게 만들면 실제 상품과 달라 신뢰가 떨어진다.]]
- `AVOIDS` → [[scene_nodes/scene__광택 제품은 창문_손 반사가 보일 수 있다__risk_small_product_listing_photo_광택_제품은_창문_손_반사가|광택 제품은 창문/손 반사가 보일 수 있다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_help.shopify.com_en_manual_products_product-media_prod__evidence_url_https_help_shopify_com_en_manual_pr|https://help.shopify.com/en/manual/products/product-media/product-photography]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_produ__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/product-photography]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.etsy.com_seller-handbook_article_154343798313__evidence_url_https_www_etsy_com_seller_handbook|https://www.etsy.com/seller-handbook/article/154343798313]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_Etsy_comments_lu2sjd_etsy_sellers_doe__evidence_url_https_www_reddit_com_r_etsy_comment|https://www.reddit.com/r/Etsy/comments/lu2sjd/etsy_sellers_does_product_photography_frustrate/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_EtsySellers_comments_1qr5f3g_struggle__evidence_url_https_www_reddit_com_r_etsysellers|https://www.reddit.com/r/EtsySellers/comments/1qr5f3g/struggle_with_product_photos/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.shopify.com_ie_blog_15163633-how-to-capture-high-q__evidence_url_https_www_shopify_com_ie_blog_15163|https://www.shopify.com/ie/blog/15163633-how-to-capture-high-quality-product-photos-with-your-smartphone]]

## Incoming
- [[scene_nodes/scene__집에서 제품 판매 사진 — 깨끗한 썸네일 만들기__scenario_small_product_listing_photo|집에서 제품 판매 사진 — 깨끗한 썸네일 만들기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__home table__environment_home_table|home table]] → `TRIGGERS`
- [[scene_nodes/scene__window light__light_window_light|window light]] → `TRIGGERS`
- [[scene_nodes/scene__clean product__editstyle_clean_product|clean product]] → `TRIGGERS`
