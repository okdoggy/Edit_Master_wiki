---
title: "Scene-first Neo4j schema — camera recommendation graph"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "neo4j_scene_schema"
---

# Scene-first Neo4j schema — camera recommendation graph

## Labels

```cypher
:ImageObservation
:Scenario
:SceneFacet
:CompositionIssue
:TechnicalIssue
:Recommendation
:Technique
:Parameter
:Outcome
:Preference
:TrendSignal
:SatisfactionSignal
:Evidence
```

## Constraints

```cypher
CREATE CONSTRAINT image_observation_id IF NOT EXISTS FOR (n:ImageObservation) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT scenario_id IF NOT EXISTS FOR (n:Scenario) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT scene_facet_id IF NOT EXISTS FOR (n:SceneFacet) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT recommendation_id IF NOT EXISTS FOR (n:Recommendation) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT technique_id IF NOT EXISTS FOR (n:Technique) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT parameter_id IF NOT EXISTS FOR (n:Parameter) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT outcome_id IF NOT EXISTS FOR (n:Outcome) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT evidence_id IF NOT EXISTS FOR (n:Evidence) REQUIRE n.id IS UNIQUE;
```

## Core query path

```text
ImageObservation -> SceneFacet/Issue -> Recommendation -> Technique -> Parameter/Outcome -> Evidence
```

## Ranking fields

Recommendation nodes include:

- `channel`: `trend | general | personalized`
- `rank_score`: default ranking score
- `source_confidence`: official/reputable/creator/inferred evidence confidence
- `actionability`: how concrete the setting/slider/crop instructions are
- `risk_penalty`: likelihood of overediting, blur, distortion, privacy issue

## Personalization fields

Preference nodes include:

- `style_preference`: warm, cool, cinematic, natural, pastel, film
- `skin_retouch_strength`: none, subtle, strong
- `subject_priority`: face, body, outfit, background, food, place
- `device`: iPhone, Galaxy, Pixel
- `editing_tool`: Lightroom, Photos, Google Photos, Samsung Gallery
