---
title: "실내 생일파티·모임 단체사진 — 어두운 실내와 움직임"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "indoor"
  - "party"
  - "group"
  - "birthday"
  - "low-light"
  - "motion"
query_aliases:
  - "실내 생일파티 사진"
  - "케이크 촛불 단체"
  - "어두운 방 단체사진"
  - "모임 사진 흐림"
  - "파티 사진 보정"
graph_nodes:
  - "subject:group"
  - "environment:indoor_party"
  - "light:warm_low_light"
  - "lens:1x_or_0_5x"
  - "mode:photo_or_night_short"
  - "edit_style:warm_documentary"
  - "risk:motion_blur"
  - "risk:mixed_white_balance"
graph_edges:
  - "group_faces_need_same_plane"
  - "short_night_mode_reduces_blur"
  - "warm_light_supports_party_mood"
  - "timer_improves_group_pose"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 실내 생일파티·모임 단체사진 — 어두운 실내와 움직임

## 추천 시스템용 요약

- **트렌드 추천:** 파티 사진은 완벽한 선명도보다 표정과 따뜻한 분위기가 중요.
- **일반 추천:** 일반 추천은 1x/0.5x, 짧은 Night mode/일반 Photo, 사람을 멈추게 하고 얼굴 WB를 맞추는 것.
- **개인화 추천 변수:** 사용자가 다큐 느낌/깨끗한 단체사진 중 무엇을 선호하는지 반영.

## 촬영 레시피

- 가능하면 조명을 하나 더 켜거나 창/벽 반사광을 활용한다.
- 인원이 많으면 모두 카메라와 비슷한 거리에 서게 한다.
- 움직임이 있으면 긴 Night mode보다 일반 Photo/Burst.
- 타이머 3초 또는 볼륨 버튼 셔터로 흔들림을 줄인다.

## 보정 레시피

- Exposure +0.2~+0.5, Highlights -20~-40, Shadows +15~+35.
- Temp는 분위기를 남기되 얼굴이 너무 노랗지 않게.
- Noise Reduction +15~+35, Texture는 인물에 과하게 올리지 않는다.
- 얼굴별 마스크가 가능하면 가장 어두운 얼굴만 살짝 밝힌다.

## 실패 방지 / 주의점

- 긴 노출은 웃는 표정과 손동작을 흐리게 만든다.
- 단체에 Portrait blur를 과하게 쓰면 일부 얼굴이 흐려질 수 있다.

## 전문가/커뮤니티 근거 반영

### 반영한 외부 근거

- Google Pixel Night Sight in Portrait는 저조도 인물에서 얼굴에 약한 ambient lighting이 필요하고, 여러 장을 정렬/합성해 디테일을 개선한다고 설명한다.
- Apple Night mode 문서는 저조도에서 Night mode가 자동으로 동작하며 안정성이 중요함을 설명한다.
- Samsung Night mode 자료는 AI multi-frame processing과 tripod/steady hold의 중요성을 설명한다.
- Google Pixel group photo features는 그룹 사진에서 Best Take/Add Me 같은 기능이 표정/인원 문제를 돕는 방향을 보여준다.

### 시나리오 수정 포인트

- 파티 단체사진은 긴 장노출보다 **표정/움직임 관리**가 더 중요하다.
- 사람들에게 잠깐 멈추게 하고, 1~2초 내 촬영/연속 확보를 우선한다.
- 촛불/조명 분위기는 살리되 얼굴이 너무 노랗지 않게 WB를 조정한다.

## Graphify 추출 힌트

```yaml
aliases:
  - 실내 생일파티 사진
  - 케이크 촛불 단체
  - 어두운 방 단체사진
  - 모임 사진 흐림
  - 파티 사진 보정
entities:
  - subject:group
  - environment:indoor_party
  - light:warm_low_light
  - lens:1x_or_0_5x
  - mode:photo_or_night_short
  - edit_style:warm_documentary
  - risk:motion_blur
  - risk:mixed_white_balance
relationships:
  - group_faces_need_same_plane
  - short_night_mode_reduces_blur
  - warm_light_supports_party_mood
  - timer_improves_group_pose
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://blog.google/products/pixel/pixel-group-photo-features-ai/

- https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/

- https://blog.google/products-and-platforms/devices/pixel/take-holiday-photos-night-sight-portrait-mode/

- ttps://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- ttps://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- ttps://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- ttps://www.adobe.com/learn/lightroom-cc/web/color-adjustment
