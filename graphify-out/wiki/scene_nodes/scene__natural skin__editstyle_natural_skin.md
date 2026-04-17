# natural skin

- id: `editstyle_natural_skin`
- graph: scene-first
- labels: EditStyle, SceneFacet
- source_file: raw/scenarios/selfie_profile_portrait.md
- source_url: 

## Properties
- **id**: editstyle_natural_skin
- **key**: edit_style
- **value**: natural_skin
- **name**: natural skin
- **source_file**: raw/scenarios/selfie_profile_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Front Camera__camera_front_camera|Front Camera]]
- [[source_nodes/source__Natural Skin__edit_style_natural_skin|Natural Skin]]
- [[source_nodes/source__Selfie Or Portrait Selfie__mode_selfie_or_portrait_selfie|Selfie Or Portrait Selfie]]
- [[source_nodes/source__Selfie Person__subject_selfie_person|Selfie Person]]
- [[source_nodes/source__Pose__tok_pose|Pose]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__rec_trend_selfie_profile_portrait|Trend recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천__rec_personalized_selfie_profile_portrait|Personalized recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]]

## Incoming
- [[scene_nodes/scene__셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__scenario_selfie_profile_portrait|셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천 seed__rec_trend_selfie_profile_portrait|Trend recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 셀카_Profile — 왜곡 적고 자연스러운 얼굴 추천__rec_personalized_selfie_profile_portrait|Personalized recommendation — 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed]] → `USES_FACET`
