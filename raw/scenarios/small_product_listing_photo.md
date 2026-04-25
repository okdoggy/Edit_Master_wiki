---
title: "집에서 제품 판매 사진 — 깨끗한 썸네일 만들기"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "product"
  - "listing"
  - "home"
  - "thumbnail"
  - "commerce"
  - "clean-background"
aliases:
  - "중고거래 사진"
  - "제품 판매 사진"
  - "쇼핑몰 썸네일"
  - "집에서 제품 찍기"
  - "배경 지저분 제품"
  - "상품 사진"
query_aliases:
  - "중고거래 사진"
  - "제품 판매 사진"
  - "쇼핑몰 썸네일"
  - "집에서 제품 찍기"
  - "배경 지저분 제품"
  - "상품 사진"
graph_nodes:
  - "subject:product"
  - "environment:home_table"
  - "light:window_light"
  - "lens:1x_2x"
  - "mode:photo_or_macro"
  - "edit_style:clean_product"
  - "risk:color_inaccuracy"
  - "risk:busy_background"
graph_edges:
  - "window_light_reveals_product_shape"
  - "1x_2x_controls_distortion"
  - "white_background_improves_listing"
  - "color_accuracy_builds_trust"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 집에서 제품 판매 사진 — 깨끗한 썸네일 만들기

## 추천 시스템용 요약

- **트렌드 추천:** 판매용 사진은 유행보다 정확하고 깨끗한 정보 전달이 중요.
- **일반 추천:** 일반 추천은 창가 자연광, 단순 배경, 1x/2x, 색 정확도, 먼지/방해물 제거.
- **개인화 추천 변수:** 사용자가 감성 썸네일/정확한 상품정보 중 무엇을 원하는지 반영.

## 촬영 레시피

- 창가 옆빛에 흰 종이/천/벽을 배경으로 둔다.
- 1x로 전체, 2x로 로고/상태/질감 디테일.
- 제품과 카메라를 평행하게 두어 형태 왜곡을 줄인다.
- 작은 제품은 macro보다 2x로 한 발 물러나 비교.

## 보정 레시피

- WB를 정확히 맞춰 실제 색과 가깝게.
- Exposure +0.1~+0.4, Highlights -10~-30, Shadows +10~+20.
- Texture +5~+20, Clarity +3~+10.
- 배경은 Saturation -10~-30 또는 Remove로 정리.

## 실패 방지 / 주의점

- 색을 과하게 예쁘게 만들면 실제 상품과 달라 신뢰가 떨어진다.
- 광택 제품은 창문/손 반사가 보일 수 있다.

## 근거

### 반영한 외부 근거

- Shopify product photography help는 smartphone 사용 가능, natural light, shadow side, background retouch/white background 정리를 언급한다.
- Shopify phone product photography article은 white backdrop이 빛을 반사해 균일한 조명을 만든다고 설명한다.
- Etsy Seller Handbook은 자연광을 쓰되 직사광을 피하고, 일관된 밝은 배경을 추천한다.
- Adobe product photography는 스마트폰도 활용 가능하지만 제품 사진에서는 조명 일관성과 retouch가 중요하다고 설명한다.
- Etsy/Shopify 커뮤니티는 자연광, 깨끗한 배경, white balance, 제품만 남기는 크롭을 반복적으로 추천한다.

### 시나리오 수정 포인트

- 제품 사진은 트렌디한 색감보다 **색 정확도와 신뢰성**이 우선이다.
- 배경 제거/화이트 배경은 “예쁘게”보다 “상품을 정확히 보여주는” 목적이다.
- 추천 그래프에서 `color_accuracy`와 `satisfaction_signal`을 더 강하게 연결해야 한다.

## Graphify 추출 힌트

```yaml
aliases:
  - 중고거래 사진
  - 제품 판매 사진
  - 쇼핑몰 썸네일
  - 집에서 제품 찍기
  - 배경 지저분 제품
  - 상품 사진
entities:
  - subject:product
  - environment:home_table
  - light:window_light
  - lens:1x_2x
  - mode:photo_or_macro
  - edit_style:clean_product
  - risk:color_inaccuracy
  - risk:busy_background
relationships:
  - window_light_reveals_product_shape
  - 1x_2x_controls_distortion
  - white_background_improves_listing
  - color_accuracy_builds_trust
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.reddit.com/r/Etsy/comments/lu2sjd/etsy_sellers_does_product_photography_frustrate/

- https://www.reddit.com/r/EtsySellers/comments/1qr5f3g/struggle_with_product_photos/

- https://www.adobe.com/creativecloud/photography/discover/product-photography

- https://www.etsy.com/seller-handbook/article/154343798313

- https://www.shopify.com/ie/blog/15163633-how-to-capture-high-quality-product-photos-with-your-smartphone

- https://help.shopify.com/en/manual/products/product-media/product-photography

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
