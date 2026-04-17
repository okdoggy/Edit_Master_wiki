# Trend recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천

- id: `rec_trend_golden_hour_travel_scale`
- graph: scene-first
- labels: Recommendation
- source_file: raw/scenarios/golden_hour_travel_scale.md
- source_url: 

## 사용자 답변에서의 역할
사용자 장면 질문에 대한 추천 단위입니다. trend/general/personalized 채널로 사용됩니다.

## Properties
- **id**: rec_trend_golden_hour_travel_scale
- **name**: Trend recommendation — 여행 골든아워 — wide/detail/scale 3컷 추천
- **channel**: trend
- **rank_score**: 0.75
- **source_file**: raw/scenarios/golden_hour_travel_scale.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Travel__edit_style_warm_travel|Warm Travel]]
- [[source_nodes/source__Golden Hour__light_golden_hour|Golden Hour]]
- [[source_nodes/source__Traveler__subject_traveler|Traveler]]
- [[source_nodes/source__Detail__tok_detail|Detail]]
- [[source_nodes/source__Detail Shot__tok_detail_shot|Detail Shot]]
- [[source_nodes/source__Golden Hour__tok_golden_hour|Golden Hour]]
- [[source_nodes/source__Location__tok_location|Location]]
- [[source_nodes/source__Memory__tok_memory|Memory]]
- [[source_nodes/source__Scale Subject__tok_scale_subject|Scale Subject]]
- [[source_nodes/source__Size__tok_size|Size]]

## Outgoing
- `SUPPORTED_BY` → [[scene_nodes/scene__여행 골든아워 — wide_detail_scale 3컷 추천__evidence_raw_scenarios_golden_hour_travel_scale|여행 골든아워 — wide/detail/scale 3컷 추천]]
- `RENDERED_BY` → [[scene_nodes/scene__Natural answer renderer guidelines__answer_renderer_contract|Natural answer renderer guidelines]]
- `USES_FACET` → [[scene_nodes/scene__landmark__environment_landmark|landmark]]
- `USES_FACET` → [[scene_nodes/scene__golden hour__light_golden_hour|golden hour]]
- `USES_FACET` → [[scene_nodes/scene__warm travel__editstyle_warm_travel|warm travel]]
- `OPTIMIZES` → [[scene_nodes/scene__Social-ready crop_export__out_social_readiness|Social-ready crop/export]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__0.5x_1x로 장소 전체, 2x_5x로 디테일, 사람을 넣어 scale 컷 촬영__tech_golden_hour_travel_scale_0_5x_1x로_장소_전체_2x|0.5x/1x로 장소 전체, 2x/5x로 디테일, 사람을 넣어 scale 컷 촬영.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__일출 직후_일몰 직전 측광을 사용__tech_golden_hour_travel_scale_일출_직후_일몰_직전_측광을_사용|일출 직후/일몰 직전 측광을 사용.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__하늘이 밝으면 EV -0.3~-1.0__param_golden_hour_travel_scale_하늘이_밝으면_ev_0_3_1|하늘이 밝으면 EV -0.3~-1.0.]]
- `USES_TECHNIQUE` → [[scene_nodes/scene__볼륨 버튼 셔터_격자로 수평 유지__tech_golden_hour_travel_scale_볼륨_버튼_셔터_격자로_수평_유지|볼륨 버튼 셔터/격자로 수평 유지.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__전체 시리즈 WB 통일__param_golden_hour_travel_scale_전체_시리즈_wb_통일|전체 시리즈 WB 통일.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Highlights -30~-60, Shadows +10~+30__param_golden_hour_travel_scale_highlights_30_60|Highlights -30~-60, Shadows +10~+30.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Temp +300~+900K, Vibrance +5~+15__param_golden_hour_travel_scale_temp_300_900k_vib|Temp +300~+900K, Vibrance +5~+15.]]
- `SETS_PARAMETER` → [[scene_nodes/scene__Geometry_Upright로 건축 수직 보정__param_golden_hour_travel_scale_geometry_upright로|Geometry/Upright로 건축 수직 보정.]]
- `AVOIDS` → [[scene_nodes/scene__골든아워 색을 과하게 올리면 피부가 주황색이 된다__risk_golden_hour_travel_scale_골든아워_색을_과하게_올리면_피부|골든아워 색을 과하게 올리면 피부가 주황색이 된다.]]
- `AVOIDS` → [[scene_nodes/scene__한 장만 찍으면 추천 시스템에서 스토리 맥락이 부족하다__risk_golden_hour_travel_scale_한_장만_찍으면_추천_시스템에서|한 장만 찍으면 추천 시스템에서 스토리 맥락이 부족하다.]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_blog.google_products-and-platforms_devices_pixel_trave__evidence_url_https_blog_google_products_and_plat|https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_helpx.adobe.com_lightroom-cc_using_edit-photos-mobile-__evidence_url_https_helpx_adobe_com_lightroom_cc|https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.adobe.com_creativecloud_photography_discover_smart__evidence_url_https_www_adobe_com_creativecloud_p|https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html]]
- `SUPPORTED_BY` → [[scene_nodes/scene__https_www.nationalgeographic.com_photography_article_camera-__evidence_url_https_www_nationalgeographic_com_ph|https://www.nationalgeographic.com/photography/article/camera-phone-photos]]

## Incoming
- [[scene_nodes/scene__여행 골든아워 — wide_detail_scale 3컷 추천__scenario_golden_hour_travel_scale|여행 골든아워 — wide/detail/scale 3컷 추천]] → `HAS_RECOMMENDATION`
- [[scene_nodes/scene__landmark__environment_landmark|landmark]] → `TRIGGERS`
- [[scene_nodes/scene__golden hour__light_golden_hour|golden hour]] → `TRIGGERS`
- [[scene_nodes/scene__warm travel__editstyle_warm_travel|warm travel]] → `TRIGGERS`
