---
title: "한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "beach"
  - "noon"
  - "harsh-sun"
  - "portrait"
  - "sky"
  - "shadow"
query_aliases:
  - "한낮 해변 인물"
  - "해변 얼굴 그림자"
  - "하늘 날아감"
  - "정오 바닷가 사진"
  - "햇빛 너무 셈"
  - "해변 인물 보정"
graph_nodes:
  - "subject:person"
  - "environment:noon_beach"
  - "light:harsh_overhead_sun"
  - "lens:1x_2x_portrait"
  - "mode:photo_or_portrait"
  - "edit_style:bright_blue_travel"
  - "risk:harsh_shadow"
  - "risk:blown_highlights"
graph_edges:
  - "harsh_sun CAUSES_face_shadow"
  - "sky_mask RECOVERS_highlights"
  - "subject_mask LIFTS_face"
  - "2x_portrait REDUCES_distortion"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 한낮 해변 인물 — 강한 그림자와 날아간 하늘 잡기

## 추천 시스템용 요약

- **트렌드 추천:** 청량한 blue travel 스타일은 유지하되 얼굴 그림자는 부드럽게 줄이는 방향.
- **일반 추천:** 일반 추천은 그늘/측광으로 옮기고 하늘 노출을 보호한 뒤 얼굴만 마스크로 밝히는 것.
- **개인화 추천 변수:** 사용자가 청량한 파랑/따뜻한 노을/자연색 중 무엇을 선호하는지 반영.

## 촬영 레시피

- 가능하면 정오 직사광을 피하고 파라솔/건물 그림자/open shade를 찾는다.
- 2x/Portrait로 인물 왜곡을 줄이고, 하늘은 프레임 일부만 남긴다.
- 촬영 시 EV -0.3~-0.7로 하늘을 보호한다.
- 얼굴에 반사광이 오도록 흰 모래/벽을 활용한다.

## 보정 레시피

- Sky mask: Highlights -30~-60, Dehaze +5~+12.
- Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.
- Blue Luminance -5~-20, Orange Luminance +5~+15.
- 피부가 너무 주황이면 Orange Saturation -5~-10.

## 실패 방지 / 주의점

- 정면 직사광은 눈 찡그림과 코 그림자를 만든다.
- 하늘을 살리려고 전체 노출을 낮추면 얼굴이 죽는다.

## 전문가/커뮤니티 근거 반영

### 반영한 외부 근거

- Adobe beach photography tips와 golden hour 자료는 해변 사진에서 빛의 시간대와 방향이 결과를 크게 좌우한다고 설명한다.
- Google Pixel travel tips는 HDR, volume button 셔터, Light/Color/Pop 조정으로 여행 사진을 다듬는 흐름을 제시한다.
- Adobe/portrait lighting 계열 자료는 얼굴에 부드러운 빛을 주고 역광/측광을 활용하는 원칙을 제공한다.

### 시나리오 수정 포인트

- 한낮 해변은 “보정으로 해결”보다 **그늘/측광/반사광 위치로 이동**하는 게 먼저다.
- 하늘은 전체 노출이 아니라 sky mask/highlights로 다루고, 얼굴은 subject mask로 따로 살린다.

## Graphify 추출 힌트

```yaml
aliases:
  - 한낮 해변 인물
  - 해변 얼굴 그림자
  - 하늘 날아감
  - 정오 바닷가 사진
  - 햇빛 너무 셈
  - 해변 인물 보정
entities:
  - subject:person
  - environment:noon_beach
  - light:harsh_overhead_sun
  - lens:1x_2x_portrait
  - mode:photo_or_portrait
  - edit_style:bright_blue_travel
  - risk:harsh_shadow
  - risk:blown_highlights
relationships:
  - harsh_sun CAUSES_face_shadow
  - sky_mask RECOVERS_highlights
  - subject_mask LIFTS_face
  - 2x_portrait REDUCES_distortion
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html

- https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/

- https://www.adobe.com/creativecloud/photography/technique/golden-hour.html

- https://blog.adobe.com/en/publish/2022/10/27/beach-photography-tips-techniques

- ttps://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- ttps://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- ttps://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- ttps://www.adobe.com/learn/lightroom-cc/web/color-adjustment
