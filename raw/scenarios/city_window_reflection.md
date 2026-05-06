---
title: "도시 야경 유리창 반사 — 산만한 반사 정리"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "city"
  - "night"
  - "window"
  - "reflection"
  - "neon"
  - "composition"
aliases:
  - "유리창 야경 반사"
  - "도시 야경 반사"
  - "창문에 비친 도시"
  - "반사가 지저분"
  - "호텔 창밖 야경"
  - "네온 반사 사진"
query_aliases:
  - "유리창 야경 반사"
  - "도시 야경 반사"
  - "창문에 비친 도시"
  - "반사가 지저분"
  - "호텔 창밖 야경"
  - "네온 반사 사진"
graph_nodes:
  - "subject:city_lights"
  - "environment:window_reflection_city_night"
  - "light:city_neon"
  - "lens:1x_2x"
  - "mode:night_or_photo"
  - "edit_style:moody_cinematic"
  - "risk:messy_reflection"
  - "risk:blown_city_lights"
graph_edges:
  - "window_reflection CREATES_layering"
  - "dark_clothing REDUCES_self_reflection"
  - "EV_negative PROTECTS_city_lights"
  - "crop_simplifies_reflection"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 도시 야경 유리창 반사 — 산만한 반사 정리

## 추천 시스템용 요약

- **트렌드 추천:** 도시 야경은 reflection/neon/cinematic 톤이 trend 후보.
- **일반 추천:** 일반 추천은 반사를 줄이거나 의도적으로 정리하고, 밝은 도시 조명을 먼저 보호하는 것.
- **개인화 추천 변수:** 사용자가 감성적인 반사/깨끗한 스카이라인 중 무엇을 원하는지 반영.

## 촬영 레시피

- 렌즈를 유리에 최대한 가깝게 대고, 실내 불을 끄거나 어두운 옷을 입는다.
- 반사를 쓸 경우 얼굴/손/조명이 프레임을 방해하지 않게 위치를 잡는다.
- 1x로 전체, 2x로 건물/간판 디테일.
- 밝은 간판이 있으면 EV -0.7~-1.3.

## 보정 레시피

- Highlights -40~-80, Blacks -10~-30, Dehaze +5~+15.
- 반사 영역은 Crop으로 과감히 정리한다.
- Color Grading: Shadows cool, Highlights warm.
- Noise Reduction +15~+35, Grain +10~+25.

## 실패 방지 / 주의점

- 실내 조명이 켜져 있으면 유리창에 방 안이 다 비친다.
- Night mode가 길면 손持ち 사진이 흐려질 수 있다.

## 근거

### 반영한 외부 근거

- B&H city night guide는 도시 야경에서 긴 노출, 혼합 조명, 물/창문 반사, white balance 실험을 다룬다.
- Travel Photography Magazine의 glass shooting tips는 유리에 렌즈를 가깝게 대거나 손/후드로 가리는 것, 약간의 각도 조절, CPL 활용을 설명한다.
- Adobe neon light photography는 네온과 젖은 표면/차체 반사를 활용하는 도시 야간 스타일을 제시한다.
- Reddit AskPhotography/photography 커뮤니티에서는 실내 불 끄기, 어두운 천/렌즈 후드, 유리에 직접 대기 같은 실전 팁이 반복된다.

### 시나리오 수정 포인트

- “반사를 없애는 버전”과 “반사를 의도적으로 쓰는 버전”을 분기한다.
- 실내 조명 끄기, 어두운 옷/천, 렌즈를 유리에 붙이는 방법을 촬영 레시피의 우선순위로 둔다.
- 보정으로 반사를 지우기보다, 촬영 단계에서 반사를 통제하게 한다.

## Graphify 추출 힌트

```yaml
aliases:
  - 유리창 야경 반사
  - 도시 야경 반사
  - 창문에 비친 도시
  - 반사가 지저분
  - 호텔 창밖 야경
  - 네온 반사 사진
entities:
  - subject:city_lights
  - environment:window_reflection_city_night
  - light:city_neon
  - lens:1x_2x
  - mode:night_or_photo
  - edit_style:moody_cinematic
  - risk:messy_reflection
  - risk:blown_city_lights
relationships:
  - window_reflection CREATES_layering
  - dark_clothing REDUCES_self_reflection
  - EV_negative PROTECTS_city_lights
  - crop_simplifies_reflection
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.reddit.com/r/AskPhotography/comments/1rkm1rm/how_can_i_prevent_these_reflections_on_the_glass/

- https://www.reddit.com/r/AskPhotography/comments/1hvpthv/is_there_anyway_to_get_rid_of_the_window/

- https://www.adobe.com/creativecloud/photography/discover/neon-light-photography.html

- https://travelphotographymagazine.com/how-to-photograph-through-glass/60-second/problems/

- https://www.bhphotovideo.com/explora/photography/tips-and-solutions/seven-tips-for-photographing-cities-at-night

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
