# clean influencer

- id: `editstyle_clean_influencer`
- graph: scene-first
- labels: EditStyle, SceneFacet
- source_file: raw/scenarios/window_light_cafe_portrait.md
- source_url: 

## Properties
- **id**: editstyle_clean_influencer
- **key**: edit_style
- **value**: clean_influencer
- **name**: clean influencer
- **source_file**: raw/scenarios/window_light_cafe_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Diffused Window__light_diffused_window|Diffused Window]]
- [[source_nodes/source__Skin Retouch Strength__personal_signal_skin_retouch_strength|Skin Retouch Strength]]
- [[source_nodes/source__Background Distance__tok_background_distance|Background Distance]]
- [[source_nodes/source__Separation__tok_separation|Separation]]
- [[source_nodes/source__Window Light__tok_window_light|Window Light]]
- [[source_nodes/source__Clean Influencer__edit_style_clean_influencer|Clean Influencer]]
- [[source_nodes/source__clean influencer__trend_clean_influencer|clean influencer]]
- [[source_nodes/source__clean influencer__pref_clean_influencer|clean influencer]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__rec_trend_fashion_ootd_portrait|Trend recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추__rec_personalized_fashion_ootd_portrait|Personalized recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_trend_mirror_selfie_ootd|Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_personalized_mirror_selfie_ootd|Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_trend_window_light_cafe_portrait|Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_personalized_window_light_cafe_portrait|Personalized recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]]

## Incoming
- [[scene_nodes/scene__패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__scenario_fashion_ootd_portrait|패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__rec_trend_fashion_ootd_portrait|Trend recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추__rec_personalized_fashion_ootd_portrait|Personalized recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `USES_FACET`
- [[scene_nodes/scene__거울 셀카 OOTD — 몸 비율과 거울 반사 정리__scenario_mirror_selfie_ootd|거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_trend_mirror_selfie_ootd|Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_personalized_mirror_selfie_ootd|Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_FACET`
- [[scene_nodes/scene__카페 창가 인물 — 자연광_인플루언서 프로필__scenario_window_light_cafe_portrait|카페 창가 인물 — 자연광/인플루언서 프로필]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_trend_window_light_cafe_portrait|Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 카페 창가 인물 — 자연광_인플루언서 프로필__rec_personalized_window_light_cafe_portrait|Personalized recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필]] → `USES_FACET`
