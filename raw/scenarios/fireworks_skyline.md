---
title: "불꽃놀이와 스카이라인 — 하이라이트 보호/연속 확보"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "fireworks"
  - "night"
  - "skyline"
  - "burst"
  - "long-exposure"
aliases:
  - "불꽃놀이 사진"
  - "불꽃 하이라이트 날림"
  - "스카이라인 불꽃놀이"
  - "밤하늘 불꽃 연사"
  - "fireworks skyline"
graph_nodes:
  - "subject:fireworks"
  - "environment:night_skyline"
  - "mode:night_or_pro"
  - "lens:1x_0.5x"
  - "setting:low_iso"
  - "risk:overexposure"
graph_edges:
  - "fireworks ARE_bright_subject"
  - "low_iso PROTECTS_color"
  - "wide_lens CAPTURES_context"
  - "burst_video CAPTURES_peak_shape"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
---

# 불꽃놀이와 스카이라인 — 하이라이트 보호/연속 확보

## 추천 시스템용 요약

- **트렌드 추천:** 불꽃 사진은 시즌 이벤트 트렌드. 넓은 도시 맥락+피크 순간+반사 구도가 강함.
- **일반 추천:** 일반 추천은 넓게 잡고 낮은 ISO/하이라이트 보호, 짧은 영상으로 순간 확보.
- **개인화 추천 변수:** 개인화는 선명한 기록/몽환 장노출/도시 스카이라인 강조 선호 반영.

## 촬영 레시피

- 0.5x/1x로 하늘과 스카이라인을 함께 담는다.
- 삼각대 고정, 타이머 사용.
- Pro 가능 시 ISO 50~100, 셔터 1/2~2s부터 테스트.
- 어렵다면 4K video로 찍고 피크 프레임 캡처.

## 보정 레시피

- Highlights -50~-100, Whites -10~-40.
- Blacks -10~-25로 하늘 정리.
- Saturation +5~+15, 색별 과포화 주의.
- Noise Reduction +10~+30.

## 실패 방지 / 주의점

- Night mode auto가 너무 길면 불꽃이 뭉개진다.
- 연기가 많아지기 전 초반 컷이 깨끗하다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:fireworks
  - environment:night_skyline
  - mode:night_or_pro
  - lens:1x_0.5x
  - setting:low_iso
  - risk:overexposure
relationships:
  - fireworks ARE_bright_subject
  - low_iso PROTECTS_color
  - wide_lens CAPTURES_context
  - burst_video CAPTURES_peak_shape
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
