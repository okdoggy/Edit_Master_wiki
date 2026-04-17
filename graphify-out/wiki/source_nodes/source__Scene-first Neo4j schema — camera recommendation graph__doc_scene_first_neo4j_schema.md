# Scene-first Neo4j schema — camera recommendation graph

- id: `doc_scene_first_neo4j_schema`
- graph: source-oriented
- community: 7
- source_file: raw/recommendation/scene_first_neo4j_schema.md
- source_url: None

## Outgoing
- `references` → [[source_nodes/source__MATCH obs → facet _ issue → rec → tech → param → evidence__concept_neo4j_query_shape|MATCH obs → facet / issue → rec → tech → param → evidence]]
- `references` → [[source_nodes/source__Trend _ general _ personalized recommendation channels__concept_recommendation_channel_triad|Trend / general / personalized recommendation channels]]
- `references` → [[source_nodes/source__ImageObservation → SceneFacet → Recommendation → Technique →__concept_scene_first_pipeline|ImageObservation → SceneFacet → Recommendation → Technique → Parameter → Outcome → Evidence]]

## Incoming
- [[source_nodes/source__Smartphone Photography Raw Tips__doc_raw_readme|Smartphone Photography Raw Tips]] → `conceptually_related_to`
- [[source_nodes/source__User-query scene recommendation schema — image-first shootin__doc_user_query_scene_recommendation_schema|User-query scene recommendation schema — image-first shooting/editing recommender]] → `references`
