# Q. 골목에서 전신 OOTD를 찍었는데 다리가 짧아 보이고 옷 색보다 배경이 더 튀어요. 어떻게 찍어야 할까요?

- 매칭된 scenario: `scenario_fashion_ootd_portrait` / 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed
- 의도 해석: 패션 전신, 왜곡, 옷 색 우선, 배경 절제

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed
- 기법: 렌즈: 2x 망원 우선, 공간이 좁으면 1x.; 모드: Portrait / Photo.; 포즈: 상체 3/4 각도, 한쪽 다리 앞으로, 어깨 힘 빼기.; 구도: 세로 프레임, 인물은 1/3~1/2 비중, 발끝이 잘리지 않게.
- 시작값: 카메라 시작값: Exposure 0~+0.3, Grid ON.; Temp +3~+6.; Vibrance +10~+15.; Saturation -3~-5.

### 일반 추천
- General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed
- 촬영/구도: 렌즈: 2x 망원 우선, 공간이 좁으면 1x.; 모드: Portrait / Photo.; 포즈: 상체 3/4 각도, 한쪽 다리 앞으로, 어깨 힘 빼기.; 구도: 세로 프레임, 인물은 1/3~1/2 비중, 발끝이 잘리지 않게.; 빛: 사이드 라이트 또는 open shade.
- 보정/설정: 카메라 시작값: Exposure 0~+0.3, Grid ON.; Temp +3~+6.; Vibrance +10~+15.; Saturation -3~-5.; Orange Saturation -5.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: 광각을 너무 가까이서 쓰면 신체 비율이 무너진다.; 옷 색을 살리다가 피부가 과포화되지 않게 한다.

### 개인화 추천 방향
- Personalized recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed
- 취향에 따라 조절할 기법: 렌즈: 2x 망원 우선, 공간이 좁으면 1x.; 모드: Portrait / Photo.; 포즈: 상체 3/4 각도, 한쪽 다리 앞으로, 어깨 힘 빼기.; 구도: 세로 프레임, 인물은 1/3~1/2 비중, 발끝이 잘리지 않게.
- 조절값 후보: 카메라 시작값: Exposure 0~+0.3, Grid ON.; Temp +3~+6.; Vibrance +10~+15.; Saturation -3~-5.

### 근거 파일
- `raw/scenarios/fashion_ootd_portrait.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → person (SceneFacet/Subject)
- HAS_SUBJECT → fashion outfit (SceneFacet/Subject)
- HAS_ENVIRONMENT → street or cafe (Environment/SceneFacet)
- USES_LENS → 2x or 1x (Lens/SceneFacet)
- USES_MODE → portrait or photo (Mode/SceneFacet)
- HAS_EDIT_STYLE → clean influencer (EditStyle/SceneFacet)
- HAS_PERSONALIZATION_SIGNAL → outfit color priority (Preference/SceneFacet)
- USES_TECHNIQUE → 2x_lens REDUCES_body_distortion (Technique)
- USES_TECHNIQUE → grid HELPS_body_alignment (Technique)
- USES_TECHNIQUE → outfit_color REQUIRES_skin_tone_protection (Technique)

### Recommendations
- trend: Trend recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed (rank 0.75)
- general: General recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed (rank 0.82)
- personalized: Personalized recommendation — 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed (rank 0.7)
