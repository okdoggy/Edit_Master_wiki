# General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게

- id: `rec_general_museum_gallery_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/museum_gallery_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_general_museum_gallery_portrait
- **name**: General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게
- **channel**: general
- **rank_score**: 0.82
- **source_file**: raw/scenarios/museum_gallery_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__color cast__issue_color_cast|color cast]]
- [[source_nodes/source__minimal clean gallery__trend_minimal_clean_gallery|minimal clean gallery]]
- [[source_nodes/source__minimal clean__pref_minimal_clean|minimal clean]]
- [[source_nodes/source__art centered__pref_art_centered|art centered]]
- [[source_nodes/source__minimal clean__outcome_minimal_clean|minimal clean]]
- [[source_nodes/source__art context__outcome_art_context|art context]]
- [[source_nodes/source__no flash__tech_no_flash|no flash]]
- [[source_nodes/source__white balance correction__tech_white_balance|white balance correction]]
- [[source_nodes/source__negative space__tech_negative_space|negative space]]
- [[source_nodes/source__White balance control__param_wb_control|White balance control]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__미술관·전시회 인물 — 플래시 없이 차분하게__evidence_raw_scenarios_museum_gallery_portrait_m|미술관·전시회 인물 — 플래시 없이 차분하게]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__person__subject_person|person]]
- `USES_FACET` → [[scene_nodes/scene__museum gallery__environment_museum_gallery|museum gallery]]
- `USES_FACET` → [[scene_nodes/scene__mixed gallery spotlight__light_mixed_gallery_spotlight|mixed gallery spotlight]]
- `USES_FACET` → [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]]
- `USES_FACET` → [[scene_nodes/scene__photo or portrait__mode_photo_or_portrait|photo or portrait]]
- `OPTIMIZES` → [[scene_nodes/scene__Natural skin tone__out_natural_skin_tone|Natural skin tone]]
- `OPTIMIZES` → [[scene_nodes/scene__Background separation__out_background_separation|Background separation]]
- `OPTIMIZES` → [[scene_nodes/scene__Highlight preservation__out_highlight_preservation|Highlight preservation]]
- `OPTIMIZES` → [[scene_nodes/scene__Face clarity__out_face_clarity|Face clarity]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__플래시는 끄고 작품 조명_벽 반사광을 활용한다__tech_museum_gallery_portrait_플래시는_끄고_작품_조명_벽_반사광|플래시는 끄고 작품 조명/벽 반사광을 활용한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__작품 바로 앞보다 0.5~1m 옆에 서서 인물과 작품이 겹치지 않게 한다__tech_museum_gallery_portrait_작품_바로_앞보다_0_5_1m_옆에|작품 바로 앞보다 0.5~1m 옆에 서서 인물과 작품이 겹치지 않게 한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x로 배경 산만함을 줄이고, 좁으면 1x__tech_museum_gallery_portrait_2x로_배경_산만함을_줄이고_좁으면|2x로 배경 산만함을 줄이고, 좁으면 1x.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__초점은 눈에 맞추고, 하이라이트가 날아가면 EV -0.3__param_museum_gallery_portrait_초점은_눈에_맞추고_하이라이트가|초점은 눈에 맞추고, 하이라이트가 날아가면 EV -0.3.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__WB를 먼저 맞춰 벽이 너무 노랗거나 초록색이 되지 않게 한다__param_museum_gallery_portrait_wb를_먼저_맞춰_벽이_너무_노랗|WB를 먼저 맞춰 벽이 너무 노랗거나 초록색이 되지 않게 한다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -10~-30, Shadows +10~+20__param_museum_gallery_portrait_highlights_10_30_s|Highlights -10~-30, Shadows +10~+20.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-20, Subject Exposure +0.1~+0.3__param_museum_gallery_portrait_background_saturat|Background Saturation -5~-20, Subject Exposure +0.1~+0.3.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Geometry로 벽_프레임 수직을 정리한다__param_museum_gallery_portrait_geometry로_벽_프레임_수직|Geometry로 벽/프레임 수직을 정리한다.]]
- `AVOIDS` → [[scene_nodes/scene__전시 작품 촬영 규칙과 저작권_플래시 금지를 확인한다__risk_museum_gallery_portrait_전시_작품_촬영_규칙과_저작권_플래|전시 작품 촬영 규칙과 저작권/플래시 금지를 확인한다.]]
- `AVOIDS` → [[scene_nodes/scene__작품이 인물 머리 뒤로 튀어나오면 산만하다__risk_museum_gallery_portrait_작품이_인물_머리_뒤로_튀어나오면|작품이 인물 머리 뒤로 튀어나오면 산만하다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_assets.rafmuseum.org.uk_app_uploads_2023_08_Photograph__evidence_url_https_assets_rafmuseum_org_uk_app_u|https://assets.rafmuseum.org.uk/app/uploads/2023/08/Photography-Resources.pdf]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-holiday-photos-night-sight-portrait-mode/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.lifepixel.com_photo-tutorials_6-tips-photographing__evidence_url_https_www_lifepixel_com_photo_tutor|https://www.lifepixel.com/photo-tutorials/6-tips-photographing-museums-galleries]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_photography_comments_1llhctf_problems__evidence_url_https_www_reddit_com_r_photography|https://www.reddit.com/r/photography/comments/1llhctf/problems_with_reflections_in_the_glass_while/]]

## Incoming
- [[scene_nodes/scene__미술관·전시회 인물 — 플래시 없이 차분하게__scenario_museum_gallery_portrait|미술관·전시회 인물 — 플래시 없이 차분하게]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__person__subject_person|person]] → `TRIGGERS`
- [[scene_nodes/scene__museum gallery__environment_museum_gallery|museum gallery]] → `TRIGGERS`
- [[scene_nodes/scene__mixed gallery spotlight__light_mixed_gallery_spotlight|mixed gallery spotlight]] → `TRIGGERS`
- [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]] → `TRIGGERS`
- [[scene_nodes/scene__photo or portrait__mode_photo_or_portrait|photo or portrait]] → `TRIGGERS`
