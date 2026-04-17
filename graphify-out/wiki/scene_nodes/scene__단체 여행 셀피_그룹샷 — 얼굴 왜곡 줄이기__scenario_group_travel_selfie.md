# 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기

- id: `scenario_group_travel_selfie`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/group_travel_selfie.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_group_travel_selfie
- **name**: 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기
- **source_file**: raw/scenarios/group_travel_selfie.md
- **tags**: ['group', 'selfie', 'travel', 'wide', 'portrait']

## Source-oriented graph 연결
- [[source_nodes/source__0.5x 1x Front__lens_0_5x_1x_front|0.5x 1x Front]]
- [[source_nodes/source__Selfie Or Timer__mode_selfie_or_timer|Selfie Or Timer]]
- [[source_nodes/source__Group__subject_group|Group]]
- [[source_nodes/source__Edge Distortion__tok_edge_distortion|Edge Distortion]]
- [[source_nodes/source__Face__tok_face|Face]]
- [[source_nodes/source__Faces__tok_faces|Faces]]
- [[source_nodes/source__Group__tok_group|Group]]
- [[source_nodes/source__Landmark Context__tok_landmark_context|Landmark Context]]
- [[source_nodes/source__Stability__tok_stability|Stability]]
- [[source_nodes/source__Story__tok_story|Story]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__evidence_raw_scenarios_group_travel_selfie_md|단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `HAS_SUBJECT` → [[scene_nodes/scene__group__subject_group|group]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__travel landmark__environment_travel_landmark|travel landmark]]
- `USES_LENS` → [[scene_nodes/scene__0.5x 1x front__lens_0_5x_1x_front|0.5x 1x front]]
- `USES_MODE` → [[scene_nodes/scene__selfie or timer__mode_selfie_or_timer|selfie or timer]]
- `HAS_FACET` → [[scene_nodes/scene__face center__composition_face_center|face center]]
- `HAS_RISK` → [[scene_nodes/scene__edge distortion__risk_edge_distortion|edge distortion]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__ultrawide FITS_group__tech_group_travel_selfie_ultrawide_fits_group|ultrawide FITS_group]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__edge_distortion HARMS_faces__tech_group_travel_selfie_edge_distortion_harms_f|edge_distortion HARMS_faces]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__timer IMPROVES_stability__tech_group_travel_selfie_timer_improves_stabilit|timer IMPROVES_stability]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__landmark_context ADDS_story__tech_group_travel_selfie_landmark_context_adds_s|landmark_context ADDS_story]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_trend_group_travel_selfie|Trend recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_general_group_travel_selfie|General recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_personalized_group_travel_selfie|Personalized recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_pixel-group-photo-features-__evidence_url_https_blog_google_products_pixel_pi|https://blog.google/products/pixel/pixel-group-photo-features-ai/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-a-selfie-iph1b8842__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_support_answer_ANS10004858__evidence_url_https_www_samsung_com_us_support_an|https://www.samsung.com/us/support/answer/ANS10004858/]]

## Incoming
