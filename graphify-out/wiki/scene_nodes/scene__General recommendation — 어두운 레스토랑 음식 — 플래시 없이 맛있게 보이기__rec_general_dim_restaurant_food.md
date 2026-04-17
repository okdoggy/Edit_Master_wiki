# General recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기

- id: `rec_general_dim_restaurant_food`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/dim_restaurant_food.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_dim_restaurant_food
- **name**: General recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/dim_restaurant_food.md

## Source-oriented graph 연결
- [[source_nodes/source__mixed white balance__issue_mixed_white_balance|mixed white balance]]
- [[source_nodes/source__warm editorial food__trend_editorial_food|warm editorial food]]
- [[source_nodes/source__natural review look__pref_natural_review|natural review look]]
- [[source_nodes/source__strong SNS look__pref_strong_sns|strong SNS look]]
- [[source_nodes/source__appetite__outcome_appetite|appetite]]
- [[source_nodes/source__window _ side light__tech_window_or_side_light|window / side light]]
- [[source_nodes/source__food mode__tech_food_mode|food mode]]
- [[source_nodes/source__Texture +5 to +25__param_texture_plus_5_to_25|Texture +5 to +25]]
- [[source_nodes/source__Clarity +3 to +10__param_clarity_plus_3_to_10|Clarity +3 to +10]]
- [[source_nodes/source__Green Saturation -5 to -20__param_green_saturation_minus_5_to_20|Green Saturation -5 to -20]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기__evidence_raw_scenarios_dim_restaurant_food_md|어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__food__subject_food|food]]
- `USES_FACET` → [[scene_nodes/scene__dim restaurant__environment_dim_restaurant|dim restaurant]]
- `USES_FACET` → [[scene_nodes/scene__warm mixed indoor__light_warm_mixed_indoor|warm mixed indoor]]
- `USES_FACET` → [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]]
- `USES_FACET` → [[scene_nodes/scene__night or food or photo__mode_night_or_food_or_photo|night or food or photo]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__플래시는 끄고, 테이블 조명이나 창가_벽 반사광을 찾는다__tech_dim_restaurant_food_플래시는_끄고_테이블_조명이나_창가_벽_반|플래시는 끄고, 테이블 조명이나 창가/벽 반사광을 찾는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x로 전체 접시, 2x로 가장 맛있어 보이는 디테일을 찍는다__tech_dim_restaurant_food_1x로_전체_접시_2x로_가장_맛있어_보이|1x로 전체 접시, 2x로 가장 맛있어 보이는 디테일을 찍는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__흰 접시가 날아가면 EV -0.3~-0.7__param_dim_restaurant_food_흰_접시가_날아가면_ev_0_3_0_7|흰 접시가 날아가면 EV -0.3~-0.7.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__폰을 테이블에 기대고 흔들림을 줄인다__tech_dim_restaurant_food_폰을_테이블에_기대고_흔들림을_줄인다|폰을 테이블에 기대고 흔들림을 줄인다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__WB를 먼저 맞춰 흰 접시가 너무 노랗지 않게 한다__param_dim_restaurant_food_wb를_먼저_맞춰_흰_접시가_너무_노랗지|WB를 먼저 맞춰 흰 접시가 너무 노랗지 않게 한다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.2~+0.4, Highlights -20~-40, Shadows +10~+25__param_dim_restaurant_food_exposure_0_2_0_4_highl|Exposure +0.2~+0.4, Highlights -20~-40, Shadows +10~+25.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture +10~+25, Clarity +3~+10, Vibrance +5~+12__param_dim_restaurant_food_texture_10_25_clarity|Texture +10~+25, Clarity +3~+10, Vibrance +5~+12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Orange_Yellow Saturation +5~+15, Green은 과하면 -5~-20__param_dim_restaurant_food_orange_yellow_saturati|Orange/Yellow Saturation +5~+15, Green은 과하면 -5~-20.]]
- `AVOIDS` → [[scene_nodes/scene__Clarity_Dehaze를 과하게 올리면 음식이 건조해 보인다__risk_dim_restaurant_food_clarity_dehaze를_과하게_올리면|Clarity/Dehaze를 과하게 올리면 음식이 건조해 보인다.]]
- `AVOIDS` → [[scene_nodes/scene__Night mode가 길면 손_젓가락 움직임이 흐려질 수 있다__risk_dim_restaurant_food_night_mode가_길면_손_젓가락_움직|Night mode가 길면 손/젓가락 움직임이 흐려질 수 있다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_four-tips-taking-delectable__evidence_url_https_blog_google_products_pixel_fo|https://blog.google/products/pixel/four-tips-taking-delectable-food-photos-pixel-2/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_ph_fil_lightroom-cc_how-to_mobile-food__evidence_url_https_helpx_adobe_com_ph_fil_lightr|https://helpx.adobe.com/ph_fil/lightroom-cc/how-to/mobile-food-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_time.com_3603028_take-better-food-photos-iphone__evidence_url_https_time_com_3603028_take_better|https://time.com/3603028/take-better-food-photos-iphone/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_foodphotography_comments_1n6jnmx_food__evidence_url_https_www_reddit_com_r_foodphotogra|https://www.reddit.com/r/foodphotography/comments/1n6jnmx/food_photography_tips_on_restaurant_menu/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_productphotography_comments_1sn1msr_h__evidence_url_https_www_reddit_com_r_productphoto|https://www.reddit.com/r/productphotography/comments/1sn1msr/how_to_get_foodrestaurant_photos_like_these/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_support_answer_ANS10001377__evidence_url_https_www_samsung_com_us_support_an|https://www.samsung.com/us/support/answer/ANS10001377/]]

## Incoming
- [[scene_nodes/scene__어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기__scenario_dim_restaurant_food|어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__food__subject_food|food]] → `TRIGGERS`
- [[scene_nodes/scene__dim restaurant__environment_dim_restaurant|dim restaurant]] → `TRIGGERS`
- [[scene_nodes/scene__warm mixed indoor__light_warm_mixed_indoor|warm mixed indoor]] → `TRIGGERS`
- [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]] → `TRIGGERS`
- [[scene_nodes/scene__night or food or photo__mode_night_or_food_or_photo|night or food or photo]] → `TRIGGERS`
