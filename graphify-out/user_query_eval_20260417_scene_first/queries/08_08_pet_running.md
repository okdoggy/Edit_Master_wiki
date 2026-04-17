# Q. 강아지가 뛰어오는 사진을 찍고 싶은데 매번 흔들려요. 휴대폰으로 생동감 있게 찍으려면 어떻게 해야 하나요?

- 매칭된 scenario: `scenario_pets_children_action` / 아이·반려동물 액션 — 순간 포착/연사/짧은 영상
- 의도 해석: 반려동물 액션, 연사/영상, 눈높이, 흔들림 방지

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상
- 기법: 야외 밝은 그늘에서 촬영한다.; 1x는 움직임 추적, 2x는 표정 클로즈업.; Burst/Live Photo/4K video still로 순간을 확보.; 눈 높이 또는 더 낮은 앵글로 촬영.
- 시작값: Exposure +0.1~+0.3, Highlights -10~-30.; Texture/Clarity +5~+15 for fur/detail.; Background Saturation -5~-15.; 움직임 blur가 매력적이면 Grain +10~+20로 스타일화.

### 일반 추천
- General recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상
- 촬영/구도: 야외 밝은 그늘에서 촬영한다.; 1x는 움직임 추적, 2x는 표정 클로즈업.; Burst/Live Photo/4K video still로 순간을 확보.; 눈 높이 또는 더 낮은 앵글로 촬영.
- 보정/설정: Exposure +0.1~+0.3, Highlights -10~-30.; Texture/Clarity +5~+15 for fur/detail.; Background Saturation -5~-15.; 움직임 blur가 매력적이면 Grain +10~+20로 스타일화.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: Night mode는 움직이는 아이/동물에 부적합.; 디지털 줌보다 가까이 가거나 2x optical/quality zoom.

### 개인화 추천 방향
- Personalized recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상
- 취향에 따라 조절할 기법: 야외 밝은 그늘에서 촬영한다.; 1x는 움직임 추적, 2x는 표정 클로즈업.; Burst/Live Photo/4K video still로 순간을 확보.; 눈 높이 또는 더 낮은 앵글로 촬영.
- 조절값 후보: Exposure +0.1~+0.3, Highlights -10~-30.; Texture/Clarity +5~+15 for fur/detail.; Background Saturation -5~-15.; 움직임 blur가 매력적이면 Grain +10~+20로 스타일화.

### 근거 파일
- `raw/scenarios/pets_children_action.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → kids or pets (SceneFacet/Subject)
- HAS_FACET → fast (Motion/SceneFacet)
- USES_MODE → burst live video (Mode/SceneFacet)
- USES_LENS → 1x 2x (Lens/SceneFacet)
- HAS_LIGHT → bright natural (Light/SceneFacet)
- HAS_EDIT_STYLE → clear action (EditStyle/SceneFacet)
- USES_TECHNIQUE → fast_motion REQUIRES_short_shutter (Technique)
- USES_TECHNIQUE → burst CAPTURES_expression (Technique)
- USES_TECHNIQUE → bright_light REDUCES_blur (Technique)
- USES_TECHNIQUE → eye_focus DRIVES_satisfaction (Technique)

### Recommendations
- trend: Trend recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상 (rank 0.75)
- general: General recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상 (rank 0.82)
- personalized: Personalized recommendation — 아이·반려동물 액션 — 순간 포착/연사/짧은 영상 (rank 0.7)
