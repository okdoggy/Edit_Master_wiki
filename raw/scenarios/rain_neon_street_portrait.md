---
title: "비 오는 밤 네온 거리 인물 — moody city look"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "rain"
  - "neon"
  - "night"
  - "street"
  - "portrait"
  - "moody"
  - "reflection"
graph_nodes:
  - "subject:person"
  - "environment:rain_neon_street"
  - "light:neon_backlight"
  - "mode:night_or_portrait"
  - "lens:1x_2x"
  - "edit_style:moody_cinematic"
  - "risk:motion_blur"
graph_edges:
  - "wet_ground CREATES_reflection"
  - "neon_light CREATES_color_cast"
  - "night_mode INCREASES_exposure_time"
  - "subject_mask FIXES_skin_tone"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.google.com/pixelcamera/answer/9708795?hl=en"
  - "https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://business.adobe.com/resources/creative-trends-report.html"
---

# 비 오는 밤 네온 거리 인물 — moody city look

## 추천 시스템용 요약

- **트렌드 추천:** 최근 SNS에서는 rain/neon/cinematic, 플래시/로우파이, 젖은 노면 반사 스타일이 trend 후보.
- **일반 추천:** 일반 추천은 젖은 바닥 반사를 활용하고, 얼굴은 네온 컬러 캐스트를 줄이는 것.
- **개인화 추천 변수:** 사용자가 moody/cinematic/flash_raw 중 선호하는 야간 스타일을 반영.

## 촬영 레시피

- 젖은 노면이나 유리창 반사를 찾아 피사체를 네온과 반사 사이에 둔다.
- 움직이는 인물은 Night mode 시간을 줄이고 1x/2x로 촬영.
- 정적인 장면은 폰을 기대고 Night mode 또는 Pro 장노출.
- 네온이 날아가면 EV -0.7~-1.3.

## 보정 레시피

- Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15.
- Color Grading: Shadows teal/blue, Highlights warm/magenta.
- Subject mask로 피부 Tint/Temp를 중립에 가깝게.
- Noise Reduction +15~+35, Grain +10~+25로 노이즈를 스타일화.

## 실패 방지 / 주의점

- Night mode가 사람을 흐리게 만들 수 있다.
- 네온 색을 피부에 그대로 두면 얼굴이 초록/보라로 보인다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person
  - environment:rain_neon_street
  - light:neon_backlight
  - mode:night_or_portrait
  - lens:1x_2x
  - edit_style:moody_cinematic
  - risk:motion_blur
relationships:
  - wet_ground CREATES_reflection
  - neon_light CREATES_color_cast
  - night_mode INCREASES_exposure_time
  - subject_mask FIXES_skin_tone
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.google.com/pixelcamera/answer/9708795?hl=en
- https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://business.adobe.com/resources/creative-trends-report.html
