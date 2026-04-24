---
title: "벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "spring"
  - "cherry-blossom"
  - "flowers"
  - "portrait"
  - "airy"
  - "pink"
aliases:
  - "벚꽃 인물"
  - "꽃나무 아래 프로필"
  - "봄 핑크 보정"
  - "벚꽃 사진 밝게"
  - "cherry blossom portrait"
graph_nodes:
  - "subject:person"
  - "environment:flower_tree"
  - "light:soft_overcast"
  - "lens:2x_portrait"
  - "edit_style:airy_pink"
  - "trend_signal:spring_blossom"
  - "satisfaction_signal:soft_skin_clean_background"
graph_edges:
  - "flower_background SUPPORTS airy_style"
  - "overcast_light SOFTENS_skin"
  - "2x_portrait SEPARATES_subject"
  - "pink_tint CONNECTS spring_trend"
urls:
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html"
  - "https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://www.nationalgeographic.com/photography/article/people-quick-tips"
---

# 벚꽃·꽃나무 아래 인물 — 밝고 부드러운 봄 스타일

## 추천 시스템용 요약

- **트렌드 추천:** 봄 시즌에는 밝고 airy한 핑크/파스텔, 배경 꽃 bokeh, 깨끗한 피부 톤이 trend 후보.
- **일반 추천:** 일반 추천은 직사광을 피하고 흐린 날/그늘/역광에서 꽃을 배경 bokeh로 만드는 것.
- **개인화 추천 변수:** 사용자가 파스텔/고채도/필름 중 무엇을 선호하는지에 따라 꽃 채도와 grain 조절.

## 촬영 레시피

- 흐린 날 또는 그늘에서 촬영해 얼굴 그림자를 줄인다.
- 2x/3x 또는 Portrait mode로 꽃 배경을 흐린다.
- 꽃이 얼굴에 너무 겹치지 않게 눈 주변은 깨끗하게 둔다.
- 흰 꽃은 EV -0.3으로 하이라이트 보호.

## 보정 레시피

- Exposure +0.2~+0.5, Highlights -20~-40.
- Pink/Magenta Saturation +5~+15, 전체 Tint +3~+10.
- Subject mask로 피부 Red/Orange saturation 과다를 낮춘다.
- Texture -5~-12 for soft portrait, Background Clarity -5~-15.

## 실패 방지 / 주의점

- 핑크를 전체에 넣으면 피부가 붉어진다.
- 꽃이 너무 가까우면 얼굴보다 꽃에 초점이 잡힌다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person
  - environment:flower_tree
  - light:soft_overcast
  - lens:2x_portrait
  - edit_style:airy_pink
  - trend_signal:spring_blossom
  - satisfaction_signal:soft_skin_clean_background
relationships:
  - flower_background SUPPORTS airy_style
  - overcast_light SOFTENS_skin
  - 2x_portrait SEPARATES_subject
  - pink_tint CONNECTS spring_trend
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://www.nationalgeographic.com/photography/article/people-quick-tips
