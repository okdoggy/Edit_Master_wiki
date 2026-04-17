# Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리

- id: `rec_personalized_mirror_selfie_ootd`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/mirror_selfie_ootd.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_personalized_mirror_selfie_ootd
- **name**: Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리
- **channel**: personalized
- **rank_score**: 0.7
- **source_file**: raw/scenarios/mirror_selfie_ootd.md

## Source-oriented graph 연결
- [[source_nodes/source__mirror distortion__issue_mirror_distortion|mirror distortion]]
- [[source_nodes/source__dirty mirror__issue_dirty_mirror|dirty mirror]]
- [[source_nodes/source__clean influencer__trend_clean_influencer|clean influencer]]
- [[source_nodes/source__clean influencer__pref_clean_influencer|clean influencer]]
- [[source_nodes/source__longer-looking legs__pref_longer_legs|longer-looking legs]]
- [[source_nodes/source__fashion proportion__outcome_fashion_proportion|fashion proportion]]
- [[source_nodes/source__rear camera + timer__tech_rear_camera_timer|rear camera + timer]]
- [[source_nodes/source__clean mirror__tech_clean_mirror|clean mirror]]
- [[source_nodes/source__4_5 crop__param_crop_4_5|4:5 crop]]
- [[source_nodes/source__MakeUseOf mirror selfie poses__evidence_makeuseof_mirror_selfie|MakeUseOf mirror selfie poses]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__거울 셀카 OOTD — 몸 비율과 거울 반사 정리__evidence_raw_scenarios_mirror_selfie_ootd_md|거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__person__subject_person|person]]
- `USES_FACET` → [[scene_nodes/scene__fashion outfit__subject_fashion_outfit|fashion outfit]]
- `USES_FACET` → [[scene_nodes/scene__mirror indoor__environment_mirror_indoor|mirror indoor]]
- `USES_FACET` → [[scene_nodes/scene__clean influencer__editstyle_clean_influencer|clean influencer]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers warm tone__pref_warm|Prefers warm tone]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers cinematic look__pref_cinematic|Prefers cinematic look]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers natural color__pref_natural|Prefers natural color]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers film grain__pref_film|Prefers film grain]]
- `ADAPTS_TO` → [[scene_nodes/scene__Prefers bright_airy style__pref_bright|Prefers bright/airy style]]
- `ADAPTS_TO` → [[scene_nodes/scene__Low skin retouch__pref_low_retouch|Low skin retouch]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__거울과 폰을 최대한 수직으로 맞춘다__tech_mirror_selfie_ootd_거울과_폰을_최대한_수직으로_맞춘다|거울과 폰을 최대한 수직으로 맞춘다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__폰을 가슴~얼굴 높이에 두고 아래로 과하게 기울이지 않는다__tech_mirror_selfie_ootd_폰을_가슴_얼굴_높이에_두고_아래로_과하게|폰을 가슴~얼굴 높이에 두고 아래로 과하게 기울이지 않는다.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__가능하면 후면 1x_2x + 타이머, 아니면 전면 카메라 왜곡을 주의__param_mirror_selfie_ootd_가능하면_후면_1x_2x_타이머_아니면_전|가능하면 후면 1x/2x + 타이머, 아니면 전면 카메라 왜곡을 주의.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__촬영 전 거울 얼룩과 배경 물건을 정리한다__tech_mirror_selfie_ootd_촬영_전_거울_얼룩과_배경_물건을_정리한다|촬영 전 거울 얼룩과 배경 물건을 정리한다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Geometry_Vertical로 기울어진 선을 바로잡는다__param_mirror_selfie_ootd_geometry_vertical로_기울어진|Geometry/Vertical로 기울어진 선을 바로잡는다.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Subject_Outfit mask로 옷 색을 살리고 피부는 과포화 방지__param_mirror_selfie_ootd_subject_outfit_mask로_옷|Subject/Outfit mask로 옷 색을 살리고 피부는 과포화 방지.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Background Saturation -5~-20, Clarity -5~-15__param_mirror_selfie_ootd_background_saturation_5|Background Saturation -5~-20, Clarity -5~-15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Crop은 4_5 기준으로 발끝_머리 여백 확보__param_mirror_selfie_ootd_crop은_4_5_기준으로_발끝_머리_여백|Crop은 4:5 기준으로 발끝/머리 여백 확보.]]
- `AVOIDS` → [[scene_nodes/scene__거울이 기울면 다리_상체 비율이 왜곡된다__risk_mirror_selfie_ootd_거울이_기울면_다리_상체_비율이_왜곡된다|거울이 기울면 다리/상체 비율이 왜곡된다.]]
- `AVOIDS` → [[scene_nodes/scene__초광각 전면 셀카는 얼굴과 손이 커질 수 있다__risk_mirror_selfie_ootd_초광각_전면_셀카는_얼굴과_손이_커질_수_있|초광각 전면 셀카는 얼굴과 손이 커질 수 있다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_frame-10-tips-getting-great__evidence_url_https_blog_google_products_pixel_fr|https://blog.google/products/pixel/frame-10-tips-getting-great-portraits-pixel-2/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products_pixel_take-id-photo-google-pixel-__evidence_url_https_blog_google_products_pixel_ta|https://blog.google/products/pixel/take-id-photo-google-pixel-tips/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_en-lamr_guide_iphone_iph1a3c5b4c3_io__evidence_url_https_support_apple_com_en_lamr_gui|https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_support.apple.com_guide_iphone_take-portraits-iphd7d3a__evidence_url_https_support_apple_com_guide_iphon|https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_learn_lightroom-cc_web_color-adjustment__evidence_url_https_www_adobe_com_learn_lightroom|https://www.adobe.com/learn/lightroom-cc/web/color-adjustment]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.makeuseof.com_mirror-selfie-poses__evidence_url_https_www_makeuseof_com_mirror_self|https://www.makeuseof.com/mirror-selfie-poses/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_MtF_comments_nnzr6s_its_not_you_its_y__evidence_url_https_www_reddit_com_r_mtf_comments|https://www.reddit.com/r/MtF/comments/nnzr6s/its_not_you_its_your_camera_photography_tips_for/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.reddit.com_r_femalefashionadvice_comments_2iupe5_t__evidence_url_https_www_reddit_com_r_femalefashio|https://www.reddit.com/r/femalefashionadvice/comments/2iupe5/taking_outfit_photos_with_your_phone/]]

## Incoming
- [[scene_nodes/scene__거울 셀카 OOTD — 몸 비율과 거울 반사 정리__scenario_mirror_selfie_ootd|거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__person__subject_person|person]] → `TRIGGERS`
- [[scene_nodes/scene__fashion outfit__subject_fashion_outfit|fashion outfit]] → `TRIGGERS`
- [[scene_nodes/scene__mirror indoor__environment_mirror_indoor|mirror indoor]] → `TRIGGERS`
- [[scene_nodes/scene__clean influencer__editstyle_clean_influencer|clean influencer]] → `TRIGGERS`
