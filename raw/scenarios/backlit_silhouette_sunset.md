---
title: "노을 실루엣 — 감성 여행/커플/인물"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "sunset"
  - "silhouette"
  - "backlight"
  - "couple"
  - "travel"
graph_nodes:
  - "subject:person_or_couple"
  - "environment:sunset"
  - "light:strong_backlight"
  - "lens:1x_2x"
  - "edit_style:silhouette_warm"
  - "risk:lost_subject_shape"
graph_edges:
  - "backlight CREATES_silhouette"
  - "negative_exposure PROTECTS_sky"
  - "clear_outline INCREASES_readability"
  - "warm_gradient DRIVES_emotion"
urls:
  - "https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html"
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
---

# 노을 실루엣 — 감성 여행/커플/인물

## 추천 시스템용 요약

- **트렌드 추천:** 노을/실루엣은 계절을 타지 않는 evergreen trend. SNS에서는 작은 사람+큰 하늘 구도도 강함.
- **일반 추천:** 일반 추천은 하늘 노출을 보호하고 피사체 윤곽이 읽히는 포즈를 만드는 것.
- **개인화 추천 변수:** 개인화는 로맨틱/시네마틱/미니멀 선호에 따라 인물 크기와 contrast 조절.

## 촬영 레시피

- 해를 피사체 뒤나 프레임 가장자리에 둔다.
- 하늘 밝은 부분을 탭하고 EV -0.7~-1.7.
- 피사체는 옆모습/팔 간격/드레스 라인처럼 윤곽이 보이게 포즈.
- 1x는 풍경, 2x는 커플/상반신 압축.

## 보정 레시피

- Highlights -30~-60, Blacks -20~-40.
- Temp +500~+1200K, Orange/Red Saturation +5~+20.
- Subject는 밝히지 말고 outline만 유지.
- Grain +5~+20 for film mood.

## 실패 방지 / 주의점

- 피사체가 덩어리처럼 붙으면 실루엣이 읽히지 않는다.
- 얼굴 디테일을 살리는 사진이 아니라는 점을 선택해야 한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person_or_couple
  - environment:sunset
  - light:strong_backlight
  - lens:1x_2x
  - edit_style:silhouette_warm
  - risk:lost_subject_shape
relationships:
  - backlight CREATES_silhouette
  - negative_exposure PROTECTS_sky
  - clear_outline INCREASES_readability
  - warm_gradient DRIVES_emotion
recommendation_modes:
  - trend
  - general
  - personalized
```

## 추가 검증 인물 시작값 — 실루엣 / Rim light

**Rim light**
- 광원을 등 뒤에 두고 얼굴은 약간 옆으로 돌린다.
- 머리카락/어깨 가장자리에 빛 테두리가 생기게 한다.
- 노출은 -0.3~-1.0부터 시작하고, 얼굴이 너무 어두우면 반사광을 찾는다.
- Lightroom: Highlights -25~-40, Shadows +10~+20, Dehaze +2~+5.

**Silhouette**
- 밝은 하늘/노을을 배경으로 피사체 윤곽이 읽히게 포즈를 만든다.
- 플래시 OFF.
- 노출 -1.0~-2.0.
- Lightroom: Contrast +15~+25, Shadows -100에 가깝게, Blacks -20~-40, Whites +5~+15.

- https://www.adobe.com/creativecloud/photography/type/silhouette-photography.html
- https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html
- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
