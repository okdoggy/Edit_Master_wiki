# 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed

- id: `scenario_fashion_ootd_portrait`
- graph: scene-first
- labels: Scenario
- source_file: raw/scenarios/fashion_ootd_portrait.md
- source_url: 

## 사용자 답변에서의 역할
한국어 사용자 질문을 장면 단위로 매칭하는 노드입니다.

## Properties
- **id**: scenario_fashion_ootd_portrait
- **name**: 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed
- **source_file**: raw/scenarios/fashion_ootd_portrait.md
- **tags**: ['fashion', 'ootd', 'portrait', 'full-body', 'instagram']

## Source-oriented graph 연결
- [[source_nodes/source__Clean Influencer__edit_style_clean_influencer|Clean Influencer]]
- [[source_nodes/source__Outfit Color Priority__personal_signal_outfit_color_priority|Outfit Color Priority]]
- [[source_nodes/source__Fashion Outfit__subject_fashion_outfit|Fashion Outfit]]
- [[source_nodes/source__2x Lens__tok_2x_lens|2x Lens]]
- [[source_nodes/source__Body Alignment__tok_body_alignment|Body Alignment]]
- [[source_nodes/source__Body Distortion__tok_body_distortion|Body Distortion]]
- [[source_nodes/source__Grid__tok_grid|Grid]]
- [[source_nodes/source__Outfit Color__tok_outfit_color|Outfit Color]]
- [[source_nodes/source__Skin Tone Protection__tok_skin_tone_protection|Skin Tone Protection]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__evidence_raw_scenarios_fashion_ootd_portrait_md|패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `HAS_SUBJECT` → [[scene_nodes/scene__person__subject_person|person]]
- `HAS_SUBJECT` → [[scene_nodes/scene__fashion outfit__subject_fashion_outfit|fashion outfit]]
- `HAS_ENVIRONMENT` → [[scene_nodes/scene__street or cafe__environment_street_or_cafe|street or cafe]]
- `USES_LENS` → [[scene_nodes/scene__2x or 1x__lens_2x_or_1x|2x or 1x]]
- `USES_MODE` → [[scene_nodes/scene__portrait or photo__mode_portrait_or_photo|portrait or photo]]
- `HAS_EDIT_STYLE` → [[scene_nodes/scene__clean influencer__editstyle_clean_influencer|clean influencer]]
- `HAS_PERSONALIZATION_SIGNAL` → [[scene_nodes/scene__outfit color priority__preference_outfit_color_priority|outfit color priority]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_lens REDUCES_body_distortion__tech_fashion_ootd_portrait_2x_lens_reduces_body|2x_lens REDUCES_body_distortion]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__grid HELPS_body_alignment__tech_fashion_ootd_portrait_grid_helps_body_align|grid HELPS_body_alignment]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__outfit_color REQUIRES_skin_tone_protection__tech_fashion_ootd_portrait_outfit_color_requires|outfit_color REQUIRES_skin_tone_protection]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Trend recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__rec_trend_fashion_ootd_portrait|Trend recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__General recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 see__rec_general_fashion_ootd_portrait|General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `HAS_RECOMMENDATION` → [[scene_nodes/scene__Personalized recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추__rec_personalized_fashion_ootd_portrait|Personalized recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-a-selfie-iph1b8842__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_express_learn_blog_how-to-take-portrait-__evidence_url_https_www_adobe_com_express_learn_b|https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.samsung.com_us_explore_photography_still-life_how-__evidence_url_https_www_samsung_com_us_explore_ph|https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/]]

## Incoming
