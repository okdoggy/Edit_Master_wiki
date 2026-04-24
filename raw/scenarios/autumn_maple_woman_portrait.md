---
title: "단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "autumn"
  - "maple"
  - "woman"
  - "portrait"
  - "foliage"
  - "golden-hour"
  - "personalization-seed"
aliases:
  - "단풍 인물"
  - "가을 프로필 사진"
  - "단풍나무 아래 여자"
  - "가을 색감 보정"
  - "autumn foliage portrait"
graph_nodes:
  - "subject:woman"
  - "environment:autumn_maple_tree"
  - "light:golden_hour_or_backlight"
  - "lens:2x_3x_portrait"
  - "mode:portrait_or_photo"
  - "edit_style:warm_foliage"
  - "trend_signal:seasonal_fall_color"
  - "personal_signal:skin_tone_preference"
  - "satisfaction_signal:clear_face_warm_background"
graph_edges:
  - "woman UNDER maple_tree"
  - "autumn_foliage SUPPORTS warm_color_grade"
  - "2x_3x REDUCES face_distortion"
  - "backlight CREATES rim_light"
  - "subject_mask PROTECTS skin_tone"
  - "leaf_foreground CREATES depth"
urls:
  - "https://www.samsung.com/us/explore/photography/how-to-pull-off-the-perfect-fall-photoshoot/"
  - "https://iphonephotographyschool.com/fall/"
  - "https://iphonephotographyschool.com/leaves/"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 단풍나무 아래 여성 인물 — 트렌드/일반/개인화 추천 seed

## 추천 시스템용 요약

- **트렌드 추천:** 가을 시즌에는 단풍색을 살린 warm foliage, 얕은 심도, leaf foreground framing, 역광 rim light가 trend 후보.
- **일반 추천:** 사람들이 만족하기 쉬운 기본값은 얼굴은 선명하고 피부색은 자연스럽게, 배경 단풍은 따뜻하고 풍부하게, 가장자리 잎으로 깊이를 만드는 방식.
- **개인화 추천 변수:** 사용자가 평소 warm/film/cinematic 중 무엇을 선호하는지, 피부 보정 강도, 채도 선호, 얼굴 클로즈업 vs 전신샷 선호를 반영.

## 촬영 레시피

- 2x/3x 또는 Portrait mode로 얼굴 왜곡을 줄인다.
- 단풍잎을 전경에 걸쳐 프레임을 만들고, 피사체와 배경 나무 사이를 1~3m 이상 벌린다.
- 해 질 무렵 역광/측광에서 머리카락 rim light가 생기게 위치를 잡는다.
- 밝은 하늘이 있으면 EV -0.3~-0.7로 하이라이트를 보호한다.
- 잎을 뿌리는 액션은 Burst/Live/8K Video Snap류로 여러 프레임 확보.

## 보정 레시피

- Subject mask: Exposure +0.1~+0.3, Texture -5~0.
- Background/foliage mask: Orange/Yellow Saturation +5~+18, Luminance +0~+10.
- Green이 탁하면 Green Saturation -10~-25, Yellow Hue를 orange 쪽으로 약간.
- 전체 Temp +300~+900K, Tint +2~+6.
- Film trend이면 Grain +10~+25, cinematic이면 Shadows를 살짝 cool.

## 실패 방지 / 주의점

- 단풍 채도를 과하게 올리면 피부도 주황색이 된다. Subject mask로 피부를 분리한다.
- 0.5x 인물은 얼굴/몸 왜곡 위험이 크다.
- 그늘이 너무 깊으면 얼굴보다 배경이 먼저 예뻐지는 실패가 생긴다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:woman
  - environment:autumn_maple_tree
  - light:golden_hour_or_backlight
  - lens:2x_3x_portrait
  - mode:portrait_or_photo
  - edit_style:warm_foliage
  - trend_signal:seasonal_fall_color
  - personal_signal:skin_tone_preference
  - satisfaction_signal:clear_face_warm_background
relationships:
  - woman UNDER maple_tree
  - autumn_foliage SUPPORTS warm_color_grade
  - 2x_3x REDUCES face_distortion
  - backlight CREATES rim_light
  - subject_mask PROTECTS skin_tone
  - leaf_foreground CREATES depth
recommendation_modes:
  - trend
  - general
  - personalized
```

## 추가 검증 인물 시작값 — 여성 + 나무 아래 / 가을 포트레이트

**촬영 시작값**
- 렌즈: 가능하면 2x, 없으면 1x.
- 모드: Portrait / Live Focus / Photo+Depth.
- 포즈: 얼굴은 고른 그늘 쪽, 몸은 30~45도 틀기.
- 구도: 눈을 상단 1/3 근처, 배경은 단순하게.
- 빛: 나무 아래 open shade를 쓰되 얼굴에 반점광이 떨어지지 않게 한다.
- 노출: -0.3~0 시작.

**Lightroom 피부/단풍 시작값**
- Profile: Adobe Portrait.
- Temp +5~+8, Tint +2~+4.
- Vibrance +8~+12.
- Orange Saturation -5~-10.
- Orange Luminance +8~+15.

**추천 연결 해석**
- 트렌드 추천은 단풍색/warm/cinematic을 올릴 수 있지만, 개인화 추천에서 피부 자연색 선호가 강하면 Orange Saturation을 더 낮춘다.

- https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone
- https://www.samsung.com/us/explore/photography/how-to-pull-off-the-perfect-fall-photoshoot/
- https://iphonephotographyschool.com/fall/
- https://iphonephotographyschool.com/leaves/
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment

- https://www.adobe.com/learn/lightroom-cc/web/photo-filters
