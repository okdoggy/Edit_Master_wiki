# Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필

- id: `rec_trend_window_light_cafe_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/window_light_cafe_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_window_light_cafe_portrait
- **name**: Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/window_light_cafe_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Diffused Window__light_diffused_window|Diffused Window]]
- [[source_nodes/source__Skin Retouch Strength__personal_signal_skin_retouch_strength|Skin Retouch Strength]]
- [[source_nodes/source__Background Distance__tok_background_distance|Background Distance]]
- [[source_nodes/source__Separation__tok_separation|Separation]]
- [[source_nodes/source__Window Light__tok_window_light|Window Light]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__카페 창가 인물 — 자연광_인플루언서 프로필__evidence_raw_scenarios_window_light_cafe_portrai|카페 창가 인물 — 자연광/인플루언서 프로필]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__cafe window__environment_cafe_window|cafe window]]
- `USES_FACET` → [[scene_nodes/scene__diffused window__light_diffused_window|diffused window]]
- `USES_FACET` → [[scene_nodes/scene__clean influencer__editstyle_clean_influencer|clean influencer]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__창문 옆 45도에 앉히고 얼굴이 창을 향하게 한다__tech_window_light_cafe_portrait_창문_옆_45도에_앉히고_얼굴|창문 옆 45도에 앉히고 얼굴이 창을 향하게 한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_Portrait, 눈 초점, 배경과 1m 이상 거리__tech_window_light_cafe_portrait_2x_portrait_눈_초점|2x/Portrait, 눈 초점, 배경과 1m 이상 거리.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__테이블 위 소품은 1~2개만 남긴다__tech_window_light_cafe_portrait_테이블_위_소품은_1_2개만|테이블 위 소품은 1~2개만 남긴다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__텍스트_스토리용이면 상단 여백 확보__tech_window_light_cafe_portrait_텍스트_스토리용이면_상단_여백|텍스트/스토리용이면 상단 여백 확보.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject Exposure +0.1~+0.4, Texture -5~-12__param_window_light_cafe_portrait_subject_exposur|Subject Exposure +0.1~+0.4, Texture -5~-12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-20, Clarity -5~-15__param_window_light_cafe_portrait_background_satu|Background Saturation -5~-20, Clarity -5~-15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Orange Luminance +5~+10, Saturation -5~+5__param_window_light_cafe_portrait_orange_luminanc|Orange Luminance +5~+10, Saturation -5~+5.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__전체 Exposure +0.1~+0.3, Highlights -10~-30__param_window_light_cafe_portrait_전체_exposure_0_1|전체 Exposure +0.1~+0.3, Highlights -10~-30.]]
- `AVOIDS` → [[scene_nodes/scene__창문 직사광은 코_눈 밑 그림자를 강하게 만든다__risk_window_light_cafe_portrait_창문_직사광은_코_눈_밑_그림|창문 직사광은 코/눈 밑 그림자를 강하게 만든다.]]
- `AVOIDS` → [[scene_nodes/scene__실내 조명+창빛 혼합은 WB가 어려워 RAW 권장__risk_window_light_cafe_portrait_실내_조명_창빛_혼합은_wb가|실내 조명+창빛 혼합은 WB가 어려워 RAW 권장.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_take-__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_masking-mobile-ios__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_portr__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_express_learn_blog_how-to-take-portrait-__evidence_url_https_www_adobe_com_express_learn_b|https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_people-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/people-quick-tips]]

## Incoming
- [[scene_nodes/scene__카페 창가 인물 — 자연광_인플루언서 프로필__scenario_window_light_cafe_portrait|카페 창가 인물 — 자연광/인플루언서 프로필]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__cafe window__environment_cafe_window|cafe window]] → `TRIGGERS`
- [[scene_nodes/scene__diffused window__light_diffused_window|diffused window]] → `TRIGGERS`
- [[scene_nodes/scene__clean influencer__editstyle_clean_influencer|clean influencer]] → `TRIGGERS`
