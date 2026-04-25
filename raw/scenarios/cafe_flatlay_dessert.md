---
title: "카페 디저트 플랫레이 — 수평과 왜곡 잡기"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "food"
  - "cafe"
  - "flatlay"
  - "dessert"
  - "coffee"
  - "geometry"
aliases:
  - "카페 플랫레이"
  - "디저트 위에서 찍기"
  - "커피 디저트 테이블 삐뚤"
  - "접시 왜곡"
  - "라떼아트 탑뷰"
  - "브런치 플랫레이"
query_aliases:
  - "카페 플랫레이"
  - "디저트 위에서 찍기"
  - "커피 디저트 테이블 삐뚤"
  - "접시 왜곡"
  - "라떼아트 탑뷰"
  - "브런치 플랫레이"
graph_nodes:
  - "subject:dessert_coffee"
  - "environment:cafe_table"
  - "composition:flatlay_topview"
  - "lens:1x_or_0_5x"
  - "edit_style:food_cafe_warm"
  - "risk:tilted_table"
  - "risk:edge_distortion"
graph_edges:
  - "grid_level FIXES_tilted_table"
  - "1x REDUCES_plate_distortion"
  - "0_5x FITS_large_table_but_distorts_edges"
  - "geometry_edit STRAIGHTENS_table"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 카페 디저트 플랫레이 — 수평과 왜곡 잡기

## 추천 시스템용 요약

- **트렌드 추천:** 카페 감성은 깔끔한 정렬, 여백, 따뜻한 색, 과하지 않은 질감이 trend 후보.
- **일반 추천:** 일반 추천은 1x와 그리드/수평을 우선하고 0.5x는 공간 부족할 때만 쓴다.
- **개인화 추천 변수:** 사용자가 미니멀/풍성한 소품/따뜻한 카페톤 중 무엇을 선호하는지 반영.

## 촬영 레시피

- Grid/Level을 켜고 완전 탑뷰로 맞춘다.
- 가능하면 의자에 올라가 1x로 찍고, 공간이 부족할 때만 0.5x.
- 접시와 컵이 가장자리에서 잘리지 않게 여백을 둔다.
- 손/스푼/냅킨은 1~2개만 포인트로 둔다.

## 보정 레시피

- Crop/Geometry로 테이블 수평을 먼저 맞춘다.
- Exposure +0.2~+0.5, Highlights -10~-25, Shadows +10~+20.
- Whites +5~+15, Vibrance +3~+8, Texture +3~+10.
- 흰 접시 기준으로 WB를 맞춘다.

## 실패 방지 / 주의점

- 0.5x로 가까이 찍으면 접시가 타원형으로 늘어난다.
- 소품이 많으면 음식보다 배경이 먼저 보인다.

## 근거

### 반영한 외부 근거

- Adobe mobile food tutorial은 음식 사진을 모바일에서 light/color/preset으로 마무리하는 기본 흐름을 준다.
- Google Pixel food tips는 음식 디테일을 위해 가까이 가고 배경 흐림을 활용하는 방식, shade/low-light 대응을 설명한다.
- Samsung Food mode 문서는 highlighted area와 blur effect를 공식화한다.
- 음식 사진 커뮤니티 피드백에서는 white balance, tripod/consistent framing, 자연광이 반복적으로 나온다.

### 시나리오 수정 포인트

- 플랫레이는 0.5x보다 **1x + 높이 확보 + grid/level**을 우선한다.
- 넓게 담아야 할 때만 0.5x를 쓰고, 접시가 가장자리에서 늘어나는 것을 위험으로 둔다.
- 카페 디저트는 “맛있게”보다 **정렬/여백/화이트밸런스**가 먼저다.

## Graphify 추출 힌트

```yaml
aliases:
  - 카페 플랫레이
  - 디저트 위에서 찍기
  - 커피 디저트 테이블 삐뚤
  - 접시 왜곡
  - 라떼아트 탑뷰
  - 브런치 플랫레이
entities:
  - subject:dessert_coffee
  - environment:cafe_table
  - composition:flatlay_topview
  - lens:1x_or_0_5x
  - edit_style:food_cafe_warm
  - risk:tilted_table
  - risk:edge_distortion
relationships:
  - grid_level FIXES_tilted_table
  - 1x REDUCES_plate_distortion
  - 0_5x FITS_large_table_but_distorts_edges
  - geometry_edit STRAIGHTENS_table
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.reddit.com/r/foodphotography/comments/1n6jnmx/food_photography_tips_on_restaurant_menu/

- https://www.samsung.com/us/support/answer/ANS10001377/

- https://blog.google/products/pixel/four-tips-taking-delectable-food-photos-pixel-2/

- https://helpx.adobe.com/ph_fil/lightroom-cc/how-to/mobile-food-photography.html

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
