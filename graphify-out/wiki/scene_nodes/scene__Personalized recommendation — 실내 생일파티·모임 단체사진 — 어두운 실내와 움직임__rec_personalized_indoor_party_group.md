# Personalized recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임

- id: `rec_personalized_indoor_party_group`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/indoor_party_group.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_indoor_party_group
- **name**: Personalized recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/indoor_party_group.md

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
- `USES_FACET` → [[scene_nodes/scene__group__subject_group|group]]
- `USES_FACET` → [[scene_nodes/scene__indoor party__environment_indoor_party|indoor party]]
- `USES_FACET` → [[scene_nodes/scene__warm documentary__editstyle_warm_documentary|warm documentary]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__가능하면 조명을 하나 더 켜거나 창_벽 반사광을 활용한다__tech_indoor_party_group_가능하면_조명을_하나_더_켜거나_창_벽_반사|가능하면 조명을 하나 더 켜거나 창/벽 반사광을 활용한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__인원이 많으면 모두 카메라와 비슷한 거리에 서게 한다__tech_indoor_party_group_인원이_많으면_모두_카메라와_비슷한_거리에|인원이 많으면 모두 카메라와 비슷한 거리에 서게 한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__움직임이 있으면 긴 Night mode보다 일반 Photo_Burst__tech_indoor_party_group_움직임이_있으면_긴_night_mode보다|움직임이 있으면 긴 Night mode보다 일반 Photo/Burst.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__타이머 3초 또는 볼륨 버튼 셔터로 흔들림을 줄인다__tech_indoor_party_group_타이머_3초_또는_볼륨_버튼_셔터로_흔들림을|타이머 3초 또는 볼륨 버튼 셔터로 흔들림을 줄인다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.2~+0.5, Highlights -20~-40, Shadows +15~+35__param_indoor_party_group_exposure_0_2_0_5_highli|Exposure +0.2~+0.5, Highlights -20~-40, Shadows +15~+35.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Temp는 분위기를 남기되 얼굴이 너무 노랗지 않게__param_indoor_party_group_temp는_분위기를_남기되_얼굴이_너무_노|Temp는 분위기를 남기되 얼굴이 너무 노랗지 않게.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Noise Reduction +15~+35, Texture는 인물에 과하게 올리지 않는다__param_indoor_party_group_noise_reduction_15_35_t|Noise Reduction +15~+35, Texture는 인물에 과하게 올리지 않는다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__얼굴별 마스크가 가능하면 가장 어두운 얼굴만 살짝 밝힌다__param_indoor_party_group_얼굴별_마스크가_가능하면_가장_어두운_얼굴|얼굴별 마스크가 가능하면 가장 어두운 얼굴만 살짝 밝힌다.]]
- `AVOIDS` → [[scene_nodes/scene__긴 노출은 웃는 표정과 손동작을 흐리게 만든다__risk_indoor_party_group_긴_노출은_웃는_표정과_손동작을_흐리게_만든|긴 노출은 웃는 표정과 손동작을 흐리게 만든다.]]
- `AVOIDS` → [[scene_nodes/scene__단체에 Portrait blur를 과하게 쓰면 일부 얼굴이 흐려질 수 있다__risk_indoor_party_group_단체에_portrait_blur를_과하게_쓰|단체에 Portrait blur를 과하게 쓰면 일부 얼굴이 흐려질 수 있다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-holiday-photos-night-sight-portrait-mode/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_pixel-group-photo-features-__evidence_url_https_blog_google_products_pixel_pi|https://blog.google/products/pixel/pixel-group-photo-features-ai/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
- [[scene_nodes/scene__실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__scenario_indoor_party_group|실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__group__subject_group|group]] → `TRIGGERS`
- [[scene_nodes/scene__indoor party__environment_indoor_party|indoor party]] → `TRIGGERS`
- [[scene_nodes/scene__warm documentary__editstyle_warm_documentary|warm documentary]] → `TRIGGERS`
