# Trend recommendation — 도시 야경 장노출 — 빛줄기/스카이라인

- id: `rec_trend_city_night_long_exposure`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/city_night_long_exposure.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_city_night_long_exposure
- **name**: Trend recommendation — 도시 야경 장노출 — 빛줄기/스카이라인
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/city_night_long_exposure.md

## Source-oriented graph 연결
- [[source_nodes/source__Pro Or Night__mode_pro_or_night|Pro Or Night]]
- [[source_nodes/source__City Lights__subject_city_lights|City Lights]]
- [[source_nodes/source__Low Iso__tok_low_iso|Low Iso]]
- [[source_nodes/source__Noise__tok_noise|Noise]]
- [[source_nodes/source__Noise Reduction__tok_noise_reduction|Noise Reduction]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__도시 야경 장노출 — 빛줄기_스카이라인__evidence_raw_scenarios_city_night_long_exposure|도시 야경 장노출 — 빛줄기/스카이라인]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__night city__environment_night_city|night city]]
- `USES_FACET` → [[scene_nodes/scene__moody cinematic__editstyle_moody_cinematic|moody cinematic]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__삼각대_난간 고정__tech_city_night_long_exposure_삼각대_난간_고정|삼각대/난간 고정.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__Galaxy Pro 시작점_ ISO 50~200, 2~8s, WB 4300K 전후__param_city_night_long_exposure_galaxy_pro_시작점_is|Galaxy Pro 시작점: ISO 50~200, 2~8s, WB 4300K 전후.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__iPhone_Pixel Night mode는 정적인 스카이라인에 사용__tech_city_night_long_exposure_iphone_pixel_night|iPhone/Pixel Night mode는 정적인 스카이라인에 사용.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__차량 빛줄기는 도로가 프레임을 통과하게 구성__tech_city_night_long_exposure_차량_빛줄기는_도로가_프레임을_통|차량 빛줄기는 도로가 프레임을 통과하게 구성.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -40~-80, Blacks -10~-30__param_city_night_long_exposure_highlights_40_80|Highlights -40~-80, Blacks -10~-30.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Dehaze +5~+20, Noise Reduction +15~+35__param_city_night_long_exposure_dehaze_5_20_noise|Dehaze +5~+20, Noise Reduction +15~+35.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Color Grading_ shadows cool, highlights warm__param_city_night_long_exposure_color_grading_sha|Color Grading: shadows cool, highlights warm.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Geometry로 수평_수직 정리__param_city_night_long_exposure_geometry로_수평_수직_정|Geometry로 수평/수직 정리.]]
- `AVOIDS` → [[scene_nodes/scene__사람_나무가 움직이면 번짐__risk_city_night_long_exposure_사람_나무가_움직이면_번짐|사람/나무가 움직이면 번짐.]]
- `AVOIDS` → [[scene_nodes/scene__장노출은 작은 흔들림도 치명적__risk_city_night_long_exposure_장노출은_작은_흔들림도_치명적|장노출은 작은 흔들림도 치명적.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.google.com_pixelcamera_answer_9708795_hl=en__evidence_url_https_support_google_com_pixelcamer|https://support.google.com/pixelcamera/answer/9708795?hl=en]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
- [[scene_nodes/scene__도시 야경 장노출 — 빛줄기_스카이라인__scenario_city_night_long_exposure|도시 야경 장노출 — 빛줄기/스카이라인]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__night city__environment_night_city|night city]] → `TRIGGERS`
- [[scene_nodes/scene__moody cinematic__editstyle_moody_cinematic|moody cinematic]] → `TRIGGERS`
