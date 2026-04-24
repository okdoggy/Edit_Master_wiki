# Edit Master Wiki

현재 버전: `0.2`

스마트폰 촬영과 사진 편집을 전문가처럼 가이드하는 Learnable Agent를 만들기 위한 지식 기반 프로젝트입니다.

이 저장소의 핵심 흐름은 다음과 같습니다.

```text
raw 자료 수집/정제
-> graphify wiki/graph 생성
-> scene-first matcher와 추천 런타임
-> 사용자 질의/이미지 관찰 기반 답변
-> 사용자 피드백으로 개인화
```

## 0. Harness Quickstart

이제 사용자는 개별 Python 스크립트를 직접 실행하기보다 `uv run edit-master ...` 하네스를 사용합니다. Python 코드는 내부 런타임으로 유지하고, 운영 표면은 하나의 CLI로 묶었습니다.

```powershell
uv sync
uv run edit-master doctor
uv run edit-master validate
```

전체 재생성 루프를 한 번에 돌릴 때:

```powershell
uv run edit-master all
```

주요 명령:

- `uv run edit-master doctor`: uv/Python/graphify 의존성과 필수 파일 확인
- `uv run edit-master build`: `raw/`에서 `graphify-out/` 재생성
- `uv run edit-master bridge --write`: source graph와 recommender graph 연결 리포트 생성
- `uv run edit-master validate`: raw/graph/bridge/learning/eval/답변 품질 스모크 검증
- `uv run edit-master eval`: matcher 회귀 평가
- `uv run edit-master answer "질문"`: 자연어 photo-coach 답변 생성
- `uv run edit-master feedback record/show/rebuild`: 개인화 피드백 기록과 프로필 관리

## 핵심 방향

이 프로젝트는 단순한 사진 문제 해결 FAQ가 아니라, 장면과 취향에 맞춰 촬영법과 편집법을 추천하는 지식 그래프를 목표로 합니다.

중심 경로는 다음과 같습니다.

```text
TrendSignal + UserPreference
-> EditStyle / StyleRecipe
-> Scenario
-> RecommendationVariant
-> Technique / Parameter
-> Evidence
```

`underexposed_face`, `busy_background`, `motion_blur` 같은 이미지 이슈는 중요하지만, 추천의 중심축이 아니라 파라미터를 조정하는 guardrail로 다룹니다.

## 1. Raw 자료를 추가할 때

새 자료를 추가할 때는 "자료를 많이 넣기"보다 "Agent가 추천에 쓸 수 있는 단위로 정제하기"가 중요합니다.

시나리오 파일은 보통 `raw/scenarios/` 아래에 추가하며, 최소한 아래 frontmatter를 갖추는 것을 권장합니다.

```yaml
title: "카페 창가 인물 - 자연광/인플루언서 프로필"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
scenario_tags:
aliases:
graph_nodes:
graph_edges:
urls:
```

특히 중요한 필드:

- `aliases`: 실제 사용자가 말할 표현. 예: "얼굴 한쪽 어두움", "카페 프로필", "cafe window portrait"
- `graph_nodes`: subject, environment, light, lens, edit_style, risk, preference 등
- `graph_edges`: 추천 논리. 예: `window_light SOFTENS_skin`
- `urls`: 공식 문서, 전문 튜토리얼, creator/community 근거
- 본문: 상황, 촬영법, 보정법, 주의점, 근거

현재는 hourly 자동 수집을 사용하지 않습니다. 새 raw는 사람이 검수한 뒤 `raw/scenarios/`, `raw/trends/`, `raw/techniques/`, `raw/lightroom/`, `raw/magazine/`, `raw/sns/`, `raw/youtube/`처럼 목적이 분명한 폴더에 직접 추가합니다.

검증:

```powershell
uv run edit-master validate
```

## 2. Wiki/Graph를 만들 때

단순히 `graphify wiki`만 실행하면 사람이 탐색하기 좋은 wiki는 만들 수 있지만, Agent 추천용 graph로는 부족할 수 있습니다.

이 저장소에서는 설치한 `graphifyy` 패키지를 `scripts/run_graphify_raw.py`가 호출해 source 중심 graph/wiki를 재생성합니다. `graphify`의 build, cluster, report, HTML, Cypher, Obsidian export API를 사용합니다.

```powershell
uv run edit-master build
```

재생성 대상:

- `graphify-out/graph.json`
- `graphify-out/graph.html`
- `graphify-out/cypher.txt`
- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/wiki/`

Source graph와 추천 graph의 연결 상태는 bridge 스크립트로 확인합니다.

```powershell
uv run edit-master bridge --write
```

생성/검증 대상:

- `graphify-out/source_recommender_bridge.json`
- `graphify-out/SOURCE_RECOMMENDER_BRIDGE_REPORT.md`

이 bridge는 `source_file` 기준으로 `graphify-out/graph.json`의 source/evidence 노드와 `graphify-out/scene_recommender_graph.json`의 Scenario/Recommendation을 연결합니다. raw가 늘어났을 때는 이 coverage가 깨지지 않는지 먼저 봅니다.

현재 산출물은 두 성격으로 나뉩니다.

- Source 중심 그래프: `graphify-out/graph.json`, `graphify-out/cypher.txt`
- 추천 중심 그래프: `graphify-out/scene_recommender_graph.json`, `graphify-out/cypher_scene_recommender.txt`

Agent에는 추천 중심의 scene-first graph가 더 중요합니다.

```text
User Query
-> QueryAlias
-> Scenario
-> Recommendation
-> Technique / Parameter
-> Evidence
```

스키마는 매번 바꿀 필요가 없습니다. 기존 노드 타입으로 표현 가능하면 raw 문서를 잘 쓰는 쪽이 우선입니다.

스키마를 바꿔야 하는 경우:

- 새 노드 타입이 필요할 때: `ImageObservation`, `UserPreferenceProfile`, `SatisfactionSignal`
- 새 edge 의미가 필요할 때: `ADJUSTS_PARAMETER`, `LEARNED_FROM`, `RERANKS`
- 개인화 결과나 이미지 분석 결과를 Neo4j에 실제 저장하려는 경우

관련 문서:

- `raw/recommendation/scene_first_neo4j_schema.md`
- `raw/recommendation/agent_runtime_pipeline.md`
- `raw/recommendation/personalization_learning_schema.md`
- `raw/recommendation/image_facet_extraction_contract.md`

## 3. Wiki/Graph에 쿼리할 때

서비스나 Agent 관점에서는 wiki에 직접 쿼리하기보다 `edit-master` 하네스가 감싼 런타임을 거치는 방식이 안정적입니다.

권장 흐름:

```text
사용자 질문/이미지 설명
-> query normalization
-> ScenarioMatcher Top-K
-> graph recommendation 조회
-> personalization reranking
-> natural answer renderer
```

시나리오 매칭 품질 평가:

```powershell
uv run edit-master eval --min-top1 1.0
```

자연어 답변 생성 예시:

```powershell
uv run edit-master answer "카페 창가에서 인물 사진을 찍었는데 얼굴 한쪽이 어둡고 배경이 지저분해요"
```

Client가 이미지 분석 결과를 이미 만든 경우에는 JSON facet을 함께 넘길 수 있습니다. 이 저장소는 이미지 분석 모델을 직접 수행하지 않고, Client가 보낸 `subject/environment/light/issues/preferences` 같은 분석 결과를 추천 쿼리에 합치는 계약만 유지합니다.

```powershell
uv run edit-master answer "자연스럽게 보정하고 싶어요" --observation-json .\client_observation.json
```

현재 주요 런타임/하네스 코드:

- `edit_master/cli.py`
- `edit_master/config.py`
- `edit-master.toml`
- `scripts/recommender/scenario_matcher.py`
- `scripts/recommender/normalization.py`
- `scripts/recommender/graph_loader.py`
- `scripts/recommender/source_bridge.py`
- `scripts/recommender/answer_renderer.py`
- `scripts/recommender/personalization.py`
- `scripts/recommender/learning_loop.py`
- `scripts/recommender/image_facets.py`
- `scripts/evaluate_scene_matcher.py`
- `scripts/agent_pipeline.py`

## 4. 개인화 학습 루프

개인화는 사용자가 고른 답변, 저장한 답변, 거절한 답변, 다시 보정한 흔적을 작은 피드백 이벤트로 저장하고 `UserPreferenceProfile`을 갱신하는 방식으로 동작합니다. 원본 이미지나 전체 대화문을 저장하지 않고, 이벤트 로그와 프로필만 `data/personalization/` 아래에 저장합니다. 이 폴더는 로컬 메모리라서 git에는 올라가지 않습니다.

기본 흐름:

```text
Client feedback
-> FeedbackEvent
-> data/personalization/{user}.events.jsonl
-> UserPreferenceProfile 갱신
-> 다음 answer_renderer 호출 때 추천 순위와 파라미터 힌트에 반영
```

피드백 기록 예시:

```powershell
uv run edit-master feedback --memory-dir data\personalization\local --user-id local record --query "카페 창가에서 인물 사진을 찍었는데 얼굴 한쪽이 어둡고 배경이 지저분해요" --action accepted --channel personalized --style-tags natural clean low_retouch --issue-tags busy_background --note "자연스럽고 낮은 피부 보정 선호"
```

현재 프로필 확인:

```powershell
uv run edit-master feedback --memory-dir data\personalization\local --user-id local show
```

학습된 프로필을 적용해 답변 생성:

```powershell
uv run edit-master feedback --memory-dir data\personalization\local --user-id local render "카페 창가 인물 사진을 자연스럽게 보정하고 싶어요"
```

이벤트 로그에서 프로필 재생성:

```powershell
uv run edit-master feedback --memory-dir data\personalization\local --user-id local rebuild
```

Client가 보내면 좋은 피드백 신호:

- `accepted`, `saved`, `copied`: 해당 스타일/채널 선호를 강화
- `rejected`: 해당 시나리오/채널/스타일 선호를 약화
- `edited_again`: 답변은 도움이 됐지만 추가 보정이 필요했다는 약한 부정 신호
- `toned_down`: 과한 보정을 줄이고 `natural`, `low_retouch` 쪽으로 이동

Client가 이미지 분석 결과를 이미 가지고 있다면 `record`와 `render` 양쪽에 `--observation-json`을 넘길 수 있습니다. 이 경우에도 이 저장소는 이미지 분석을 직접 수행하지 않고, Client가 만든 facet을 시나리오 매칭과 개인화에만 사용합니다.

## 5. graph.html을 볼 때

`graph.html`은 Neo4j 자체라기보다 정적 그래프 시각화 파일에 가깝습니다. Neo4j로 사용하려면 `graphify-out/cypher_scene_recommender.txt` 같은 Cypher를 Neo4j DB에 import해야 합니다.

그래프를 볼 때는 예쁜 모양보다 아래 품질 신호를 봅니다.

1. Scenario가 중심에 있는가
   - 좋은 흐름: `Scenario -> Recommendation -> Technique/Parameter -> Evidence`
   - source/creator가 중심이면 사용자 추천에는 경로가 멀어집니다.

2. Trend, General, Personalized 추천이 분리되어 있는가
   - 현재 기본 구조는 30 scenario x 3 channel = 90 recommendation입니다.

3. 고립 노드가 많은가
   - 고립된 `Issue`, `Outcome`, `Evidence`는 검색과 추천에 잘 쓰이지 않습니다.
   - `uv run edit-master validate`에서 isolate 수를 확인합니다.

4. Issue가 중심축이 되지 않는가
   - 나쁜 구조: `underexposed_face -> all recommendations`
   - 좋은 구조: `Scenario + Preference + Trend -> Recommendation`, issue는 parameter 조정

5. Evidence가 추천까지 붙어 있는가
   - 좋은 흐름: `Recommendation -[:SUPPORTED_BY]-> Evidence`
   - 근거 없는 추천은 Agent 답변 신뢰도를 낮춥니다.

## 운영 루프

raw를 추가하거나 graph를 갱신할 때는 아래 루프를 따릅니다.

```text
raw 추가/수정
-> scenario alias, graph_nodes, graph_edges, urls 확인
-> graphify/wiki/graph 재생성
-> source_bridge로 source graph와 추천 graph 연결 검증
-> edit-master validate 실행
-> tests/eval_queries.json 회귀 평가 통과 확인
-> graph.html에서 Scenario 중심성, 고립 노드, Evidence 연결 확인
```

현재 matcher 회귀 평가:

```powershell
uv run edit-master eval --min-top1 1.0
```

통합 검증:

```powershell
uv run edit-master validate
```

legacy entrypoint인 `scripts/*.py`와 `python -m scripts.recommender...` 명령은 유지하지만, 일반 운영에서는 위 하네스 명령을 우선 사용합니다.

## Source-backed raw intake harness

새 raw 시나리오는 기존 raw를 짜깁기하지 않고 외부 근거를 먼저 수집한 뒤 추가합니다. 토픽을 직접 넣지 않으면 2026년 기준 최신 전문가/공식/creator 기반 촬영·보정 기법 토픽을 count만큼 생성합니다. 병렬 Codex/Claude 작업 패킷을 만들고, 후보 파일과 source note JSON을 검증한 뒤에만 `raw/scenarios`로 승격합니다.

```powershell
uv run edit-master raw intake --engine codex --parallel max --count 5
```

위 명령은 `brief -> dispatch -> validate`를 한 번에 실행합니다. 검증된 후보를 실제 graph에 반영하려면 결과를 확인한 뒤 아래 명령을 실행합니다.

```powershell
uv run edit-master raw promote --build
```

단계를 나누어 실행하려면:

```powershell
uv run edit-master raw brief --engine both --parallel max --count 5
uv run edit-master raw dispatch --run-id latest --engine codex --parallel max
uv run edit-master raw validate --scope incoming
uv run edit-master raw promote --build
```

엄격 출처 검증에서 통과한 후보만 한 번에 승격하려면:

```powershell
uv run edit-master raw promote --strict-sources --passing-only --delete-incoming --build
```

실패 후보까지 incoming에서 정리하려면 `--delete-failed`를 추가합니다.

```powershell
uv run edit-master raw promote --strict-sources --passing-only --delete-incoming --delete-failed --build
```

각 후보는 `raw/_incoming/scenarios/{slug}.md`와 `raw/_incoming/source_notes/{slug}.json`을 함께 만들어야 합니다. `intake`/`dispatch`는 설치/인증된 `codex` 또는 `claude` CLI가 있을 때 사용합니다. 자세한 절차는 `docs/raw_intake_harness.md`를 참고합니다.

## 아직 남은 일

- 평가 쿼리를 늘려 자연어 답변 품질과 개인화 variant 차이를 회귀 테스트하기
- 실제 Client 피드백 action 이름과 `learning_loop.py`의 action/rating 정책을 맞추기
