# Trend recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리

- id: `rec_trend_city_window_reflection`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/city_window_reflection.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_city_window_reflection
- **name**: Trend recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/city_window_reflection.md

## Source-oriented graph 연결
- [[source_nodes/source__blown city lights__issue_blown_city_lights|blown city lights]]
- [[source_nodes/source__reflection _ neon _ cinematic__trend_reflection_neon_cinematic|reflection / neon / cinematic]]
- [[source_nodes/source__moody cinematic__pref_moody_cinematic|moody cinematic]]
- [[source_nodes/source__clean skyline__pref_clean_skyline|clean skyline]]
- [[source_nodes/source__reflection control__outcome_reflection_control|reflection control]]
- [[source_nodes/source__cinematic mood__outcome_cinematic_mood|cinematic mood]]
- [[source_nodes/source__lens close to glass__tech_lens_close_to_glass|lens close to glass]]
- [[source_nodes/source__dark clothing reduces self-reflection__tech_dark_clothing|dark clothing reduces self-reflection]]
- [[source_nodes/source__EV negative__tech_ev_negative|EV negative]]
- [[source_nodes/source__crop simplifies reflection__tech_crop_simplifies|crop simplifies reflection]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__도시 야경 유리창 반사 — 산만한 반사 정리__evidence_raw_scenarios_city_window_reflection_md|도시 야경 유리창 반사 — 산만한 반사 정리]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__window reflection city night__environment_window_reflection_city_night|window reflection city night]]
- `USES_FACET` → [[scene_nodes/scene__city neon__light_city_neon|city neon]]
- `USES_FACET` → [[scene_nodes/scene__moody cinematic__editstyle_moody_cinematic|moody cinematic]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__렌즈를 유리에 최대한 가깝게 대고, 실내 불을 끄거나 어두운 옷을 입는다__tech_city_window_reflection_렌즈를_유리에_최대한_가깝게_대고_실|렌즈를 유리에 최대한 가깝게 대고, 실내 불을 끄거나 어두운 옷을 입는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__반사를 쓸 경우 얼굴_손_조명이 프레임을 방해하지 않게 위치를 잡는다__tech_city_window_reflection_반사를_쓸_경우_얼굴_손_조명이_프레|반사를 쓸 경우 얼굴/손/조명이 프레임을 방해하지 않게 위치를 잡는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x로 전체, 2x로 건물_간판 디테일__tech_city_window_reflection_1x로_전체_2x로_건물_간판_디테일|1x로 전체, 2x로 건물/간판 디테일.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__밝은 간판이 있으면 EV -0.7~-1.3__param_city_window_reflection_밝은_간판이_있으면_ev_0_7_1|밝은 간판이 있으면 EV -0.7~-1.3.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15__param_city_window_reflection_highlights_40_80_bl|Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__반사 영역은 Crop으로 과감히 정리한다__param_city_window_reflection_반사_영역은_crop으로_과감히_정|반사 영역은 Crop으로 과감히 정리한다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Color Grading_ Shadows cool, Highlights warm__param_city_window_reflection_color_grading_shado|Color Grading: Shadows cool, Highlights warm.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Noise Reduction +15~+35, Grain +10~+25__param_city_window_reflection_noise_reduction_15|Noise Reduction +15~+35, Grain +10~+25.]]
- `AVOIDS` → [[scene_nodes/scene__실내 조명이 켜져 있으면 유리창에 방 안이 다 비친다__risk_city_window_reflection_실내_조명이_켜져_있으면_유리창에_방|실내 조명이 켜져 있으면 유리창에 방 안이 다 비친다.]]
- `AVOIDS` → [[scene_nodes/scene__Night mode가 길면 손持ち 사진이 흐려질 수 있다__risk_city_window_reflection_night_mode가_길면_손_사진이|Night mode가 길면 손持ち 사진이 흐려질 수 있다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_travelphotographymagazine.com_how-to-photograph-throug__evidence_url_https_travelphotographymagazine_com|https://travelphotographymagazine.com/how-to-photograph-through-glass/60-second/problems/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_neon-__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/neon-light-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.bhphotovideo.com_explora_photography_tips-and-solu__evidence_url_https_www_bhphotovideo_com_explora|https://www.bhphotovideo.com/explora/photography/tips-and-solutions/seven-tips-for-photographing-cities-at-night]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_AskPhotography_comments_1hvpthv_is_th__evidence_url_https_www_reddit_com_r_askphotograp|https://www.reddit.com/r/AskPhotography/comments/1hvpthv/is_there_anyway_to_get_rid_of_the_window/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_AskPhotography_comments_1rkm1rm_how_c__evidence_url_https_www_reddit_com_r_askphotograp|https://www.reddit.com/r/AskPhotography/comments/1rkm1rm/how_can_i_prevent_these_reflections_on_the_glass/]]

## Incoming
- [[scene_nodes/scene__도시 야경 유리창 반사 — 산만한 반사 정리__scenario_city_window_reflection|도시 야경 유리창 반사 — 산만한 반사 정리]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__window reflection city night__environment_window_reflection_city_night|window reflection city night]] → `TRIGGERS`
- [[scene_nodes/scene__city neon__light_city_neon|city neon]] → `TRIGGERS`
- [[scene_nodes/scene__moody cinematic__editstyle_moody_cinematic|moody cinematic]] → `TRIGGERS`
