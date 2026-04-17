# General recommendation — 건축·실내 공간 — 초광각 왜곡 제어

- id: `rec_general_architecture_interior_wide`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/architecture_interior_wide.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_architecture_interior_wide
- **name**: General recommendation — 건축·실내 공간 — 초광각 왜곡 제어
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/architecture_interior_wide.md

## Source-oriented graph 연결
- [[source_nodes/source__0.5x 1x__lens_0_5x_1x|0.5x 1x]]
- [[source_nodes/source__Geometry Edit__tok_geometry_edit|Geometry Edit]]
- [[source_nodes/source__Lines__tok_lines|Lines]]
- [[source_nodes/source__Space__tok_space|Space]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__건축·실내 공간 — 초광각 왜곡 제어__evidence_raw_scenarios_architecture_interior_wid|건축·실내 공간 — 초광각 왜곡 제어]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__building or room__subject_building_or_room|building or room]]
- `USES_FACET` → [[scene_nodes/scene__interior__environment_interior|interior]]
- `USES_FACET` → [[scene_nodes/scene__0.5x 1x__lens_0_5x_1x|0.5x 1x]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__0.5x를 쓰되 폰을 위로 기울이지 말고 가슴~눈높이에서 수평__tech_architecture_interior_wide_0_5x를_쓰되_폰을_위로_기|0.5x를 쓰되 폰을 위로 기울이지 말고 가슴~눈높이에서 수평.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__방 모서리보다 정면_대칭 구도를 먼저 시도__tech_architecture_interior_wide_방_모서리보다_정면_대칭_구도|방 모서리보다 정면/대칭 구도를 먼저 시도.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__창문이 밝으면 EV -0.3~-1.0, HDR_RAW 사용__param_architecture_interior_wide_창문이_밝으면_ev_0_3|창문이 밝으면 EV -0.3~-1.0, HDR/RAW 사용.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x로 디테일 컷도 함께__tech_architecture_interior_wide_1x로_디테일_컷도_함께|1x로 디테일 컷도 함께.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Geometry_Upright_Vertical 수직 보정__param_architecture_interior_wide_geometry_uprigh|Geometry/Upright/Vertical 수직 보정.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -30~-60, Shadows +10~+30__param_architecture_interior_wide_highlights_30_6|Highlights -30~-60, Shadows +10~+30.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__실내 mixed light는 WB를 중립화__param_architecture_interior_wide_실내_mixed_light는|실내 mixed light는 WB를 중립화.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Warm interior면 Temp +200~+600K, Green cast는 Tint +5~+12__param_architecture_interior_wide_warm_interior면|Warm interior면 Temp +200~+600K, Green cast는 Tint +5~+12.]]
- `AVOIDS` → [[scene_nodes/scene__0.5x 가장자리 가구_사람 왜곡 주의__risk_architecture_interior_wide_0_5x_가장자리_가구_사람|0.5x 가장자리 가구/사람 왜곡 주의.]]
- `AVOIDS` → [[scene_nodes/scene__수직선이 무너지면 공간이 싸 보인다__risk_architecture_interior_wide_수직선이_무너지면_공간이_싸|수직선이 무너지면 공간이 싸 보인다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_how-to-use-camera-coach__evidence_url_https_blog_google_products_pixel_ho|https://blog.google/products/pixel/how-to-use-camera-coach/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]

## Incoming
- [[scene_nodes/scene__건축·실내 공간 — 초광각 왜곡 제어__scenario_architecture_interior_wide|건축·실내 공간 — 초광각 왜곡 제어]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__building or room__subject_building_or_room|building or room]] → `TRIGGERS`
- [[scene_nodes/scene__interior__environment_interior|interior]] → `TRIGGERS`
- [[scene_nodes/scene__0.5x 1x__lens_0_5x_1x|0.5x 1x]] → `TRIGGERS`
