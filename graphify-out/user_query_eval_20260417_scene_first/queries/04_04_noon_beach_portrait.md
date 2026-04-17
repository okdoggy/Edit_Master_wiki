# Q. 한낮 해변에서 인물 사진을 찍으면 얼굴에 그림자가 세고 하늘은 날아가요. 어떤 렌즈와 보정이 나을까요?

- 매칭된 scenario: `scenario_beach_backlit_portrait` / 해변 역광 인물 — 여름/휴양지 SNS 스타일
- 의도 해석: 해변 인물, 강한 빛, 하늘/얼굴 균형

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일
- 기법: 해가 낮을 때 피사체 뒤나 45도 뒤에 두어 rim light를 만든다.; 2x/Portrait로 인물, 0.5x로 장소 전체 컷도 함께.
- 시작값: 하늘 기준으로 EV -0.3~-0.7, 얼굴은 후보정에서 mask로 보정.; 바닷가 수평선은 Level/Grid로 맞춘다.; Sky mask: Highlights -30~-60, Dehaze +5~+12.; Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.

### 일반 추천
- General recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일
- 촬영/구도: 해가 낮을 때 피사체 뒤나 45도 뒤에 두어 rim light를 만든다.; 2x/Portrait로 인물, 0.5x로 장소 전체 컷도 함께.
- 보정/설정: 하늘 기준으로 EV -0.3~-0.7, 얼굴은 후보정에서 mask로 보정.; 바닷가 수평선은 Level/Grid로 맞춘다.; Sky mask: Highlights -30~-60, Dehaze +5~+12.; Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.; Blue Luminance -5~-20, Orange Luminance +5~+15.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: 직사광 정면 얼굴은 눈 찡그림/강한 그림자 발생.; 바다/하늘 채도를 너무 올리면 인공적.

### 개인화 추천 방향
- Personalized recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일
- 취향에 따라 조절할 기법: 해가 낮을 때 피사체 뒤나 45도 뒤에 두어 rim light를 만든다.; 2x/Portrait로 인물, 0.5x로 장소 전체 컷도 함께.
- 조절값 후보: 하늘 기준으로 EV -0.3~-0.7, 얼굴은 후보정에서 mask로 보정.; 바닷가 수평선은 Level/Grid로 맞춘다.; Sky mask: Highlights -30~-60, Dehaze +5~+12.; Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.

### 근거 파일
- `raw/scenarios/beach_backlit_portrait.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → person (SceneFacet/Subject)
- HAS_ENVIRONMENT → beach (Environment/SceneFacet)
- HAS_LIGHT → backlight golden hour (Light/SceneFacet)
- USES_LENS → 2x portrait (Lens/SceneFacet)
- HAS_EDIT_STYLE → warm blue travel (EditStyle/SceneFacet)
- HAS_RISK → blown highlights (Risk/SceneFacet)
- USES_TECHNIQUE → backlight CREATES_hair_glow (Technique)
- USES_TECHNIQUE → beach_reflects_light (Technique)
- USES_TECHNIQUE → sky_mask PROTECTS_cloud_detail (Technique)
- USES_TECHNIQUE → 2x_portrait FLATTERS_face (Technique)

### Recommendations
- trend: Trend recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일 (rank 0.75)
- general: General recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일 (rank 0.82)
- personalized: Personalized recommendation — 해변 역광 인물 — 여름/휴양지 SNS 스타일 (rank 0.7)
