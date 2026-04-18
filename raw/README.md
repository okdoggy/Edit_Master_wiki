# Smartphone Photography Raw Tips

업데이트: 2026-04-17

이 폴더는 “누가 유명한가”보다 **어떤 상황에서 어떻게 찍고 어떻게 보정하는가**를 보기 위한 raw tip corpus다. 각 md 파일은 아래 형식의 팁 카드로 바뀌었다.

```text
상황 → 촬영/작업 순서 → 추천 시작값/조작값 → 보정 루틴 → 주의점 → 근거/출처
```


## 추가 수집/보강 파일 — 2026-04-17

- 줌/렌즈별 상황 가이드: `raw/techniques/zoom_lens_situation_guide.md`
- 야간·인물·음식·매크로 모드 가이드: `raw/techniques/camera_modes_night_portrait_food_macro.md`
- 음식 사진 실전 레시피: `raw/techniques/food_photography_recipes.md`
- SNS 연도별 인물·여행 보정 트렌드: `raw/trends/sns_editing_trends_by_year.md`
- 인물·여행 Lightroom Mobile 스타일별 레시피: `raw/trends/portrait_travel_editing_styles.md`

### 이번 추가 데이터의 핵심

- 0.5x/1x/2x/3x/5x/10x+ 줌별로 어울리는 장면과 피해야 할 장면 정리.
- 야간 모드, 인물 모드, 음식 모드, 매크로 모드를 “언제 켜고 언제 피할지” 기준으로 정리.
- Galaxy Food mode의 highlighted area, radial blur, 색 조정 흐름 추가.
- Instagram/SNS 보정 흐름을 2012~2026 타임라인으로 정리.
- 인물/여행/음식에 바로 적용할 Lightroom Mobile 시작값 추가.


## Graphify/추천 연결용 scenario corpus — 2026-04-17

추가로 `raw/scenarios/`와 `raw/recommendation/`를 만들었다. 목적은 단순 팁 저장이 아니라, 입력 장면을 graphify 지식그래프와 추천 시스템에 연결하기 위한 seed를 늘리는 것이다.

- scenario files: 18개
- 추천 스키마: `raw/recommendation/graphify_recommendation_schema.md`
- scenario index: `raw/recommendation/scenario_corpus_index.md`

예시 입력: “단풍나무 아래 여성”

- 트렌드 추천: warm foliage, leaf foreground, 4:5 crop, subtle film grain.
- 일반 추천: 2x/Portrait, golden-hour/backlight, subject 1~3m from background, subject mask.
- 개인화 추천: 사용자의 bright/cinematic/natural 선호에 따라 색/contrast/grain/skin retouch 변형.

- 전문가/인기 Lightroom 보정 스타일: `raw/trends/professional_popular_editing_recipes.md`


## 피드백 반영 — 자연어 답변과 시나리오 매칭 보강 (2026-04-17)

- 자연스러운 사용자 답변 렌더링 규칙: `raw/recommendation/natural_answer_renderer_guidelines.md`
- 한국어 시나리오 매칭 alias 사전: `raw/recommendation/scenario_matching_lexicon.md`
- 추가 scenario 10개: 어두운 식당 음식, 카페 플랫레이, 도시 유리창 반사, 한낮 해변 인물, 미술관 인물, 실내 파티 단체, 관광지 랜드마크, 제품 판매 사진, 거울 OOTD, 카페 음료/디저트 클로즈업.

이번 보강의 목표는 “그래프 노드 문장”을 그대로 답하지 않고 자연스러운 사진 코치 답변으로 바꾸는 것, 그리고 실제 사용자가 말할 법한 한국어 장면 질문을 더 잘 scenario에 붙이는 것이다.

## 가장 먼저 볼 파일

- 달/갤럭시 Pro mode: `raw/magazine/samsung_camera_modes_settings.md`
- 갤럭시 야간/라이트드로잉: `raw/magazine/samsung_low_light_galaxy.md`
- 아이폰 Night mode: `raw/magazine/apple_support_night_mode.md`
- iPhone Photography School 팁: `raw/sns/iphone_photography_school_emil_pakarklis.md`
- SNS 창의적 트릭: `raw/sns/jordi_koalitic.md`, `raw/youtube/cooph_youtube.md`
- Lightroom Mobile 보정 spine: `raw/lightroom/adobe_edit_photos_mobile_ios.md`
- Lightroom Community/인기글 역분석: `raw/lightroom/adobe_in_app_learning_community_ios.md`

## 대표 레시피 예시

### 갤럭시로 달 찍기

- Pro mode/Expert RAW → 10x 광학 망원 → 삼각대/고정 → MF 무한대.
- 시작값: ISO 50~100, 셔터 1/125~1/500s, WB 4000~5200K 또는 Auto.
- Lightroom: Highlights -50~-100, Texture/Clarity +10~+30.
- 주의: Night mode로 달을 밝게 만들면 표면 디테일이 날아갈 수 있다.

### 아이폰 야경

- Night mode 자동 활성화 확인 → 정적 장면은 가능한 긴 노출 옵션 → 삼각대/난간 고정.
- 십자선이 뜨면 맞춰 흔들림을 줄인다.
- 네온/간판은 EV -0.3~-1.0으로 하이라이트를 먼저 살린다.

### Lightroom Mobile 인물 보정

- Masking → Select Subject.
- 인물: Exposure +0.1~+0.4, Contrast +5~+15 시작.
- 배경: Exposure -0.1~-0.4 또는 Saturation -5~-20.
- 피부색은 Orange Saturation/Luminance를 작게만 조절한다.

## 파일 수

- source tip files: 47개
- SNS/creator: 12개
- YouTube: 7개
- Magazine/official: 15개
- Lightroom: 13개

## 확실성 표기

- `source-supported`: 출처가 직접 기능/절차/수치 일부를 뒷받침.
- `실전 시작점`: 출처의 원칙을 바탕으로 실제 촬영 때 테스트할 범위. 기기·빛·거리마다 조정 필요.

원문 전문 복사는 하지 않는다. 대신 실전 팁과 출처 URL을 저장한다.

## 보강 — 다국어 매칭/토큰 정규화/5W1H 슬롯 (2026-04-18)

- 한국어+영어 혼합 질의 대응 alias 사전: `raw/recommendation/scenario_matching_lexicon.md`
- 토큰 정규화 플레이북: `raw/recommendation/token_normalization_playbook.md`
- 질의 슬롯 스키마(언제/누가/어디서/무엇을/어떻게): `raw/recommendation/query_slot_schema_5w1h.md`

핵심 목표:
- 영어뿐 아니라 한국어/코드믹스 질의의 scenario 매칭률 개선.
- `Woman`, `tok_woman`, `subject:woman` 같은 분산 토큰을 canonical token으로 통합.
- scenario/recommendation 연결에 5W1H 슬롯을 강제해서 검색 경로를 안정화.

## 신규 외부 출처 raw 추가 (기존 출처와 다른 소스)

- Sony Support (Xperia Photography Pro 모드): `raw/magazine/sony_photography_pro_modes.md`
- Xiaomi Support (Phone camera Pro mode): `raw/magazine/xiaomi_phone_pro_mode.md`
- YouTube Help (Shorts 규격/정책): `raw/magazine/youtube_shorts_specs.md`

원칙:
- 기존 raw 내용을 재포장하지 않고, 신규 외부 URL 기반으로 별도 파일 생성.
- 각 파일은 동일하게 “상황 → 작업 순서 → 시작값 → 주의점 → 근거” 구조를 유지.

## 시간 단위 증분 수집 — raw/hourly

- 자동 수집 스크립트: `scripts/collect_hourly_raw.py`
- 저장 위치: `raw/hourly/YYYY-MM-DD-HHMM-*.md`
- 실행 주기: launchd 설정 시 1시간마다 실행
- 중복 방지: 기존 `raw/**/*.md`, `raw/manifests/sources.csv`, `raw/manifests/hourly_collection_state.json`의 URL과 제목 fingerprint를 기준으로 이미 수집된 항목을 건너뜀
- 원칙: 인터넷에서 새로 확인한 SNS/커뮤니티/전문 매체 신호만 추가하고, 기존 raw를 짜깁기하지 않음. 원문 전문은 복사하지 않고 출처 URL과 한국어 실전 팁 카드로 요약함.

## 온라인 자동 수집 — GitHub Actions

- 워크플로: `.github/workflows/hourly-raw-collector.yml`
- 실행 주기: GitHub Actions `schedule`로 매시간 17분에 실행 (`17 * * * *`)
- 수동 실행: GitHub Actions 탭에서 `Hourly raw collector` → `Run workflow`
- 누적 방식: 새 raw content/index 변경이 있을 때만 `automation/hourly-raw-collector` 브랜치에 commit/push
- 리뷰 방식: GitHub Actions가 `Review hourly raw photo-technique updates` PR을 생성하거나 기존 PR을 업데이트
- main 보호 원칙: scheduled workflow는 `main`에 직접 push하지 않음. 사람이 PR을 검토/merge해야 canonical raw에 반영됨
- 빈 실행 처리: 새 raw 파일 없이 `hourly_collection_state.json`만 바뀐 경우는 commit하지 않음
- 주의: GitHub scheduled workflow는 GitHub 큐 상황에 따라 지연될 수 있고, public repo는 장기간 활동이 없으면 schedule이 비활성화될 수 있음

로컬 macOS LaunchAgent는 Mac이 켜져 있을 때만 동작하는 fallback이다. 온라인 누적이 목적이면 GitHub Actions를 우선 사용하되, raw 결과는 PR 리뷰 후 main에 병합한다.

