# Trend recommendation — 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일

- id: `rec_trend_cherry_blossom_flower_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/cherry_blossom_flower_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_cherry_blossom_flower_portrait
- **name**: Trend recommendation — 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/cherry_blossom_flower_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Airy Pink__edit_style_airy_pink|Airy Pink]]
- [[source_nodes/source__Soft Skin Clean Background__satisfaction_signal_soft_skin_clean_background|Soft Skin Clean Background]]
- [[source_nodes/source__Spring Blossom__trend_signal_spring_blossom|Spring Blossom]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일__evidence_raw_scenarios_cherry_blossom_flower_por|벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__flower tree__environment_flower_tree|flower tree]]
- `USES_FACET` → [[scene_nodes/scene__soft overcast__light_soft_overcast|soft overcast]]
- `USES_FACET` → [[scene_nodes/scene__airy pink__editstyle_airy_pink|airy pink]]
- `USES_FACET` → [[scene_nodes/scene__spring blossom__trendsignal_spring_blossom|spring blossom]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__흐린 날 또는 그늘에서 촬영해 얼굴 그림자를 줄인다__tech_cherry_blossom_flower_portrait_흐린_날_또는_그늘에서|흐린 날 또는 그늘에서 촬영해 얼굴 그림자를 줄인다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_3x 또는 Portrait mode로 꽃 배경을 흐린다__tech_cherry_blossom_flower_portrait_2x_3x_또는_por|2x/3x 또는 Portrait mode로 꽃 배경을 흐린다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__꽃이 얼굴에 너무 겹치지 않게 눈 주변은 깨끗하게 둔다__tech_cherry_blossom_flower_portrait_꽃이_얼굴에_너무_겹치|꽃이 얼굴에 너무 겹치지 않게 눈 주변은 깨끗하게 둔다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__흰 꽃은 EV -0.3으로 하이라이트 보호__param_cherry_blossom_flower_portrait_흰_꽃은_ev_0_3|흰 꽃은 EV -0.3으로 하이라이트 보호.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Exposure +0.2~+0.5, Highlights -20~-40__param_cherry_blossom_flower_portrait_exposure_0|Exposure +0.2~+0.5, Highlights -20~-40.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Pink_Magenta Saturation +5~+15, 전체 Tint +3~+10__param_cherry_blossom_flower_portrait_pink_magent|Pink/Magenta Saturation +5~+15, 전체 Tint +3~+10.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject mask로 피부 Red_Orange saturation 과다를 낮춘다__param_cherry_blossom_flower_portrait_subject_mas|Subject mask로 피부 Red/Orange saturation 과다를 낮춘다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Texture -5~-12 for soft portrait, Background Clarity -5~-15__param_cherry_blossom_flower_portrait_texture_5_1|Texture -5~-12 for soft portrait, Background Clarity -5~-15.]]
- `AVOIDS` → [[scene_nodes/scene__핑크를 전체에 넣으면 피부가 붉어진다__risk_cherry_blossom_flower_portrait_핑크를_전체에_넣으면|핑크를 전체에 넣으면 피부가 붉어진다.]]
- `AVOIDS` → [[scene_nodes/scene__꽃이 너무 가까우면 얼굴보다 꽃에 초점이 잡힌다__risk_cherry_blossom_flower_portrait_꽃이_너무_가까우면_얼|꽃이 너무 가까우면 얼굴보다 꽃에 초점이 잡힌다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_masking-mobile-ios__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_portr__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_people-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/people-quick-tips]]

## Incoming
- [[scene_nodes/scene__벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일__scenario_cherry_blossom_flower_portrait|벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__flower tree__environment_flower_tree|flower tree]] → `TRIGGERS`
- [[scene_nodes/scene__soft overcast__light_soft_overcast|soft overcast]] → `TRIGGERS`
- [[scene_nodes/scene__airy pink__editstyle_airy_pink|airy pink]] → `TRIGGERS`
- [[scene_nodes/scene__spring blossom__trendsignal_spring_blossom|spring blossom]] → `TRIGGERS`
