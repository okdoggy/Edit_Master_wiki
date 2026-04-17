# 공연·무대 저조도 — 망원/하이라이트 보호

- id: `scenario_concert_stage_low_light`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/concert_stage_low_light.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_concert_stage_low_light
- **name**: 공연·무대 저조도 — 망원/하이라이트 보호
- **source_file**: raw/scenarios/concert_stage_low_light.md
- **tags**: ['concert', 'stage', 'low-light', 'telephoto', 'performance']

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
- `HAS_SUBJECT` → [[scene_nodes/scene__performer__subject_performer|performer]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__stage__environment_stage|stage]]
- `HAS_LIGHT` → [[scene_nodes/scene__spotlight__light_spotlight|spotlight]]
- `USES_LENS` → [[scene_nodes/scene__3x 5x 10x__lens_3x_5x_10x|3x 5x 10x]]
- `USES_MODE` → [[scene_nodes/scene__photo or pro__mode_photo_or_pro|photo or pro]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__moody stage__editstyle_moody_stage|moody stage]]
- `HAS_RISK` → [[scene_nodes/scene__highlight clipping__risk_highlight_clipping|highlight clipping]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__spotlight CAUSES_clipping__tech_concert_stage_low_light_spotlight_causes_cl|spotlight CAUSES_clipping]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__telephoto REACHES_stage__tech_concert_stage_low_light_telephoto_reaches_s|telephoto REACHES_stage]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__fast_shutter FREEZES_motion__tech_concert_stage_low_light_fast_shutter_freeze|fast_shutter FREEZES_motion]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__noise_reduction BALANCES_detail__tech_concert_stage_low_light_noise_reduction_bal|noise_reduction BALANCES_detail]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_trend_concert_stage_low_light|Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_general_concert_stage_low_light|General recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 공연·무대 저조도 — 망원_하이라이트 보호__rec_personalized_concert_stage_low_light|Personalized recommendation — 공연·무대 저조도 — 망원/하이라이트 보호]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.google.com_pixelcamera_answer_9708795_hl=en__evidence_url_https_support_google_com_pixelcamer|https://support.google.com/pixelcamera/answer/9708795?hl=en]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_ae_mobile-phone-buying-guide_samsung-n__evidence_url_https_www_samsung_com_ae_mobile_pho|https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/]]

## Incoming
