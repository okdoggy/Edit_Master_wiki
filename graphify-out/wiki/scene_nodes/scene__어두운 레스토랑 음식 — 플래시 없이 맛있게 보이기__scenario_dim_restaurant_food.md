# 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기

- id: `scenario_dim_restaurant_food`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/dim_restaurant_food.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_dim_restaurant_food
- **name**: 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기
- **source_file**: raw/scenarios/dim_restaurant_food.md
- **tags**: ['food', 'restaurant', 'low-light', 'white-balance', 'no-flash']

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
- `HAS_SUBJECT` → [[scene_nodes/scene__food__subject_food|food]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__dim restaurant__environment_dim_restaurant|dim restaurant]]
- `HAS_LIGHT` → [[scene_nodes/scene__warm mixed indoor__light_warm_mixed_indoor|warm mixed indoor]]
- `USES_LENS` → [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]]
- `USES_MODE` → [[scene_nodes/scene__night or food or photo__mode_night_or_food_or_photo|night or food or photo]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__food glow__editstyle_food_glow|food glow]]
- `HAS_RISK` → [[scene_nodes/scene__mixed white balance__risk_mixed_white_balance|mixed white balance]]
- `HAS_RISK` → [[scene_nodes/scene__motion blur__risk_motion_blur|motion blur]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__warm_mixed_light CAUSES_yellow_cast__tech_dim_restaurant_food_warm_mixed_light_causes|warm_mixed_light CAUSES_yellow_cast]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x_2x BALANCES_quality_and_detail__tech_dim_restaurant_food_1x_2x_balances_quality|1x_2x BALANCES_quality_and_detail]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__window_or_side_light IMPROVES_food_texture__tech_dim_restaurant_food_window_or_side_light_im|window_or_side_light IMPROVES_food_texture]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__food_mask ENHANCES_texture__tech_dim_restaurant_food_food_mask_enhances_text|food_mask ENHANCES_texture]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기__rec_trend_dim_restaurant_food|Trend recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기__rec_general_dim_restaurant_food|General recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기__rec_personalized_dim_restaurant_food|Personalized recommendation — 어두운 레스토랑 음식 — 플래시 없이 맛있게 보이기]]
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
- [[scene_nodes/scene__어두운 식당 음식__alias_어두운_식당_음식|어두운 식당 음식]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__레스토랑 파스타 노랗다__alias_레스토랑_파스타_노랗다|레스토랑 파스타 노랗다]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__음식이 흐릿해요__alias_음식이_흐릿해요|음식이 흐릿해요]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__플래시 없이 음식__alias_플래시_없이_음식|플래시 없이 음식]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__노란 조명 음식 보정__alias_노란_조명_음식_보정|노란 조명 음식 보정]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__저조도 음식사진__alias_저조도_음식사진|저조도 음식사진]] → `MATCHES_SCENARIO`
