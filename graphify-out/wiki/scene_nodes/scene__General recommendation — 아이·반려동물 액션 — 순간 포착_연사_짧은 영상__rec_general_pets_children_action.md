# General recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상

- id: `rec_general_pets_children_action`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/pets_children_action.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_pets_children_action
- **name**: General recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/pets_children_action.md

## Source-oriented graph 연결
- [[source_nodes/source__Clear Action__edit_style_clear_action|Clear Action]]
- [[source_nodes/source__Burst Live Video__mode_burst_live_video|Burst Live Video]]
- [[source_nodes/source__Kids Or Pets__subject_kids_or_pets|Kids Or Pets]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__아이·반려동물 액션 — 순간 포착_연사_짧은 영상__evidence_raw_scenarios_pets_children_action_md|아이·반려동물 액션 — 순간 포착/연사/짧은 영상]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__kids or pets__subject_kids_or_pets|kids or pets]]
- `USES_FACET` → [[scene_nodes/scene__burst live video__mode_burst_live_video|burst live video]]
- `USES_FACET` → [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]]
- `USES_FACET` → [[scene_nodes/scene__bright natural__light_bright_natural|bright natural]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__야외 밝은 그늘에서 촬영한다__tech_pets_children_action_야외_밝은_그늘에서_촬영한다|야외 밝은 그늘에서 촬영한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x는 움직임 추적, 2x는 표정 클로즈업__tech_pets_children_action_1x는_움직임_추적_2x는_표정_클로즈업|1x는 움직임 추적, 2x는 표정 클로즈업.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__Burst_Live Photo_4K video still로 순간을 확보__tech_pets_children_action_burst_live_photo_4k_vi|Burst/Live Photo/4K video still로 순간을 확보.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__눈 높이 또는 더 낮은 앵글로 촬영__tech_pets_children_action_눈_높이_또는_더_낮은_앵글로_촬영|눈 높이 또는 더 낮은 앵글로 촬영.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.1~+0.3, Highlights -10~-30__param_pets_children_action_exposure_0_1_0_3_high|Exposure +0.1~+0.3, Highlights -10~-30.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture_Clarity +5~+15 for fur_detail__param_pets_children_action_texture_clarity_5_15|Texture/Clarity +5~+15 for fur/detail.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-15__param_pets_children_action_background_saturation|Background Saturation -5~-15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__움직임 blur가 매력적이면 Grain +10~+20로 스타일화__param_pets_children_action_움직임_blur가_매력적이면_grain|움직임 blur가 매력적이면 Grain +10~+20로 스타일화.]]
- `AVOIDS` → [[scene_nodes/scene__Night mode는 움직이는 아이_동물에 부적합__risk_pets_children_action_night_mode는_움직이는_아이_동물|Night mode는 움직이는 아이/동물에 부적합.]]
- `AVOIDS` → [[scene_nodes/scene__디지털 줌보다 가까이 가거나 2x optical_quality zoom__risk_pets_children_action_디지털_줌보다_가까이_가거나_2x_opt|디지털 줌보다 가까이 가거나 2x optical/quality zoom.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_pet-photography-tips__evidence_url_https_blog_google_products_pixel_pe|https://blog.google/products/pixel/pet-photography-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-burst-mode-shots-i__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-burst-mode-shots-ipha42c55cd0/26/ios/26]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_how-to-nail-pet__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/how-to-nail-pet-photography-in-minutes/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_how-to-pull-off__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/how-to-pull-off-the-perfect-fall-photoshoot/]]

## Incoming
- [[scene_nodes/scene__아이·반려동물 액션 — 순간 포착_연사_짧은 영상__scenario_pets_children_action|아이·반려동물 액션 — 순간 포착/연사/짧은 영상]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__kids or pets__subject_kids_or_pets|kids or pets]] → `TRIGGERS`
- [[scene_nodes/scene__burst live video__mode_burst_live_video|burst live video]] → `TRIGGERS`
- [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]] → `TRIGGERS`
- [[scene_nodes/scene__bright natural__light_bright_natural|bright natural]] → `TRIGGERS`
