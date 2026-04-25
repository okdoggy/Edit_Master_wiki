---
title: "Personalization preference expansion - trend-aware photo recommendation signals"
category: "recommendation"
updated_at: "2026-04-25"
content_type: "personalization_preference_expansion"
scenario_tags:
  - "personalization"
  - "preference_profile"
  - "trend_reranking"
  - "style_recipe"
  - "recommendation_variant"
practical_tags:
  - "natural"
  - "cinematic"
  - "warm"
  - "low_retouch"
  - "film_grain"
  - "authentic"
  - "bright_airy"
  - "flash"
graph_nodes:
  - "personalization_signal:edit_strength"
  - "personalization_signal:warmth_coolness"
  - "personalization_signal:brightness_contrast"
  - "personalization_signal:saturation_vibrance"
  - "personalization_signal:grain_retro"
  - "personalization_signal:skin_texture_retouch"
  - "personalization_signal:candid_vs_polished"
  - "personalization_signal:platform_intent"
  - "personalization_signal:place_story_depth"
  - "personalization_signal:identity_story"
  - "preference:natural_low_edit"
  - "preference:warm_glow"
  - "preference:cool_cinematic"
  - "preference:bright_airy"
  - "preference:film_grain_nostalgia"
  - "preference:flash_editorial"
  - "preference:low_retouch_skin"
  - "preference:photo_dump_story"
  - "preference:local_texture"
  - "edit_style:raw_human_documentary"
  - "edit_style:flash_on_candid"
  - "edit_style:bright_airy_clean"
  - "edit_style:cinematic_teal_warm"
  - "edit_style:food_glow_texture"
  - "edit_style:film_look"
  - "edit_style:local_color_story"
  - "style_recipe:adaptive_preset_start_then_customize"
  - "style_recipe:subject_mask_skin_protection"
  - "style_recipe:platform_crop_variant"
  - "recommendation_variant:trend"
  - "recommendation_variant:general"
  - "recommendation_variant:personalized"
  - "parameter:preset_amount"
  - "parameter:subject_mask_exposure"
  - "parameter:background_saturation"
  - "parameter:grain_amount"
  - "parameter:color_temperature"
  - "evidence:adobe_lightroom_presets_mobile"
  - "evidence:adobe_lightroom_masking"
  - "evidence:adobe_2026_creative_trends"
  - "evidence:tiktok_next_2026"
  - "evidence:youtube_personally_relevant_pop_culture"
  - "evidence:meta_instagram_trend_talk"
  - "evidence:petapixel_2026_authenticity"
graph_edges:
  - "personalization_signal:edit_strength MODIFIES parameter:preset_amount"
  - "personalization_signal:warmth_coolness MODIFIES parameter:color_temperature"
  - "personalization_signal:grain_retro MODIFIES parameter:grain_amount"
  - "personalization_signal:skin_texture_retouch MODIFIES style_recipe:subject_mask_skin_protection"
  - "personalization_signal:platform_intent MODIFIES style_recipe:platform_crop_variant"
  - "personalization_signal:candid_vs_polished RERANKS recommendation_variant:personalized"
  - "personalization_signal:place_story_depth RERANKS edit_style:local_color_story"
  - "preference:natural_low_edit ADAPTS_TO edit_style:raw_human_documentary"
  - "preference:flash_editorial ADAPTS_TO edit_style:flash_on_candid"
  - "preference:bright_airy ADAPTS_TO edit_style:bright_airy_clean"
  - "preference:cool_cinematic ADAPTS_TO edit_style:cinematic_teal_warm"
  - "preference:film_grain_nostalgia ADAPTS_TO edit_style:film_look"
  - "style_recipe:adaptive_preset_start_then_customize SETS parameter:preset_amount"
  - "style_recipe:subject_mask_skin_protection SETS parameter:subject_mask_exposure"
  - "style_recipe:subject_mask_skin_protection SETS parameter:background_saturation"
  - "recommendation_variant:personalized SUPPORTED_BY evidence:adobe_lightroom_presets_mobile"
  - "recommendation_variant:personalized SUPPORTED_BY evidence:adobe_lightroom_masking"
  - "recommendation_variant:trend SUPPORTED_BY evidence:adobe_2026_creative_trends"
  - "recommendation_variant:trend SUPPORTED_BY evidence:tiktok_next_2026"
  - "recommendation_variant:personalized SUPPORTED_BY evidence:youtube_personally_relevant_pop_culture"
urls:
  - "https://www.adobe.com/learn/lightroom-cc/web/use-presets-in-lightroom-mobile"
  - "https://helpx.adobe.com/lightroom-cc/using/presets-lightroom-ios.html"
  - "https://www.adobe.com/products/photoshop-lightroom/masking.html"
  - "https://business.adobe.com/resources/creative-trends-report.html"
  - "https://blog.adobe.com/en/publish/2025/12/09/four-creative-trends-define-marketing-2026"
  - "https://newsroom.tiktok.com/introducing-tiktok-next-2026-our-trend-forecast-for-marketers-for-the-year-ahead?lang=en"
  - "https://ads.tiktok.com/business/en-US/next"
  - "https://blog.youtube/culture-and-trends/culture-trends-report-gen-z-multiformat-shorts-creator-pop-culture/"
  - "https://support.google.com/youtube/answer/10059070"
  - "https://about.fb.com/news/2023/12/2024-instagram-trend-talk-indian-gen-z-are-trend-setters/"
  - "https://petapixel.com/2026/01/22/the-top-five-photography-trends-of-2026/"
---

# Personalization preference expansion - trend-aware photo recommendation signals

## 수집 목적

개인화는 "사용자가 좋아할 것 같은 필터"를 붙이는 단계가 아니라, 같은 `Scenario`에서 trend/general/personalized 추천을 다르게 랭킹하고 파라미터 강도를 바꾸는 신호다.

권장 흐름:

```text
Scenario
+ TrendSignal
+ PersonalizationSignal
-> EditStyle / StyleRecipe
-> RecommendationVariant
-> Technique / Parameter
-> Evidence
```

이미지 이슈는 스타일 선택을 대체하지 않는다. `underexposed_face`, `red_eye_flash_glare`, `mixed_white_balance` 같은 이슈는 파라미터의 안전 범위를 조정하는 guardrail로만 둔다.

## 근거 기반 개인화 축

### 1. Edit strength

**의미**
- 사용자가 강한 보정, 은은한 보정, 거의 무보정을 선호하는지 나타낸다.
- Adobe Lightroom mobile 문서는 preset을 시작점으로 쓰고 sliders로 커스터마이즈할 수 있다고 설명한다. Lightroom iOS presets 문서는 Recommended/Premium preset과 style/intensity 필터, preset Amount 조절을 제공한다고 설명한다.

**입력 신호**
- "티 안 나게", "자연스럽게", "필터 느낌 세게", "요즘 감성 확 나게".
- 사용자가 이전에 `strong_edit`를 거절했거나 `natural`, `low_retouch`에 높은 rating을 준 경우.

**추천 변환**
- 낮은 강도: `parameter:preset_amount` 20~45%, Saturation -5~+5, Texture -5~+5.
- 중간 강도: preset amount 45~70%, Color Mix는 피부 보호 후 적용.
- 높은 강도: preset amount 70~100%, 단 피부/하이라이트 guardrail 유지.

**Graphify**
```yaml
personalization_signal: edit_strength
modifies:
  - parameter:preset_amount
  - parameter:saturation_vibrance
  - parameter:contrast
guardrails:
  - skin_tone_shift
  - blown_highlight
```

### 2. Warmth / coolness

**의미**
- 따뜻한 감성, 차가운 시네마틱, 중립 색을 선호하는지 나타낸다.
- Adobe 2026 trend의 All the Feels / Local Flavor는 감각, 질감, 장소성을 강조하므로, WB는 단순 정확도뿐 아니라 기억의 온도를 표현하는 개인화 파라미터가 된다.

**입력 신호**
- "따뜻하게", "카페 감성", "차분하게", "영화처럼", "겨울 느낌".

**추천 변환**
- `preference:warm_glow`: Temp +300~+900K, Orange/Yellow Saturation +5~+12.
- `preference:cool_cinematic`: Shadows에 blue/teal 약하게, Blacks -5~-20, 피부 Orange 보호.
- `preference:natural_low_edit`: WB를 회색/피부 기준으로 먼저 맞추고 색 보정은 작게.

**주의**
- 음식은 너무 차갑게 만들면 맛있어 보이는 질감이 줄어든다.
- 눈/겨울 사진은 파란 그림자를 모두 제거하지 말고 피부만 따뜻하게 조정한다.

### 3. Brightness / contrast

**의미**
- 밝고 맑은 결과, 어둡고 깊은 결과, 플래시 대비가 강한 결과 중 무엇을 선호하는지 나타낸다.

**입력 신호**
- "화사하게", "깨끗하게", "무드 있게", "콘트라스트 있게", "플래시 느낌".

**추천 변환**
- `preference:bright_airy`: Exposure +0.2~+0.5, Highlights -20~-45, Shadows +10~+30.
- `preference:cool_cinematic`: Contrast +10~+25, Blacks -5~-20, Highlights -10~-30.
- `preference:flash_editorial`: face/glare mask 먼저 만든 뒤 global Contrast +5~+20.

**Graphify**
```yaml
personalization_signal: brightness_contrast
reranks:
  - edit_style:bright_airy_clean
  - edit_style:cinematic_teal_warm
  - edit_style:flash_on_candid
sets:
  - parameter:exposure
  - parameter:contrast
  - parameter:highlights
  - parameter:blacks
```

### 4. Saturation / vibrance

**의미**
- 풍부한 색, 낮은 채도, 플랫폼에서 눈에 띄는 색, 정확한 색을 구분한다.

**입력 신호**
- "쨍하게", "빈티지하게", "차분하게", "먹음직스럽게", "피부 자연스럽게".

**추천 변환**
- 음식/카페: Vibrance +5~+12, Orange/Yellow Saturation +5~+15, Green Saturation -5~-15.
- 자연/여행: sky/foliage는 Color Mix로 분리하고 피부는 subject mask로 보호.
- 2016 nostalgia: Saturation +5~+15, Tint +5~+15 magenta.
- natural: Saturation -5~+5, Vibrance +0~+8.

**근거**
- Lightroom masking 문서는 subject/sky/color/luminance range mask를 통해 특정 영역만 조정할 수 있다고 설명한다. 따라서 개인화 색 취향은 전체 사진에 무조건 적용하지 말고 피사체와 배경을 분리해 적용한다.

### 5. Grain / retro / analog tolerance

**의미**
- 사용자가 그레인, 흐림, 플래시 그림자, 2016 필터, 필름 느낌을 감성으로 받아들이는지 나타낸다.

**근거**
- PetaPixel은 2026 사진 트렌드에서 analog/film의 인기가 진정성 및 불완전성과 연결된다고 정리한다.
- Digital Camera World는 레트로 사진 감성에서 grain, blur, direct flash가 다시 쓰인다고 설명한다.

**추천 변환**
- `preference:film_grain_nostalgia`: Grain +15~+35, Contrast -5~+10, black point 살짝 올림.
- `preference:flash_editorial`: Grain +10~+25, Blacks -5~-20.
- `preference:natural_low_edit`: Grain 0~+10, ISO 노이즈가 많으면 추가하지 않는다.

**Guardrail**
- 얼굴 클로즈업, 제품 사진, 문서/영수증 인식 시 grain을 낮춘다.
- 저조도 노이즈가 이미 큰 사진은 grain 대신 색 노이즈 감소를 먼저 한다.

### 6. Skin texture / retouch strength

**의미**
- 피부 결 보존, 은은한 정리, 강한 보정 선호를 구분한다.

**근거**
- Adobe Lightroom masking은 subject mask와 brush를 통해 특정 영역만 조정할 수 있고, nondestructive로 조정 가능하다고 설명한다.
- 2026 authenticity 관련 보도는 실제 텍스처와 감정, 연결성을 중요한 신호로 제시한다.

**추천 변환**
- `preference:low_retouch_skin`: Texture -5~-10, Clarity -3~0, 피부 Hue/Saturation은 작게.
- `preference:natural_low_edit`: 잡티 제거보다 노출/WB 정리 우선.
- `preference:clean_influencer`: face mask로 Texture -10~-20, 단 눈/입/머리카락은 선명도 유지.

**Guardrail**
- 얼굴이 어두우면 피부 보정보다 `subject_mask_exposure` +0.1~+0.4가 먼저다.
- 피부가 주황/마젠타로 치우치면 preset amount를 낮추고 Orange/Red HSL을 분리한다.

### 7. Candid vs polished

**의미**
- 사용자가 즉흥적인 순간, BTS, photo dump, paparazzi flash를 선호하는지, 아니면 정돈된 editorial/profile 이미지를 원하는지 나타낸다.

**근거**
- TikTok Next 2026은 인간성, 유머, 불완전함, 실제 대화를 강조한다.
- Vogue는 패션 캠페인에서 candid/lo-fi처럼 보이는 paparazzi 이미지가 진정성 수요와 연결되어 반복적으로 쓰였다고 분석한다.
- PetaPixel은 정체성 기반 사진과 narrative-driven 이미지를 2026 신호로 정리한다.

**추천 변환**
- candid 높음: burst, walking shot, 표정 변화, 주변 단서 유지, crop은 느슨하게.
- polished 높음: eye sharpness, 수평/수직 정리, 배경 간소화, 피부/의상 디테일 정리.
- flash candid 높음: direct flash를 허용하되 red eye/glare를 guardrail로 둔다.

### 8. Platform intent

**의미**
- 같은 사진도 Instagram carousel, TikTok discovery, YouTube Shorts, 프로필 사진, 블로그용에 따라 crop/sequence/text-safe area가 달라진다.

**근거**
- YouTube Shorts 공식 도움말은 vertical videos를 Shorts로 업로드할 수 있고 Shorts feed, 검색, 홈 등에서 발견될 수 있다고 설명한다.
- YouTube Culture & Trends Report는 개인적으로 관련 있는 콘텐츠가 중요하다는 Gen Z 조사 결과를 제시한다.
- Meta/Instagram Trend Talk는 Gen Z의 fandom, DIY, day-in-the-life, relatable content 선호를 보여준다.

**추천 변환**
- Instagram feed/carousel: 4:5 cover, story sequence, 색 일관성.
- TikTok/Shorts cover: 9:16, 얼굴/핵심 피사체 중앙, 자막 영역 고려.
- 프로필/데이트앱: 얼굴 선명도, 자연광, 배경 정보는 적당히.
- 커뮤니티/후기: 디테일 컷, 전후/과정 컷, 로컬 단서 포함.

### 9. Place story depth

**의미**
- 배경을 지우는 깔끔함보다 장소와 문화 단서를 살릴지 판단한다.

**근거**
- Adobe 2026 Local Flavor는 특정 장소와 문화에 뿌리내린 진정성을 강조한다.
- TikTok Curiosity Detours는 사용자가 새로운 탐색 경로와 예상 밖의 답을 찾는다고 설명한다.

**추천 변환**
- 여행/시장/축제: background saturation을 완전히 낮추지 않고 핵심 색 1~2개를 보존한다.
- 카페/식당: 테이블 질감, 메뉴, 간판, 손동작을 보조 컷으로 남긴다.
- 인물 중심 요청이면 장소 단서는 frame edge에 남기고 얼굴/눈 우선.

### 10. Identity story

**의미**
- 인물 사진에서 "예쁘게"보다 "이 사람의 취향/직업/성격/브랜드"를 드러내려는 선호다.

**근거**
- PetaPixel 2026 트렌드는 portrait가 단순한 portrait가 아니라 identity가 된다고 설명한다.
- YouTube/Meta 자료는 개인적 관련성, creator/community, fandom, relatable content의 중요성을 보여준다.

**추천 변환**
- 직업/창작자: 작업 도구, 장소, 손동작, 의상 질감 포함.
- 데이트/프로필: 과한 retouch보다 표정, 빛, 배경 신뢰감 우선.
- 패션/OOTD: 실루엣과 옷 질감, walking candid, flash editorial 변형.

## 개인화 프로필 확장안

```json
{
  "preferences": {
    "edit_strength": 0.0,
    "warmth": 0.0,
    "cool_cinematic": 0.0,
    "brightness": 0.0,
    "contrast": 0.0,
    "saturation": 0.0,
    "grain": 0.0,
    "skin_retouch": 0.0,
    "natural_texture": 0.0,
    "candid_energy": 0.0,
    "polished_editorial": 0.0,
    "flash_editorial": 0.0,
    "place_storytelling": 0.0,
    "photo_dump_sequence": 0.0,
    "identity_story": 0.0
  },
  "platform_intent_weights": {
    "instagram_feed": 1.0,
    "instagram_carousel": 1.0,
    "tiktok_vertical": 1.0,
    "youtube_shorts": 1.0,
    "profile_photo": 1.0,
    "blog_review": 1.0
  },
  "scenario_affinity": {
    "paparazzi_flash_candid": 0.0,
    "window_light_cafe_portrait": 0.0,
    "marketplace_street_food_story": 0.0,
    "dating_profile_natural_portrait": 0.0
  },
  "issue_sensitivity": {
    "red_eye_flash_glare": 1.0,
    "skin_tone_shift": 1.0,
    "blown_highlight": 1.0,
    "motion_blur_face": 1.0,
    "busy_background": 0.5
  }
}
```

## 추천 랭킹 규칙

1. 안전 guardrail 먼저 적용: 얼굴 노출, 하이라이트 복구, 피부 색, 레드아이, 심한 모션블러.
2. Scenario와 TrendSignal 매칭: 계절, 플랫폼, 장면, 로컬 단서, candid/flash 여부.
3. PreferenceProfile로 `RecommendationVariant` rerank: 사용자가 좋아한 스타일을 올리고 거절한 태그를 내린다.
4. StyleRecipe는 고정값이 아니라 시작값: Adobe preset처럼 빠른 출발점으로 쓰고, 장면/취향에 따라 Amount와 mask를 조정한다.
5. Evidence가 약한 트렌드는 추천 문구에서 단정하지 않는다. "요즘 일부 SNS/패션 캠페인에서 보이는"처럼 출처 강도에 맞게 표현한다.

## Scenario -> StyleRecipe 매핑 예시

```yaml
scenario: paparazzi_flash_candid
trend_signal:
  - direct_flash_retro_candid
  - reali_tea_unfiltered_story
preferences:
  high_flash_editorial:
    style_recipe: direct_flash_controlled_highlight
    parameters:
      highlights: -20_to_-45
      whites: -5_to_+10
      blacks: -5_to_-20
      grain: +10_to_+25
  high_natural_low_edit:
    style_recipe: soft_flash_low_retouch
    parameters:
      highlights: -15_to_-30
      texture: -5_to_0
      saturation: -5_to_+5
guardrails:
  red_eye_flash_glare: local_correction_first
  motion_blur_face: choose_sharper_frame_first
```

```yaml
scenario: window_light_cafe_portrait
trend_signal:
  - authentic_human_moment
  - local_flavor_place_specificity
preferences:
  high_warm_glow:
    style_recipe: warm_cafe_skin_protected
    parameters:
      temp: +300_to_+700K
      shadows: +10_to_+25
      orange_luminance: +5_to_+12
  high_clean_profile:
    style_recipe: natural_profile_light
    parameters:
      exposure: +0.1_to_+0.3
      texture: -5_to_-10
      background_saturation: -5_to_-15
guardrails:
  mixed_white_balance: correct_skin_before_style
  busy_background: crop_or_mask_before_blur
```

```yaml
scenario: marketplace_street_food_story
trend_signal:
  - local_flavor_place_specificity
  - photo_dump_bts_sequence
preferences:
  high_place_storytelling:
    style_recipe: local_food_texture_sequence
    parameters:
      texture: +10_to_+25
      vibrance: +5_to_+12
      orange_yellow_saturation: +5_to_+15
      green_saturation: -5_to_-15
  high_natural:
    style_recipe: documentary_food_memory
    parameters:
      exposure: +0.0_to_+0.3
      saturation: -5_to_+5
      grain: 0_to_+10
guardrails:
  mixed_light: set_food_white_balance_first
  blown_highlight: recover_plate_highlights
```

## Graphify 추출 노트

```yaml
entities:
  personalization_signal:
    - edit_strength
    - warmth_coolness
    - brightness_contrast
    - saturation_vibrance
    - grain_retro
    - skin_texture_retouch
    - candid_vs_polished
    - platform_intent
    - place_story_depth
    - identity_story
  preference:
    - natural_low_edit
    - warm_glow
    - cool_cinematic
    - bright_airy
    - film_grain_nostalgia
    - flash_editorial
    - low_retouch_skin
    - photo_dump_story
    - local_texture
  style_recipe:
    - adaptive_preset_start_then_customize
    - subject_mask_skin_protection
    - platform_crop_variant
relationships:
  - PersonalizationSignal MODIFIES Parameter
  - PersonalizationSignal RERANKS RecommendationVariant
  - Preference ADAPTS_TO EditStyle
  - StyleRecipe SETS Parameter
  - ImageIssue CONSTRAINS Parameter
  - Evidence SUPPORTS RecommendationVariant
extraction_priority:
  - scenario
  - trend_signal
  - preference
  - edit_style
  - style_recipe
  - recommendation_variant
  - technique
  - parameter
  - evidence
```

## 출처와 신뢰 메모

- Adobe Learn, Lightroom mobile presets - official docs on presets as starting points and customizable edit settings. URL: https://www.adobe.com/learn/lightroom-cc/web/use-presets-in-lightroom-mobile
- Adobe Help, Lightroom for mobile iOS presets - official docs on Recommended/Premium presets, style filters, adaptive presets, and intensity/amount workflow. URL: https://helpx.adobe.com/lightroom-cc/using/presets-lightroom-ios.html
- Adobe Lightroom masking - official docs on subject/sky/color/luminance masks and nondestructive local edits. URL: https://www.adobe.com/products/photoshop-lightroom/masking.html
- Adobe 2026 Creative Trends Forecast - official trend report for authenticity, sensory content, connection, local flavor. URL: https://business.adobe.com/resources/creative-trends-report.html
- Adobe Blog, 2026 creative trends - official summary of human, sensory, playful, local culture trend direction. URL: https://blog.adobe.com/en/publish/2025/12/09/four-creative-trends-define-marketing-2026
- TikTok Next 2026 - official platform trend forecast for Reali-TEA, Curiosity Detours, Emotional ROI. URL: https://newsroom.tiktok.com/introducing-tiktok-next-2026-our-trend-forecast-for-marketers-for-the-year-ahead?lang=en
- TikTok Next 2026 report page - official guidance on tracking real-time sentiment, language, and trends. URL: https://ads.tiktok.com/business/en-US/next
- YouTube Culture & Trends Report - official Gen Z personally relevant content signal. URL: https://blog.youtube/culture-and-trends/culture-trends-report-gen-z-multiformat-shorts-creator-pop-culture/
- YouTube Shorts Help - official vertical/Shorts creation and discovery documentation. URL: https://support.google.com/youtube/answer/10059070
- Meta/Instagram Trend Talk - official Instagram/Meta survey reference for Gen Z relatability, fandom, DIY, day-in-the-life. URL: https://about.fb.com/news/2023/12/2024-instagram-trend-talk-indian-gen-z-are-trend-setters/
- PetaPixel, 2026 photography trends - professional photography source on authenticity, analog, identity-driven portraiture. URL: https://petapixel.com/2026/01/22/the-top-five-photography-trends-of-2026/
