---
title: "꽃·잎 매크로 — 질감과 배경 bokeh"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "macro"
  - "flowers"
  - "leaves"
  - "bokeh"
  - "nature"
graph_nodes:
  - "subject:flower_or_leaf"
  - "environment:nature"
  - "mode:macro"
  - "lens:ultrawide_macro_or_2x"
  - "light:soft_side_light"
  - "edit_style:detail_bokeh"
graph_edges:
  - "macro REVEALS_texture"
  - "soft_light PRESERVES_detail"
  - "background_distance CREATES_bokeh"
  - "color_mix CONTROLS_green"
urls:
  - "https://support.apple.com/en-mz/guide/iphone/iphfaacf2eb0/ios"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html"
  - "https://iphonephotographyschool.com/leaves/"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
---

# 꽃·잎 매크로 — 질감과 배경 bokeh

## 추천 시스템용 요약

- **트렌드 추천:** 꽃/잎 매크로는 계절 추천과 개인 취향 추천에 모두 좋은 evergreen 콘텐츠.
- **일반 추천:** 일반 추천은 가까이보다 초점 성공, 배경 거리, 부드러운 빛.
- **개인화 추천 변수:** 개인화는 선명한 자연 다큐/몽환 bokeh/파스텔 꽃톤 선호 반영.

## 촬영 레시피

- iPhone은 2cm macro, Galaxy/Pixel은 Macro Focus/0.5x/0.6x 동작 확인.
- 피사체 뒤 배경을 멀리 두고, 그늘/흐린 날 빛을 쓴다.
- 초점은 꽃술/잎맥/물방울에 맞춘다.
- 바람이 있으면 Burst/Video.

## 보정 레시피

- Texture +10~+25, Clarity +5~+15.
- Background mask Saturation -5~-20, Subject Saturation +5~+12.
- Green Saturation -10~-25, Yellow/Orange를 계절에 맞게.
- Vignette -5~-15 가능.

## 실패 방지 / 주의점

- 너무 가까이 가면 초점 실패/렌즈 전환 발생.
- 직사광 물방울은 하이라이트가 쉽게 날아감.

## Graphify 추출 힌트

```yaml
entities:
  - subject:flower_or_leaf
  - environment:nature
  - mode:macro
  - lens:ultrawide_macro_or_2x
  - light:soft_side_light
  - edit_style:detail_bokeh
relationships:
  - macro REVEALS_texture
  - soft_light PRESERVES_detail
  - background_distance CREATES_bokeh
  - color_mix CONTROLS_green
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/en-mz/guide/iphone/iphfaacf2eb0/ios
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://iphonephotographyschool.com/leaves/
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
