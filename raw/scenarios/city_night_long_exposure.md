---
title: "도시 야경 장노출 — 빛줄기/스카이라인"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "city-night"
  - "long-exposure"
  - "traffic-trails"
  - "skyline"
  - "tripod"
aliases:
  - "도시 야경 장노출"
  - "차 불빛 궤적"
  - "스카이라인 야경"
  - "폰으로 장노출"
  - "city night long exposure"
graph_nodes:
  - "subject:city_lights"
  - "environment:night_city"
  - "mode:pro_or_night"
  - "lens:1x_2x_5x"
  - "setting:low_iso_long_shutter"
  - "edit_style:moody_cinematic"
graph_edges:
  - "tripod ENABLES_long_exposure"
  - "low_iso REDUCES_noise"
  - "traffic CREATES_light_trails"
  - "highlights NEED_protection"
urls:
  - "https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/"
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.google.com/pixelcamera/answer/9708795?hl=en"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
---

# 도시 야경 장노출 — 빛줄기/스카이라인

## 추천 시스템용 요약

- **트렌드 추천:** 도시 야경은 cinematic night, 빛줄기, 반사, 높은 전망대 구도가 trend 후보.
- **일반 추천:** 일반 추천은 삼각대/고정, 낮은 ISO, 하이라이트 보호, 여러 노출 비교.
- **개인화 추천 변수:** 개인화는 선명한 도시/몽환 빛줄기/로우파이 야경 선호를 반영.

## 촬영 레시피

- 삼각대/난간 고정.
- Galaxy Pro 시작점: ISO 50~200, 2~8s, WB 4300K 전후.
- iPhone/Pixel Night mode는 정적인 스카이라인에 사용.
- 차량 빛줄기는 도로가 프레임을 통과하게 구성.

## 보정 레시피

- Highlights -40~-80, Blacks -10~-30.
- Dehaze +5~+20, Noise Reduction +15~+35.
- Color Grading: shadows cool, highlights warm.
- Geometry로 수평/수직 정리.

## 실패 방지 / 주의점

- 사람/나무가 움직이면 번짐.
- 장노출은 작은 흔들림도 치명적.

## 근거

### 반영한 외부 근거

- Samsung Night Mode와 Apple Night mode 문서는 저조도에서 긴 노출과 흔들림 제어가 중요하다는 공식 근거를 제공한다.
- Google Pixel Night Sight/장노출 자료는 야간 장면에서 카메라를 안정적으로 유지하고 빛의 움직임을 활용하는 방향을 뒷받침한다.
- Adobe Lightroom 모바일 편집 문서는 야경의 노출, 색, 노이즈 보정을 후처리에서 정리하는 근거다.

### 시나리오 수정 포인트

- 야경 장노출은 분위기보다 안정화가 먼저이며, 손持ち 실패 가능성을 전제로 둔다.
- 빛줄기는 살리되 노이즈 감소와 선명도는 과하지 않게 제한한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:city_lights
  - environment:night_city
  - mode:pro_or_night
  - lens:1x_2x_5x
  - setting:low_iso_long_shutter
  - edit_style:moody_cinematic
relationships:
  - tripod ENABLES_long_exposure
  - low_iso REDUCES_noise
  - traffic CREATES_light_trails
  - highlights NEED_protection
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/
- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.google.com/pixelcamera/answer/9708795?hl=en
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
