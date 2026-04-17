---
title: "셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags: ["selfie", "profile", "portrait", "front-camera", "skin-tone"]
graph_nodes:
  - "subject:selfie_person"
  - "camera:front_camera"
  - "mode:selfie_or_portrait_selfie"
  - "light:window_or_open_shade"
  - "edit_style:natural_skin"
  - "risk:wide_angle_face_distortion"
graph_edges:
  - "close_front_camera CAUSES face_distortion"
  - "timer IMPROVES_pose"
  - "window_light SOFTENS_skin"
urls:

- https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone
- https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/
- https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/
- https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios
---

# 셀카/Profile — 왜곡 적고 자연스러운 얼굴 추천 seed

## 추천 시스템용 요약

- **트렌드 추천:** 무리한 뷰티보다 natural skin, clean background, 눈빛/catchlight를 살린 프로필.
- **일반 추천:** 카메라를 눈보다 약간 위, 창가/그늘의 고른 빛, 타이머/볼륨 버튼으로 흔들림 줄이기.
- **개인화 추천 변수:** 피부 보정 강도, 얼굴 클로즈업 선호, 밝은 톤/무디 톤 선호.

## 촬영 레시피

- 렌즈: 전면 카메라, 그룹이면 Wide Selfie.
- 모드: Selfie / Portrait selfie.
- 포즈: 카메라를 눈보다 약간 위, 턱 살짝 앞으로.
- 구도: 눈을 상단 1/3 근처, 팔이 너무 크게 들어오지 않게.
- 빛: 창가/그늘/아침·저녁 고른 빛.
- 시작값: 타이머 3초, Apple은 볼륨 버튼, Samsung/Pixel은 palm timer류 기능 활용.

## 보정 레시피

- Profile: Adobe Portrait.
- Temp +4.
- Tint +2.
- Vibrance +8.
- Orange Saturation -5~-8.
- Orange Luminance +8~+12.
- Texture -5~-12, 단 피부 질감을 모두 지우지 않는다.

## 실패 방지 / 주의점

- 너무 가까운 초광각 셀카는 코/이마 왜곡이 크다.
- 위에서 내려찍는 각도는 적당히만 사용한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:selfie_person
  - camera:front_camera
  - mode:portrait_selfie
  - edit_style:natural_skin
relationships:
  - front_camera USES selfie_mode
  - close_distance CAUSES face_distortion
  - natural_skin MATCHES authenticity_trend
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.adobe.com/express/learn/blog/how-to-take-portrait-photos-with-your-phone
- https://blog.google/products-and-platforms/devices/pixel/take-id-photo-google-pixel-tips/
- https://www.samsung.com/us/explore/photography/still-life/how-to-capture-your-best-profile-picture/
- https://support.apple.com/guide/iphone/take-a-selfie-iph1b88429a6/ios
