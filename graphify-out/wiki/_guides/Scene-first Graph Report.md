# Scene-first Recommender Graph Report v2

Generated: 2026-04-17

## What changed from v1

- Added `QueryAlias` nodes so Korean user phrasing can match scenarios directly.
- Added `AnswerRenderer` and `AnswerPattern` nodes so graph output can be rendered as natural photo-coach language.
- Added 10 more practical scenarios: dim restaurant food, cafe flatlay, city window reflection, harsh noon beach portrait, museum portrait, indoor party group, crowded landmark portrait, product listing, mirror selfie OOTD, cafe drink/dessert closeup.

## Stats

- Nodes: 989
- Edges: 2796
- Scenario files parsed: 30
- QueryAlias nodes: 58
- AnswerPattern nodes: 10
- Neo4j Cypher: `graphify-out/cypher_scene_recommender.txt`
- Scene wiki: `graphify-out/obsidian_scene/`

## Primary query path

```text
User Korean Query -> QueryAlias -> Scenario -> Recommendation -> Technique/Parameter -> Natural Answer Renderer
```

## Node counts

- AnswerPattern: 10
- AnswerRenderer: 1
- Camera: 2
- Composition: 3
- CompositionIssue: 8
- EditStyle: 20
- Environment: 26
- Evidence: 56
- ImageObservation: 1
- Lens: 16
- Light: 20
- MatchingLexicon: 1
- Mode: 15
- Motion: 1
- Outcome: 7
- Parameter: 154
- Preference: 9
- Prop: 1
- QueryAlias: 58
- QueryAliasRule: 4
- Recommendation: 90
- Risk: 82
- SatisfactionSignal: 2
- Scenario: 30
- SceneFacet: 160
- Subject: 21
- TechnicalIssue: 8
- Technique: 333
- TrendSignal: 17


## External evidence augmentation

- Added external source URL evidence nodes from scenario files.
- New total nodes: 1049
- New total edges: 3532
- Evidence nodes: 116
- External evidence edges added/checked: 184
