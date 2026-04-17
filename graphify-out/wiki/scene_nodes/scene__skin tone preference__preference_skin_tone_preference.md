# skin tone preference

- id: `preference_skin_tone_preference`
- graph: scene-first
- labels: Preference, SceneFacet
- source_file: raw/scenarios/autumn_maple_woman_portrait.md
- source_url: 

## Properties
- **id**: preference_skin_tone_preference
- **key**: personal_signal
- **value**: skin_tone_preference
- **name**: skin tone preference
- **source_file**: raw/scenarios/autumn_maple_woman_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Warm Foliage__edit_style_warm_foliage|Warm Foliage]]
- [[source_nodes/source__Autumn Maple Tree__environment_autumn_maple_tree|Autumn Maple Tree]]
- [[source_nodes/source__2x 3x Portrait__lens_2x_3x_portrait|2x 3x Portrait]]
- [[source_nodes/source__Golden Hour Or Backlight__light_golden_hour_or_backlight|Golden Hour Or Backlight]]
- [[source_nodes/source__Portrait Or Photo__mode_portrait_or_photo|Portrait Or Photo]]
- [[source_nodes/source__Skin Tone Preference__personal_signal_skin_tone_preference|Skin Tone Preference]]
- [[source_nodes/source__Clear Face Warm Background__satisfaction_signal_clear_face_warm_background|Clear Face Warm Background]]
- [[source_nodes/source__Woman__subject_woman|Woman]]
- [[source_nodes/source__2x__tok_2x|2x]]
- [[source_nodes/source__2x 3x__tok_2x_3x|2x 3x]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천__rec_personalized_autumn_maple_woman_portrait|Personalized recommendation — 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]]

## Incoming
- [[scene_nodes/scene__단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천 seed__scenario_autumn_maple_woman_portrait|단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]] → `HAS_PERSONALIZATION_SIGNAL`
- [[scene_nodes/scene__Example_ 단풍나무 아래 여성__obs_autumn_woman_maple|Example: 단풍나무 아래 여성]] → `OBSERVED_AS`
- [[scene_nodes/scene__Personalized recommendation — 단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천__rec_personalized_autumn_maple_woman_portrait|Personalized recommendation — 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]] → `USES_FACET`
