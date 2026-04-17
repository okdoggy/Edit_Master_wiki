# Graphify recommendation schema

- id: `graphify_recommendation_schema`
- graph: source-oriented
- community: 6
- source_file: raw/recommendation/graphify_recommendation_schema.md
- source_url: None

## Outgoing
- `references` → [[source_nodes/source__Scenario Node__scenario_node|Scenario Node]]
- `references` → [[source_nodes/source__Trend Signal Node__trend_signal_node|Trend Signal Node]]
- `references` → [[source_nodes/source__Personalization Signal Node__personalization_signal_node|Personalization Signal Node]]
- `references` → [[source_nodes/source__Satisfaction Signal Node__satisfaction_signal_node|Satisfaction Signal Node]]
- `references` → [[source_nodes/source__Edit Style Node__edit_style_node|Edit Style Node]]
- `references` → [[source_nodes/source__Technique Node__technique_node|Technique Node]]
- `references` → [[source_nodes/source__Subject Facet__subject_facet|Subject Facet]]
- `references` → [[source_nodes/source__Environment Facet__environment_facet|Environment Facet]]
- `references` → [[source_nodes/source__Light Facet__light_facet|Light Facet]]
- `references` → [[source_nodes/source__Capture Facet__capture_facet|Capture Facet]]
- `references` → [[source_nodes/source__Edit Facet__edit_facet|Edit Facet]]
- `references` → [[source_nodes/source__Recommendation Signal Facet__recommendation_signal_facet|Recommendation Signal Facet]]
- `has_trend_signal` → [[source_nodes/source__Warm Foliage and Leaf Foreground__warm_foliage_leaf_foreground|Warm Foliage and Leaf Foreground]]
- `has_trend_signal` → [[source_nodes/source__Film Grain and Cinematic Style__film_grain_cinematic_style|Film Grain and Cinematic Style]]
- `matches_user_pref` → [[source_nodes/source__Moody Cinematic Style__moody_cinematic_style|Moody Cinematic Style]]
- `matches_user_pref` → [[source_nodes/source__Bright Natural Style__bright_natural_style|Bright Natural Style]]
- `rationale_for` → [[source_nodes/source__Subject-Background Separation__subject_background_separation|Subject-Background Separation]]

## Incoming
- [[source_nodes/source__Photo metadata standards mapping__metadata_standards_mapping|Photo metadata standards mapping]] → `references`
