# General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed

- id: `rec_general_fashion_ootd_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/fashion_ootd_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_fashion_ootd_portrait
- **name**: General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/fashion_ootd_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Clean Influencer__edit_style_clean_influencer|Clean Influencer]]
- [[source_nodes/source__Outfit Color Priority__personal_signal_outfit_color_priority|Outfit Color Priority]]
- [[source_nodes/source__Fashion Outfit__subject_fashion_outfit|Fashion Outfit]]
- [[source_nodes/source__2x Lens__tok_2x_lens|2x Lens]]
- [[source_nodes/source__Body Alignment__tok_body_alignment|Body Alignment]]
- [[source_nodes/source__Body Distortion__tok_body_distortion|Body Distortion]]
- [[source_nodes/source__Grid__tok_grid|Grid]]
- [[source_nodes/source__Outfit Color__tok_outfit_color|Outfit Color]]
- [[source_nodes/source__Skin Tone Protection__tok_skin_tone_protection|Skin Tone Protection]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__evidence_raw_scenarios_fashion_ootd_portrait_md|패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__person__subject_person|person]]
- `USES_FACET` → [[scene_nodes/scene__fashion outfit__subject_fashion_outfit|fashion outfit]]
- `USES_FACET` → [[scene_nodes/scene__street or cafe__environment_street_or_cafe|street or cafe]]
- `USES_FACET` → [[scene_nodes/scene__2x or 1x__lens_2x_or_1x|2x or 1x]]
- `USES_FACET` → [[scene_nodes/scene__portrait or photo__mode_portrait_or_photo|portrait or photo]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__렌즈_ 2x 망원 우선, 공간이 좁으면 1x__tech_fashion_ootd_portrait_렌즈_2x_망원_우선_공간이_좁으면_1|렌즈: 2x 망원 우선, 공간이 좁으면 1x.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__모드_ Portrait _ Photo__tech_fashion_ootd_portrait_모드_portrait_photo|모드: Portrait / Photo.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__포즈_ 상체 3_4 각도, 한쪽 다리 앞으로, 어깨 힘 빼기__tech_fashion_ootd_portrait_포즈_상체_3_4_각도_한쪽_다리_앞으|포즈: 상체 3/4 각도, 한쪽 다리 앞으로, 어깨 힘 빼기.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__구도_ 세로 프레임, 인물은 1_3~1_2 비중, 발끝이 잘리지 않게__tech_fashion_ootd_portrait_구도_세로_프레임_인물은_1_3_1_2|구도: 세로 프레임, 인물은 1/3~1/2 비중, 발끝이 잘리지 않게.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__빛_ 사이드 라이트 또는 open shade__tech_fashion_ootd_portrait_빛_사이드_라이트_또는_open_sha|빛: 사이드 라이트 또는 open shade.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__카메라 시작값_ Exposure 0~+0.3, Grid ON__param_fashion_ootd_portrait_카메라_시작값_exposure_0_0|카메라 시작값: Exposure 0~+0.3, Grid ON.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Profile_ Adobe Portrait__param_fashion_ootd_portrait_profile_adobe_portra|Profile: Adobe Portrait.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Temp +3~+6__param_fashion_ootd_portrait_temp_3_6|Temp +3~+6.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Vibrance +10~+15__param_fashion_ootd_portrait_vibrance_10_15|Vibrance +10~+15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Saturation -3~-5__param_fashion_ootd_portrait_saturation_3_5|Saturation -3~-5.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Orange Saturation -5__param_fashion_ootd_portrait_orange_saturation_5|Orange Saturation -5.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Orange Luminance +8~+12__param_fashion_ootd_portrait_orange_luminance_8_1|Orange Luminance +8~+12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__옷 색은 Color Mix로 따로 살리고, 피부는 Subject mask로 보호__param_fashion_ootd_portrait_옷_색은_color_mix로_따로_살|옷 색은 Color Mix로 따로 살리고, 피부는 Subject mask로 보호.]]
- `AVOIDS` → [[scene_nodes/scene__광각을 너무 가까이서 쓰면 신체 비율이 무너진다__risk_fashion_ootd_portrait_광각을_너무_가까이서_쓰면_신체_비율이|광각을 너무 가까이서 쓰면 신체 비율이 무너진다.]]
- `AVOIDS` → [[scene_nodes/scene__옷 색을 살리다가 피부가 과포화되지 않게 한다__risk_fashion_ootd_portrait_옷_색을_살리다가_피부가_과포화되지_않|옷 색을 살리다가 피부가 과포화되지 않게 한다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-a-selfie-iph1b8842__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_express_learn_blog_how-to-take-portrait-__evidence_url_https_www_adobe_com_express_learn_b|https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_still-life_how-__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/]]

## Incoming
- [[scene_nodes/scene__패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__scenario_fashion_ootd_portrait|패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__person__subject_person|person]] → `TRIGGERS`
- [[scene_nodes/scene__fashion outfit__subject_fashion_outfit|fashion outfit]] → `TRIGGERS`
- [[scene_nodes/scene__street or cafe__environment_street_or_cafe|street or cafe]] → `TRIGGERS`
- [[scene_nodes/scene__2x or 1x__lens_2x_or_1x|2x or 1x]] → `TRIGGERS`
- [[scene_nodes/scene__portrait or photo__mode_portrait_or_photo|portrait or photo]] → `TRIGGERS`
