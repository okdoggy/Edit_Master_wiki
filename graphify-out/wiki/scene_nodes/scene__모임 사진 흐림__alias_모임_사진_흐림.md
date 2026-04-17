# 모임 사진 흐림

- id: `alias_모임_사진_흐림`
- graph: scene-first
- labels: QueryAlias
- source_file: raw/scenarios/indoor_party_group.md
- source_url: 

## 사용자 답변에서의 역할
사용자가 실제로 말할 법한 표현을 scenario에 연결합니다.

## Properties
- **id**: alias_모임_사진_흐림
- **name**: 모임 사진 흐림
- **language**: ko
- **source_file**: raw/scenarios/indoor_party_group.md

## Source-oriented graph 연결
- [[source_nodes/source__motion blur__issue_motion_blur|motion blur]]
- [[source_nodes/source__warm documentary party mood__trend_warm_documentary_party|warm documentary party mood]]
- [[source_nodes/source__documentary__pref_documentary|documentary]]
- [[source_nodes/source__clean group shot__pref_clean_group|clean group shot]]
- [[source_nodes/source__party mood__outcome_party_mood|party mood]]
- [[source_nodes/source__timer _ burst__tech_timer_or_burst|timer / burst]]
- [[source_nodes/source__keep faces on the same plane__tech_same_plane_faces|keep faces on the same plane]]
- [[source_nodes/source__Noise Reduction +15 to +35__param_noise_reduction_plus_15_to_35|Noise Reduction +15 to +35]]
- [[source_nodes/source__Warm temperature, controlled__param_temp_warm_controlled|Warm temperature, controlled]]
- [[source_nodes/source__Google Pixel group photo features__evidence_google_pixel_group_photo_features|Google Pixel group photo features]]

## Outgoing
- `MATCHES_SCENARIO` → [[scene_nodes/scene__실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__scenario_indoor_party_group|실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]

## Incoming
- [[scene_nodes/scene__Korean scenario matching lexicon__scenario_matching_lexicon|Korean scenario matching lexicon]] → `DEFINES_ALIAS`
