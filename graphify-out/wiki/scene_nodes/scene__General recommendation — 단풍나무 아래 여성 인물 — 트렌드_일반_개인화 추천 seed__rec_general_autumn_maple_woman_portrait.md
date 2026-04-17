# General recommendation — 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed

- id: `rec_general_autumn_maple_woman_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/autumn_maple_woman_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_autumn_maple_woman_portrait
- **name**: General recommendation — 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/autumn_maple_woman_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Foliage__edit_style_warm_foliage|Warm Foliage]]
- [[source_nodes/source__Autumn Maple Tree__environment_autumn_maple_tree|Autumn Maple Tree]]
- [[source_nodes/source__2x 3x Portrait__lens_2x_3x_portrait|2x 3x Portrait]]
- [[source_nodes/source__Golden Hour Or Backlight__light_golden_hour_or_backlight|Golden Hour Or Backlight]]
- [[source_nodes/source__Portrait Or Photo__mode_portrait_or_photo|Portrait Or Photo]]
- [[source_nodes/source__Skin Tone Preference__personal_signal_skin_tone_preference|Skin Tone Preference]]
- [[source_nodes/source__Clear Face Warm Background__satisfaction_signal_clear_face_warm_background|Clear Face Warm Background]]
- [[source_nodes/source__Woman__subject_woman|Woman]]
- [[source_nodes/source__2x__tok_2x|2x]]
- [[source_nodes/source__2x 3x__tok_2x_3x|2x 3x]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천 seed__evidence_raw_scenarios_autumn_maple_woman_portra|단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__woman__subject_woman|woman]]
- `USES_FACET` → [[scene_nodes/scene__autumn maple tree__environment_autumn_maple_tree|autumn maple tree]]
- `USES_FACET` → [[scene_nodes/scene__golden hour or backlight__light_golden_hour_or_backlight|golden hour or backlight]]
- `USES_FACET` → [[scene_nodes/scene__2x 3x portrait__lens_2x_3x_portrait|2x 3x portrait]]
- `USES_FACET` → [[scene_nodes/scene__portrait or photo__mode_portrait_or_photo|portrait or photo]]
- `USES_FACET` → [[scene_nodes/scene__clear face warm background__satisfactionsignal_clear_face_warm_background|clear face warm background]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_3x 또는 Portrait mode로 얼굴 왜곡을 줄인다__tech_autumn_maple_woman_portrait_2x_3x_또는_portra|2x/3x 또는 Portrait mode로 얼굴 왜곡을 줄인다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__단풍잎을 전경에 걸쳐 프레임을 만들고, 피사체와 배경 나무 사이를 1~3m 이상 벌린다__tech_autumn_maple_woman_portrait_단풍잎을_전경에_걸쳐_프레임|단풍잎을 전경에 걸쳐 프레임을 만들고, 피사체와 배경 나무 사이를 1~3m 이상 벌린다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__해 질 무렵 역광_측광에서 머리카락 rim light가 생기게 위치를 잡는다__tech_autumn_maple_woman_portrait_해_질_무렵_역광_측광에서|해 질 무렵 역광/측광에서 머리카락 rim light가 생기게 위치를 잡는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__밝은 하늘이 있으면 EV -0.3~-0.7로 하이라이트를 보호한다__param_autumn_maple_woman_portrait_밝은_하늘이_있으면_ev|밝은 하늘이 있으면 EV -0.3~-0.7로 하이라이트를 보호한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__잎을 뿌리는 액션은 Burst_Live_8K Video Snap류로 여러 프레임 확보__tech_autumn_maple_woman_portrait_잎을_뿌리는_액션은_burs|잎을 뿌리는 액션은 Burst/Live/8K Video Snap류로 여러 프레임 확보.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject mask_ Exposure +0.1~+0.3, Texture -5~0__param_autumn_maple_woman_portrait_subject_mask_e|Subject mask: Exposure +0.1~+0.3, Texture -5~0.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background_foliage mask_ Orange_Yellow Saturation +5~+18, Lu__param_autumn_maple_woman_portrait_background_fol|Background/foliage mask: Orange/Yellow Saturation +5~+18, Luminance +0~+10.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Green이 탁하면 Green Saturation -10~-25, Yellow Hue를 orange 쪽으로__param_autumn_maple_woman_portrait_green이_탁하면_gre|Green이 탁하면 Green Saturation -10~-25, Yellow Hue를 orange 쪽으로 약간.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__전체 Temp +300~+900K, Tint +2~+6__param_autumn_maple_woman_portrait_전체_temp_300_90|전체 Temp +300~+900K, Tint +2~+6.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Film trend이면 Grain +10~+25, cinematic이면 Shadows를 살짝 cool__param_autumn_maple_woman_portrait_film_trend이면_g|Film trend이면 Grain +10~+25, cinematic이면 Shadows를 살짝 cool.]]
- `AVOIDS` → [[scene_nodes/scene__단풍 채도를 과하게 올리면 피부도 주황색이 된다. Subject mask로 피부를 분리한다__risk_autumn_maple_woman_portrait_단풍_채도를_과하게_올리면|단풍 채도를 과하게 올리면 피부도 주황색이 된다. Subject mask로 피부를 분리한다.]]
- `AVOIDS` → [[scene_nodes/scene__0.5x 인물은 얼굴_몸 왜곡 위험이 크다__risk_autumn_maple_woman_portrait_0_5x_인물은_얼굴_몸_왜|0.5x 인물은 얼굴/몸 왜곡 위험이 크다.]]
- `AVOIDS` → [[scene_nodes/scene__그늘이 너무 깊으면 얼굴보다 배경이 먼저 예뻐지는 실패가 생긴다__risk_autumn_maple_woman_portrait_그늘이_너무_깊으면_얼굴보다|그늘이 너무 깊으면 얼굴보다 배경이 먼저 예뻐지는 실패가 생긴다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_masking-mobile-ios__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_iphonephotographyschool.com_fall__evidence_url_https_iphonephotographyschool_com_f|https://iphonephotographyschool.com/fall/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_iphonephotographyschool.com_leaves__evidence_url_https_iphonephotographyschool_com_l|https://iphonephotographyschool.com/leaves/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_express_learn_blog_how-to-take-portrait-__evidence_url_https_www_adobe_com_express_learn_b|https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_photo-filters__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/photo-filters]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_how-to-pull-off__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/how-to-pull-off-the-perfect-fall-photoshoot/]]

## Incoming
- [[scene_nodes/scene__단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천 seed__scenario_autumn_maple_woman_portrait|단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__Example_ 단풍나무 아래 여성__obs_autumn_woman_maple|Example: 단풍나무 아래 여성]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__woman__subject_woman|woman]] → `TRIGGERS`
- [[scene_nodes/scene__autumn maple tree__environment_autumn_maple_tree|autumn maple tree]] → `TRIGGERS`
- [[scene_nodes/scene__golden hour or backlight__light_golden_hour_or_backlight|golden hour or backlight]] → `TRIGGERS`
- [[scene_nodes/scene__2x 3x portrait__lens_2x_3x_portrait|2x 3x portrait]] → `TRIGGERS`
- [[scene_nodes/scene__portrait or photo__mode_portrait_or_photo|portrait or photo]] → `TRIGGERS`
- [[scene_nodes/scene__clear face warm background__satisfactionsignal_clear_face_warm_background|clear face warm background]] → `TRIGGERS`
- [[scene_nodes/scene__woman__subject_woman|woman]] → `TRIGGERS`
- [[scene_nodes/scene__golden hour or backlight__light_golden_hour_or_backlight|golden hour or backlight]] → `TRIGGERS`
- [[scene_nodes/scene__Blown highlights__issue_blown_highlights|Blown highlights]] → `TRIGGERS`
