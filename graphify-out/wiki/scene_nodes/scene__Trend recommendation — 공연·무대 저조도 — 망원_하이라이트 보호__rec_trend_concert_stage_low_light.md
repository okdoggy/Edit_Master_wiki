# Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호

- id: `rec_trend_concert_stage_low_light`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/concert_stage_low_light.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_concert_stage_low_light
- **name**: Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/concert_stage_low_light.md

## Source-oriented graph 연결
- [[source_nodes/source__Moody Stage__edit_style_moody_stage|Moody Stage]]
- [[source_nodes/source__3x 5x 10x__lens_3x_5x_10x|3x 5x 10x]]
- [[source_nodes/source__Spotlight__light_spotlight|Spotlight]]
- [[source_nodes/source__Photo Or Pro__mode_photo_or_pro|Photo Or Pro]]
- [[source_nodes/source__Performer__subject_performer|Performer]]
- [[source_nodes/source__Clipping__tok_clipping|Clipping]]
- [[source_nodes/source__Fast Shutter__tok_fast_shutter|Fast Shutter]]
- [[source_nodes/source__Motion__tok_motion|Motion]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__공연·무대 저조도 — 망원_하이라이트 보호__evidence_raw_scenarios_concert_stage_low_light_m|공연·무대 저조도 — 망원/하이라이트 보호]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__stage__environment_stage|stage]]
- `USES_FACET` → [[scene_nodes/scene__spotlight__light_spotlight|spotlight]]
- `USES_FACET` → [[scene_nodes/scene__moody stage__editstyle_moody_stage|moody stage]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__3x_5x optical 우선, 너무 멀면 10x 기록용__tech_concert_stage_low_light_3x_5x_optical_우선_너무|3x/5x optical 우선, 너무 멀면 10x 기록용.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__스포트라이트가 밝으면 EV -0.7~-1.3__param_concert_stage_low_light_스포트라이트가_밝으면_ev_0_7|스포트라이트가 밝으면 EV -0.7~-1.3.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__움직임이 빠르면 Night mode보다 일반 Photo_Burst_Video__tech_concert_stage_low_light_움직임이_빠르면_night_mode|움직임이 빠르면 Night mode보다 일반 Photo/Burst/Video.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__난간_몸에 팔꿈치 고정__tech_concert_stage_low_light_난간_몸에_팔꿈치_고정|난간/몸에 팔꿈치 고정.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -40~-80, Whites -10~-30__param_concert_stage_low_light_highlights_40_80_w|Highlights -40~-80, Whites -10~-30.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Shadows +5~+20 또는 moody면 Blacks -10~-25__param_concert_stage_low_light_shadows_5_20_또는_mo|Shadows +5~+20 또는 moody면 Blacks -10~-25.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Noise Reduction +15~+35, Sharpen +10~+25__param_concert_stage_low_light_noise_reduction_15|Noise Reduction +15~+35, Sharpen +10~+25.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__색 조명은 완전 중립으로 만들지 말고 분위기 유지__param_concert_stage_low_light_색_조명은_완전_중립으로_만들지|색 조명은 완전 중립으로 만들지 말고 분위기 유지.]]
- `AVOIDS` → [[scene_nodes/scene__Night mode 장노출은 공연자를 흐리게 만든다__risk_concert_stage_low_light_night_mode_장노출은_공연자|Night mode 장노출은 공연자를 흐리게 만든다.]]
- `AVOIDS` → [[scene_nodes/scene__디지털 줌으로 과하게 당기면 디테일이 뭉개진다__risk_concert_stage_low_light_디지털_줌으로_과하게_당기면_디테일|디지털 줌으로 과하게 당기면 디테일이 뭉개진다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.google.com_pixelcamera_answer_9708795_hl=en__evidence_url_https_support_google_com_pixelcamer|https://support.google.com/pixelcamera/answer/9708795?hl=en]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
- [[scene_nodes/scene__공연·무대 저조도 — 망원_하이라이트 보호__scenario_concert_stage_low_light|공연·무대 저조도 — 망원/하이라이트 보호]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__stage__environment_stage|stage]] → `TRIGGERS`
- [[scene_nodes/scene__spotlight__light_spotlight|spotlight]] → `TRIGGERS`
- [[scene_nodes/scene__moody stage__editstyle_moody_stage|moody stage]] → `TRIGGERS`
