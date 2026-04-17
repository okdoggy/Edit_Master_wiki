# Trend recommendation — 불꽃놀이와 스카이라인 — 하이라이트 보호/연속 확보

- id: `rec_trend_fireworks_skyline`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/fireworks_skyline.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_fireworks_skyline
- **name**: Trend recommendation — 불꽃놀이와 스카이라인 — 하이라이트 보호/연속 확보
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/fireworks_skyline.md

## Source-oriented graph 연결
- [[source_nodes/source__Night Or Pro__mode_night_or_pro|Night Or Pro]]
- [[source_nodes/source__Fireworks__subject_fireworks|Fireworks]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__불꽃놀이와 스카이라인 — 하이라이트 보호_연속 확보__evidence_raw_scenarios_fireworks_skyline_md|불꽃놀이와 스카이라인 — 하이라이트 보호/연속 확보]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__night skyline__environment_night_skyline|night skyline]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__0.5x_1x로 하늘과 스카이라인을 함께 담는다__tech_fireworks_skyline_0_5x_1x로_하늘과_스카이라인을_함께_담는|0.5x/1x로 하늘과 스카이라인을 함께 담는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__삼각대 고정, 타이머 사용__tech_fireworks_skyline_삼각대_고정_타이머_사용|삼각대 고정, 타이머 사용.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__Pro 가능 시 ISO 50~100, 셔터 1_2~2s부터 테스트__param_fireworks_skyline_pro_가능_시_iso_50_100_셔터_1|Pro 가능 시 ISO 50~100, 셔터 1/2~2s부터 테스트.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__어렵다면 4K video로 찍고 피크 프레임 캡처__tech_fireworks_skyline_어렵다면_4k_video로_찍고_피크_프레임|어렵다면 4K video로 찍고 피크 프레임 캡처.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -50~-100, Whites -10~-40__param_fireworks_skyline_highlights_50_100_whites|Highlights -50~-100, Whites -10~-40.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Blacks -10~-25로 하늘 정리__param_fireworks_skyline_blacks_10_25로_하늘_정리|Blacks -10~-25로 하늘 정리.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Saturation +5~+15, 색별 과포화 주의__param_fireworks_skyline_saturation_5_15_색별_과포화_주|Saturation +5~+15, 색별 과포화 주의.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Noise Reduction +10~+30__param_fireworks_skyline_noise_reduction_10_30|Noise Reduction +10~+30.]]
- `AVOIDS` → [[scene_nodes/scene__Night mode auto가 너무 길면 불꽃이 뭉개진다__risk_fireworks_skyline_night_mode_auto가_너무_길면_불꽃|Night mode auto가 너무 길면 불꽃이 뭉개진다.]]
- `AVOIDS` → [[scene_nodes/scene__연기가 많아지기 전 초반 컷이 깨끗하다__risk_fireworks_skyline_연기가_많아지기_전_초반_컷이_깨끗하다|연기가 많아지기 전 초반 컷이 깨끗하다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
- [[scene_nodes/scene__불꽃놀이와 스카이라인 — 하이라이트 보호_연속 확보__scenario_fireworks_skyline|불꽃놀이와 스카이라인 — 하이라이트 보호/연속 확보]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__night skyline__environment_night_skyline|night skyline]] → `TRIGGERS`
