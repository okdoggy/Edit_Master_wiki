# 전신 셀카

- id: `alias_전신_셀카`
- graph: scene-first
- labels: QueryAlias
- source_file: raw/scenarios/mirror_selfie_ootd.md
- source_url: 

## 사용자 답변에서의 역할
사용자가 실제로 말할 법한 표현을 scenario에 연결합니다.

## Properties
- **id**: alias_전신_셀카
- **name**: 전신 셀카
- **language**: ko
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
- `MATCHES_SCENARIO` → [[scene_nodes/scene__거울 셀카 OOTD — 몸 비율과 거울 반사 정리__scenario_mirror_selfie_ootd|거울 셀카 OOTD — 몸 비율과 거울 반사 정리]]

## Incoming
- [[scene_nodes/scene__Korean scenario matching lexicon__scenario_matching_lexicon|Korean scenario matching lexicon]] → `DEFINES_ALIAS`
