# warm low light

- id: `light_warm_low_light`
- graph: scene-first
- labels: Light, SceneFacet
- source_file: raw/scenarios/indoor_party_group.md
- source_url: 

## Properties
- **id**: light_warm_low_light
- **key**: light
- **value**: warm_low_light
- **name**: warm low light
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
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_trend_indoor_party_group|Trend recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_general_indoor_party_group|General recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]]

## Incoming
- [[scene_nodes/scene__실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__scenario_indoor_party_group|실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]] → `HAS_LIGHT`
- [[scene_nodes/scene__Trend recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_trend_indoor_party_group|Trend recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]] → `USES_FACET`
- [[scene_nodes/scene__General recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임__rec_general_indoor_party_group|General recommendation — 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임]] → `USES_FACET`
