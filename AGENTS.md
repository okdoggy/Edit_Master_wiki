# AGENTS.md — Edit_Master_wiki Project Guidance

## Project purpose

This project builds a smartphone photography/editing knowledge wiki for **trend-aware and personalization-aware recommendations**.

The wiki is not primarily a generic “photo problem troubleshooting FAQ.” Its main purpose is to organize:

1. **Trend signals** — current/seasonal/platform photo and editing styles.
2. **Personalization signals** — user taste, preferred mood, edit strength, and style variants.
3. **Style recipes** — reusable shooting/editing looks such as warm foliage, cinematic night, clean influencer, food glow, film nostalgia.
4. **Scenarios** — user-facing image situations where trends and personal preferences can be applied.
5. **Evidence** — official docs, expert/tutorial sources, creator/community references that support recommendations.

## Core graph direction

Use this as the primary conceptual path:

```text
TrendSignal + UserPreference
→ EditStyle / StyleRecipe
→ Scenario
→ RecommendationVariant
→ Technique / Parameter
→ Evidence
```

A user query may start from an image scene, but the wiki should ultimately help decide **which trend/style/personalized variant** fits that scene.

## Role of image issues

Image problems such as underexposed face, blown highlights, tilted horizon, mixed white balance, motion blur, or busy background are important, but they are **modifiers/guardrails**, not the main organizing axis.

Use issues like this:

```text
ImageIssue
→ adjusts / constrains
RecommendationVariant / Parameter
```

Do **not** let the graph become primarily issue-centered:

```text
underexposed_face → all recommendations  # avoid as main architecture
```

Prefer:

```text
Scenario + TrendSignal + Preference
→ RecommendationVariant
→ if issue exists, adjust parameters safely
```

## Recommended node priorities

### Core nodes

- `TrendSignal`
- `Preference` / `PersonalizationSignal`
- `EditStyle`
- `StyleRecipe`
- `Scenario`
- `RecommendationVariant`
- `Evidence`

### Supporting nodes

- `Technique`
- `Parameter`
- `Outcome`
- `Platform`
- `Season`
- `Device`
- `LensMode`

### Modifier nodes

- `ImageIssue`
- `Risk`
- `Constraint`

## Scenario guidance

Scenarios should not be mere combinations of existing raw notes. When adding or revising scenario files under `raw/scenarios/`, ground them in at least one of:

- official vendor documentation,
- professional photography/tutorial sources,
- recognized creators/influencers,
- community discussions with practical consensus.

Each scenario should connect to trend and personalization concepts, not just a problem/solution pair.

Good scenario structure:

```text
Scenario
→ supports TrendSignal
→ supports EditStyle
→ has RecommendationVariant
→ supported_by Evidence
→ optionally adjusted_by ImageIssue
```

## Trend and personalization indexes

When expanding the wiki, prioritize these indexes and relationships:

- trend signal index: current/seasonal/platform styles and their visual traits;
- personalization preference index: warm, natural, cinematic, low-retouch, bright-airy, film-grain, food-texture, travel-storytelling, etc.;
- style recipe index: concrete Lightroom/camera recipes that convert trend/preference into parameters;
- scenario-to-style mappings: which styles work for each situation.

## Answering user-facing queries

When rendering graph output to a user, answer naturally as a photo coach. Do not expose internal graph labels unless debugging.

Preferred user answer shape:

```text
1. One-line diagnosis
2. If reshooting: lens / light / composition advice
3. If editing: exposure / mask / color / crop advice
4. Style variants: trend / general / personalized
5. Optional evidence summary
```

Avoid raw graph phrasing such as `SceneFacet`, `TrendSignal`, `confidence_score`, or repeated node labels in the user-facing answer.

## Current wiki organization

Use a single Obsidian vault:

```text
graphify-out/wiki/
```

Archived legacy vaults may exist under:

```text
graphify-out/_archive/
```

The service-oriented graph should prefer the scene-first / trend-personalization model. Neo4j imports should use the current scene-first Cypher unless explicitly doing source-only research:

```text
graphify-out/cypher_scene_recommender.txt
graphify-out/cypher.txt
```

