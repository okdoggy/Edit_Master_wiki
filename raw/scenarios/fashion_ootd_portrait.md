---
title: "패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags: ["fashion", "ootd", "portrait", "full-body", "instagram"]
aliases:
  - "골목 OOTD"
  - "전신 사진 다리 짧아보임"
  - "옷 색 살리는 사진"
  - "패션 전신 인물"
  - "full body outfit portrait"
graph_nodes:
  - "subject:person"
  - "subject:fashion_outfit"
  - "environment:street_or_cafe"
  - "lens:2x_or_1x"
  - "mode:portrait_or_photo"
  - "edit_style:clean_influencer"
  - "personal_signal:outfit_color_priority"
graph_edges:
  - "2x_lens REDUCES_body_distortion"
  - "grid HELPS_body_alignment"
  - "outfit_color REQUIRES_skin_tone_protection"
urls:

- https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone
- https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/
- https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/
- https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios
---

# 패션/OOTD 인물 — 전신 비율과 옷 색을 살리는 추천 seed

## 추천 시스템용 요약

- **트렌드 추천:** 4:5 세로 프레임, 길어 보이는 전신 구도, 깨끗한 배경, 옷 색이 주인공인 clean influencer look.
- **일반 추천:** 광각 왜곡을 피하고, 1x/2x에서 카메라를 허리~가슴 높이에 두며, 그리드로 수직을 맞춘다.
- **개인화 추천 변수:** 사용자가 옷 색/피부톤/배경 감성 중 무엇을 더 중시하는지.

## 촬영 레시피

- 렌즈: 2x 망원 우선, 공간이 좁으면 1x.
- 모드: Portrait / Photo.
- 포즈: 상체 3/4 각도, 한쪽 다리 앞으로, 어깨 힘 빼기.
- 구도: 세로 프레임, 인물은 1/3~1/2 비중, 발끝이 잘리지 않게.
- 빛: 사이드 라이트 또는 open shade.
- 카메라 시작값: Exposure 0~+0.3, Grid ON.

## 보정 레시피

- Profile: Adobe Portrait.
- Temp +3~+6.
- Vibrance +10~+15.
- Saturation -3~-5.
- Orange Saturation -5.
- Orange Luminance +8~+12.
- 옷 색은 Color Mix로 따로 살리고, 피부는 Subject mask로 보호.

## 실패 방지 / 주의점

- 광각을 너무 가까이서 쓰면 신체 비율이 무너진다.
- 옷 색을 살리다가 피부가 과포화되지 않게 한다.

## 근거

### 반영한 외부 근거

- Adobe Express 인물 사진 가이드는 스마트폰 인물에서 빛, 포즈, 배경 정리를 함께 다루는 근거를 제공한다.
- Google Pixel 프로필/ID 사진 팁과 Samsung 프로필 사진 가이드는 얼굴·몸 정렬과 배경 단순화를 촬영 단계에서 해결하는 방향을 뒷받침한다.
- Apple selfie/portrait 문서와 Adobe masking/color 자료는 렌즈·인물 분리·옷 색 보정을 분리하는 공식 근거다.

### 시나리오 수정 포인트

- OOTD는 인물 미용 보정보다 비율, 수직선, 옷 색 재현을 먼저 최적화한다.
- 개인화는 clean influencer, film, warm street 등 피드 스타일에 맞춰 색 강도를 조정한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person
  - subject:fashion_outfit
  - lens:2x_or_1x
  - edit_style:clean_influencer
relationships:
  - outfit_color MODIFIES edit_style
  - 2x_lens REDUCES distortion
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone
- https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/
- https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/
- https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios
