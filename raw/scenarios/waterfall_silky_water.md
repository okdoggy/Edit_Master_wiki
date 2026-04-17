---
title: "폭포·계곡 물결 — 장노출/Live 효과"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "waterfall"
  - "river"
  - "long-exposure"
  - "nature"
  - "tripod"
graph_nodes:
  - "subject:waterfall"
  - "environment:nature"
  - "mode:live_or_pro"
  - "lens:1x_0.5x"
  - "setting:long_exposure"
  - "edit_style:nature_green"
graph_edges:
  - "moving_water BENEFITS_long_exposure"
  - "tripod STABILIZES_scene"
  - "green_foliage NEEDS_control"
  - "polarizing_effect UNAVAILABLE_on_phone_without_filter"
urls:
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
---

# 폭포·계곡 물결 — 장노출/Live 효과

## 추천 시스템용 요약

- **트렌드 추천:** 자연 여행에서는 부드러운 물결/폭포 장노출이 전문적인 느낌을 준다.
- **일반 추천:** 일반 추천은 삼각대+긴 셔터 또는 Live Photo long exposure 효과, 물과 바위/나무를 함께 구성.
- **개인화 추천 변수:** 개인화는 선명한 물방울/몽환 실키 워터/짙은 숲톤 선호 반영.

## 촬영 레시피

- 삼각대/바위에 고정.
- iPhone Live Photo를 찍고 Long Exposure 효과를 시도하거나, Pro mode에서 1/4~2s 테스트.
- 밝은 낮에는 셔터가 길어지기 어려우므로 그늘/해질녘 추천.
- 전경 바위/잎을 넣어 깊이감.

## 보정 레시피

- Highlights -20~-50, Shadows +10~+30.
- Green Saturation -5~-20로 네온 녹색 방지.
- Texture +5~+15 for rocks, water는 Clarity 낮게.
- Dehaze +3~+10.

## 실패 방지 / 주의점

- 손持ち 장노출은 배경까지 흔들린다.
- 밝은 낮 장노출은 ND필터 없이는 한계.

## Graphify 추출 힌트

```yaml
entities:
  - subject:waterfall
  - environment:nature
  - mode:live_or_pro
  - lens:1x_0.5x
  - setting:long_exposure
  - edit_style:nature_green
relationships:
  - moving_water BENEFITS_long_exposure
  - tripod STABILIZES_scene
  - green_foliage NEEDS_control
  - polarizing_effect UNAVAILABLE_on_phone_without_filter
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
