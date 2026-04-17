# Q. 콘서트장에서 멀리 있는 가수를 폰으로 찍었는데 조명은 다 날아가고 얼굴은 뭉개져요. 그래도 건질 방법이 있을까요?

- 매칭된 scenario: `scenario_concert_stage_low_light` / 공연·무대 저조도 — 망원/하이라이트 보호
- 의도 해석: 무대 저조도, 망원, 하이라이트 보호, 노이즈

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호
- 기법: 3x/5x optical 우선, 너무 멀면 10x 기록용.; 움직임이 빠르면 Night mode보다 일반 Photo/Burst/Video.; 난간/몸에 팔꿈치 고정.; 색 조명은 완전 중립으로 만들지 말고 분위기 유지.
- 시작값: 스포트라이트가 밝으면 EV -0.7~-1.3.; Highlights -40~-80, Whites -10~-30.; Shadows +5~+20 또는 moody면 Blacks -10~-25.; Noise Reduction +15~+35, Sharpen +10~+25.

### 일반 추천
- General recommendation — 공연·무대 저조도 — 망원/하이라이트 보호
- 촬영/구도: 3x/5x optical 우선, 너무 멀면 10x 기록용.; 움직임이 빠르면 Night mode보다 일반 Photo/Burst/Video.; 난간/몸에 팔꿈치 고정.; 색 조명은 완전 중립으로 만들지 말고 분위기 유지.
- 보정/설정: 스포트라이트가 밝으면 EV -0.7~-1.3.; Highlights -40~-80, Whites -10~-30.; Shadows +5~+20 또는 moody면 Blacks -10~-25.; Noise Reduction +15~+35, Sharpen +10~+25.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: Night mode 장노출은 공연자를 흐리게 만든다.; 디지털 줌으로 과하게 당기면 디테일이 뭉개진다.

### 개인화 추천 방향
- Personalized recommendation — 공연·무대 저조도 — 망원/하이라이트 보호
- 취향에 따라 조절할 기법: 3x/5x optical 우선, 너무 멀면 10x 기록용.; 움직임이 빠르면 Night mode보다 일반 Photo/Burst/Video.; 난간/몸에 팔꿈치 고정.; 색 조명은 완전 중립으로 만들지 말고 분위기 유지.
- 조절값 후보: 스포트라이트가 밝으면 EV -0.7~-1.3.; Highlights -40~-80, Whites -10~-30.; Shadows +5~+20 또는 moody면 Blacks -10~-25.; Noise Reduction +15~+35, Sharpen +10~+25.

### 근거 파일
- `raw/scenarios/concert_stage_low_light.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → performer (SceneFacet/Subject)
- HAS_ENVIRONMENT → stage (Environment/SceneFacet)
- HAS_LIGHT → spotlight (Light/SceneFacet)
- USES_LENS → 3x 5x 10x (Lens/SceneFacet)
- USES_MODE → photo or pro (Mode/SceneFacet)
- HAS_EDIT_STYLE → moody stage (EditStyle/SceneFacet)
- HAS_RISK → highlight clipping (Risk/SceneFacet)
- USES_TECHNIQUE → spotlight CAUSES_clipping (Technique)
- USES_TECHNIQUE → telephoto REACHES_stage (Technique)
- USES_TECHNIQUE → fast_shutter FREEZES_motion (Technique)
- USES_TECHNIQUE → noise_reduction BALANCES_detail (Technique)

### Recommendations
- trend: Trend recommendation — 공연·무대 저조도 — 망원/하이라이트 보호 (rank 0.75)
- general: General recommendation — 공연·무대 저조도 — 망원/하이라이트 보호 (rank 0.82)
- personalized: Personalized recommendation — 공연·무대 저조도 — 망원/하이라이트 보호 (rank 0.7)
