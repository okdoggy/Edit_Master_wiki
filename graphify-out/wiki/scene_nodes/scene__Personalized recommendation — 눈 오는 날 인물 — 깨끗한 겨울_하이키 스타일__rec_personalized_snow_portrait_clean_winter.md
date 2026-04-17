# Personalized recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일

- id: `rec_personalized_snow_portrait_clean_winter`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/snow_portrait_clean_winter.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_snow_portrait_clean_winter
- **name**: Personalized recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/snow_portrait_clean_winter.md

## Source-oriented graph 연결
- [[source_nodes/source__Clean Winter__edit_style_clean_winter|Clean Winter]]
- [[source_nodes/source__Snow__environment_snow|Snow]]
- [[source_nodes/source__Person__subject_person|Person]]
- [[source_nodes/source__Blue Cast__tok_blue_cast|Blue Cast]]
- [[source_nodes/source__Camera Meter__tok_camera_meter|Camera Meter]]
- [[source_nodes/source__Light__tok_light|Light]]
- [[source_nodes/source__Subject Mask__tok_subject_mask|Subject Mask]]
- [[source_nodes/source__Underexpose Snow__tok_underexpose_snow|Underexpose Snow]]
- [[source_nodes/source__White Balance__tok_white_balance|White Balance]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__evidence_raw_scenarios_snow_portrait_clean_winte|눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__person__subject_person|person]]
- `USES_FACET` → [[scene_nodes/scene__snow__environment_snow|snow]]
- `USES_FACET` → [[scene_nodes/scene__clean winter__editstyle_clean_winter|clean winter]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__눈 배경이 많으면 카메라가 어둡게 찍을 수 있어 EV +0.3~+1.0을 테스트한다__param_snow_portrait_clean_winter_눈_배경이_많으면_카메라가|눈 배경이 많으면 카메라가 어둡게 찍을 수 있어 EV +0.3~+1.0을 테스트한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__얼굴은 2x_Portrait, 풍경 포함은 1x_0.5x__tech_snow_portrait_clean_winter_얼굴은_2x_portrait|얼굴은 2x/Portrait, 풍경 포함은 1x/0.5x.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__눈발은 어두운 배경 앞에서 더 잘 보인다__tech_snow_portrait_clean_winter_눈발은_어두운_배경_앞에서_더|눈발은 어두운 배경 앞에서 더 잘 보인다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__장갑_빨간 목도리 같은 포인트 컬러를 넣는다__tech_snow_portrait_clean_winter_장갑_빨간_목도리_같은_포인트|장갑/빨간 목도리 같은 포인트 컬러를 넣는다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__WB_ 눈이 파랗게 보이면 Temp +300~+800K__param_snow_portrait_clean_winter_wb_눈이_파랗게_보이면_t|WB: 눈이 파랗게 보이면 Temp +300~+800K.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -10~-30로 눈 디테일 유지__param_snow_portrait_clean_winter_highlights_10_3|Highlights -10~-30로 눈 디테일 유지.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Whites +5~+20, Blacks -5~-15__param_snow_portrait_clean_winter_whites_5_20_bla|Whites +5~+20, Blacks -5~-15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject mask_ Face Exposure +0.1~+0.3, Orange Luminance +5__param_snow_portrait_clean_winter_subject_mask_fa|Subject mask: Face Exposure +0.1~+0.3, Orange Luminance +5.]]
- `AVOIDS` → [[scene_nodes/scene__눈을 순백으로만 밀면 디테일이 사라진다__risk_snow_portrait_clean_winter_눈을_순백으로만_밀면_디테일이|눈을 순백으로만 밀면 디테일이 사라진다.]]
- `AVOIDS` → [[scene_nodes/scene__스마트폰 렌즈에 눈_물방울이 묻으면 콘트라스트가 급격히 떨어진다__risk_snow_portrait_clean_winter_스마트폰_렌즈에_눈_물방울이|스마트폰 렌즈에 눈/물방울이 묻으면 콘트라스트가 급격히 떨어진다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]

## Incoming
- [[scene_nodes/scene__눈 오는 날 인물 — 깨끗한 겨울_하이키 스타일__scenario_snow_portrait_clean_winter|눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__person__subject_person|person]] → `TRIGGERS`
- [[scene_nodes/scene__snow__environment_snow|snow]] → `TRIGGERS`
- [[scene_nodes/scene__clean winter__editstyle_clean_winter|clean winter]] → `TRIGGERS`
