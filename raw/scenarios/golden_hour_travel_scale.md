---
title: "여행 골든아워 — wide/detail/scale 3컷 추천"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "travel"
  - "golden-hour"
  - "landscape"
  - "scale"
  - "storytelling"
graph_nodes:
  - "subject:traveler"
  - "environment:landmark"
  - "light:golden_hour"
  - "shot_set:wide_detail_scale"
  - "lens:0.5x_1x_2x_5x"
  - "edit_style:warm_travel"
graph_edges:
  - "golden_hour WARMS_skin"
  - "wide_shot ESTABLISHES_location"
  - "detail_shot CREATES_memory"
  - "scale_subject SHOWS_size"
urls:
  - "https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/"
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
---

# 여행 골든아워 — wide/detail/scale 3컷 추천

## 추천 시스템용 요약

- **트렌드 추천:** 여행 trend는 한 장보다 carousel/story: wide, detail, scale을 묶는 방식.
- **일반 추천:** 일반 추천은 장소 전체-사람 포함-디테일을 함께 찍어 만족도 높은 스토리 세트를 만드는 것.
- **개인화 추천 변수:** 사용자의 피드가 미니멀/컬러풀/시네마틱인지에 따라 3컷 톤 통일.

## 촬영 레시피

- 0.5x/1x로 장소 전체, 2x/5x로 디테일, 사람을 넣어 scale 컷 촬영.
- 일출 직후/일몰 직전 측광을 사용.
- 하늘이 밝으면 EV -0.3~-1.0.
- 볼륨 버튼 셔터/격자로 수평 유지.

## 보정 레시피

- 전체 시리즈 WB 통일.
- Highlights -30~-60, Shadows +10~+30.
- Temp +300~+900K, Vibrance +5~+15.
- Geometry/Upright로 건축 수직 보정.

## 실패 방지 / 주의점

- 골든아워 색을 과하게 올리면 피부가 주황색이 된다.
- 한 장만 찍으면 추천 시스템에서 스토리 맥락이 부족하다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:traveler
  - environment:landmark
  - light:golden_hour
  - shot_set:wide_detail_scale
  - lens:0.5x_1x_2x_5x
  - edit_style:warm_travel
relationships:
  - golden_hour WARMS_skin
  - wide_shot ESTABLISHES_location
  - detail_shot CREATES_memory
  - scale_subject SHOWS_size
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/
- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
