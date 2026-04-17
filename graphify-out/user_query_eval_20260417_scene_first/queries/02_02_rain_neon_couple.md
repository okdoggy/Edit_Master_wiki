# Q. 비 오는 밤 네온 간판 앞에서 커플 사진을 찍었는데 얼굴은 어둡고 네온만 너무 튀어요. 트렌디하지만 얼굴도 살리는 방법이 있을까요?

- 매칭된 scenario: `scenario_rain_neon_street_portrait` / 비 오는 밤 네온 거리 인물 — moody city look
- 의도 해석: 비/네온/야간 인물, 얼굴 보정, moody cinematic

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 비 오는 밤 네온 거리 인물 — moody city look
- 기법: 젖은 노면이나 유리창 반사를 찾아 피사체를 네온과 반사 사이에 둔다.; 움직이는 인물은 Night mode 시간을 줄이고 1x/2x로 촬영.; 정적인 장면은 폰을 기대고 Night mode 또는 Pro 장노출.
- 시작값: 네온이 날아가면 EV -0.7~-1.3.; Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15.; Color Grading: Shadows teal/blue, Highlights warm/magenta.; Subject mask로 피부 Tint/Temp를 중립에 가깝게.

### 일반 추천
- General recommendation — 비 오는 밤 네온 거리 인물 — moody city look
- 촬영/구도: 젖은 노면이나 유리창 반사를 찾아 피사체를 네온과 반사 사이에 둔다.; 움직이는 인물은 Night mode 시간을 줄이고 1x/2x로 촬영.; 정적인 장면은 폰을 기대고 Night mode 또는 Pro 장노출.
- 보정/설정: 네온이 날아가면 EV -0.7~-1.3.; Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15.; Color Grading: Shadows teal/blue, Highlights warm/magenta.; Subject mask로 피부 Tint/Temp를 중립에 가깝게.; Noise Reduction +15~+35, Grain +10~+25로 노이즈를 스타일화.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: Night mode가 사람을 흐리게 만들 수 있다.; 네온 색을 피부에 그대로 두면 얼굴이 초록/보라로 보인다.

### 개인화 추천 방향
- Personalized recommendation — 비 오는 밤 네온 거리 인물 — moody city look
- 취향에 따라 조절할 기법: 젖은 노면이나 유리창 반사를 찾아 피사체를 네온과 반사 사이에 둔다.; 움직이는 인물은 Night mode 시간을 줄이고 1x/2x로 촬영.; 정적인 장면은 폰을 기대고 Night mode 또는 Pro 장노출.
- 조절값 후보: 네온이 날아가면 EV -0.7~-1.3.; Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15.; Color Grading: Shadows teal/blue, Highlights warm/magenta.; Subject mask로 피부 Tint/Temp를 중립에 가깝게.

### 근거 파일
- `raw/scenarios/rain_neon_street_portrait.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → person (SceneFacet/Subject)
- HAS_ENVIRONMENT → rain neon street (Environment/SceneFacet)
- HAS_LIGHT → neon backlight (Light/SceneFacet)
- USES_MODE → night or portrait (Mode/SceneFacet)
- USES_LENS → 1x 2x (Lens/SceneFacet)
- HAS_EDIT_STYLE → moody cinematic (EditStyle/SceneFacet)
- HAS_RISK → motion blur (Risk/SceneFacet)
- USES_TECHNIQUE → wet_ground CREATES_reflection (Technique)
- USES_TECHNIQUE → neon_light CREATES_color_cast (Technique)
- USES_TECHNIQUE → night_mode INCREASES_exposure_time (Technique)
- USES_TECHNIQUE → subject_mask FIXES_skin_tone (Technique)

### Recommendations
- trend: Trend recommendation — 비 오는 밤 네온 거리 인물 — moody city look (rank 0.75)
- general: General recommendation — 비 오는 밤 네온 거리 인물 — moody city look (rank 0.82)
- personalized: Personalized recommendation — 비 오는 밤 네온 거리 인물 — moody city look (rank 0.7)
