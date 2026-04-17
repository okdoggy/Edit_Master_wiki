# mirror indoor

- id: `environment_mirror_indoor`
- graph: scene-first
- labels: Environment, SceneFacet
- source_file: raw/scenarios/mirror_selfie_ootd.md
- source_url: 

## Properties
- **id**: environment_mirror_indoor
- **key**: environment
- **value**: mirror_indoor
- **name**: mirror indoor
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
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_trend_mirror_selfie_ootd|Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_general_mirror_selfie_ootd|General recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_personalized_mirror_selfie_ootd|Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]

## Incoming
- [[scene_nodes/scene__거울 셀카 OOTD — 몸 비율과 거울 반사 정리__scenario_mirror_selfie_ootd|거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `HAS_ENVIRONMENT`
- [[scene_nodes/scene__Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_trend_mirror_selfie_ootd|Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_general_mirror_selfie_ootd|General recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_personalized_mirror_selfie_ootd|Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_FACET`
