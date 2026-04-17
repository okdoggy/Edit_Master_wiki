# 미술관·전시회 인물 — 플래시 없이 차분하게

- id: `scenario_museum_gallery_portrait`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/museum_gallery_portrait.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_museum_gallery_portrait
- **name**: 미술관·전시회 인물 — 플래시 없이 차분하게
- **source_file**: raw/scenarios/museum_gallery_portrait.md
- **tags**: ['museum', 'gallery', 'indoor', 'portrait', 'no-flash', 'mixed-light']

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
- `HAS_SUBJECT` → [[scene_nodes/scene__person__subject_person|person]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__museum gallery__environment_museum_gallery|museum gallery]]
- `HAS_LIGHT` → [[scene_nodes/scene__mixed gallery spotlight__light_mixed_gallery_spotlight|mixed gallery spotlight]]
- `USES_LENS` → [[scene_nodes/scene__1x 2x__lens_1x_2x|1x 2x]]
- `USES_MODE` → [[scene_nodes/scene__photo or portrait__mode_photo_or_portrait|photo or portrait]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__minimal clean__editstyle_minimal_clean|minimal clean]]
- `HAS_RISK` → [[scene_nodes/scene__mixed white balance__risk_mixed_white_balance|mixed white balance]]
- `HAS_RISK` → [[scene_nodes/scene__busy background__risk_busy_background|busy background]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__no_flash_preserves_gallery_rules__tech_museum_gallery_portrait_no_flash_preserves|no_flash_preserves_gallery_rules]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_reduces_background_noise__tech_museum_gallery_portrait_2x_reduces_backgrou|2x_reduces_background_noise]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__white_balance_controls_gallery_cast__tech_museum_gallery_portrait_white_balance_contr|white_balance_controls_gallery_cast]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__negative_space_supports_art_context__tech_museum_gallery_portrait_negative_space_supp|negative_space_supports_art_context]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_trend_museum_gallery_portrait|Trend recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_general_museum_gallery_portrait|General recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게__rec_personalized_museum_gallery_portrait|Personalized recommendation — 미술관·전시회 인물 — 플래시 없이 차분하게]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_assets.rafmuseum.org.uk_app_uploads_2023_08_Photograph__evidence_url_https_assets_rafmuseum_org_uk_app_u|https://assets.rafmuseum.org.uk/app/uploads/2023/08/Photography-Resources.pdf]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-holiday-photos-night-sight-portrait-mode/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.lifepixel.com_photo-tutorials_6-tips-photographing__evidence_url_https_www_lifepixel_com_photo_tutor|https://www.lifepixel.com/photo-tutorials/6-tips-photographing-museums-galleries]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_photography_comments_1llhctf_problems__evidence_url_https_www_reddit_com_r_photography|https://www.reddit.com/r/photography/comments/1llhctf/problems_with_reflections_in_the_glass_while/]]

## Incoming
- [[scene_nodes/scene__전시회 인물__alias_전시회_인물|전시회 인물]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__미술관 사진__alias_미술관_사진|미술관 사진]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__작품 앞 인물__alias_작품_앞_인물|작품 앞 인물]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__플래시 금지__alias_플래시_금지|플래시 금지]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__실내 조명 인물__alias_실내_조명_인물|실내 조명 인물]] → `MATCHES_SCENARIO`
- [[scene_nodes/scene__갤러리 프로필__alias_갤러리_프로필|갤러리 프로필]] → `MATCHES_SCENARIO`
