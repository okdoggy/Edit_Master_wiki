# 0.5x 1x front

- id: `lens_0.5x_1x_front`
- graph: scene-first
- labels: Lens, SceneFacet
- source_file: raw/scenarios/group_travel_selfie.md
- source_url: 

## Properties
- **id**: lens_0.5x_1x_front
- **key**: lens
- **value**: 0.5x_1x_front
- **name**: 0.5x 1x front
- **source_file**: raw/scenarios/group_travel_selfie.md

## Source-oriented graph 연결
- [[source_nodes/source__0.5x 1x Front__lens_0_5x_1x_front|0.5x 1x Front]]
- [[source_nodes/source__Selfie Or Timer__mode_selfie_or_timer|Selfie Or Timer]]
- [[source_nodes/source__Group__subject_group|Group]]
- [[source_nodes/source__Edge Distortion__tok_edge_distortion|Edge Distortion]]
- [[source_nodes/source__Face__tok_face|Face]]
- [[source_nodes/source__Faces__tok_faces|Faces]]
- [[source_nodes/source__Group__tok_group|Group]]
- [[source_nodes/source__Landmark Context__tok_landmark_context|Landmark Context]]
- [[source_nodes/source__Stability__tok_stability|Stability]]
- [[source_nodes/source__Story__tok_story|Story]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_general_group_travel_selfie|General recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]]

## Incoming
- [[scene_nodes/scene__단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__scenario_group_travel_selfie|단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]] → `USES_LENS`
- [[scene_nodes/scene__General recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_general_group_travel_selfie|General recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]] → `USES_FACET`
