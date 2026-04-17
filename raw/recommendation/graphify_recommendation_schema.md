---
title: "Graphify 추천 연결 스키마 — 스마트폰 촬영/보정"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "graphify_recommendation_schema"
---

# Graphify 추천 연결 스키마 — 스마트폰 촬영/보정

이 문서는 `raw/scenarios`, `raw/techniques`, `raw/trends`의 팁을 graphify로 wiki화한 뒤 추천 시스템에 연결하기 위한 노드/엣지 설계다.

## 추천 타입 3종

### 1. 트렌드 추천

**정의**
- 현재/최근 SNS·시즌·플랫폼에서 강한 신호를 보이는 촬영/보정 스타일.

**입력 신호**
- season: autumn, winter, spring, summer.
- platform: Instagram, TikTok, Reels, Stories.
- trend_style: cinematic, authentic, grainy, warm travel, no-filter, pink, film.
- recency: 2024, 2025, 2026.

**예시**
- 단풍나무 아래 여성 → `autumn + portrait + foliage + warm_foliage + leaf_foreground + 4:5`.

### 2. 일반 추천

**정의**
- 많은 사용자에게 안정적으로 만족스러운 결과를 주는 evergreen 촬영 원칙.

**입력 신호**
- subject clarity.
- flattering light.
- face/eye sharpness.
- background separation.
- highlight preservation.
- color harmony.

**예시**
- 단풍나무 아래 여성 → `2x/Portrait + golden hour/backlight + subject mask + foliage saturation`.

### 3. 개인화 추천

**정의**
- 사용자의 과거 사진 취향, 선호 보정, 자주 찍는 피사체/장소에 맞춘 변형.

**입력 신호**
- preferred_style: bright, moody, film, cinematic, natural, pastel.
- preferred_subject_size: close-up, half-body, full-body, environmental.
- skin_retouch_strength: none, subtle, strong.
- color_preference: warm, cool, muted, vibrant.
- device: iPhone, Galaxy, Pixel.
- editing_tool: Lightroom, native Photos, Google Photos, Samsung Gallery.

**예시**
- 같은 단풍 인물이라도 사용자가 `moody_cinematic`을 선호하면 단풍 채도를 덜 올리고 shadows cool + grain으로 추천.

## Graphify node taxonomy

```yaml
node_types:
  subject:
    - woman
    - man
    - couple
    - group
    - child
    - pet
    - food
    - flower
    - architecture
  environment:
    - autumn_maple_tree
    - beach
    - cafe_window
    - night_neon_street
    - snow
    - market
    - concert_stage
  light:
    - golden_hour
    - backlight
    - diffused_window
    - overcast
    - neon
    - spotlight
    - mixed_indoor
  capture:
    - lens_0_5x
    - lens_1x
    - lens_2x
    - lens_3x
    - lens_5x
    - zoom_10x_plus
    - portrait_mode
    - night_mode
    - food_mode
    - pro_raw
    - macro
  edit:
    - subject_mask
    - sky_mask
    - background_mask
    - color_mix
    - hsl
    - grain
    - cinematic_color_grade
    - warm_foliage
    - natural_skin
  recommendation_signal:
    - trend_signal
    - general_satisfaction_signal
    - personalization_signal
```

## Edge patterns

```yaml
edge_patterns:
  - subject IN environment
  - environment HAS light
  - light SUPPORTS capture_mode
  - capture_mode USES lens
  - lens AFFECTS distortion
  - edit_style MATCHES trend_signal
  - subject_mask PROTECTS skin_tone
  - background_mask ENHANCES separation
  - personal_preference MODIFIES edit_style
  - trend_signal RANKS recommendation
  - satisfaction_signal VALIDATES general_recommendation
```

## 단풍나무 아래 여성 예시

```yaml
query_scene:
  subject: woman
  environment: autumn_maple_tree
  season: autumn
  possible_light:
    - golden_hour
    - backlight
    - overcast
recommendations:
  trend:
    - warm_foliage portrait
    - leaf foreground framing
    - 4:5 Instagram crop
    - subtle film grain
  general:
    - 2x or 3x portrait
    - subject 1-3m from background
    - face/eyes sharp
    - EV -0.3~-0.7 for sky/highlights
    - subject mask protects skin
  personalized:
    if_user_likes_bright:
      - Exposure +0.2~+0.5
      - Texture -5~-12
      - pastel orange/yellow
    if_user_likes_cinematic:
      - Contrast +15~+30
      - shadows cool
      - highlights warm
      - Grain +15~+30
    if_user_likes_natural:
      - modest saturation
      - preserve skin texture
      - WB accurate
```

## 추천 랭킹에 쓸 수 있는 점수 후보

- `source_confidence`: official / reputable / creator / inferred.
- `actionability`: 수치/순서가 구체적인가.
- `scenario_match`: subject/environment/light가 입력 장면과 얼마나 맞는가.
- `trend_recency`: 최근 트렌드와 가까운가.
- `personal_style_match`: 사용자 선호 스타일과 가까운가.
- `risk_penalty`: 과보정, 움직임 blur, 왜곡, 개인정보/윤리 위험.

## 표준 메타데이터 연결

표준 기반 필드와 추천용 추론 필드의 상세 매핑은 `raw/recommendation/metadata_standards_mapping.md`에 정리했다. Schema.org ImageObject/Photograph, IPTC Photo Metadata, IPTC Media Topics, Exif/CIPA를 사용해 원천 메타데이터와 추천 노드를 분리한다.

## 출처

- https://www.cipa.jp/e/std/std-sec.html
- https://www.iptc.org/std/photometadata/documentation/userguide/
- https://schema.org/Photograph
- https://schema.org/ImageObject
- https://business.adobe.com/resources/creative-trends-report.html
- https://newsroom.tiktok.com/year-on-tiktok-2024
- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://www.samsung.com/us/explore/photography/how-to-pull-off-the-perfect-fall-photoshoot/
