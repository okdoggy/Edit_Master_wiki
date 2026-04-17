# Trend recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기

- id: `rec_trend_marketplace_street_food_story`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/marketplace_street_food_story.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_marketplace_street_food_story
- **name**: Trend recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/marketplace_street_food_story.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Documentary__edit_style_warm_documentary|Warm Documentary]]
- [[source_nodes/source__Street Food__subject_street_food|Street Food]]
- [[source_nodes/source__Consistent WB__tok_consistent_wb|Consistent WB]]
- [[source_nodes/source__Human Hands__tok_human_hands|Human Hands]]
- [[source_nodes/source__Series__tok_series|Series]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__시장·길거리 음식 스토리 — 사람_손_음식_장소 묶기__evidence_raw_scenarios_marketplace_street_food_s|시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__market__environment_market|market]]
- `USES_FACET` → [[scene_nodes/scene__warm documentary__editstyle_warm_documentary|warm documentary]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__1x로 시장_가게 전체, 2x로 음식 질감, 1x_2x로 손이나 조리 장면__tech_marketplace_street_food_story_1x로_시장_가게_전체|1x로 시장/가게 전체, 2x로 음식 질감, 1x/2x로 손이나 조리 장면.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__조리 불빛_김_기름 윤기를 역광으로 살린다__tech_marketplace_street_food_story_조리_불빛_김_기름_윤기|조리 불빛/김/기름 윤기를 역광으로 살린다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__사람을 찍을 때는 맥락과 예의를 지킨다__tech_marketplace_street_food_story_사람을_찍을_때는_맥락과|사람을 찍을 때는 맥락과 예의를 지킨다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__Photo + 짧은 Video로 소리_움직임도 확보__param_marketplace_street_food_story_photo_짧은_vid|Photo + 짧은 Video로 소리/움직임도 확보.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__WB를 시리즈 전체에 맞춘다__param_marketplace_street_food_story_wb를_시리즈_전체에|WB를 시리즈 전체에 맞춘다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -20~-50, Shadows +10~+25__param_marketplace_street_food_story_highlights_2|Highlights -20~-50, Shadows +10~+25.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture +10~+20 for food, Grain +10~+25 for documentary__param_marketplace_street_food_story_texture_10_2|Texture +10~+20 for food, Grain +10~+25 for documentary.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-15__param_marketplace_street_food_story_background_s|Background Saturation -5~-15.]]
- `AVOIDS` → [[scene_nodes/scene__형광등_노란등 혼합으로 색이 틀어질 수 있어 RAW 권장__risk_marketplace_street_food_story_형광등_노란등_혼합으로|형광등/노란등 혼합으로 색이 틀어질 수 있어 RAW 권장.]]
- `AVOIDS` → [[scene_nodes/scene__사람 얼굴 공개는 동의_맥락 고려__risk_marketplace_street_food_story_사람_얼굴_공개는_동의|사람 얼굴 공개는 동의/맥락 고려.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_four-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/four-tips-taking-delectable-food-photos-pixel-2/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_iphonephotographyschool.com_food__evidence_url_https_iphonephotographyschool_com_f|https://iphonephotographyschool.com/food/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_people-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/people-quick-tips]]

## Incoming
- [[scene_nodes/scene__시장·길거리 음식 스토리 — 사람_손_음식_장소 묶기__scenario_marketplace_street_food_story|시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__market__environment_market|market]] → `TRIGGERS`
- [[scene_nodes/scene__warm documentary__editstyle_warm_documentary|warm documentary]] → `TRIGGERS`
