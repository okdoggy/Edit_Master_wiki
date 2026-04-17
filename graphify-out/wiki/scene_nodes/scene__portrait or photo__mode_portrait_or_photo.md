# portrait or photo

- id: `mode_portrait_or_photo`
- graph: scene-first
- labels: Mode, SceneFacet
- source_file: raw/scenarios/fashion_ootd_portrait.md
- source_url: 

## Properties
- **id**: mode_portrait_or_photo
- **key**: mode
- **value**: portrait_or_photo
- **name**: portrait or photo
- **source_file**: raw/scenarios/fashion_ootd_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Clean Influencer__edit_style_clean_influencer|Clean Influencer]]
- [[source_nodes/source__Outfit Color Priority__personal_signal_outfit_color_priority|Outfit Color Priority]]
- [[source_nodes/source__Fashion Outfit__subject_fashion_outfit|Fashion Outfit]]
- [[source_nodes/source__2x Lens__tok_2x_lens|2x Lens]]
- [[source_nodes/source__Body Alignment__tok_body_alignment|Body Alignment]]
- [[source_nodes/source__Body Distortion__tok_body_distortion|Body Distortion]]
- [[source_nodes/source__Grid__tok_grid|Grid]]
- [[source_nodes/source__Outfit Color__tok_outfit_color|Outfit Color]]
- [[source_nodes/source__Skin Tone Protection__tok_skin_tone_protection|Skin Tone Protection]]
- [[source_nodes/source__Portrait Or Photo__mode_portrait_or_photo|Portrait Or Photo]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천 seed__rec_general_autumn_maple_woman_portrait|General recommendation — 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]]
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 see__rec_general_fashion_ootd_portrait|General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]

## Incoming
- [[scene_nodes/scene__단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천 seed__scenario_autumn_maple_woman_portrait|단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]] → `USES_MODE`
- [[scene_nodes/scene__Example_ 단풍나무 아래 여성__obs_autumn_woman_maple|Example: 단풍나무 아래 여성]] → `OBSERVED_AS`
- [[scene_nodes/scene__General recommendation — 단풍나무 아래 여성 인물 — 트렌드_일반_개인화 추천 seed__rec_general_autumn_maple_woman_portrait|General recommendation — 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed]] → `USES_FACET`
- [[scene_nodes/scene__패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__scenario_fashion_ootd_portrait|패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `USES_MODE`
- [[scene_nodes/scene__General recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 see__rec_general_fashion_ootd_portrait|General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `USES_FACET`
