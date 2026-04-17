# Scene-first Neo4j schema — camera recommendation graph

- id: `guide_scene_first_neo4j_schema`
- graph: scene-first
- labels: Evidence
- source_file: raw/recommendation/scene_first_neo4j_schema.md
- source_url: 

## 사용자 답변에서의 역할
추천/기법의 근거 출처입니다. 사용자에게는 근거 보기 영역에서 노출합니다.

## Properties
- **id**: guide_scene_first_neo4j_schema
- **name**: Scene-first Neo4j schema — camera recommendation graph
- **source_file**: raw/recommendation/scene_first_neo4j_schema.md
- **source_type**: derived_guide

## Source-oriented graph 연결
- [[source_nodes/source__Scene-first Neo4j schema — camera recommendation graph__doc_scene_first_neo4j_schema|Scene-first Neo4j schema — camera recommendation graph]]
- [[source_nodes/source__MATCH obs → facet _ issue → rec → tech → param → evidence__concept_neo4j_query_shape|MATCH obs → facet / issue → rec → tech → param → evidence]]

## Outgoing
- `REFERENCES` → [[scene_nodes/scene__Labels__guide_concept_scene_first_neo4j_schema_labels|Labels]]
- `REFERENCES` → [[scene_nodes/scene__Constraints__guide_concept_scene_first_neo4j_schema_constrain|Constraints]]
- `REFERENCES` → [[scene_nodes/scene__Core query path__guide_concept_scene_first_neo4j_schema_core_quer|Core query path]]
- `REFERENCES` → [[scene_nodes/scene__Ranking fields__guide_concept_scene_first_neo4j_schema_ranking_f|Ranking fields]]
- `REFERENCES` → [[scene_nodes/scene__Personalization fields__guide_concept_scene_first_neo4j_schema_personali|Personalization fields]]

## Incoming
