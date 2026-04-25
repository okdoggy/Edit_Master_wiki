# Raw Intake Harness

이 하네스는 기존 raw를 짜깁기하지 않고, 외부 근거가 있는 신규 raw 시나리오를 병렬로 수집하기 위한 작업면입니다.

## 목표

- Codex/Claude 워커가 같은 포맷으로 후보 raw를 작성한다.
- 각 후보는 공식 문서, 전문가 튜토리얼, 신뢰할 만한 creator/SNS, 또는 실전 커뮤니티 근거를 포함한다.
- 기존 `raw/scenarios`와 slug/title/alias/graph_nodes가 과하게 겹치면 승격하지 않는다.
- 최종 반영은 사람이 직접 파일을 복사하는 대신 하네스 검증을 통과해야 수행한다.

## 한 번에 수집하기

가장 쉬운 운영 명령은 `intake`입니다. 이 명령은 `brief -> dispatch -> validate`를 한 번에 실행합니다.
토픽을 직접 넣지 않으면 2026년 기준 최신 전문가/공식/creator 기반 촬영·보정 기법 토픽을 `--count`만큼 생성합니다.

```powershell
uv run edit-master raw intake --engine codex --parallel max --count 5
```

특정 주제를 지정하려면:

```powershell
uv run edit-master raw intake --engine codex --parallel max --topic "스마트폰 기차 창가 인물, 유리 반사와 얼굴 노출 제어"
```

실행 전에 작업 생성과 병렬 실행 계획만 보려면:

```powershell
uv run edit-master raw intake --engine codex --parallel max --count 5 --dry-run
```

`intake`는 후보를 `raw/scenarios`로 바로 넣지 않습니다. 검증 결과를 확인한 뒤 `raw promote --build`를 실행해야 합니다.

## 병렬 작업 나눠서 실행하기

```powershell
uv run edit-master raw brief --engine both --parallel max --count 5
```

특정 주제를 지정하려면:

```powershell
uv run edit-master raw brief --topic "스마트폰 기차 창가 인물, 유리 반사와 얼굴 노출 제어" --topic "홈오피스 책상 셋업 사진"
```

생성물:

- `data/raw_intake_runs/{run_id}/tasks/task_*.md`
- `data/raw_intake_runs/{run_id}/manifest.json`
- `data/raw_intake_runs/{run_id}/RUN_PARALLEL.md`

각 task는 한 워커가 맡습니다. 워커는 `raw/_incoming/scenarios/{slug}.md`와 `raw/_incoming/source_notes/{slug}.json`만 작성해야 합니다. `source_notes` JSON은 어떤 URL을 왜 신뢰했는지와 기존 시나리오와 어떻게 다른지를 기록하는 감사 메모입니다.

설치/인증된 `codex` 또는 `claude` CLI가 있으면 하네스에서 바로 병렬 실행할 수 있습니다.

```powershell
uv run edit-master raw dispatch --run-id latest --engine codex --parallel max
uv run edit-master raw dispatch --run-id latest --engine claude --parallel max
```

실행 전에 계획만 보려면:

```powershell
uv run edit-master raw dispatch --run-id latest --engine codex --parallel max --dry-run
```

## 후보 검증

```powershell
uv run edit-master raw validate --scope incoming --strict-sources
```

검증 항목:

- `scenario_tags`, `aliases`, `graph_nodes`, `graph_edges`, `urls` 존재
- frontmatter `aliases` 최소 5개 이상
- 최소 source URL 수
- official/expert/creator_social/community 근거 최소 1개 이상
- incoming 후보의 `raw/_incoming/source_notes/{slug}.json` 존재 여부와 URL 설명
- 필수 본문 섹션 존재: `## 추천 시스템용 요약`, `## 촬영 레시피`, `## 보정 레시피`, `## 근거`, `## Graphify 추출 힌트`
- 기존 scenario와 slug/title/alias/graph_nodes 중복 검사

unknown domain을 경고로만 보고 싶다면 `--strict-sources`를 빼고 먼저 점검할 수 있습니다.

```powershell
uv run edit-master raw validate --scope incoming
```

## 승격

```powershell
uv run edit-master raw promote --build
```

이 명령은 검증된 후보만 `raw/scenarios`로 복사하고 `raw/manifests/scenario_files.csv`를 갱신합니다. source note가 있으면 `raw/source_notes/{slug}.json`으로 보존합니다. `--build`를 붙이면 `build -> bridge --write -> validate`까지 이어서 실행합니다.

후보 파일을 승격 후 삭제하려면:

```powershell
uv run edit-master raw promote --build --delete-incoming
```

엄격 출처 검증에서 통과한 후보만 한 번에 승격하려면:

```powershell
uv run edit-master raw promote --strict-sources --passing-only --delete-incoming --build
```

이 명령은 실패 후보를 `raw/_incoming`에 그대로 남기고, 통과 후보만 `raw/scenarios`로 복사한 뒤 incoming 사본을 정리합니다.

실패 후보까지 incoming에서 삭제하려면:

```powershell
uv run edit-master raw promote --strict-sources --passing-only --delete-incoming --delete-failed --build
```

통과 후보가 하나도 없고 실패 후보만 정리되는 경우에는 `--build`가 자동으로 생략됩니다.

## 운영 원칙

- raw 후보는 외부 근거를 먼저 수집한 뒤 작성한다.
- 기존 raw는 중복 회피용 inventory로만 사용한다.
- issue 중심 문서가 아니라 trend/preference/style recipe 중심 문서를 만든다.
- source note JSON에는 어떤 URL을 어떤 판단에 썼는지 적는다.
