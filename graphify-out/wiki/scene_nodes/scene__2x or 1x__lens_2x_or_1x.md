# 2x or 1x

- id: `lens_2x_or_1x`
- graph: scene-first
- labels: Lens, SceneFacet
- source_file: raw/scenarios/fashion_ootd_portrait.md
- source_url: 

## Properties
- **id**: lens_2x_or_1x
- **key**: lens
- **value**: 2x_or_1x
- **name**: 2x or 1x
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

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 see__rec_general_fashion_ootd_portrait|General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]]

## Incoming
- [[scene_nodes/scene__패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed__scenario_fashion_ootd_portrait|패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `USES_LENS`
- [[scene_nodes/scene__General recommendation — 패션_OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 see__rec_general_fashion_ootd_portrait|General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed]] → `USES_FACET`
