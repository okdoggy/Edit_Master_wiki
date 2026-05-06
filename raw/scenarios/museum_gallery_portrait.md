---
title: "미술관·전시회 인물 — 플래시 없이 차분하게"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "museum"
  - "gallery"
  - "indoor"
  - "portrait"
  - "no-flash"
  - "mixed-light"
aliases:
  - "전시회 인물"
  - "미술관 사진"
  - "작품 앞 인물"
  - "플래시 금지"
  - "실내 조명 인물"
  - "갤러리 프로필"
query_aliases:
  - "전시회 인물"
  - "미술관 사진"
  - "작품 앞 인물"
  - "플래시 금지"
  - "실내 조명 인물"
  - "갤러리 프로필"
graph_nodes:
  - "subject:person"
  - "environment:museum_gallery"
  - "light:mixed_gallery_spotlight"
  - "lens:1x_2x"
  - "mode:photo_or_portrait"
  - "edit_style:minimal_clean"
  - "risk:mixed_white_balance"
  - "risk:busy_background"
graph_edges:
  - "no_flash_preserves_gallery_rules"
  - "2x_reduces_background_noise"
  - "white_balance_controls_gallery_cast"
  - "negative_space_supports_art_context"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 미술관·전시회 인물 — 플래시 없이 차분하게

## 추천 시스템용 요약

- **트렌드 추천:** 전시회 사진은 minimal/clean, 작품과 인물의 거리감, 조용한 톤이 trend 후보.
- **일반 추천:** 일반 추천은 플래시 없이 1x/2x, 작품과 인물 간격, WB 정리, 배경 단순화.
- **개인화 추천 변수:** 사용자가 작품 중심/인물 중심 중 무엇을 선호하는지 반영.

## 촬영 레시피

- 플래시는 끄고 작품 조명/벽 반사광을 활용한다.
- 작품 바로 앞보다 0.5~1m 옆에 서서 인물과 작품이 겹치지 않게 한다.
- 2x로 배경 산만함을 줄이고, 좁으면 1x.
- 초점은 눈에 맞추고, 하이라이트가 날아가면 EV -0.3.

## 보정 레시피

- WB를 먼저 맞춰 벽이 너무 노랗거나 초록색이 되지 않게 한다.
- Highlights -10~-30, Shadows +10~+20.
- Background Saturation -5~-20, Subject Exposure +0.1~+0.3.
- Geometry로 벽/프레임 수직을 정리한다.

## 실패 방지 / 주의점

- 전시 작품 촬영 규칙과 저작권/플래시 금지를 확인한다.
- 작품이 인물 머리 뒤로 튀어나오면 산만하다.

## 근거

### 반영한 외부 근거

- RAF Museum photography resource는 저조도에서 white balance 조정, 각도 변화, 프레임 체크, 배경 정리를 강조한다.
- LifePixel museum/gallery tips는 박물관·갤러리 규칙 확인, flash/tripod 제한, 전시 조명 활용을 제안한다.
- Pixel Night Sight in Portrait 자료는 저조도 인물에서 얼굴에 soft ambient lighting이 필요하고 Portrait Light가 후처리에 도움이 된다고 말한다.
- Reddit museum/glass discussion은 유리 전시물에서는 CPL, 각도 변경, 유리에 가깝게 대기, Google PhotoScan 같은 다중사진 방식이 언급된다.

### 시나리오 수정 포인트

- “작품 앞 인물”은 플래시 금지/규칙 준수가 먼저다.
- 전시 조명을 그대로 활용하고, 배경 작품과 인물이 겹치지 않도록 위치를 조금 옆으로 뺀다.
- 유리 전시물은 반사 통제가 핵심 issue로 별도 처리한다.

## Graphify 추출 힌트

```yaml
aliases:
  - 전시회 인물
  - 미술관 사진
  - 작품 앞 인물
  - 플래시 금지
  - 실내 조명 인물
  - 갤러리 프로필
entities:
  - subject:person
  - environment:museum_gallery
  - light:mixed_gallery_spotlight
  - lens:1x_2x
  - mode:photo_or_portrait
  - edit_style:minimal_clean
  - risk:mixed_white_balance
  - risk:busy_background
relationships:
  - no_flash_preserves_gallery_rules
  - 2x_reduces_background_noise
  - white_balance_controls_gallery_cast
  - negative_space_supports_art_context
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.reddit.com/r/photography/comments/1llhctf/problems_with_reflections_in_the_glass_while/

- https://blog.google/products-and-platforms/devices/pixel/take-holiday-photos-night-sight-portrait-mode/

- https://www.lifepixel.com/photo-tutorials/6-tips-photographing-museums-galleries

- https://assets.rafmuseum.org.uk/app/uploads/2023/08/Photography-Resources.pdf

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
