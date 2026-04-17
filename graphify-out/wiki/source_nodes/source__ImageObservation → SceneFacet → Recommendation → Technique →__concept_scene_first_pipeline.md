# ImageObservation → SceneFacet → Recommendation → Technique → Parameter → Outcome → Evidence

- id: `concept_scene_first_pipeline`
- graph: source-oriented
- community: 7
- source_file: raw/recommendation/user_query_scene_recommendation_schema.md
- source_url: None

## Outgoing
- `conceptually_related_to` → [[source_nodes/source__Natural coaching language instead of internal graph terms__concept_answer_renderer_contract|Natural coaching language instead of internal graph terms]]
- `conceptually_related_to` → [[source_nodes/source__Express numeric settings as starting values__answer_pattern_start_values|Express numeric settings as starting values]]
- `conceptually_related_to` → [[source_nodes/source__Start with one-line diagnosis__answer_pattern_one_line_diagnosis|Start with one-line diagnosis]]
- `conceptually_related_to` → [[source_nodes/source__Separate reshoot advice from editing advice__answer_pattern_shooting_vs_editing|Separate reshoot advice from editing advice]]

## Incoming
- [[source_nodes/source__User-query scene recommendation schema — image-first shootin__doc_user_query_scene_recommendation_schema|User-query scene recommendation schema — image-first shooting/editing recommender]] → `references`
- [[source_nodes/source__Korean scenario matching lexicon — scene query aliases__doc_scenario_matching_lexicon|Korean scenario matching lexicon — scene query aliases]] → `conceptually_related_to`
- [[source_nodes/source__Scene-first Neo4j schema — camera recommendation graph__doc_scene_first_neo4j_schema|Scene-first Neo4j schema — camera recommendation graph]] → `references`
- [[source_nodes/source__Scenario Corpus Index — graphify용 촬영_보정 상황 seed__doc_scenario_corpus_index|Scenario Corpus Index — graphify용 촬영/보정 상황 seed]] → `conceptually_related_to`
