---
title: "해변 역광 인물 — 여름/휴양지 SNS 스타일"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "beach"
  - "backlight"
  - "portrait"
  - "summer"
  - "travel"
  - "blue-orange"
aliases:
  - "해변 역광 인물"
  - "휴양지 인물 사진"
  - "바다에서 인물 보정"
  - "여름 여행 프로필"
  - "beach backlit portrait"
graph_nodes:
  - "subject:person"
  - "environment:beach"
  - "light:backlight_golden_hour"
  - "lens:2x_portrait"
  - "edit_style:warm_blue_travel"
  - "risk:blown_highlights"
graph_edges:
  - "backlight CREATES_hair_glow"
  - "beach_reflects_light"
  - "sky_mask PROTECTS_cloud_detail"
  - "2x_portrait FLATTERS_face"
urls:
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/"
  - "https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
---

# 해변 역광 인물 — 여름/휴양지 SNS 스타일

## 추천 시스템용 요약

- **트렌드 추천:** 여름/여행 trend는 해변 golden hour, 하늘/바다 blue, 피부 warm, 4:5 portrait.
- **일반 추천:** 사람들이 좋아하는 일반값은 얼굴이 어둡지 않고 하늘/바다 디테일이 살아있는 균형.
- **개인화 추천 변수:** 사용자가 청량한 blue/따뜻한 sunset/film grain 중 선호하는 룩 반영.

## 촬영 레시피

- 해가 낮을 때 피사체 뒤나 45도 뒤에 두어 rim light를 만든다.
- 2x/Portrait로 인물, 0.5x로 장소 전체 컷도 함께.
- 하늘 기준으로 EV -0.3~-0.7, 얼굴은 후보정에서 mask로 보정.
- 바닷가 수평선은 Level/Grid로 맞춘다.

## 보정 레시피

- Sky mask: Highlights -30~-60, Dehaze +5~+12.
- Subject mask: Exposure +0.2~+0.5, Shadows +10~+25.
- Blue Luminance -5~-20, Orange Luminance +5~+15.
- Warm travel이면 Temp +300~+900K.

## 실패 방지 / 주의점

- 직사광 정면 얼굴은 눈 찡그림/강한 그림자 발생.
- 바다/하늘 채도를 너무 올리면 인공적.

## 근거

### 반영한 외부 근거

- Apple Portrait 문서는 인물과 배경 분리, 조명 효과, Depth Control 조절을 공식적으로 설명한다.
- Google Pixel 여행 사진 자료와 National Geographic 스마트폰 사진 팁은 여행지에서 빛·장소감·구도를 함께 보는 근거가 된다.
- Adobe Lightroom masking/color 자료는 얼굴 마스크, 하늘/배경 하이라이트, 색 보정을 분리하는 후처리 흐름을 제공한다.

### 시나리오 수정 포인트

- 해변 역광은 얼굴 밝기와 하늘 보존을 같은 슬라이더로 해결하지 않고 subject/sky 영역을 분리한다.
- 여름 travel look은 파란 하늘과 피부톤이 동시에 과포화되지 않도록 제한한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person
  - environment:beach
  - light:backlight_golden_hour
  - lens:2x_portrait
  - edit_style:warm_blue_travel
  - risk:blown_highlights
relationships:
  - backlight CREATES_hair_glow
  - beach_reflects_light
  - sky_mask PROTECTS_cloud_detail
  - 2x_portrait FLATTERS_face
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
