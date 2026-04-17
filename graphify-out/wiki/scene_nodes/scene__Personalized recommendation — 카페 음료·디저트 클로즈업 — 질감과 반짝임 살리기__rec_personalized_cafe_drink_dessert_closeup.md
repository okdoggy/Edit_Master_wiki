# Personalized recommendation — 카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기

- id: `rec_personalized_cafe_drink_dessert_closeup`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/cafe_drink_dessert_closeup.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_cafe_drink_dessert_closeup
- **name**: Personalized recommendation — 카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/cafe_drink_dessert_closeup.md

## Source-oriented graph 연결
- [[source_nodes/source__focus miss__issue_focus_miss|focus miss]]
- [[source_nodes/source__highlight reflection__issue_highlight_reflection|highlight reflection]]
- [[source_nodes/source__texture-first cafe close-up__trend_texture_first_cafe|texture-first cafe close-up]]
- [[source_nodes/source__soft and edible__pref_soft_edible|soft and edible]]
- [[source_nodes/source__crisp texture__pref_crisp_texture|crisp texture]]
- [[source_nodes/source__texture detail__outcome_texture_detail|texture detail]]
- [[source_nodes/source__macro or 2x__tech_macro_or_2x|macro or 2x]]
- [[source_nodes/source__Vibrance +5 to +15__param_vibrance_plus_5_to_15|Vibrance +5 to +15]]
- [[source_nodes/source__Google Pixel food tips__evidence_google_pixel_food_tips|Google Pixel food tips]]
- [[source_nodes/source__Samsung Food mode__evidence_samsung_food_mode|Samsung Food mode]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기__evidence_raw_scenarios_cafe_drink_dessert_closeu|카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__cafe drink dessert__subject_cafe_drink_dessert|cafe drink dessert]]
- `USES_FACET` → [[scene_nodes/scene__cafe table__environment_cafe_table|cafe table]]
- `USES_FACET` → [[scene_nodes/scene__food glow__editstyle_food_glow|food glow]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__컵_케이크 전체는 1x_2x, 거품_시럽_크림은 macro 또는 2x__tech_cafe_drink_dessert_closeup_컵_케이크_전체는_1x_2x|컵/케이크 전체는 1x/2x, 거품/시럽/크림은 macro 또는 2x.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__창가 사광_역광으로 유리컵 반짝임을 만든다__tech_cafe_drink_dessert_closeup_창가_사광_역광으로_유리컵_반|창가 사광/역광으로 유리컵 반짝임을 만든다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__초점은 크림 결, 라떼아트, 시럽 라인에 맞춘다__tech_cafe_drink_dessert_closeup_초점은_크림_결_라떼아트_시럽|초점은 크림 결, 라떼아트, 시럽 라인에 맞춘다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__하이라이트가 반짝이면 EV -0.3__param_cafe_drink_dessert_closeup_하이라이트가_반짝이면_ev|하이라이트가 반짝이면 EV -0.3.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.1~+0.3, Highlights -10~-30, Shadows +5~+15__param_cafe_drink_dessert_closeup_exposure_0_1_0|Exposure +0.1~+0.3, Highlights -10~-30, Shadows +5~+15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Whites +5~+15, Temp +5~+10__param_cafe_drink_dessert_closeup_whites_5_15_tem|Whites +5~+15, Temp +5~+10.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture +5~+15, Clarity 0~+5__param_cafe_drink_dessert_closeup_texture_5_15_cl|Texture +5~+15, Clarity 0~+5.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-15로 시선 정리__param_cafe_drink_dessert_closeup_background_satu|Background Saturation -5~-15로 시선 정리.]]
- `AVOIDS` → [[scene_nodes/scene__macro는 초점 실패가 잦으니 여러 장 찍는다__risk_cafe_drink_dessert_closeup_macro는_초점_실패가_잦으|macro는 초점 실패가 잦으니 여러 장 찍는다.]]
- `AVOIDS` → [[scene_nodes/scene__Clarity를 과하게 올리면 크림이 딱딱해 보인다__risk_cafe_drink_dessert_closeup_clarity를_과하게_올리면|Clarity를 과하게 올리면 크림이 딱딱해 보인다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_four-tips-taking-delectable__evidence_url_https_blog_google_products_pixel_fo|https://blog.google/products/pixel/four-tips-taking-delectable-food-photos-pixel-2/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_ph_fil_lightroom-cc_how-to_mobile-food__evidence_url_https_helpx_adobe_com_ph_fil_lightr|https://helpx.adobe.com/ph_fil/lightroom-cc/how-to/mobile-food-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_productphotography_comments_1sn1msr_h__evidence_url_https_www_reddit_com_r_productphoto|https://www.reddit.com/r/productphotography/comments/1sn1msr/how_to_get_foodrestaurant_photos_like_these/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_support_answer_ANS10001377__evidence_url_https_www_samsung_com_us_support_an|https://www.samsung.com/us/support/answer/ANS10001377/]]

## Incoming
- [[scene_nodes/scene__카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기__scenario_cafe_drink_dessert_closeup|카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__cafe drink dessert__subject_cafe_drink_dessert|cafe drink dessert]] → `TRIGGERS`
- [[scene_nodes/scene__cafe table__environment_cafe_table|cafe table]] → `TRIGGERS`
- [[scene_nodes/scene__food glow__editstyle_food_glow|food glow]] → `TRIGGERS`
