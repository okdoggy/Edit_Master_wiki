# Personalized recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기

- id: `rec_personalized_group_travel_selfie`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/group_travel_selfie.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_group_travel_selfie
- **name**: Personalized recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/group_travel_selfie.md

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
- `USES_FACET` → [[scene_nodes/scene__group__subject_group|group]]
- `USES_FACET` → [[scene_nodes/scene__travel landmark__environment_travel_landmark|travel landmark]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__0.5x는 단체가 많거나 장소를 넣을 때, 얼굴은 중앙 70% 안에__tech_group_travel_selfie_0_5x는_단체가_많거나_장소를_넣을_때|0.5x는 단체가 많거나 장소를 넣을 때, 얼굴은 중앙 70% 안에.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__삼각대_난간 + 타이머 3초로 후면 카메라 사용하면 품질 상승__param_group_travel_selfie_삼각대_난간_타이머_3초로_후면_카메라|삼각대/난간 + 타이머 3초로 후면 카메라 사용하면 품질 상승.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__랜드마크는 사람 머리 뒤로 튀어나오지 않게 옆으로 배치__tech_group_travel_selfie_랜드마크는_사람_머리_뒤로_튀어나오지_않게|랜드마크는 사람 머리 뒤로 튀어나오지 않게 옆으로 배치.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__빛은 얼굴 쪽에서 부드럽게 들어오게__tech_group_travel_selfie_빛은_얼굴_쪽에서_부드럽게_들어오게|빛은 얼굴 쪽에서 부드럽게 들어오게.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Faces_Subject mask Exposure +0.1~+0.3__param_group_travel_selfie_faces_subject_mask_exp|Faces/Subject mask Exposure +0.1~+0.3.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__하늘_배경 Highlights -20~-50__param_group_travel_selfie_하늘_배경_highlights_20_50|하늘/배경 Highlights -20~-50.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__전체 색온도와 피부색을 우선 맞춘 뒤 프리셋 적용__param_group_travel_selfie_전체_색온도와_피부색을_우선_맞춘_뒤_프|전체 색온도와 피부색을 우선 맞춘 뒤 프리셋 적용.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__4_5 피드와 9_16 스토리 크롭 둘 다 저장__param_group_travel_selfie_4_5_피드와_9_16_스토리_크롭_둘|4:5 피드와 9:16 스토리 크롭 둘 다 저장.]]
- `AVOIDS` → [[scene_nodes/scene__초광각 가장자리 얼굴은 늘어진다__risk_group_travel_selfie_초광각_가장자리_얼굴은_늘어진다|초광각 가장자리 얼굴은 늘어진다.]]
- `AVOIDS` → [[scene_nodes/scene__역광 단체샷은 얼굴이 모두 어두워질 수 있어 HDR_보정 전제__risk_group_travel_selfie_역광_단체샷은_얼굴이_모두_어두워질_수_있|역광 단체샷은 얼굴이 모두 어두워질 수 있어 HDR/보정 전제.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_pixel-group-photo-features-__evidence_url_https_blog_google_products_pixel_pi|https://blog.google/products/pixel/pixel-group-photo-features-ai/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-a-selfie-iph1b8842__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_support_answer_ANS10004858__evidence_url_https_www_samsung_com_us_support_an|https://www.samsung.com/us/support/answer/ANS10004858/]]

## Incoming
- [[scene_nodes/scene__단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__scenario_group_travel_selfie|단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__group__subject_group|group]] → `TRIGGERS`
- [[scene_nodes/scene__travel landmark__environment_travel_landmark|travel landmark]] → `TRIGGERS`
