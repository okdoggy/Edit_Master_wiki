# Disconnected Nodes Analysis

## 요약

| Graph | Nodes | Edges | Components | Largest component | Isolates | 해석 |
|---|---:|---:|---:|---:|---:|---|
| 기본 graphify source graph | 541 | 715 | 96 | 198 | 48 | source/문서 중심이라 leaf 개념과 독립 문서가 많음 |
| scene-first recommender graph | 1049 | 3529 | 33 | 893 | 21 | 추천 경로는 대부분 연결되지만 일부 guide/evidence/미사용 issue가 분리 |
| unified Obsidian wiki link graph | 1599 | 12011 | 19 | 1548 | 12 | 실제 wiki 링크 기준으로는 대부분 연결됨 |

## 왜 연결이 안 된 노드가 생기나

1. **의도적으로 source와 scene 역할이 다르다.** 기본 graphify graph는 출처/문서/작가 중심이고, scene graph는 사용자 장면 추천 중심이다. 모든 source 노드가 모든 scene 추천에 직접 연결될 필요는 없다.
2. **leaf node가 많다.** `Parameter`, `Risk`, `QueryAlias`, `Evidence URL`은 보통 하나의 scenario/recommendation에 붙는 말단 노드라 독립적으로 보일 수 있다.
3. **guide 문서에서 추출된 섹션 노드가 scenario와 아직 매핑되지 않은 경우가 있다.** 예: 전체 가이드 문서의 heading은 추출됐지만 특정 scenario로 연결되지 않은 경우.
4. **generic issue/outcome 노드가 아직 라우팅 규칙에 충분히 연결되지 않았다.** 예: `tilted_horizon`, `motion_blur`, `storytelling`, `texture_detail`은 후보로 만들어졌지만 모든 관련 scenario에 연결되지 않았다.
5. **한국어/영어 중복 개념이 아직 정규화되지 않은 곳이 있다.** `Woman`, `subject:woman`, `tok_woman`처럼 같은 의미가 여러 그래프에서 다르게 생길 수 있다.

## Scene-first graph 분리 노드

- components: 33
- largest component: 893/1049 (85.1%)
- isolates: 21

### Isolate categories
- Evidence: 13
- CompositionIssue/TechnicalIssue: 6
- Outcome: 2

### Isolate samples
- `out_storytelling` — Storytelling (Outcome)
- `out_texture_detail` — Texture detail (Outcome)
- `evidence_raw_techniques_food_photography_recipes.md` — 스마트폰 음식 사진 실전 레시피 (Evidence)
- `evidence_raw_techniques_camera_modes_night_portrait_food_macro.md` — 야간·인물·음식·매크로 모드별 촬영 가이드 (Evidence)
- `evidence_raw_techniques_zoom_lens_situation_guide.md` — 카메라 줌/렌즈별 상황 가이드 (Evidence)
- `evidence_raw_trends_sns_editing_trends_by_year.md` — SNS 인물·여행 사진 보정 트렌드 타임라인 (Evidence)
- `evidence_raw_trends_professional_popular_editing_recipes.md` — 전문가/인기 스타일 보정 레시피 — Lightroom Mobile 중심 (Evidence)
- `evidence_raw_trends_portrait_travel_editing_styles.md` — 인물·여행 사진 보정 스타일별 Lightroom Mobile 레시피 (Evidence)
- `evidence_raw_recommendation_metadata_standards_mapping.md` — Photo metadata standards mapping — Schema.org/IPTC/Exif to recommender graph (Evidence)
- `evidence_raw_recommendation_natural_answer_renderer_guidelines.md` — Natural answer renderer guidelines — graph result to user-facing photo coaching (Evidence)
- `evidence_raw_recommendation_user_query_scene_recommendation_schema.md` — User-query scene recommendation schema — image-first shooting/editing recommender (Evidence)
- `evidence_raw_recommendation_scenario_matching_lexicon.md` — Korean scenario matching lexicon — scene query aliases (Evidence)
- `evidence_raw_recommendation_scene_first_neo4j_schema.md` — Scene-first Neo4j schema — camera recommendation graph (Evidence)
- `evidence_raw_recommendation_scenario_corpus_index.md` — Scenario Corpus Index — graphify용 촬영/보정 상황 seed (Evidence)
- `evidence_raw_recommendation_graphify_recommendation_schema.md` — Graphify 추천 연결 스키마 — 스마트폰 촬영/보정 (Evidence)
- `issue_busy_background` — Busy background (CompositionIssue,TechnicalIssue)
- `issue_underexposed_face` — Underexposed face (CompositionIssue,TechnicalIssue)
- `issue_tilted_horizon` — Tilted horizon (CompositionIssue,TechnicalIssue)
- `issue_edge_distortion` — Edge distortion (CompositionIssue,TechnicalIssue)
- `issue_mixed_white_balance` — Mixed white balance (CompositionIssue,TechnicalIssue)
- `issue_motion_blur` — Motion blur (CompositionIssue,TechnicalIssue)

### Components outside largest, top 12
- size 27: Pixel Night Sight 공식 조작, Pixel semi-backlit 음식 조명, 스마트폰 음식 사진 실전 레시피, 모드별 공식 검증값 추가, Samsung Pro mode / Expert RAW 범위, Tip 4. 플랫레이 — 0.5x보다 1x + 높이 확보가 안전, 인플루언서 인물, iPhone Camera Control / Exposure / Depth
- size 19: 인플루언서 인물, Style 1. Clean influencer portrait — 밝고 깨끗한 인물, 야간 음식, Style 10. Food/cafe warm editorial — 음식과 공간을 같이 살리는 톤, 카페 음료·디저트, 여행 골든아워, 음식·여행·인물 공통 Lightroom 스타터, Style 5. Moody city night — 도시 야경/네온/비 오는 거리
- size 15: 2012~2014: 기본 Instagram 필터 / 고채도 / 비네트, 2025~2026 검증 보강: 확정 스타일보다 방향성으로 보기, 2022: no-filter / photo dump / authenticity, 왜 “연도별 고정 룩”이 아니라 “신호”로 봐야 하나, 2025: cinematic / low-fi / AI-assisted / texture, 2024: Reels/vertical-first / text overlay / mixed media, 2023: pink / light reflection / drama / warm tones, 2018~2019: 따뜻한 여행 인플루언서 / orange-teal / curated feed
- size 13: Tip 4. 매크로/근접 모드 — 가까이보다 “초점 거리”가 중요, Samsung Food mode 세부 조작, Tip 3. 음식 모드 — “맛있게” 보이지만 과포화는 줄이기, Samsung Night mode 세부 원리, 야간·인물·음식·매크로 모드별 촬영 가이드, Tip 5. Pro / Expert RAW — 자동 모드가 틀리는 장면에서만 꺼내기, Samsung Pro mode / Expert RAW 범위, Pixel Night Sight 공식 조작
- size 13: Pixel Pro 계열 기준, Tip 2. 1x 메인 — 품질이 가장 안정적인 기본 선택, Tip 3. iPhone 1.2x/1.5x — 거리와 카페 스냅용 28/35mm 느낌, Tip 6. 5x — 여행 레이어와 먼 디테일, Tip 7. 10x 이상 — 달, 무대, 기록용 디테일, 빠른 선택표, Galaxy S24/S25 Ultra 계열 기준, 카메라 줌/렌즈별 상황 가이드
- size 12: General recommendation, Trend recommendation, User-query scene recommendation schema — image-first shooting/editing recommender, Personalized recommendation, 추천 채널 분리, 엣지 타입, 노드 타입, 핵심 판단
- size 10: 표준 기반 필드, IPTC Photo Metadata, 추천용 추론 필드, 왜 필요한가, Schema.org ImageObject / Photograph, Privacy / safety rules, 추천 그래프 필드로 매핑, Photo metadata standards mapping — Schema.org/IPTC/Exif to recommender graph
- size 10: Graphify 추천 연결 스키마 — 스마트폰 촬영/보정, 추천 타입 3종, 단풍나무 아래 여성 예시, Edge patterns, Graphify node taxonomy, 표준 메타데이터 연결, 추천 랭킹에 쓸 수 있는 점수 후보, 3. 개인화 추천
- size 8: Graphify 추출 힌트, Style 3. Food glow / delicious warm editorial, Style 1. Teal & Orange cinematic, 전문가/인기 스타일 보정 레시피 — Lightroom Mobile 중심, Style 4. Film look / nostalgic grain, Style 5. Autumn foliage color grade, Style 6. Snow clean high-key, Style 2. Bright pastel beach / airy travel
- size 6: Constraints, Core query path, Labels, Scene-first Neo4j schema — camera recommendation graph, Ranking fields, Personalization fields
- size 2: Scenario Corpus Index — graphify용 촬영/보정 상황 seed, 추가된 scenario files
- size 1: Storytelling

## Source graph 분리 노드

- components: 96
- largest component: 198/541 (36.6%)
- isolates: 48

### Source isolate samples
- `iphone_portrait_distance_depth` — iPhone Portrait Distance and Depth
- `astrophotography_night_sky` — Astrophotography / night sky
- `moment_capture_burst` — Moment capture / burst
- `style_old_instagram_selfie` — Old Instagram Selfie
- `lens_0_5x_1x_front` — 0.5x 1x Front
- `mode_selfie_or_timer` — Selfie Or Timer
- `subject_group` — Group
- `subject_traveler` — Traveler
- `tok_golden_hour` — Golden Hour
- `edit_style_clean_winter` — Clean Winter
- `subject_person` — Person
- `edit_style_warm_foliage` — Warm Foliage
- `lens_2x_3x_portrait` — 2x 3x Portrait
- `mode_portrait_or_photo` — Portrait Or Photo
- `tok_backlight` — Backlight
- `tok_maple_tree` — Maple Tree
- `tok_woman` — Woman
- `subject_fashion_outfit` — Fashion Outfit
- `edit_style_warm_blue_travel` — Warm Blue Travel
- `lens_2x_portrait` — 2x Portrait
- `tok_window_light` — Window Light
- `mode_night_or_portrait` — Night Or Portrait
- `mode_pro_or_night` — Pro Or Night
- `subject_city_lights` — City Lights
- `edit_style_detail_bokeh` — Detail Bokeh
- `subject_flower_or_leaf` — Flower Or Leaf
- `edit_style_clear_action` — Clear Action
- `mode_burst_live_video` — Burst Live Video
- `subject_kids_or_pets` — Kids Or Pets
- `edit_style_silhouette_warm` — Silhouette Warm
- `subject_person_or_couple` — Person Or Couple
- `edit_style_warm_documentary` — Warm Documentary
- `subject_street_food` — Street Food
- `edit_style_creative_reflection` — Creative Reflection
- `lens_0_5x_1x_2x` — 0.5x 1x 2x
- `subject_person_or_city` — Person Or City
- `edit_style_natural_skin` — Natural Skin
- `mode_selfie_or_portrait_selfie` — Selfie Or Portrait Selfie
- `subject_selfie_person` — Selfie Person
- `lens_0_5x_1x` — 0.5x 1x

### Source components outside largest, top 12
- size 80: Lock Camera Settings, Subject Code / Media Topics, Nicolai Ahn, Edit Style Node, Tyler Stalman, Environment Facet, Benjamin Lowy, IPTC Photo Metadata
- size 58: Night Mode, Pro Mode, Tip Matrix — 상황별 스마트폰 촬영/보정 팁 인덱스, Parallel Research Notes — 실행형 팁으로 재작성한 기준, Phone Polarizing Filter Limit, Local Adjustments, Long Exposure, 폭포·계곡 물결 — 장노출/Live 효과
- size 21: Amateur Photographer — Android camera photography tips, 인물·제품은 살리고 배경은 정리하고 싶을 때, PetaPixel — 10 tips and tricks for better smartphone photos, TechRadar — Android phone photography tips, 후보정을 크게 할 사진을 찍을 때 — 노을, 야경, 실내, 공연, 역광, Landscape and architecture composition, 사진 전체 필터가 아니라 특정 색만 고치고 싶을 때, Tyler Stalman YouTube
- size 11: 스마트폰으로 자연스러운 인물 사진을 찍을 때, Night mode / low-light shooting, iPhone Photography School YouTube, 스마트폰으로 자연스러운 인물 사진을 찍을 때, Apple Support — iPhone Night mode, Portrait and subject separation, National Geographic — Camera phone pictures, 스마트폰으로 자연스러운 인물 사진을 찍을 때
- size 8: 2015~2016: VSCO / Hipstamatic / 앱 프리셋 시대, 2024: Reels/vertical-first / text overlay / mixed media, 2026 현재 적용 방향: 덜 완벽하지만 더 정확한 국소 보정, 2012~2014: 기본 Instagram 필터 / 고채도 / 비네트, 2018~2019: 따뜻한 여행 인플루언서 / orange-teal / curated feed, 2025: cinematic / low-fi / AI-assisted / texture, 2022: no-filter / photo dump / authenticity, SNS 인물·여행 사진 보정 트렌드 타임라인
- size 7: 2x Portrait, Skin Tone, Subject Mask, Reflection, Subject, Face, Rain Neon Street
- size 6: Samsung Support — Camera modes and settings, Samsung Explore — Master low-light photography with Galaxy, Long exposure / light drawing, 달 촬영 — 사용자가 예시로 든 “10배 줌 + Pro mode” 케이스, Moon photography / Pro mode, 갤럭시로 달 표면을 선명하게 찍고 싶을 때
- size 6: Style 3. Food glow / delicious warm editorial, Style 4. Film look / nostalgic grain, Style 6. Snow clean high-key, Style 1. Teal & Orange cinematic, 전문가/인기 스타일 보정 레시피 — Lightroom Mobile 중심, Style 2. Bright pastel beach / airy travel
- size 5: Google Photos Help, AI cleanup / object removal, Apple Support — Apple Intelligence in Photos, 사진 속 작은 방해물·먼지·사람·쓰레기를 지우고 싶을 때, 사진 속 작은 방해물·먼지·사람·쓰레기를 지우고 싶을 때
- size 4: Skin Tone Preference, Skin Retouch Strength, Outfit Color Priority, Personalized Recommendation
- size 4: Trend Recommendation, Spring Blossom, Playful Visual Hook, Seasonal Fall Color
- size 3: 인스타그램·틱톡·블로그에 올릴 최종본을 만들 때, Social crop, framing, and export, TIME — Apple Instagram celebrates iPhone photographers

## Unified wiki link graph

- components: 19
- largest component: 1548/1599 (96.8%)
- isolates: 12

### Wiki isolates
- `scene_nodes/scene__Tilted horizon__issue_tilted_horizon`
- `scene_nodes/scene__Storytelling__out_storytelling`
- `source_nodes/source__Woman__tok_woman`
- `source_nodes/source__Maple Tree__tok_maple_tree`
- `source_nodes/source__Reddit food_product photography restaurant tips__evidence_reddit_foodphotography_restaurant`
- `source_nodes/source__Astrophotography _ night sky__astrophotography_night_sky`
- `source_nodes/source__Moment capture _ burst__moment_capture_burst`
- `source_nodes/source__iPhone Portrait Distance and Depth__iphone_portrait_distance_depth`
- `source_nodes/source__Reddit food photography menu tips__evidence_reddit_foodphotography_menu`
- `source_nodes/source__Backlight__tok_backlight`
- `_guides/Scene-first Graph Report`
- `_guides/Source Graph Report`

## 개선 제안

### 우선순위 높음
- `CompositionIssue` / `TechnicalIssue` generic 노드를 관련 scenario에 더 연결한다. 예: `tilted_horizon → cafe_flatlay_dessert`, `motion_blur → pets_children_action/concert_stage_low_light`, `mixed_white_balance → dim_restaurant_food/museum_gallery_portrait`.
- `Outcome` 노드 중 `Storytelling`, `Texture detail`을 관련 recommendation에 연결한다. 예: `marketplace_street_food_story → Storytelling`, `cafe_drink_dessert_closeup → Texture detail`.
- guide-level evidence nodes를 scenario로 연결한다. 예: food guide → food scenarios, zoom guide → lens scenarios, trend guide → trend recommendations.

### 우선순위 중간
- source graph의 isolated token nodes는 alias/정규화 테이블로 합친다. 예: `Woman`, `subject:woman`, `tok_woman`.
- source graph에서 scenario index가 너무 큰 bridge가 되므로, scenario별 source evidence를 더 직접 연결한다.

### 우선순위 낮음
- Obsidian report 파일 자체는 독립이어도 큰 문제는 없다. 원하면 HOME에서 report로 링크를 추가하면 된다.
