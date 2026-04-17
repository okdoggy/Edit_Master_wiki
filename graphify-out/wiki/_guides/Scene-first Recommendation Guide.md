# Scene-first Recommendation Guide

서비스 추천 개발은 이 흐름을 기준으로 봅니다.

```text
User Korean Query -> QueryAlias -> Scenario -> Recommendation -> Technique/Parameter -> Natural Answer Renderer
```

- Neo4j: `graphify-out/cypher_scene_recommender.txt`
- Scene JSON: `graphify-out/scene_recommender_graph.json`
