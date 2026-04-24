---
title: "Agent runtime pipeline — scene matcher, personalization, and evaluation"
category: "recommendation"
updated_at: "2026-04-24"
content_type: "agent_runtime_pipeline"
---

# Agent runtime pipeline — scene matcher, personalization, and evaluation

## 현재 실행 경로

```text
User query / image observation
→ normalize slots
→ ScenarioMatcher top-k
→ graph recommendations
→ personalization reranking
→ natural answer renderer
→ feedback event
→ user preference profile
```

## 추가된 런타임 코드

- Scenario matcher: `scripts/recommender/scenario_matcher.py`
- Token/slot normalization: `scripts/recommender/normalization.py`
- Graph loader: `scripts/recommender/graph_loader.py`
- Personalization profile: `scripts/recommender/personalization.py`
- Image facet adapter: `scripts/recommender/image_facets.py`
- Matcher evaluation: `scripts/evaluate_scene_matcher.py`
- Asset validation pipeline: `scripts/agent_pipeline.py`

## 검증 명령

```powershell
& 'C:\Users\swss2\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\agent_pipeline.py
```

또는 상세 JSON:

```powershell
& 'C:\Users\swss2\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\agent_pipeline.py --json
```

## 평가셋

`tests/eval_queries.json`은 실제 사용자처럼 묻는 한국어 질의 10개를 기준으로 한다.

현재 중점 회귀 케이스:

- 어두운 레스토랑 음식이 시장 음식 스토리로 잘못 붙지 않아야 한다.
- 카페 플랫레이가 시장 음식 스토리로 잘못 붙지 않아야 한다.
- 도시 유리창 야경 반사가 일반 창의적 반사 컷으로 너무 쉽게 흘러가지 않아야 한다.

## 아직 남은 작업

- graphify build/export 자체를 재현하는 명령은 저장소에 없다. graphify 실행 방식이 확정되면 `scripts/agent_pipeline.py` 앞단에 `build-graph` 단계를 추가한다.
- 실제 이미지 분석 모델은 아직 연결하지 않았다. `image_facets.py` 계약에 맞춰 외부 vision output을 넣으면 matcher와 연결할 수 있다.
- 자연어 답변 렌더러는 문서 계약이 먼저 있으며, 다음 단계에서 코드화한다.

