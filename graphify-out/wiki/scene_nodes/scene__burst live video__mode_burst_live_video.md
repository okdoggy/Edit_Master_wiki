# burst live video

- id: `mode_burst_live_video`
- graph: scene-first
- labels: Mode, SceneFacet
- source_file: raw/scenarios/pets_children_action.md
- source_url: 

## Properties
- **id**: mode_burst_live_video
- **key**: mode
- **value**: burst_live_video
- **name**: burst live video
- **source_file**: raw/scenarios/pets_children_action.md

## Source-oriented graph 연결
- [[source_nodes/source__Clear Action__edit_style_clear_action|Clear Action]]
- [[source_nodes/source__Burst Live Video__mode_burst_live_video|Burst Live Video]]
- [[source_nodes/source__Kids Or Pets__subject_kids_or_pets|Kids Or Pets]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 아이·반려동물 액션 — 순간 포착_연사_짧은 영상__rec_general_pets_children_action|General recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상]]

## Incoming
- [[scene_nodes/scene__아이·반려동물 액션 — 순간 포착_연사_짧은 영상__scenario_pets_children_action|아이·반려동물 액션 — 순간 포착/연사/짧은 영상]] → `USES_MODE`
- [[scene_nodes/scene__General recommendation — 아이·반려동물 액션 — 순간 포착_연사_짧은 영상__rec_general_pets_children_action|General recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상]] → `USES_FACET`
