---
title: "거울 셀카 OOTD — 몸 비율과 거울 반사 정리"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "mirror-selfie"
  - "ootd"
  - "fashion"
  - "indoor"
  - "body-alignment"
aliases:
  - "거울 셀카"
  - "엘리베이터 셀카"
  - "거울 OOTD"
  - "몸 비율 이상"
  - "거울 더러움"
  - "전신 셀카"
query_aliases:
  - "거울 셀카"
  - "엘리베이터 셀카"
  - "거울 OOTD"
  - "몸 비율 이상"
  - "거울 더러움"
  - "전신 셀카"
graph_nodes:
  - "subject:person"
  - "subject:fashion_outfit"
  - "environment:mirror_indoor"
  - "camera:front_or_rear_camera"
  - "lens:1x_2x"
  - "edit_style:clean_influencer"
  - "risk:mirror_distortion"
  - "risk:dirty_mirror"
graph_edges:
  - "mirror_angle_changes_body_ratio"
  - "grid_improves_body_alignment"
  - "clean_mirror_reduces_distraction"
  - "1x_2x_reduces_wide_distortion"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
  - "https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios"
  - "https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 거울 셀카 OOTD — 몸 비율과 거울 반사 정리

## 추천 시스템용 요약

- **트렌드 추천:** 거울 OOTD는 clean influencer, 정렬, 옷 색, 몸 비율이 핵심.
- **일반 추천:** 일반 추천은 거울/폰 수직, 1x/2x, 렌즈 높이 조절, 배경 정리.
- **개인화 추천 변수:** 사용자가 다리 길어 보임/옷 색 정확도/자연스러운 셀카 중 무엇을 원하는지 반영.

## 촬영 레시피

- 거울과 폰을 최대한 수직으로 맞춘다.
- 폰을 가슴~얼굴 높이에 두고 아래로 과하게 기울이지 않는다.
- 가능하면 후면 1x/2x + 타이머, 아니면 전면 카메라 왜곡을 주의.
- 촬영 전 거울 얼룩과 배경 물건을 정리한다.

## 보정 레시피

- Geometry/Vertical로 기울어진 선을 바로잡는다.
- Subject/Outfit mask로 옷 색을 살리고 피부는 과포화 방지.
- Background Saturation -5~-20, Clarity -5~-15.
- Crop은 4:5 기준으로 발끝/머리 여백 확보.

## 실패 방지 / 주의점

- 거울이 기울면 다리/상체 비율이 왜곡된다.
- 초광각 전면 셀카는 얼굴과 손이 커질 수 있다.

## 근거

### 반영한 외부 근거

- Google Pixel ID photo tips는 얼굴에 반사되어 들어오는 부드러운 빛이 좋은 인물 사진의 핵심이라고 설명한다.
- Google Pixel portrait tips는 중요한 피사체를 탭해 노출/초점 우선순위를 주고, 더 좋은 빛을 찾아야 한다고 설명한다.
- MakeUseOf mirror selfie tips는 거울 셀피에서 구도 요소를 더 많이 활용할 수 있고, 폰을 무엇에 주목시키고 싶은지에 맞춰 배치하라고 설명한다.
- Reddit fashion advice community는 mirror OOTD에서 카메라-거울-몸 거리와 폰이 옷의 핵심 부분을 가리지 않는 점을 지적한다.
- 셀피/폰카 커뮤니티에서는 렌즈와 너무 가까우면 얼굴/몸 왜곡이 커진다는 피드백이 반복된다.

### 시나리오 수정 포인트

- 거울 OOTD는 단순 셀카가 아니라 **몸 비율, 옷 색, 거울/배경 정리** 문제다.
- 폰을 거울에 비스듬히 들기보다 수직/평행을 맞추고, 가능하면 타이머+후면 카메라 대안도 제시한다.

## Graphify 추출 힌트

```yaml
aliases:
  - 거울 셀카
  - 엘리베이터 셀카
  - 거울 OOTD
  - 몸 비율 이상
  - 거울 더러움
  - 전신 셀카
entities:
  - subject:person
  - subject:fashion_outfit
  - environment:mirror_indoor
  - camera:front_or_rear_camera
  - lens:1x_2x
  - edit_style:clean_influencer
  - risk:mirror_distortion
  - risk:dirty_mirror
relationships:
  - mirror_angle_changes_body_ratio
  - grid_improves_body_alignment
  - clean_mirror_reduces_distraction
  - 1x_2x_reduces_wide_distortion
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.reddit.com/r/MtF/comments/nnzr6s/its_not_you_its_your_camera_photography_tips_for/

- https://www.reddit.com/r/femalefashionadvice/comments/2iupe5/taking_outfit_photos_with_your_phone/

- https://www.makeuseof.com/mirror-selfie-poses/

- https://blog.google/products/pixel/frame-10-tips-getting-great-portraits-pixel-2/

- https://blog.google/products/pixel/take-id-photo-google-pixel-tips/

- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
