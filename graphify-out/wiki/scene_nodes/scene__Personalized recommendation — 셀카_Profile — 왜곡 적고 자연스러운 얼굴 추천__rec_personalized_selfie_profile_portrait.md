# Personalized recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed

- id: `rec_personalized_selfie_profile_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/selfie_profile_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_selfie_profile_portrait
- **name**: Personalized recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/selfie_profile_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Front Camera__camera_front_camera|Front Camera]]
- [[source_nodes/source__Natural Skin__edit_style_natural_skin|Natural Skin]]
- [[source_nodes/source__Selfie Or Portrait Selfie__mode_selfie_or_portrait_selfie|Selfie Or Portrait Selfie]]
- [[source_nodes/source__Selfie Person__subject_selfie_person|Selfie Person]]
- [[source_nodes/source__Pose__tok_pose|Pose]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__evidence_raw_scenarios_selfie_profile_portrait_m|셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__selfie person__subject_selfie_person|selfie person]]
- `USES_FACET` → [[scene_nodes/scene__natural skin__editstyle_natural_skin|natural skin]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__렌즈_ 전면 카메라, 그룹이면 Wide Selfie__tech_selfie_profile_portrait_렌즈_전면_카메라_그룹이면_wide|렌즈: 전면 카메라, 그룹이면 Wide Selfie.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__모드_ Selfie _ Portrait selfie__tech_selfie_profile_portrait_모드_selfie_portrait|모드: Selfie / Portrait selfie.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__포즈_ 카메라를 눈보다 약간 위, 턱 살짝 앞으로__tech_selfie_profile_portrait_포즈_카메라를_눈보다_약간_위_턱|포즈: 카메라를 눈보다 약간 위, 턱 살짝 앞으로.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__구도_ 눈을 상단 1_3 근처, 팔이 너무 크게 들어오지 않게__tech_selfie_profile_portrait_구도_눈을_상단_1_3_근처_팔이|구도: 눈을 상단 1/3 근처, 팔이 너무 크게 들어오지 않게.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__빛_ 창가_그늘_아침·저녁 고른 빛__tech_selfie_profile_portrait_빛_창가_그늘_아침_저녁_고른_빛|빛: 창가/그늘/아침·저녁 고른 빛.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__시작값_ 타이머 3초, Apple은 볼륨 버튼, Samsung_Pixel은 palm timer류 기능 활용__tech_selfie_profile_portrait_시작값_타이머_3초_apple은_볼|시작값: 타이머 3초, Apple은 볼륨 버튼, Samsung/Pixel은 palm timer류 기능 활용.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Profile_ Adobe Portrait__param_selfie_profile_portrait_profile_adobe_port|Profile: Adobe Portrait.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Temp +4__param_selfie_profile_portrait_temp_4|Temp +4.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Tint +2__param_selfie_profile_portrait_tint_2|Tint +2.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Vibrance +8__param_selfie_profile_portrait_vibrance_8|Vibrance +8.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Orange Saturation -5~-8__param_selfie_profile_portrait_orange_saturation|Orange Saturation -5~-8.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Orange Luminance +8~+12__param_selfie_profile_portrait_orange_luminance_8|Orange Luminance +8~+12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture -5~-12, 단 피부 질감을 모두 지우지 않는다__param_selfie_profile_portrait_texture_5_12_단_피부|Texture -5~-12, 단 피부 질감을 모두 지우지 않는다.]]
- `AVOIDS` → [[scene_nodes/scene__너무 가까운 초광각 셀카는 코_이마 왜곡이 크다__risk_selfie_profile_portrait_너무_가까운_초광각_셀카는_코_이마|너무 가까운 초광각 셀카는 코/이마 왜곡이 크다.]]
- `AVOIDS` → [[scene_nodes/scene__위에서 내려찍는 각도는 적당히만 사용한다__risk_selfie_profile_portrait_위에서_내려찍는_각도는_적당히만_사|위에서 내려찍는 각도는 적당히만 사용한다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-a-selfie-iph1b8842__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_express_learn_blog_how-to-take-portrait-__evidence_url_https_www_adobe_com_express_learn_b|https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_still-life_how-__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/]]

## Incoming
- [[scene_nodes/scene__셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__scenario_selfie_profile_portrait|셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__selfie person__subject_selfie_person|selfie person]] → `TRIGGERS`
- [[scene_nodes/scene__natural skin__editstyle_natural_skin|natural skin]] → `TRIGGERS`
