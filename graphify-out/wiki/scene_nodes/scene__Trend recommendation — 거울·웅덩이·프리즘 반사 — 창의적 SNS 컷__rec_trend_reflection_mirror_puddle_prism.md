# Trend recommendation — 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷

- id: `rec_trend_reflection_mirror_puddle_prism`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/reflection_mirror_puddle_prism.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_reflection_mirror_puddle_prism
- **name**: Trend recommendation — 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/reflection_mirror_puddle_prism.md

## Source-oriented graph 연결
- [[source_nodes/source__Creative Reflection__edit_style_creative_reflection|Creative Reflection]]
- [[source_nodes/source__0.5x 1x 2x__lens_0_5x_1x_2x|0.5x 1x 2x]]
- [[source_nodes/source__Person Or City__subject_person_or_city|Person Or City]]
- [[source_nodes/source__Symmetry__tok_symmetry|Symmetry]]
- [[source_nodes/source__Visual Interest__tok_visual_interest|Visual Interest]]
- [[source_nodes/source__Playful Visual Hook__trend_signal_playful_visual_hook|Playful Visual Hook]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__거울·웅덩이·프리즘 반사 — 창의적 SNS 컷__evidence_raw_scenarios_reflection_mirror_puddle|거울·웅덩이·프리즘 반사 — 창의적 SNS 컷]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__urban or nature__environment_urban_or_nature|urban or nature]]
- `USES_FACET` → [[scene_nodes/scene__creative reflection__editstyle_creative_reflection|creative reflection]]
- `USES_FACET` → [[scene_nodes/scene__playful visual hook__trendsignal_playful_visual_hook|playful visual hook]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__웅덩이는 폰을 낮게 내려 반사면을 크게 만든다__tech_reflection_mirror_puddle_prism_웅덩이는_폰을_낮게_내|웅덩이는 폰을 낮게 내려 반사면을 크게 만든다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__거울은 프레임 안 프레임처럼 사용__tech_reflection_mirror_puddle_prism_거울은_프레임_안_프레|거울은 프레임 안 프레임처럼 사용.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__프리즘_CD_유리컵은 렌즈 가장자리에 살짝 대고 빛 번짐을 만든다__tech_reflection_mirror_puddle_prism_프리즘_cd_유리컵은|프리즘/CD/유리컵은 렌즈 가장자리에 살짝 대고 빛 번짐을 만든다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__결과 컷과 BTS 컷을 함께 저장__tech_reflection_mirror_puddle_prism_결과_컷과_bts_컷을|결과 컷과 BTS 컷을 함께 저장.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -20~-60로 반사 하이라이트 보호__param_reflection_mirror_puddle_prism_highlights|Highlights -20~-60로 반사 하이라이트 보호.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Contrast +5~+20, Dehaze +3~+12__param_reflection_mirror_puddle_prism_contrast_5|Contrast +5~+20, Dehaze +3~+12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Prism 색은 Saturation +5~+15, 피부는 mask로 보호__param_reflection_mirror_puddle_prism_prism_색은_sa|Prism 색은 Saturation +5~+15, 피부는 mask로 보호.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__불필요한 손_소품 가장자리는 Remove_Heal__param_reflection_mirror_puddle_prism_불필요한_손_소품_가|불필요한 손/소품 가장자리는 Remove/Heal.]]
- `AVOIDS` → [[scene_nodes/scene__유리_거울은 안전과 주변 반사 노출 주의__risk_reflection_mirror_puddle_prism_유리_거울은_안전과_주|유리/거울은 안전과 주변 반사 노출 주의.]]
- `AVOIDS` → [[scene_nodes/scene__효과가 얼굴을 가리면 시선이 분산__risk_reflection_mirror_puddle_prism_효과가_얼굴을_가리면|효과가 얼굴을 가리면 시선이 분산.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_business.adobe.com_resources_creative-trends-report.ht__evidence_url_https_business_adobe_com_resources|https://business.adobe.com/resources/creative-trends-report.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_masking-mobile-ios__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_creative-photog__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/creative-photography-tricks-thatll-get-you-all-the-likes/]]

## Incoming
- [[scene_nodes/scene__거울·웅덩이·프리즘 반사 — 창의적 SNS 컷__scenario_reflection_mirror_puddle_prism|거울·웅덩이·프리즘 반사 — 창의적 SNS 컷]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__urban or nature__environment_urban_or_nature|urban or nature]] → `TRIGGERS`
- [[scene_nodes/scene__creative reflection__editstyle_creative_reflection|creative reflection]] → `TRIGGERS`
- [[scene_nodes/scene__playful visual hook__trendsignal_playful_visual_hook|playful visual hook]] → `TRIGGERS`
