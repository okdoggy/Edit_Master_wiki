# Graphify 추천 연결 스키마 — 스마트폰 촬영/보정

- id: `guide_graphify_recommendation_schema`
- graph: scene-first
- labels: Evidence
- source_file: raw/recommendation/graphify_recommendation_schema.md
- source_url: 

## 사용자 답변에서의 역할
추천/기법의 근거 출처입니다. 사용자에게는 근거 보기 영역에서 노출합니다.

## Properties
- **id**: guide_graphify_recommendation_schema
- **name**: Graphify 추천 연결 스키마 — 스마트폰 촬영/보정
- **source_file**: raw/recommendation/graphify_recommendation_schema.md
- **source_type**: derived_guide

## Source-oriented graph 연결
- [[source_nodes/source__Graphify recommendation schema__graphify_recommendation_schema|Graphify recommendation schema]]
- [[source_nodes/source__Scenario Node__scenario_node|Scenario Node]]
- [[source_nodes/source__Trend Signal Node__trend_signal_node|Trend Signal Node]]
- [[source_nodes/source__Personalization Signal Node__personalization_signal_node|Personalization Signal Node]]
- [[source_nodes/source__Satisfaction Signal Node__satisfaction_signal_node|Satisfaction Signal Node]]
- [[source_nodes/source__Edit Style Node__edit_style_node|Edit Style Node]]
- [[source_nodes/source__Technique Node__technique_node|Technique Node]]
- [[source_nodes/source__Subject Facet__subject_facet|Subject Facet]]
- [[source_nodes/source__Environment Facet__environment_facet|Environment Facet]]
- [[source_nodes/source__Light Facet__light_facet|Light Facet]]

## Outgoing
- `REFERENCES` → [[scene_nodes/scene__추천 타입 3종__guide_concept_graphify_recommendation_schema_추천|추천 타입 3종]]
- `REFERENCES` → [[scene_nodes/scene__1. 트렌드 추천__guide_concept_graphify_recommendation_schema_1_트|1. 트렌드 추천]]
- `REFERENCES` → [[scene_nodes/scene__2. 일반 추천__guide_concept_graphify_recommendation_schema_2_일|2. 일반 추천]]
- `REFERENCES` → [[scene_nodes/scene__3. 개인화 추천__guide_concept_graphify_recommendation_schema_3_개|3. 개인화 추천]]
- `REFERENCES` → [[scene_nodes/scene__Graphify node taxonomy__guide_concept_graphify_recommendation_schema_gra|Graphify node taxonomy]]
- `REFERENCES` → [[scene_nodes/scene__Edge patterns__guide_concept_graphify_recommendation_schema_edg|Edge patterns]]
- `REFERENCES` → [[scene_nodes/scene__단풍나무 아래 여성 예시__guide_concept_graphify_recommendation_schema_단풍나|단풍나무 아래 여성 예시]]
- `REFERENCES` → [[scene_nodes/scene__추천 랭킹에 쓸 수 있는 점수 후보__guide_concept_graphify_recommendation_schema_추천|추천 랭킹에 쓸 수 있는 점수 후보]]
- `REFERENCES` → [[scene_nodes/scene__표준 메타데이터 연결__guide_concept_graphify_recommendation_schema_표준|표준 메타데이터 연결]]

## Incoming
