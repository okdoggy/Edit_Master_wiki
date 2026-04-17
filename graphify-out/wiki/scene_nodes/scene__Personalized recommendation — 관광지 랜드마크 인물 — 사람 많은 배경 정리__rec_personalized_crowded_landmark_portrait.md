# Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리

- id: `rec_personalized_crowded_landmark_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/crowded_landmark_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_crowded_landmark_portrait
- **name**: Personalized recommendation — 관광지 랜드마크 인물 — 사람 많은 배경 정리
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/crowded_landmark_portrait.md

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
- `USES_FACET` → [[scene_nodes/scene__person__subject_person|person]]
- `USES_FACET` → [[scene_nodes/scene__crowded landmark__environment_crowded_landmark|crowded landmark]]
- `USES_FACET` → [[scene_nodes/scene__warm travel__editstyle_warm_travel|warm travel]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__사람이 적은 아침_해질녘 시간대를 노린다__tech_crowded_landmark_portrait_사람이_적은_아침_해질녘_시간대|사람이 적은 아침/해질녘 시간대를 노린다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__랜드마크 전체 컷 1장, 2x_3x 인물 컷 1장, 디테일 컷 1장을 세트로 찍는다__tech_crowded_landmark_portrait_랜드마크_전체_컷_1장_2x_3|랜드마크 전체 컷 1장, 2x/3x 인물 컷 1장, 디테일 컷 1장을 세트로 찍는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__배경 관광객이 인물 머리와 겹치지 않게 옆으로 이동한다__tech_crowded_landmark_portrait_배경_관광객이_인물_머리와_겹치|배경 관광객이 인물 머리와 겹치지 않게 옆으로 이동한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__밝은 하늘은 EV -0.3~-0.7__param_crowded_landmark_portrait_밝은_하늘은_ev_0_3_0|밝은 하늘은 EV -0.3~-0.7.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject mask로 인물 Exposure +0.1~+0.3__param_crowded_landmark_portrait_subject_mask로_인물|Subject mask로 인물 Exposure +0.1~+0.3.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-20, Clarity -5~-15__param_crowded_landmark_portrait_background_satur|Background Saturation -5~-20, Clarity -5~-15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Remove_Heal로 작은 방해물 제거__param_crowded_landmark_portrait_remove_heal로_작은|Remove/Heal로 작은 방해물 제거.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Geometry로 건축 수직 보정__param_crowded_landmark_portrait_geometry로_건축_수직|Geometry로 건축 수직 보정.]]
- `AVOIDS` → [[scene_nodes/scene__Remove로 큰 사람 무리를 지우려 하면 티가 난다__risk_crowded_landmark_portrait_remove로_큰_사람_무리를|Remove로 큰 사람 무리를 지우려 하면 티가 난다.]]
- `AVOIDS` → [[scene_nodes/scene__초광각으로 가까이 찍으면 얼굴_몸 왜곡이 커진다__risk_crowded_landmark_portrait_초광각으로_가까이_찍으면_얼굴|초광각으로 가까이 찍으면 얼굴/몸 왜곡이 커진다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]

## Incoming
- [[scene_nodes/scene__관광지 랜드마크 인물 — 사람 많은 배경 정리__scenario_crowded_landmark_portrait|관광지 랜드마크 인물 — 사람 많은 배경 정리]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__person__subject_person|person]] → `TRIGGERS`
- [[scene_nodes/scene__crowded landmark__environment_crowded_landmark|crowded landmark]] → `TRIGGERS`
- [[scene_nodes/scene__warm travel__editstyle_warm_travel|warm travel]] → `TRIGGERS`
