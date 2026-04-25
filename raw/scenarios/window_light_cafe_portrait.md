---
title: "카페 창가 인물 — 자연광/인플루언서 프로필"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "cafe"
  - "window-light"
  - "portrait"
  - "influencer"
  - "soft-light"
aliases:
  - "카페 창가 인물"
  - "창가 프로필 사진"
  - "얼굴 한쪽 어두움"
  - "배경 지저분 카페"
  - "cafe window portrait"
graph_nodes:
  - "subject:person"
  - "environment:cafe_window"
  - "light:diffused_window"
  - "lens:2x_portrait"
  - "edit_style:clean_influencer"
  - "personal_signal:skin_retouch_strength"
graph_edges:
  - "window_light SOFTENS_skin"
  - "2x REDUCES_distortion"
  - "background_distance CREATES_separation"
  - "negative_space SUPPORTS_text_overlay"
urls:
  - "https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://www.nationalgeographic.com/photography/article/people-quick-tips"
---

# 카페 창가 인물 — 자연광/인플루언서 프로필

## 추천 시스템용 요약

- **트렌드 추천:** SNS 프로필/브랜드 협업은 clean influencer, 밝고 자연스러운 피부, 카페 공간감이 trend 후보.
- **일반 추천:** 일반 추천은 창문 45도 옆빛, 배경 정리, 2x/Portrait, 피부색 보호.
- **개인화 추천 변수:** 사용자 피부 보정 강도/밝은 피드 선호/카페톤 선호에 맞춰 Exposure와 Texture 조절.

## 촬영 레시피

- 창문 옆 45도에 앉히고 얼굴이 창을 향하게 한다.
- 2x/Portrait, 눈 초점, 배경과 1m 이상 거리.
- 테이블 위 소품은 1~2개만 남긴다.
- 텍스트/스토리용이면 상단 여백 확보.

## 보정 레시피

- Subject Exposure +0.1~+0.4, Texture -5~-12.
- Background Saturation -5~-20, Clarity -5~-15.
- Orange Luminance +5~+10, Saturation -5~+5.
- 전체 Exposure +0.1~+0.3, Highlights -10~-30.

## 실패 방지 / 주의점

- 창문 직사광은 코/눈 밑 그림자를 강하게 만든다.
- 실내 조명+창빛 혼합은 WB가 어려워 RAW 권장.

## 근거

### 반영한 외부 근거

- Adobe portrait lighting 자료는 창가처럼 방향성 있는 부드러운 빛을 인물에 적용하는 근거를 제공한다.
- Apple Portrait 문서는 배경 흐림과 조명 효과 조절을, Adobe Lightroom masking/color 문서는 얼굴과 배경을 분리하는 후처리 근거를 제공한다.
- National Geographic people tips와 Google Pixel 사진 팁은 인물 사진에서 배경 정리와 빛의 방향을 우선하는 접근을 보강한다.

### 시나리오 수정 포인트

- 창가 인물은 창문 45도 방향의 부드러운 빛과 배경 거리 확보를 우선한다.
- 보정은 얼굴 노출, 피부 Texture, 배경 채도를 분리해 clean influencer 톤으로 조정한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person
  - environment:cafe_window
  - light:diffused_window
  - lens:2x_portrait
  - edit_style:clean_influencer
  - personal_signal:skin_retouch_strength
relationships:
  - window_light SOFTENS_skin
  - 2x REDUCES_distortion
  - background_distance CREATES_separation
  - negative_space SUPPORTS_text_overlay
recommendation_modes:
  - trend
  - general
  - personalized
```

## 추가 검증 인물 시작값 — 창가(Window light)

**촬영 시작값**
- 렌즈: 1x 또는 2x.
- 모드: Portrait / Photo.
- 포즈: 창을 향해 30~45도, 턱 살짝 내리기.
- 빛: 커튼/확산된 창광. 직사광은 피한다.
- 카메라: 얼굴이 어두우면 Exposure +0.2, 눈에 탭 포커스, Grid ON.

**Lightroom 시작값**
- Profile: Adobe Portrait.
- Temp +3~+6.
- Highlights -20~-30.
- Shadows +15~+25.
- Orange Saturation -5.
- Orange Luminance +8~+12.

- https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone
- https://www.adobe.com/creativecloud/photography/discover/portrait-lighting.html
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://www.nationalgeographic.com/photography/article/people-quick-tips

- https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/
