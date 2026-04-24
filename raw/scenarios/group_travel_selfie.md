---
title: "단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "group"
  - "selfie"
  - "travel"
  - "wide"
  - "portrait"
aliases:
  - "단체 셀피"
  - "여행 그룹샷"
  - "셀카 얼굴 왜곡"
  - "친구 단체사진"
  - "group travel selfie"
graph_nodes:
  - "subject:group"
  - "environment:travel_landmark"
  - "lens:0.5x_1x_front"
  - "mode:selfie_or_timer"
  - "composition:face_center"
  - "risk:edge_distortion"
graph_edges:
  - "ultrawide FITS_group"
  - "edge_distortion HARMS_faces"
  - "timer IMPROVES_stability"
  - "landmark_context ADDS_story"
urls:
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.nationalgeographic.com/photography/article/camera-phone-photos"
---

# 단체 여행 셀피/그룹샷 — 얼굴 왜곡 줄이기

## 추천 시스템용 요약

- **트렌드 추천:** 여행 photo dump에서는 완벽한 한 장보다 친구/장소/소품이 함께 보이는 자연스러운 단체컷이 trend.
- **일반 추천:** 일반 추천은 얼굴을 가장자리에 두지 않고, 장소 맥락은 남기고, 타이머로 흔들림을 줄이는 것.
- **개인화 추천 변수:** 개인화는 셀피 선호/전신샷 선호/장소 강조 선호에 따라 0.5x와 1x 선택.

## 촬영 레시피

- 0.5x는 단체가 많거나 장소를 넣을 때, 얼굴은 중앙 70% 안에.
- 삼각대/난간 + 타이머 3초로 후면 카메라 사용하면 품질 상승.
- 랜드마크는 사람 머리 뒤로 튀어나오지 않게 옆으로 배치.
- 빛은 얼굴 쪽에서 부드럽게 들어오게.

## 보정 레시피

- Faces/Subject mask Exposure +0.1~+0.3.
- 하늘/배경 Highlights -20~-50.
- 전체 색온도와 피부색을 우선 맞춘 뒤 프리셋 적용.
- 4:5 피드와 9:16 스토리 크롭 둘 다 저장.

## 실패 방지 / 주의점

- 초광각 가장자리 얼굴은 늘어진다.
- 역광 단체샷은 얼굴이 모두 어두워질 수 있어 HDR/보정 전제.

## Graphify 추출 힌트

```yaml
entities:
  - subject:group
  - environment:travel_landmark
  - lens:0.5x_1x_front
  - mode:selfie_or_timer
  - composition:face_center
  - risk:edge_distortion
relationships:
  - ultrawide FITS_group
  - edge_distortion HARMS_faces
  - timer IMPROVES_stability
  - landmark_context ADDS_story
recommendation_modes:
  - trend
  - general
  - personalized
```

## 추가 검증 그룹/셀피 시작값

**그룹 사진**
- 렌즈: 0.5x는 가까운 그룹/작은 공간, 1x는 왜곡이 적은 기본 그룹샷.
- 모두 카메라와 비슷한 거리에 서게 한다.
- 얼굴을 가장자리로 보내지 않는다.
- 타이머 3~10초.
- 그룹이면 Portrait blur는 최소 또는 OFF.
- Pixel: Auto Best Take / Add Me / Palm Timer 같은 그룹 보조 기능을 고려.
- Samsung: Motion Photo / Wide Selfie / Palm shutter 활용.

**Lightroom**
- 다인원은 얼굴별 마스크 또는 전체 WB 통일이 우선.
- Temp +3~+5, Vibrance +6~+10.

- https://blog.google/products/pixel/pixel-group-photo-features-ai/
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://blog.google/products-and-platforms/devices/pixel/travel-photography-101-teampixel/
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.nationalgeographic.com/photography/article/camera-phone-photos

- https://www.samsung.com/us/support/answer/ANS10004858/

- https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios
