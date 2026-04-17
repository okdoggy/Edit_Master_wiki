# Q. 눈 오는 날 가족 사진을 찍었는데 눈이 회색이고 얼굴은 칙칙해 보여요. 겨울 느낌은 살리면서 깨끗하게 보정하고 싶어요.

- 매칭된 scenario: `scenario_snow_portrait_clean_winter` / 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일
- 의도 해석: 눈/겨울 인물, 하이키, WB, 얼굴 톤

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일
- 기법: 얼굴은 2x/Portrait, 풍경 포함은 1x/0.5x.; 눈발은 어두운 배경 앞에서 더 잘 보인다.; 장갑/빨간 목도리 같은 포인트 컬러를 넣는다.
- 시작값: 눈 배경이 많으면 카메라가 어둡게 찍을 수 있어 EV +0.3~+1.0을 테스트한다.; WB: 눈이 파랗게 보이면 Temp +300~+800K.; Highlights -10~-30로 눈 디테일 유지.; Whites +5~+20, Blacks -5~-15.

### 일반 추천
- General recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일
- 촬영/구도: 얼굴은 2x/Portrait, 풍경 포함은 1x/0.5x.; 눈발은 어두운 배경 앞에서 더 잘 보인다.; 장갑/빨간 목도리 같은 포인트 컬러를 넣는다.
- 보정/설정: 눈 배경이 많으면 카메라가 어둡게 찍을 수 있어 EV +0.3~+1.0을 테스트한다.; WB: 눈이 파랗게 보이면 Temp +300~+800K.; Highlights -10~-30로 눈 디테일 유지.; Whites +5~+20, Blacks -5~-15.; Subject mask: Face Exposure +0.1~+0.3, Orange Luminance +5.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: 눈을 순백으로만 밀면 디테일이 사라진다.; 스마트폰 렌즈에 눈/물방울이 묻으면 콘트라스트가 급격히 떨어진다.

### 개인화 추천 방향
- Personalized recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일
- 취향에 따라 조절할 기법: 얼굴은 2x/Portrait, 풍경 포함은 1x/0.5x.; 눈발은 어두운 배경 앞에서 더 잘 보인다.; 장갑/빨간 목도리 같은 포인트 컬러를 넣는다.
- 조절값 후보: 눈 배경이 많으면 카메라가 어둡게 찍을 수 있어 EV +0.3~+1.0을 테스트한다.; WB: 눈이 파랗게 보이면 Temp +300~+800K.; Highlights -10~-30로 눈 디테일 유지.; Whites +5~+20, Blacks -5~-15.

### 근거 파일
- `raw/scenarios/snow_portrait_clean_winter.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → person (SceneFacet/Subject)
- HAS_ENVIRONMENT → snow (Environment/SceneFacet)
- HAS_LIGHT → overcast reflection (Light/SceneFacet)
- USES_LENS → 1x 2x (Lens/SceneFacet)
- HAS_EDIT_STYLE → clean winter (EditStyle/SceneFacet)
- HAS_RISK → underexposed snow (Risk/SceneFacet)
- USES_TECHNIQUE → snow REFLECTS_light (Technique)
- USES_TECHNIQUE → camera_meter MAY underexpose_snow (Technique)
- USES_TECHNIQUE → white_balance CONTROLS blue_cast (Technique)
- USES_TECHNIQUE → subject_mask PROTECTS_face (Technique)

### Recommendations
- trend: Trend recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일 (rank 0.75)
- general: General recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일 (rank 0.82)
- personalized: Personalized recommendation — 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일 (rank 0.7)
