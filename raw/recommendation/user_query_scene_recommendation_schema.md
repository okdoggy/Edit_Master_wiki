---
title: "User-query scene recommendation schema — image-first shooting/editing recommender"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "scene_first_recommendation_schema"
---

# User-query scene recommendation schema — image-first shooting/editing recommender

## 핵심 판단

현재 graphify 기본 그래프의 source/creator 중심 허브는 연구 자료 탐색에는 좋지만, 실제 사용자 쿼리에는 최단 경로가 길다. 사용자는 보통 “라이트룸”, “SNS 인플루언서”, “Austin Mann”을 말하지 않는다. 사용자는 이미지를 주고 이렇게 묻는다.

> “이 장면에서 구도와 밝기/노출/보정을 어떻게 하면 좋을까?”

따라서 추천 그래프의 중심은 `Source`가 아니라 **ImageObservation / SceneFacet / Recommendation**이어야 한다.

## 새 루트 모델

```text
ImageObservation
  → SceneFacet(subject, environment, light, composition, mood, issue)
  → Recommendation(trend / general / personalized)
  → Technique(capture / edit / composition)
  → Parameter(exposure, crop, lens, mask, slider)
  → Outcome(face clarity, skin tone, background separation, highlight preservation)
  → Evidence(source / creator / official doc)
```

## 노드 타입

| Node type | 역할 | 예시 |
|---|---|---|
| `ImageObservation` | 사용자가 올린 이미지에서 감지한 장면 | `obs_autumn_woman_maple` |
| `SceneFacet` | 이미지 분석 facet | `subject:woman`, `environment:autumn_maple_tree`, `light:backlight` |
| `CompositionIssue` | 구도 문제/개선 포인트 | `face_too_centered`, `busy_background`, `tilted_horizon` |
| `TechnicalIssue` | 노출/초점/색 문제 | `underexposed_face`, `blown_highlights`, `mixed_white_balance` |
| `Recommendation` | 추천 단위 | `trend_autumn_warm_foliage`, `general_portrait_2x_subject_mask` |
| `Technique` | 촬영/보정 기법 | `2x_portrait`, `subject_mask`, `sky_highlight_recovery` |
| `Parameter` | 수치/설정 | `EV -0.3~-0.7`, `Orange Sat +5~+18` |
| `Outcome` | 추천이 최적화하는 결과 | `natural_skin_tone`, `background_separation` |
| `Preference` | 개인화 취향 | `prefers_warm_tone`, `low_skin_retouch`, `likes_cinematic` |
| `TrendSignal` | 유행/시즌 신호 | `seasonal_fall_color`, `2026_authenticity` |
| `Evidence` | 근거 출처 | official docs, creator posts, magazine articles |

## 엣지 타입

| Edge | 의미 |
|---|---|
| `OBSERVED_AS` | ImageObservation → SceneFacet |
| `HAS_ISSUE` | ImageObservation → CompositionIssue/TechnicalIssue |
| `TRIGGERS` | SceneFacet/Issue → Recommendation |
| `HAS_RECOMMENDATION` | ImageObservation/Scenario → Recommendation |
| `USES_TECHNIQUE` | Recommendation → Technique |
| `SETS_PARAMETER` | Technique/Recommendation → Parameter |
| `OPTIMIZES` | Recommendation → Outcome |
| `AVOIDS` | Recommendation → Failure/Risk |
| `ADAPTS_TO` | Recommendation → Preference |
| `SUPPORTED_BY` | Recommendation/Technique → Evidence |
| `SIMILAR_TO` | Scene/Technique/Style 간 유사성 |

## 추천 채널 분리

### Trend recommendation

- `SceneFacet + TrendSignal`로 찾는다.
- 예: `environment:autumn_maple_tree` + `seasonal_fall_color` → warm foliage, leaf foreground, 4:5 crop.

### General recommendation

- `SceneFacet + Issue + Outcome`으로 찾는다.
- 예: `subject:woman` + `underexposed_face` → subject mask exposure +0.1~+0.3, 2x portrait.

### Personalized recommendation

- `SceneFacet + Preference + history`로 찾는다.
- 예: `prefers_cinematic` → warm foliage 기본값에서 shadows cool, grain +15~+30.

## “단풍나무 아래 여성” 예시

```cypher
(:ImageObservation {id:'obs_autumn_woman_maple'})
  -[:OBSERVED_AS]->(:SceneFacet {key:'subject', value:'woman'})
  -[:OBSERVED_AS]->(:SceneFacet {key:'environment', value:'autumn_maple_tree'})
  -[:OBSERVED_AS]->(:SceneFacet {key:'light', value:'golden_hour_or_backlight'})
  -[:HAS_ISSUE]->(:TechnicalIssue {value:'skin_tone_at_risk_from_warm_foliage'})
  -[:HAS_RECOMMENDATION]->(:Recommendation {channel:'trend', name:'warm foliage portrait'})
  -[:HAS_RECOMMENDATION]->(:Recommendation {channel:'general', name:'2x portrait + subject mask'})
  -[:HAS_RECOMMENDATION]->(:Recommendation {channel:'personalized', name:'adapt foliage warmth to user style'})
```

## 왜 기존 source 중심 그래프만으로 부족한가

- source/creator hub는 “누가 말했나”를 찾는 데 좋다.
- 사용자 쿼리에는 “무엇이 보이는가 / 무엇이 문제인가 / 어떤 결과를 원하는가”가 먼저 필요하다.
- 따라서 source는 핵심 경로의 뒤쪽 `SUPPORTED_BY`로 이동해야 한다.


## 5W1H 슬롯 라우팅 (언제/누가/어디서/무엇을/어떻게)

사용자 질의에서 다음 슬롯을 우선 추출해 scenario 검색 점수에 반영한다.

- 언제(`when`): 아침/낮/밤/계절
- 누가(`who`): iPhone/Galaxy/Pixel, Lightroom/Photoshop
- 어디서(`where`): 실내/야외/카페/거리/해변/미술관
- 무엇을(`what`): 인스타 업로드, 유행 스타일, 별 촬영, 제품 사진
- 어떻게(`how`): 2x 줌, Pro mode, ISO/셔터/EV

권장 검색 순서:

```text
slot match (where+what+how)
→ language-normalized alias match (KR/EN)
→ issue adjustment
→ recommendation ranking
```

## Neo4j query shape

```cypher
MATCH (obs:ImageObservation {id:$image_id})-[:OBSERVED_AS|HAS_ISSUE]->(facet)
MATCH (facet)-[:TRIGGERS]->(rec:Recommendation)
OPTIONAL MATCH (rec)-[:USES_TECHNIQUE]->(tech)-[:SETS_PARAMETER]->(param)
OPTIONAL MATCH (rec)-[:OPTIMIZES]->(outcome)
OPTIONAL MATCH (rec)-[:SUPPORTED_BY]->(evidence)
RETURN rec, collect(tech), collect(param), collect(outcome), collect(evidence)
ORDER BY rec.rank_score DESC
```

## 출처와 관계

공식 문서/작가/매거진 자료는 이제 추천의 시작점이 아니라 근거다.

```text
Recommendation -[:SUPPORTED_BY]-> Evidence
Technique -[:SUPPORTED_BY]-> Evidence
```
