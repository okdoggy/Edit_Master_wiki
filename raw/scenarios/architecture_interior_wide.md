---
title: "건축·실내 공간 — 초광각 왜곡 제어"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "architecture"
  - "interior"
  - "ultrawide"
  - "geometry"
  - "travel"
aliases:
  - "실내 공간 넓게 찍기"
  - "건축 사진 왜곡"
  - "초광각 실내"
  - "수직선 기울어짐"
  - "architecture ultrawide distortion"
graph_nodes:
  - "subject:building_or_room"
  - "environment:interior"
  - "lens:0.5x_1x"
  - "composition:level_verticals"
  - "edit:geometry_upright"
  - "risk:keystone_distortion"
graph_edges:
  - "ultrawide CAPTURES_space"
  - "tilt CAUSES_keystone"
  - "level CORRECTS_verticals"
  - "geometry_edit RESTORES_lines"
urls:
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://blog.google/products/pixel/how-to-use-camera-coach/"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
---

# 건축·실내 공간 — 초광각 왜곡 제어

## 추천 시스템용 요약

- **트렌드 추천:** 여행/부동산/카페 공간 추천에는 넓게 보여주되 직선이 안정적인 사진이 선호됨.
- **일반 추천:** 일반 추천은 0.5x로 넓게 찍되 폰을 기울이지 않고 중앙 높이에서 수평 유지.
- **개인화 추천 변수:** 개인화는 미니멀/웜톤/시네마틱 공간 선호에 따라 색과 contrast 조절.

## 촬영 레시피

- 0.5x를 쓰되 폰을 위로 기울이지 말고 가슴~눈높이에서 수평.
- 방 모서리보다 정면/대칭 구도를 먼저 시도.
- 창문이 밝으면 EV -0.3~-1.0, HDR/RAW 사용.
- 1x로 디테일 컷도 함께.

## 보정 레시피

- Geometry/Upright/Vertical 수직 보정.
- Highlights -30~-60, Shadows +10~+30.
- 실내 mixed light는 WB를 중립화.
- Warm interior면 Temp +200~+600K, Green cast는 Tint +5~+12.

## 실패 방지 / 주의점

- 0.5x 가장자리 가구/사람 왜곡 주의.
- 수직선이 무너지면 공간이 싸 보인다.

## 근거

### 반영한 외부 근거

- Adobe 스마트폰 사진 가이드는 렌즈 선택, 구도, 빛을 먼저 정리하는 흐름을 제공하고, Lightroom 모바일 문서는 crop/geometry/color 보정으로 후처리 안정성을 보강한다.
- Google Camera Coach 공식 글은 구도와 각도 안내를 통해 촬영 단계에서 공간의 정렬을 개선하는 방향과 맞닿아 있다.
- National Geographic 스마트폰 사진 팁은 장면을 단순화하고 빛과 구도를 먼저 보는 접근을 뒷받침한다.

### 시나리오 수정 포인트

- 실내/건축은 초광각 자체보다 수평·수직 유지와 가장자리 왜곡 제어를 우선한다.
- 보정 단계에서는 전체 색감보다 geometry/upright와 하이라이트 보호를 먼저 적용한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:building_or_room
  - environment:interior
  - lens:0.5x_1x
  - composition:level_verticals
  - edit:geometry_upright
  - risk:keystone_distortion
relationships:
  - ultrawide CAPTURES_space
  - tilt CAUSES_keystone
  - level CORRECTS_verticals
  - geometry_edit RESTORES_lines
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://blog.google/products/pixel/how-to-use-camera-coach/
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
