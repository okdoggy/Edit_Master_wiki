# 전체 색온도와 피부색을 우선 맞춘 뒤 프리셋 적용.

- id: `param_group_travel_selfie_전체_색온도와_피부색을_우선_맞춘_뒤_프리셋_적용.`
- graph: scene-first
- labels: Parameter
- source_file: raw/scenarios/group_travel_selfie.md
- source_url: 

## Properties
- **id**: param_group_travel_selfie_전체_색온도와_피부색을_우선_맞춘_뒤_프리셋_적용.
- **name**: 전체 색온도와 피부색을 우선 맞춘 뒤 프리셋 적용.
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

## Incoming
- [[scene_nodes/scene__Trend recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_trend_group_travel_selfie|Trend recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]] → `SETS_PARAMETER`
- [[scene_nodes/scene__General recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_general_group_travel_selfie|General recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]] → `SETS_PARAMETER`
- [[scene_nodes/scene__Personalized recommendation — 단체 여행 셀피_그룹샷 — 얼굴 왜곡 줄이기__rec_personalized_group_travel_selfie|Personalized recommendation — 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기]] → `SETS_PARAMETER`
