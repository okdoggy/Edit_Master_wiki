# Q. 카페 창가에서 친구 프로필 사진을 찍었는데 얼굴 한쪽이 어둡고 뒤 테이블이 지저분해요. 다시 찍는다면 구도랑 보정을 어떻게 하면 좋을까요?

- 매칭된 scenario: `scenario_window_light_cafe_portrait` / 카페 창가 인물 — 자연광/인플루언서 프로필
- 의도 해석: 창가 인물, 얼굴 노출, 배경 정리, 자연스러운 프로필

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필
- 기법: 창문 옆 45도에 앉히고 얼굴이 창을 향하게 한다.; 2x/Portrait, 눈 초점, 배경과 1m 이상 거리.; 테이블 위 소품은 1~2개만 남긴다.; 텍스트/스토리용이면 상단 여백 확보.
- 시작값: Subject Exposure +0.1~+0.4, Texture -5~-12.; Background Saturation -5~-20, Clarity -5~-15.; Orange Luminance +5~+10, Saturation -5~+5.; 전체 Exposure +0.1~+0.3, Highlights -10~-30.

### 일반 추천
- General recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필
- 촬영/구도: 창문 옆 45도에 앉히고 얼굴이 창을 향하게 한다.; 2x/Portrait, 눈 초점, 배경과 1m 이상 거리.; 테이블 위 소품은 1~2개만 남긴다.; 텍스트/스토리용이면 상단 여백 확보.
- 보정/설정: Subject Exposure +0.1~+0.4, Texture -5~-12.; Background Saturation -5~-20, Clarity -5~-15.; Orange Luminance +5~+10, Saturation -5~+5.; 전체 Exposure +0.1~+0.3, Highlights -10~-30.; 실내 조명+창빛 혼합은 WB가 어려워 RAW 권장.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: 창문 직사광은 코/눈 밑 그림자를 강하게 만든다.

### 개인화 추천 방향
- Personalized recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필
- 취향에 따라 조절할 기법: 창문 옆 45도에 앉히고 얼굴이 창을 향하게 한다.; 2x/Portrait, 눈 초점, 배경과 1m 이상 거리.; 테이블 위 소품은 1~2개만 남긴다.; 텍스트/스토리용이면 상단 여백 확보.
- 조절값 후보: Subject Exposure +0.1~+0.4, Texture -5~-12.; Background Saturation -5~-20, Clarity -5~-15.; Orange Luminance +5~+10, Saturation -5~+5.; 전체 Exposure +0.1~+0.3, Highlights -10~-30.

### 근거 파일
- `raw/scenarios/window_light_cafe_portrait.md`

## 그래프 raw 요약

### Facets
- HAS_SUBJECT → person (SceneFacet/Subject)
- HAS_ENVIRONMENT → cafe window (Environment/SceneFacet)
- HAS_LIGHT → diffused window (Light/SceneFacet)
- USES_LENS → 2x portrait (Lens/SceneFacet)
- HAS_EDIT_STYLE → clean influencer (EditStyle/SceneFacet)
- HAS_PERSONALIZATION_SIGNAL → skin retouch strength (Preference/SceneFacet)
- USES_TECHNIQUE → window_light SOFTENS_skin (Technique)
- USES_TECHNIQUE → 2x REDUCES_distortion (Technique)
- USES_TECHNIQUE → background_distance CREATES_separation (Technique)
- USES_TECHNIQUE → negative_space SUPPORTS_text_overlay (Technique)

### Recommendations
- trend: Trend recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필 (rank 0.75)
- general: General recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필 (rank 0.82)
- personalized: Personalized recommendation — 카페 창가 인물 — 자연광/인플루언서 프로필 (rank 0.7)
