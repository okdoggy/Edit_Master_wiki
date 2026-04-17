---
title: "공연·무대 저조도 — 망원/하이라이트 보호"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "concert"
  - "stage"
  - "low-light"
  - "telephoto"
  - "performance"
graph_nodes:
  - "subject:performer"
  - "environment:stage"
  - "light:spotlight"
  - "lens:3x_5x_10x"
  - "mode:photo_or_pro"
  - "edit_style:moody_stage"
  - "risk:highlight_clipping"
graph_edges:
  - "spotlight CAUSES_clipping"
  - "telephoto REACHES_stage"
  - "fast_shutter FREEZES_motion"
  - "noise_reduction BALANCES_detail"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/"
  - "https://support.google.com/pixelcamera/answer/9708795?hl=en"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
---

# 공연·무대 저조도 — 망원/하이라이트 보호

## 추천 시스템용 요약

- **트렌드 추천:** 콘서트/페스티벌 SNS trend는 공연자 표정, 빛기둥, 관객 실루엣, 짧은 영상+스틸 조합.
- **일반 추천:** 일반 추천은 하이라이트를 살리고 흔들림을 줄이며 3x/5x로 프레임을 채우는 것.
- **개인화 추천 변수:** 개인화는 영상 선호/스틸 선호, 노이즈 허용, moody 색감 선호에 맞춤.

## 촬영 레시피

- 3x/5x optical 우선, 너무 멀면 10x 기록용.
- 스포트라이트가 밝으면 EV -0.7~-1.3.
- 움직임이 빠르면 Night mode보다 일반 Photo/Burst/Video.
- 난간/몸에 팔꿈치 고정.

## 보정 레시피

- Highlights -40~-80, Whites -10~-30.
- Shadows +5~+20 또는 moody면 Blacks -10~-25.
- Noise Reduction +15~+35, Sharpen +10~+25.
- 색 조명은 완전 중립으로 만들지 말고 분위기 유지.

## 실패 방지 / 주의점

- Night mode 장노출은 공연자를 흐리게 만든다.
- 디지털 줌으로 과하게 당기면 디테일이 뭉개진다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:performer
  - environment:stage
  - light:spotlight
  - lens:3x_5x_10x
  - mode:photo_or_pro
  - edit_style:moody_stage
  - risk:highlight_clipping
relationships:
  - spotlight CAUSES_clipping
  - telephoto REACHES_stage
  - fast_shutter FREEZES_motion
  - noise_reduction BALANCES_detail
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/
- https://support.google.com/pixelcamera/answer/9708795?hl=en
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
