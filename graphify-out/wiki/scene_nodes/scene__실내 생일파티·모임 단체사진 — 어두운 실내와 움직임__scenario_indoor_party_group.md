# 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임

- id: `scenario_indoor_party_group`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/indoor_party_group.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_indoor_party_group
- **name**: 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임
- **source_file**: raw/scenarios/indoor_party_group.md
- **tags**: ['indoor', 'party', 'group', 'birthday', 'low-light', 'motion']

## Source-oriented graph 연결
- [[source_nodes/source__motion blur__issue_motion_blur|motion blur]]
- [[source_nodes/source__warm documentary party mood__trend_warm_documentary_party|warm documentary party mood]]
- [[source_nodes/source__documentary__pref_documentary|documentary]]
- [[source_nodes/source__clean group shot__pref_clean_group|clean group shot]]
- [[source_nodes/source__party mood__outcome_party_mood|party mood]]
- [[source_nodes/source__timer _ burst__tech_timer_or_burst|timer / burst]]
- [[source_nodes/source__keep faces on the same plane__tech_same_plane_faces|keep faces on the same plane]]
- [[source_nodes/source__Noise Reduction +15 to +35__param_noise_reduction_plus_15_to_35|Noise Reduction +15 to +35]]
- [[source_nodes/source__Warm temperature, controlled__param_temp_warm_controlled|Warm temperature, controlled]]
- [[source_nodes/source__Google Pixel group photo features__evidence_google_pixel_group_photo_features|Google Pixel group photo features]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__evidence_raw_scenarios_indoor_party_group_md|실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `HAS_SUBJECT` → [[scene_nodes/scene__group__subject_group|group]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__indoor party__environment_indoor_party|indoor party]]
- `HAS_LIGHT` → [[scene_nodes/scene__warm low light__light_warm_low_light|warm low light]]
- `USES_LENS` → [[scene_nodes/scene__1x or 0 5x__lens_1x_or_0_5x|1x or 0 5x]]
- `USES_MODE` → [[scene_nodes/scene__photo or night short__mode_photo_or_night_short|photo or night short]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__warm documentary__editstyle_warm_documentary|warm documentary]]
- `HAS_RISK` → [[scene_nodes/scene__motion blur__risk_motion_blur|motion blur]]
- `HAS_RISK` → [[scene_nodes/scene__mixed white balance__risk_mixed_white_balance|mixed white balance]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__group_faces_need_same_plane__tech_indoor_party_group_group_faces_need_same_pl|group_faces_need_same_plane]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__short_night_mode_reduces_blur__tech_indoor_party_group_short_night_mode_reduces|short_night_mode_reduces_blur]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__warm_light_supports_party_mood__tech_indoor_party_group_warm_light_supports_part|warm_light_supports_party_mood]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__timer_improves_group_pose__tech_indoor_party_group_timer_improves_group_pos|timer_improves_group_pose]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_trend_indoor_party_group|Trend recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_general_indoor_party_group|General recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_personalized_indoor_party_group|Personalized recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-holiday-photos-night-sight-portrait-mode/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_pixel-group-photo-features-__evidence_url_https_blog_google_products_pixel_pi|https://blog.google/products/pixel/pixel-group-photo-features-ai/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
- [[scene_nodes/scene__실내 생일파티 사진__alias_실내_생일파티_사진|실내 생일파티 사진]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__케이크 촛불 단체__alias_케이크_촛불_단체|케이크 촛불 단체]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__어두운 방 단체사진__alias_어두운_방_단체사진|어두운 방 단체사진]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__모임 사진 흐림__alias_모임_사진_흐림|모임 사진 흐림]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__파티 사진 보정__alias_파티_사진_보정|파티 사진 보정]] → `MATCHES_SCENARIO`
