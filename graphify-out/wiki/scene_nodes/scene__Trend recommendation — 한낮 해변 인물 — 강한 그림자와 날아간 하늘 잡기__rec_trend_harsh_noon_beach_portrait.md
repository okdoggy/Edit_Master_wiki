# Trend recommendation — 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기

- id: `rec_trend_harsh_noon_beach_portrait`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/harsh_noon_beach_portrait.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_harsh_noon_beach_portrait
- **name**: Trend recommendation — 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/harsh_noon_beach_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__harsh shadow__issue_harsh_shadow|harsh shadow]]
- [[source_nodes/source__blown highlights__issue_blown_highlights|blown highlights]]
- [[source_nodes/source__underexposed face__issue_underexposed_face|underexposed face]]
- [[source_nodes/source__face shadow__issue_face_shadow|face shadow]]
- [[source_nodes/source__bright blue travel__trend_bright_blue_travel|bright blue travel]]
- [[source_nodes/source__bright blue travel__pref_bright_blue_travel|bright blue travel]]
- [[source_nodes/source__natural travel__pref_natural_travel|natural travel]]
- [[source_nodes/source__face clarity__outcome_face_clarity|face clarity]]
- [[source_nodes/source__sky preservation__outcome_sky_preservation|sky preservation]]
- [[source_nodes/source__open shade _ side fill__tech_open_shade|open shade / side fill]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기__evidence_raw_scenarios_harsh_noon_beach_portrait|한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__noon beach__environment_noon_beach|noon beach]]
- `USES_FACET` → [[scene_nodes/scene__harsh overhead sun__light_harsh_overhead_sun|harsh overhead sun]]
- `USES_FACET` → [[scene_nodes/scene__bright blue travel__editstyle_bright_blue_travel|bright blue travel]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__가능하면 정오 직사광을 피하고 파라솔_건물 그림자_open shade를 찾는다__tech_harsh_noon_beach_portrait_가능하면_정오_직사광을_피하고|가능하면 정오 직사광을 피하고 파라솔/건물 그림자/open shade를 찾는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__2x_Portrait로 인물 왜곡을 줄이고, 하늘은 프레임 일부만 남긴다__tech_harsh_noon_beach_portrait_2x_portrait로_인물_왜|2x/Portrait로 인물 왜곡을 줄이고, 하늘은 프레임 일부만 남긴다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__촬영 시 EV -0.3~-0.7로 하늘을 보호한다__param_harsh_noon_beach_portrait_촬영_시_ev_0_3_0_7로|촬영 시 EV -0.3~-0.7로 하늘을 보호한다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__얼굴에 반사광이 오도록 흰 모래_벽을 활용한다__tech_harsh_noon_beach_portrait_얼굴에_반사광이_오도록_흰_모래|얼굴에 반사광이 오도록 흰 모래/벽을 활용한다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Sky mask_ Highlights -30~-60, Dehaze +5~+12__param_harsh_noon_beach_portrait_sky_mask_highlig|Sky mask: Highlights -30~-60, Dehaze +5~+12.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject mask_ Exposure +0.2~+0.5, Shadows +10~+25__param_harsh_noon_beach_portrait_subject_mask_exp|Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Blue Luminance -5~-20, Orange Luminance +5~+15__param_harsh_noon_beach_portrait_blue_luminance_5|Blue Luminance -5~-20, Orange Luminance +5~+15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__피부가 너무 주황이면 Orange Saturation -5~-10__param_harsh_noon_beach_portrait_피부가_너무_주황이면_oran|피부가 너무 주황이면 Orange Saturation -5~-10.]]
- `AVOIDS` → [[scene_nodes/scene__정면 직사광은 눈 찡그림과 코 그림자를 만든다__risk_harsh_noon_beach_portrait_정면_직사광은_눈_찡그림과_코|정면 직사광은 눈 찡그림과 코 그림자를 만든다.]]
- `AVOIDS` → [[scene_nodes/scene__하늘을 살리려고 전체 노출을 낮추면 얼굴이 죽는다__risk_harsh_noon_beach_portrait_하늘을_살리려고_전체_노출을_낮|하늘을 살리려고 전체 노출을 낮추면 얼굴이 죽는다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.adobe.com_en_publish_2022_10_27_beach-photography__evidence_url_https_blog_adobe_com_en_publish_202|https://blog.adobe.com/en/publish/2022/10/27/beach-photography-tips-techniques]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_portr__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_technique_gold__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/technique/golden-hour.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]

## Incoming
- [[scene_nodes/scene__한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기__scenario_harsh_noon_beach_portrait|한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__noon beach__environment_noon_beach|noon beach]] → `TRIGGERS`
- [[scene_nodes/scene__harsh overhead sun__light_harsh_overhead_sun|harsh overhead sun]] → `TRIGGERS`
- [[scene_nodes/scene__bright blue travel__editstyle_bright_blue_travel|bright blue travel]] → `TRIGGERS`
