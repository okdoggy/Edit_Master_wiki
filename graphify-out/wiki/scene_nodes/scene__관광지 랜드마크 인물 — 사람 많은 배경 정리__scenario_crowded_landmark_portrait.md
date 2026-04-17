# 관광지 랜드마크 인물 — 사람 많은 배경 정리

- id: `scenario_crowded_landmark_portrait`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/crowded_landmark_portrait.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_crowded_landmark_portrait
- **name**: 관광지 랜드마크 인물 — 사람 많은 배경 정리
- **source_file**: raw/scenarios/crowded_landmark_portrait.md
- **tags**: ['travel', 'landmark', 'crowd', 'portrait', 'tourist']

## Source-oriented graph 연결
- [[source_nodes/source__busy background__issue_busy_background|busy background]]
- [[source_nodes/source__scale lost__issue_scale_lost|scale lost]]
- [[source_nodes/source__travel carousel with place + person__trend_travel_carousel|travel carousel with place + person]]
- [[source_nodes/source__place-centric__pref_place_centric|place-centric]]
- [[source_nodes/source__person-centric__pref_person_centric|person-centric]]
- [[source_nodes/source__background separation__outcome_background_separation|background separation]]
- [[source_nodes/source__scale + story__outcome_scale_story|scale + story]]
- [[source_nodes/source__remove _ heal__tech_remove_heal|remove / heal]]
- [[source_nodes/source__Background Saturation -5 to -20__param_background_saturation_minus_5_to_20|Background Saturation -5 to -20]]
- [[source_nodes/source__Adobe smartphone photography__evidence_adobe_smartphone_photography|Adobe smartphone photography]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__관광지 랜드마크 인물 — 사람 많은 배경 정리__evidence_raw_scenarios_crowded_landmark_portrait|관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `HAS_SUBJECT` → [[scene_nodes/scene__person__subject_person|person]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__crowded landmark__environment_crowded_landmark|crowded landmark]]
- `HAS_LIGHT` → [[scene_nodes/scene__daylight or golden hour__light_daylight_or_golden_hour|daylight or golden hour]]
- `USES_LENS` → [[scene_nodes/scene__2x 3x or 1x__lens_2x_3x_or_1x|2x 3x or 1x]]
- `USES_MODE` → [[scene_nodes/scene__photo or portrait__mode_photo_or_portrait|photo or portrait]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__warm travel__editstyle_warm_travel|warm travel]]
- `HAS_RISK` → [[scene_nodes/scene__busy background__risk_busy_background|busy background]]
- `HAS_RISK` → [[scene_nodes/scene__scale lost__risk_scale_lost|scale lost]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_3x_compresses_background__tech_crowded_landmark_portrait_2x_3x_compresses|2x_3x_compresses_background]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__early_late_time_reduces_crowd__tech_crowded_landmark_portrait_early_late_time_r|early_late_time_reduces_crowd]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__remove_tool_cleans_distractions__tech_crowded_landmark_portrait_remove_tool_clean|remove_tool_cleans_distractions]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__scale_subject_shows_landmark_size__tech_crowded_landmark_portrait_scale_subject_sho|scale_subject_shows_landmark_size]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_trend_crowded_landmark_portrait|Trend recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_general_crowded_landmark_portrait|General recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리__rec_personalized_crowded_landmark_portrait|Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]

## Incoming
- [[scene_nodes/scene__관광지 사람 많음__alias_관광지_사람_많음|관광지 사람 많음]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__랜드마크 앞 인물__alias_랜드마크_앞_인물|랜드마크 앞 인물]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__배경 관광객 지저분__alias_배경_관광객_지저분|배경 관광객 지저분]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__여행 인물 배경 정리__alias_여행_인물_배경_정리|여행 인물 배경 정리]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__명소 사진__alias_명소_사진|명소 사진]] → `MATCHES_SCENARIO`
