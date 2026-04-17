# Personalized recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일

- id: `rec_personalized_beach_backlit_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/beach_backlit_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_beach_backlit_portrait
- **name**: Personalized recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/beach_backlit_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Blue Travel__edit_style_warm_blue_travel|Warm Blue Travel]]
- [[source_nodes/source__Beach__environment_beach|Beach]]
- [[source_nodes/source__2x Portrait__lens_2x_portrait|2x Portrait]]
- [[source_nodes/source__2x Portrait__tok_2x_portrait|2x Portrait]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__해변 역광 인물 — 여름_휴양지 SNS 스타일__evidence_raw_scenarios_beach_backlit_portrait_md|해변 역광 인물 — 여름/휴양지 SNS 스타일]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__person__subject_person|person]]
- `USES_FACET` → [[scene_nodes/scene__beach__environment_beach|beach]]
- `USES_FACET` → [[scene_nodes/scene__warm blue travel__editstyle_warm_blue_travel|warm blue travel]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__해가 낮을 때 피사체 뒤나 45도 뒤에 두어 rim light를 만든다__tech_beach_backlit_portrait_해가_낮을_때_피사체_뒤나_45도_뒤|해가 낮을 때 피사체 뒤나 45도 뒤에 두어 rim light를 만든다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_Portrait로 인물, 0.5x로 장소 전체 컷도 함께__tech_beach_backlit_portrait_2x_portrait로_인물_0_5x|2x/Portrait로 인물, 0.5x로 장소 전체 컷도 함께.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__하늘 기준으로 EV -0.3~-0.7, 얼굴은 후보정에서 mask로 보정__param_beach_backlit_portrait_하늘_기준으로_ev_0_3_0_7|하늘 기준으로 EV -0.3~-0.7, 얼굴은 후보정에서 mask로 보정.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__바닷가 수평선은 Level_Grid로 맞춘다__param_beach_backlit_portrait_바닷가_수평선은_level_grid|바닷가 수평선은 Level/Grid로 맞춘다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Sky mask_ Highlights -30~-60, Dehaze +5~+12__param_beach_backlit_portrait_sky_mask_highlights|Sky mask: Highlights -30~-60, Dehaze +5~+12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject mask_ Exposure +0.2~+0.5, Shadows +10~+25__param_beach_backlit_portrait_subject_mask_exposu|Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Blue Luminance -5~-20, Orange Luminance +5~+15__param_beach_backlit_portrait_blue_luminance_5_20|Blue Luminance -5~-20, Orange Luminance +5~+15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Warm travel이면 Temp +300~+900K__param_beach_backlit_portrait_warm_travel이면_temp|Warm travel이면 Temp +300~+900K.]]
- `AVOIDS` → [[scene_nodes/scene__직사광 정면 얼굴은 눈 찡그림_강한 그림자 발생__risk_beach_backlit_portrait_직사광_정면_얼굴은_눈_찡그림_강한|직사광 정면 얼굴은 눈 찡그림/강한 그림자 발생.]]
- `AVOIDS` → [[scene_nodes/scene__바다_하늘 채도를 너무 올리면 인공적__risk_beach_backlit_portrait_바다_하늘_채도를_너무_올리면_인공적|바다/하늘 채도를 너무 올리면 인공적.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_masking-mobile-ios__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]

## Incoming
- [[scene_nodes/scene__해변 역광 인물 — 여름_휴양지 SNS 스타일__scenario_beach_backlit_portrait|해변 역광 인물 — 여름/휴양지 SNS 스타일]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__person__subject_person|person]] → `TRIGGERS`
- [[scene_nodes/scene__beach__environment_beach|beach]] → `TRIGGERS`
- [[scene_nodes/scene__warm blue travel__editstyle_warm_blue_travel|warm blue travel]] → `TRIGGERS`
