# User-perspective graphify query evaluation — scene-first graph

- generated_at: 2026-04-17T20:49:23
- graph: `graphify-out/scene_recommender_graph.json`
- method: 실제 사용자 질문처럼 한국어 장면 질문 10개를 만들고, scene-first graph의 Scenario → Recommendation → Technique/Parameter 경로를 조회했다.
- note: 기본 `graphify query`는 한국어 장면 문장 매칭이 약해서, 이번 평가는 scene-first graph 구조를 직접 조회하는 harness로 수행했다. 이는 실제 서비스 API에 더 가까운 방식이다.

## 1. 카페 창가에서 친구 프로필 사진을 찍었는데 얼굴 한쪽이 어둡고 뒤 테이블이 지저분해요. 다시 찍는다면 구도랑 보정을 어떻게 하면 좋을까요?

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

## 2. 비 오는 밤 네온 간판 앞에서 커플 사진을 찍었는데 얼굴은 어둡고 네온만 너무 튀어요. 트렌디하지만 얼굴도 살리는 방법이 있을까요?

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

## 3. 어두운 레스토랑에서 파스타 사진을 찍었는데 노랗고 흐릿해요. 플래시 없이 맛있어 보이게 찍고 보정하는 방법이 궁금해요.

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

## 4. 한낮 해변에서 인물 사진을 찍으면 얼굴에 그림자가 세고 하늘은 날아가요. 어떤 렌즈와 보정이 나을까요?

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

## 5. 골목에서 전신 OOTD를 찍었는데 다리가 짧아 보이고 옷 색보다 배경이 더 튀어요. 어떻게 찍어야 할까요?

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

## 6. 콘서트장에서 멀리 있는 가수를 폰으로 찍었는데 조명은 다 날아가고 얼굴은 뭉개져요. 그래도 건질 방법이 있을까요?

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

## 7. 눈 오는 날 가족 사진을 찍었는데 눈이 회색이고 얼굴은 칙칙해 보여요. 겨울 느낌은 살리면서 깨끗하게 보정하고 싶어요.

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

## 8. 강아지가 뛰어오는 사진을 찍고 싶은데 매번 흔들려요. 휴대폰으로 생동감 있게 찍으려면 어떻게 해야 하나요?

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

## 9. 카페에서 디저트랑 커피를 위에서 찍었는데 테이블이 삐뚤고 접시가 왜곡돼 보여요. 예쁜 플랫레이로 찍는 방법이 궁금해요.

# Q. 카페에서 디저트랑 커피를 위에서 찍었는데 테이블이 삐뚤고 접시가 왜곡돼 보여요. 예쁜 플랫레이로 찍는 방법이 궁금해요.

- 매칭된 scenario: `scenario_marketplace_street_food_story` / 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기
- 의도 해석: 플랫레이 음식, 그리드/수평, 1x/0.5x, 색감

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

## 10. 도시 야경을 유리창 반사와 같이 찍고 싶은데 반사가 지저분하고 사진이 산만해요. 더 감성적으로 만드는 방법이 있을까요?

# Q. 도시 야경을 유리창 반사와 같이 찍고 싶은데 반사가 지저분하고 사진이 산만해요. 더 감성적으로 만드는 방법이 있을까요?

- 매칭된 scenario: `scenario_reflection_mirror_puddle_prism` / 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷
- 의도 해석: 도시 반사/유리/네온, 창의적 반사, 하이라이트 제어

## 사용자에게 줄 답변

### 트렌드 추천
- Trend recommendation — 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷
- 기법: 웅덩이는 폰을 낮게 내려 반사면을 크게 만든다.; 거울은 프레임 안 프레임처럼 사용.; 프리즘/CD/유리컵은 렌즈 가장자리에 살짝 대고 빛 번짐을 만든다.; 결과 컷과 BTS 컷을 함께 저장.
- 시작값: Highlights -20~-60로 반사 하이라이트 보호.; Contrast +5~+20, Dehaze +3~+12.; Prism 색은 Saturation +5~+15, 피부는 mask로 보호.

### 일반 추천
- General recommendation — 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷
- 촬영/구도: 웅덩이는 폰을 낮게 내려 반사면을 크게 만든다.; 거울은 프레임 안 프레임처럼 사용.; 프리즘/CD/유리컵은 렌즈 가장자리에 살짝 대고 빛 번짐을 만든다.; 결과 컷과 BTS 컷을 함께 저장.; 불필요한 손/소품 가장자리는 Remove/Heal.
- 보정/설정: Highlights -20~-60로 반사 하이라이트 보호.; Contrast +5~+20, Dehaze +3~+12.; Prism 색은 Saturation +5~+15, 피부는 mask로 보호.
- 목표 결과: Natural skin tone; Background separation; Highlight preservation; Face clarity
- 주의: 유리/거울은 안전과 주변 반사 노출 주의.; 효과가 얼굴을 가리면 시선이 분산.

### 개인화 추천 방향
- Personalized recommendation — 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷
- 취향에 따라 조절할 기법: 웅덩이는 폰을 낮게 내려 반사면을 크게 만든다.; 거울은 프레임 안 프레임처럼 사용.; 프리즘/CD/유리컵은 렌즈 가장자리에 살짝 대고 빛 번짐을 만든다.; 결과 컷과 BTS 컷을 함께 저장.
- 조절값 후보: Highlights -20~-60로 반사 하이라이트 보호.; Contrast +5~+20, Dehaze +3~+12.; Prism 색은 Saturation +5~+15, 피부는 mask로 보호.

### 근거 파일
- `raw/scenarios/reflection_mirror_puddle_prism.md`
