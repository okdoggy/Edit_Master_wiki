# Q. 어두운 레스토랑에서 파스타 사진을 찍었는데 노랗고 흐릿해요. 플래시 없이 맛있어 보이게 찍고 보정하는 방법이 궁금해요.

- 매칭된 scenario: `scenario_marketplace_street_food_story` / 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기
- 의도 해석: 음식 저조도, 화이트밸런스, 질감, 플래시 회피

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기
- 기법: 1x로 시장/가게 전체, 2x로 음식 질감, 1x/2x로 손이나 조리 장면.; 조리 불빛/김/기름 윤기를 역광으로 살린다.; 사람을 찍을 때는 맥락과 예의를 지킨다.
- 시작값: Photo + 짧은 Video로 소리/움직임도 확보.; WB를 시리즈 전체에 맞춘다.; Highlights -20~-50, Shadows +10~+25.; Texture +10~+20 for food, Grain +10~+25 for documentary.

### 일반 추천
- General recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기
- 촬영/구도: 1x로 시장/가게 전체, 2x로 음식 질감, 1x/2x로 손이나 조리 장면.; 조리 불빛/김/기름 윤기를 역광으로 살린다.; 사람을 찍을 때는 맥락과 예의를 지킨다.
- 보정/설정: Photo + 짧은 Video로 소리/움직임도 확보.; WB를 시리즈 전체에 맞춘다.; Highlights -20~-50, Shadows +10~+25.; Texture +10~+20 for food, Grain +10~+25 for documentary.; Background Saturation -5~-15.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: 형광등/노란등 혼합으로 색이 틀어질 수 있어 RAW 권장.; 사람 얼굴 공개는 동의/맥락 고려.

### 개인화 추천 방향
- Personalized recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기
- 취향에 따라 조절할 기법: 1x로 시장/가게 전체, 2x로 음식 질감, 1x/2x로 손이나 조리 장면.; 조리 불빛/김/기름 윤기를 역광으로 살린다.; 사람을 찍을 때는 맥락과 예의를 지킨다.
- 조절값 후보: Photo + 짧은 Video로 소리/움직임도 확보.; WB를 시리즈 전체에 맞춘다.; Highlights -20~-50, Shadows +10~+25.; Texture +10~+20 for food, Grain +10~+25 for documentary.

### 근거 파일
- `raw/scenarios/marketplace_street_food_story.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → street food (SceneFacet/Subject)
- HAS_ENVIRONMENT → market (Environment/SceneFacet)
- HAS_FACET → hands vendor (SceneFacet/Subject)
- USES_LENS → 1x 2x (Lens/SceneFacet)
- HAS_FACET → wide detail human (SceneFacet/Technique)
- HAS_EDIT_STYLE → warm documentary (EditStyle/SceneFacet)
- USES_TECHNIQUE → human_hands ADD_story (Technique)
- USES_TECHNIQUE → 2x CAPTURES_texture (Technique)
- USES_TECHNIQUE → wide_shot ESTABLISHES_place (Technique)
- USES_TECHNIQUE → consistent_wb CONNECTS_series (Technique)

### Recommendations
- trend: Trend recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기 (rank 0.75)
- general: General recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기 (rank 0.82)
- personalized: Personalized recommendation — 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기 (rank 0.7)
