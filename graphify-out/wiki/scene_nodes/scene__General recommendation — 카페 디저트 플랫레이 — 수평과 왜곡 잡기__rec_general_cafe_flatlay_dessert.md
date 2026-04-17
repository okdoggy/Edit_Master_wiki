# General recommendation — 카페 디저트 플랫레이 — 수평과 왜곡 잡기

- id: `rec_general_cafe_flatlay_dessert`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/cafe_flatlay_dessert.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_cafe_flatlay_dessert
- **name**: General recommendation — 카페 디저트 플랫레이 — 수평과 왜곡 잡기
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/cafe_flatlay_dessert.md

## Source-oriented graph 연결
- [[source_nodes/source__tilted table__issue_tilted_table|tilted table]]
- [[source_nodes/source__warm aligned cafe flatlay__trend_cafe_alignment_warm|warm aligned cafe flatlay]]
- [[source_nodes/source__minimal props__pref_minimal_props|minimal props]]
- [[source_nodes/source__prop-rich__pref_prop_rich|prop-rich]]
- [[source_nodes/source__alignment__outcome_alignment|alignment]]
- [[source_nodes/source__grid _ level__tech_grid_level|grid / level]]
- [[source_nodes/source__geometry straighten__tech_geometry_straighten|geometry straighten]]
- [[source_nodes/source__Whites +5 to +15__param_whites_plus_5_to_15|Whites +5 to +15]]
- [[source_nodes/source__Vibrance +3 to +12__param_vibrance_plus_3_to_12|Vibrance +3 to +12]]
- [[source_nodes/source__Texture +3 to +10__param_texture_plus_3_to_10|Texture +3 to +10]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__카페 디저트 플랫레이 — 수평과 왜곡 잡기__evidence_raw_scenarios_cafe_flatlay_dessert_md|카페 디저트 플랫레이 — 수평과 왜곡 잡기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__dessert coffee__subject_dessert_coffee|dessert coffee]]
- `USES_FACET` → [[scene_nodes/scene__cafe table__environment_cafe_table|cafe table]]
- `USES_FACET` → [[scene_nodes/scene__1x or 0 5x__lens_1x_or_0_5x|1x or 0 5x]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__Grid_Level을 켜고 완전 탑뷰로 맞춘다__param_cafe_flatlay_dessert_grid_level을_켜고_완전_탑뷰로|Grid/Level을 켜고 완전 탑뷰로 맞춘다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__가능하면 의자에 올라가 1x로 찍고, 공간이 부족할 때만 0.5x__tech_cafe_flatlay_dessert_가능하면_의자에_올라가_1x로_찍고_공간|가능하면 의자에 올라가 1x로 찍고, 공간이 부족할 때만 0.5x.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__접시와 컵이 가장자리에서 잘리지 않게 여백을 둔다__tech_cafe_flatlay_dessert_접시와_컵이_가장자리에서_잘리지_않게_여|접시와 컵이 가장자리에서 잘리지 않게 여백을 둔다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__손_스푼_냅킨은 1~2개만 포인트로 둔다__tech_cafe_flatlay_dessert_손_스푼_냅킨은_1_2개만_포인트로_둔다|손/스푼/냅킨은 1~2개만 포인트로 둔다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Crop_Geometry로 테이블 수평을 먼저 맞춘다__param_cafe_flatlay_dessert_crop_geometry로_테이블_수평|Crop/Geometry로 테이블 수평을 먼저 맞춘다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.2~+0.5, Highlights -10~-25, Shadows +10~+20__param_cafe_flatlay_dessert_exposure_0_2_0_5_high|Exposure +0.2~+0.5, Highlights -10~-25, Shadows +10~+20.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Whites +5~+15, Vibrance +3~+8, Texture +3~+10__param_cafe_flatlay_dessert_whites_5_15_vibrance|Whites +5~+15, Vibrance +3~+8, Texture +3~+10.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__흰 접시 기준으로 WB를 맞춘다__param_cafe_flatlay_dessert_흰_접시_기준으로_wb를_맞춘다|흰 접시 기준으로 WB를 맞춘다.]]
- `AVOIDS` → [[scene_nodes/scene__0.5x로 가까이 찍으면 접시가 타원형으로 늘어난다__risk_cafe_flatlay_dessert_0_5x로_가까이_찍으면_접시가_타원형으|0.5x로 가까이 찍으면 접시가 타원형으로 늘어난다.]]
- `AVOIDS` → [[scene_nodes/scene__소품이 많으면 음식보다 배경이 먼저 보인다__risk_cafe_flatlay_dessert_소품이_많으면_음식보다_배경이_먼저_보인|소품이 많으면 음식보다 배경이 먼저 보인다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_four-tips-taking-delectable__evidence_url_https_blog_google_products_pixel_fo|https://blog.google/products/pixel/four-tips-taking-delectable-food-photos-pixel-2/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_ph_fil_lightroom-cc_how-to_mobile-food__evidence_url_https_helpx_adobe_com_ph_fil_lightr|https://helpx.adobe.com/ph_fil/lightroom-cc/how-to/mobile-food-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_foodphotography_comments_1n6jnmx_food__evidence_url_https_www_reddit_com_r_foodphotogra|https://www.reddit.com/r/foodphotography/comments/1n6jnmx/food_photography_tips_on_restaurant_menu/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_support_answer_ANS10001377__evidence_url_https_www_samsung_com_us_support_an|https://www.samsung.com/us/support/answer/ANS10001377/]]

## Incoming
- [[scene_nodes/scene__카페 디저트 플랫레이 — 수평과 왜곡 잡기__scenario_cafe_flatlay_dessert|카페 디저트 플랫레이 — 수평과 왜곡 잡기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__dessert coffee__subject_dessert_coffee|dessert coffee]] → `TRIGGERS`
- [[scene_nodes/scene__cafe table__environment_cafe_table|cafe table]] → `TRIGGERS`
- [[scene_nodes/scene__1x or 0 5x__lens_1x_or_0_5x|1x or 0 5x]] → `TRIGGERS`
