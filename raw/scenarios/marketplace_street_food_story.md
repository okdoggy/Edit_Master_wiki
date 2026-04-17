---
title: "시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "street-food"
  - "market"
  - "travel"
  - "food"
  - "documentary"
  - "story"
graph_nodes:
  - "subject:street_food"
  - "environment:market"
  - "human_element:hands_vendor"
  - "lens:1x_2x"
  - "shot_set:wide_detail_human"
  - "edit_style:warm_documentary"
graph_edges:
  - "human_hands ADD_story"
  - "2x CAPTURES_texture"
  - "wide_shot ESTABLISHES_place"
  - "consistent_wb CONNECTS_series"
urls:
  - "https://blog.google/products-and-platforms/devices/pixel/four-tips-taking-delectable-food-photos-pixel-2/"
  - "https://iphonephotographyschool.com/food/"
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.nationalgeographic.com/photography/article/people-quick-tips"
---

# 시장·길거리 음식 스토리 — 사람/손/음식/장소 묶기

## 추천 시스템용 요약

- **트렌드 추천:** 여행 SNS에서는 음식 단품보다 손/상인/간판/거리 맥락을 묶은 carousel이 trend 후보.
- **일반 추천:** 일반 추천은 wide-detail-human 3컷 세트와 따뜻한 다큐 톤.
- **개인화 추천 변수:** 개인화는 음식 위주/사람 위주/여행지 분위기 위주 선호를 반영.

## 촬영 레시피

- 1x로 시장/가게 전체, 2x로 음식 질감, 1x/2x로 손이나 조리 장면.
- 조리 불빛/김/기름 윤기를 역광으로 살린다.
- 사람을 찍을 때는 맥락과 예의를 지킨다.
- Photo + 짧은 Video로 소리/움직임도 확보.

## 보정 레시피

- WB를 시리즈 전체에 맞춘다.
- Highlights -20~-50, Shadows +10~+25.
- Texture +10~+20 for food, Grain +10~+25 for documentary.
- Background Saturation -5~-15.

## 실패 방지 / 주의점

- 형광등/노란등 혼합으로 색이 틀어질 수 있어 RAW 권장.
- 사람 얼굴 공개는 동의/맥락 고려.

## Graphify 추출 힌트

```yaml
entities:
  - subject:street_food
  - environment:market
  - human_element:hands_vendor
  - lens:1x_2x
  - shot_set:wide_detail_human
  - edit_style:warm_documentary
relationships:
  - human_hands ADD_story
  - 2x CAPTURES_texture
  - wide_shot ESTABLISHES_place
  - consistent_wb CONNECTS_series
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://blog.google/products-and-platforms/devices/pixel/four-tips-taking-delectable-food-photos-pixel-2/
- https://iphonephotographyschool.com/food/
- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.nationalgeographic.com/photography/article/people-quick-tips
