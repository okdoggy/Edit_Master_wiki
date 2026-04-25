---
title: "카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "cafe"
  - "drink"
  - "dessert"
  - "closeup"
  - "macro"
  - "texture"
aliases:
  - "라떼아트 사진"
  - "케이크 클로즈업"
  - "크림 질감"
  - "커피 거품 찍기"
  - "디저트 접사"
  - "카페 음료 사진"
query_aliases:
  - "라떼아트 사진"
  - "케이크 클로즈업"
  - "크림 질감"
  - "커피 거품 찍기"
  - "디저트 접사"
  - "카페 음료 사진"
graph_nodes:
  - "subject:cafe_drink_dessert"
  - "environment:cafe_table"
  - "light:side_or_back_light"
  - "lens:2x_or_macro"
  - "mode:photo_or_macro"
  - "edit_style:food_glow"
  - "risk:highlight_reflection"
  - "risk:focus_miss"
graph_edges:
  - "side_light_reveals_texture"
  - "2x_compresses_dessert"
  - "macro_shows_foam_detail"
  - "highlights_need_protection"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 카페 음료·디저트 클로즈업 — 질감과 반짝임 살리기

## 추천 시스템용 요약

- **트렌드 추천:** 카페 클로즈업은 투명감, 크림/거품 질감, 따뜻한 editorial tone이 trend 후보.
- **일반 추천:** 일반 추천은 2x 또는 macro, 옆빛/역광, 하이라이트 보호, 질감 강조.
- **개인화 추천 변수:** 사용자가 부드러운 감성/선명한 질감 중 무엇을 선호하는지 반영.

## 촬영 레시피

- 컵/케이크 전체는 1x/2x, 거품/시럽/크림은 macro 또는 2x.
- 창가 사광/역광으로 유리컵 반짝임을 만든다.
- 초점은 크림 결, 라떼아트, 시럽 라인에 맞춘다.
- 하이라이트가 반짝이면 EV -0.3.

## 보정 레시피

- Exposure +0.1~+0.3, Highlights -10~-30, Shadows +5~+15.
- Whites +5~+15, Temp +5~+10.
- Texture +5~+15, Clarity 0~+5.
- Background Saturation -5~-15로 시선 정리.

## 실패 방지 / 주의점

- macro는 초점 실패가 잦으니 여러 장 찍는다.
- Clarity를 과하게 올리면 크림이 딱딱해 보인다.

## 근거

### 반영한 외부 근거

- Google Pixel food tips는 Portrait Mode로 음식 디테일과 배경 흐림을 만들고, 음료/과일 같은 동작은 slow motion도 활용할 수 있다고 설명한다.
- Adobe mobile food tutorial은 모바일에서 음식 사진을 촬영하고 light/color/preset으로 마무리하는 흐름을 준다.
- Samsung Food mode는 Food mode의 색온도와 blur effect를 공식 지원한다.
- 음식 사진 커뮤니티에서는 자연광, window light, WB, texture를 반복적으로 강조한다.

### 시나리오 수정 포인트

- 카페 음료/디저트는 “접사”만이 아니라 **유리컵 반짝임, 크림 질감, 층 구조**가 핵심이다.
- macro가 실패하면 2x로 한 발 물러나 찍는 대체 경로를 포함한다.

## Graphify 추출 힌트

```yaml
aliases:
  - 라떼아트 사진
  - 케이크 클로즈업
  - 크림 질감
  - 커피 거품 찍기
  - 디저트 접사
  - 카페 음료 사진
entities:
  - subject:cafe_drink_dessert
  - environment:cafe_table
  - light:side_or_back_light
  - lens:2x_or_macro
  - mode:photo_or_macro
  - edit_style:food_glow
  - risk:highlight_reflection
  - risk:focus_miss
relationships:
  - side_light_reveals_texture
  - 2x_compresses_dessert
  - macro_shows_foam_detail
  - highlights_need_protection
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.reddit.com/r/productphotography/comments/1sn1msr/how_to_get_foodrestaurant_photos_like_these/

- https://www.samsung.com/us/support/answer/ANS10001377/

- https://helpx.adobe.com/ph_fil/lightroom-cc/how-to/mobile-food-photography.html

- https://blog.google/products/pixel/four-tips-taking-delectable-food-photos-pixel-2/

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
