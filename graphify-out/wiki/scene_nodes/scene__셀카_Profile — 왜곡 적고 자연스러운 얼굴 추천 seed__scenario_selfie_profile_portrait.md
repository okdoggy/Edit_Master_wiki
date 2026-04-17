# 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed

- id: `scenario_selfie_profile_portrait`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/selfie_profile_portrait.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_selfie_profile_portrait
- **name**: 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed
- **source_file**: raw/scenarios/selfie_profile_portrait.md
- **tags**: ['selfie', 'profile', 'portrait', 'front-camera', 'skin-tone']

## Source-oriented graph 연결
- [[source_nodes/source__Front Camera__camera_front_camera|Front Camera]]
- [[source_nodes/source__Natural Skin__edit_style_natural_skin|Natural Skin]]
- [[source_nodes/source__Selfie Or Portrait Selfie__mode_selfie_or_portrait_selfie|Selfie Or Portrait Selfie]]
- [[source_nodes/source__Selfie Person__subject_selfie_person|Selfie Person]]
- [[source_nodes/source__Pose__tok_pose|Pose]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__evidence_raw_scenarios_selfie_profile_portrait_m|셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `HAS_SUBJECT` → [[scene_nodes/scene__selfie person__subject_selfie_person|selfie person]]
- `HAS_FACET` → [[scene_nodes/scene__front camera__camera_front_camera|front camera]]
- `USES_MODE` → [[scene_nodes/scene__selfie or portrait selfie__mode_selfie_or_portrait_selfie|selfie or portrait selfie]]
- `HAS_LIGHT` → [[scene_nodes/scene__window or open shade__light_window_or_open_shade|window or open shade]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__natural skin__editstyle_natural_skin|natural skin]]
- `HAS_RISK` → [[scene_nodes/scene__wide angle face distortion__risk_wide_angle_face_distortion|wide angle face distortion]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__close_front_camera CAUSES face_distortion__tech_selfie_profile_portrait_close_front_camera|close_front_camera CAUSES face_distortion]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__timer IMPROVES_pose__tech_selfie_profile_portrait_timer_improves_pose|timer IMPROVES_pose]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__window_light SOFTENS_skin__tech_selfie_profile_portrait_window_light_soften|window_light SOFTENS_skin]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__rec_trend_selfie_profile_portrait|Trend recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__rec_general_selfie_profile_portrait|General recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천__rec_personalized_selfie_profile_portrait|Personalized recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-a-selfie-iph1b8842__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_express_learn_blog_how-to-take-portrait-__evidence_url_https_www_adobe_com_express_learn_b|https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_still-life_how-__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/]]

## Incoming
