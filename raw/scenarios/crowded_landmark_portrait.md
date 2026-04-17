---
title: "관광지 랜드마크 인물 — 사람 많은 배경 정리"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "travel"
  - "landmark"
  - "crowd"
  - "portrait"
  - "tourist"
query_aliases:
  - "관광지 사람 많음"
  - "랜드마크 앞 인물"
  - "배경 관광객 지저분"
  - "여행 인물 배경 정리"
  - "명소 사진"
graph_nodes:
  - "subject:person"
  - "environment:crowded_landmark"
  - "light:daylight_or_golden_hour"
  - "lens:2x_3x_or_1x"
  - "mode:photo_or_portrait"
  - "edit_style:warm_travel"
  - "risk:busy_background"
  - "risk:scale_lost"
graph_edges:
  - "2x_3x_compresses_background"
  - "early_late_time_reduces_crowd"
  - "remove_tool_cleans_distractions"
  - "scale_subject_shows_landmark_size"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 관광지 랜드마크 인물 — 사람 많은 배경 정리

## 추천 시스템용 요약

- **트렌드 추천:** 여행지 인물은 장소감과 인물 선명도를 함께 살리는 carousel/travel style이 trend 후보.
- **일반 추천:** 일반 추천은 시간대/위치/망원 압축으로 배경을 줄이고 필요한 방해물은 제거하는 것.
- **개인화 추천 변수:** 사용자가 장소 중심/인물 중심 중 무엇을 선호하는지 반영.

## 촬영 레시피

- 사람이 적은 아침/해질녘 시간대를 노린다.
- 랜드마크 전체 컷 1장, 2x/3x 인물 컷 1장, 디테일 컷 1장을 세트로 찍는다.
- 배경 관광객이 인물 머리와 겹치지 않게 옆으로 이동한다.
- 밝은 하늘은 EV -0.3~-0.7.

## 보정 레시피

- Subject mask로 인물 Exposure +0.1~+0.3.
- Background Saturation -5~-20, Clarity -5~-15.
- Remove/Heal로 작은 방해물 제거.
- Geometry로 건축 수직 보정.

## 실패 방지 / 주의점

- Remove로 큰 사람 무리를 지우려 하면 티가 난다.
- 초광각으로 가까이 찍으면 얼굴/몸 왜곡이 커진다.

## 전문가/커뮤니티 근거 반영

### 반영한 외부 근거

- Google Pixel travel tips는 HDR, volume button shutter, 여행지에서 Light/Color/Pop으로 미세 조정하는 흐름을 제시한다.
- National Geographic camera-phone tips는 빛, 구도, 배경 정리와 자연광을 강조한다.
- Adobe smartphone photography guide는 accessory, tripod, composition, editing workflow를 포함한다.

### 시나리오 수정 포인트

- 사람 많은 관광지는 보정 이전에 **시간대/위치/렌즈 압축**으로 배경을 줄여야 한다.
- 추천은 “랜드마크 전체 1장 + 2x/3x 인물 1장 + 디테일 1장” 세트로 제공하는 게 좋다.

## Graphify 추출 힌트

```yaml
aliases:
  - 관광지 사람 많음
  - 랜드마크 앞 인물
  - 배경 관광객 지저분
  - 여행 인물 배경 정리
  - 명소 사진
entities:
  - subject:person
  - environment:crowded_landmark
  - light:daylight_or_golden_hour
  - lens:2x_3x_or_1x
  - mode:photo_or_portrait
  - edit_style:warm_travel
  - risk:busy_background
  - risk:scale_lost
relationships:
  - 2x_3x_compresses_background
  - early_late_time_reduces_crowd
  - remove_tool_cleans_distractions
  - scale_subject_shows_landmark_size
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html

- https://www.nationalgeographic.com/photography/article/camera-phone-photos

- https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/

- ttps://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- ttps://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- ttps://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- ttps://www.adobe.com/learn/lightroom-cc/web/color-adjustment
