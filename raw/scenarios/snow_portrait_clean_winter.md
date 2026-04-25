---
title: "눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "winter"
  - "snow"
  - "portrait"
  - "high-key"
  - "white-balance"
aliases:
  - "눈 오는 날 인물"
  - "설경 가족 사진"
  - "눈이 회색으로 나옴"
  - "겨울 하이키 보정"
  - "snow portrait clean winter"
graph_nodes:
  - "subject:person"
  - "environment:snow"
  - "light:overcast_reflection"
  - "lens:1x_2x"
  - "edit_style:clean_winter"
  - "risk:underexposed_snow"
graph_edges:
  - "snow REFLECTS_light"
  - "camera_meter MAY underexpose_snow"
  - "white_balance CONTROLS blue_cast"
  - "subject_mask PROTECTS_face"
urls:
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
---

# 눈 오는 날 인물 — 깨끗한 겨울/하이키 스타일

## 추천 시스템용 요약

- **트렌드 추천:** 겨울에는 clean white, blue shadow, red accessory contrast, minimal look이 trend 후보.
- **일반 추천:** 눈을 회색으로 만들지 않고 얼굴을 따뜻하게 분리하는 방식이 만족도가 높다.
- **개인화 추천 변수:** 사용자가 차가운 겨울톤/따뜻한 필름톤 중 무엇을 선호하는지 반영.

## 촬영 레시피

- 눈 배경이 많으면 카메라가 어둡게 찍을 수 있어 EV +0.3~+1.0을 테스트한다.
- 얼굴은 2x/Portrait, 풍경 포함은 1x/0.5x.
- 눈발은 어두운 배경 앞에서 더 잘 보인다.
- 장갑/빨간 목도리 같은 포인트 컬러를 넣는다.

## 보정 레시피

- WB: 눈이 파랗게 보이면 Temp +300~+800K.
- Highlights -10~-30로 눈 디테일 유지.
- Whites +5~+20, Blacks -5~-15.
- Subject mask: Face Exposure +0.1~+0.3, Orange Luminance +5.

## 실패 방지 / 주의점

- 눈을 순백으로만 밀면 디테일이 사라진다.
- 스마트폰 렌즈에 눈/물방울이 묻으면 콘트라스트가 급격히 떨어진다.

## 근거

### 반영한 외부 근거

- Apple Portrait 문서는 인물과 배경 분리, 배경 흐림 조절의 공식 근거를 제공한다.
- Adobe Lightroom 모바일/color 자료는 눈의 밝기, WB, 피부톤을 분리해 보정하는 근거다.
- Adobe 스마트폰 사진 가이드와 National Geographic 스마트폰 팁은 밝은 야외 장면에서 빛과 구도를 단순화하는 접근을 뒷받침한다.

### 시나리오 수정 포인트

- 눈 사진은 전체를 밝게만 올리지 않고 snow/highlight와 face/skin을 분리한다.
- 겨울 하이키 스타일은 깨끗한 흰색을 유지하되 피부가 푸르게 식지 않도록 제한한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person
  - environment:snow
  - light:overcast_reflection
  - lens:1x_2x
  - edit_style:clean_winter
  - risk:underexposed_snow
relationships:
  - snow REFLECTS_light
  - camera_meter MAY underexpose_snow
  - white_balance CONTROLS blue_cast
  - subject_mask PROTECTS_face
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://www.nationalgeographic.com/photography/article/camera-phone-photos
