# 도시 야경 장노출 — 빛줄기/스카이라인

- id: `scenario_city_night_long_exposure`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/city_night_long_exposure.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_city_night_long_exposure
- **name**: 도시 야경 장노출 — 빛줄기/스카이라인
- **source_file**: raw/scenarios/city_night_long_exposure.md
- **tags**: ['city-night', 'long-exposure', 'traffic-trails', 'skyline', 'tripod']

## Source-oriented graph 연결
- [[source_nodes/source__Pro Or Night__mode_pro_or_night|Pro Or Night]]
- [[source_nodes/source__City Lights__subject_city_lights|City Lights]]
- [[source_nodes/source__Low Iso__tok_low_iso|Low Iso]]
- [[source_nodes/source__Noise__tok_noise|Noise]]
- [[source_nodes/source__Noise Reduction__tok_noise_reduction|Noise Reduction]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__도시 야경 장노출 — 빛줄기_스카이라인__evidence_raw_scenarios_city_night_long_exposure|도시 야경 장노출 — 빛줄기/스카이라인]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `HAS_SUBJECT` → [[scene_nodes/scene__city lights__subject_city_lights|city lights]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__night city__environment_night_city|night city]]
- `USES_MODE` → [[scene_nodes/scene__pro or night__mode_pro_or_night|pro or night]]
- `USES_LENS` → [[scene_nodes/scene__1x 2x 5x__lens_1x_2x_5x|1x 2x 5x]]
- `HAS_FACET` → [[scene_nodes/scene__low iso long shutter__parameter_low_iso_long_shutter|low iso long shutter]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__moody cinematic__editstyle_moody_cinematic|moody cinematic]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__tripod ENABLES_long_exposure__tech_city_night_long_exposure_tripod_enables_lon|tripod ENABLES_long_exposure]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__low_iso REDUCES_noise__tech_city_night_long_exposure_low_iso_reduces_no|low_iso REDUCES_noise]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__traffic CREATES_light_trails__tech_city_night_long_exposure_traffic_creates_li|traffic CREATES_light_trails]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__highlights NEED_protection__tech_city_night_long_exposure_highlights_need_pr|highlights NEED_protection]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_trend_city_night_long_exposure|Trend recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_general_city_night_long_exposure|General recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_personalized_city_night_long_exposure|Personalized recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.google.com_pixelcamera_answer_9708795_hl=en__evidence_url_https_support_google_com_pixelcamer|https://support.google.com/pixelcamera/answer/9708795?hl=en]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
