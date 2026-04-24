---
title: "단체 모임 그룹샷 — 눈 감음과 표정 실패를 줄이는 베스트컷 루프"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-24"
scenario_tags:
  - "group"
  - "gathering"
  - "best-face"
  - "burst"
  - "motion-photo"
  - "family"
aliases:
  - "단체사진 눈 감음"
  - "친구 모임 그룹샷"
  - "가족 단체사진"
  - "표정 좋은 단체사진"
  - "group best face"
  - "best take group photo"
query_aliases:
  - "단체 사진에서 한 명이 자꾸 눈을 감아요"
  - "모임 사진 표정을 다 살리고 싶어요"
  - "친구들 단체샷 베스트컷 고르는 법"
graph_nodes:
  - "subject:group"
  - "environment:gathering_or_travel"
  - "mode:burst_motion_photo_top_shot"
  - "trend_signal:candid_group_memory"
  - "preference:natural_expression"
  - "edit_style:clean_group_memory"
  - "style_recipe:best_expression_frame_selection"
  - "technique:timer_rear_camera"
  - "technique:burst_or_motion_photo"
  - "parameter:faces_exposure_plus_0_1_to_0_3"
  - "issue:closed_eyes"
  - "risk:edge_face_distortion"
  - "outcome:everyone_readable_and_natural"
graph_edges:
  - "candid_group_memory VALUES natural_expression"
  - "burst_or_motion_photo ENABLES best_expression_frame_selection"
  - "timer_rear_camera IMPROVES_stability"
  - "edge_face_distortion CONSTRAINS ultrawide_composition"
  - "closed_eyes TRIGGERS frame_selection"
urls:
  - "https://support.google.com/pixelcamera/answer/9937175?hl=en"
  - "https://support.apple.com/guide/iphone/take-burst-mode-shots-ipha42c55cd0/ios"
  - "https://support.apple.com/en-us/102398"
---

# 단체 모임 그룹샷 — 눈 감음과 표정 실패를 줄이는 베스트컷 루프

## 추천 시스템용 요약

- **트렌드 추천:** 여행 photo dump와 가족/친구 모임에서는 완벽한 포즈보다 자연스러운 표정이 살아 있는 candid group memory가 강하다.
- **일반 추천:** 한 장만 찍지 말고 Burst/Motion/Top Shot 계열로 표정 후보를 확보한 뒤 골라낸다.
- **개인화 추천 변수:** 사용자가 자연스러운 웃음/깔끔한 기록/장소 맥락 중 무엇을 우선하는지에 따라 렌즈와 크롭을 조절한다.

## 촬영 레시피

- 가능하면 후면 카메라 + 타이머로 찍고, 폰은 난간/삼각대/고정 표면에 둔다.
- 0.5x를 쓸 때 얼굴은 중앙 70% 안에 배치하고, 가장자리에는 몸/배경 여백을 둔다.
- Burst 또는 Motion Photo/Top Shot을 켜고 3~5초 동안 여러 표정이 나오게 유도한다.
- 조명은 얼굴 전체가 비슷하게 밝아지는 그늘/창가/벽 반사광을 고른다.

## 보정 레시피

- Faces/Subject mask: Exposure +0.1~+0.3, Shadows +5~+20.
- 배경 하이라이트는 -15~-40으로 낮추고, 얼굴 톤은 과한 필터보다 WB 우선.
- 4:5와 16:9 버전을 따로 저장해 피드/앨범/스토리에 맞춘다.
- 눈 감은 컷은 보정으로 살리기보다 프레임 선택 또는 Best Take 계열 기능을 먼저 검토한다.

## 실패 방지 / 주의점

- 초광각 가장자리 얼굴은 늘어나므로, 사람이 많아도 얼굴을 프레임 끝에 붙이지 않는다.
- Portrait blur는 단체에서 일부 얼굴을 잘못 흐릴 수 있어 약하게 쓰거나 끈다.
- 표정 실패는 후반 보정보다 촬영 단계의 프레임 수가 더 중요하다.

## 전문가/공식 근거 반영

### 반영한 외부 근거

- Google Pixel Camera 도움말은 Top Shot이 burst 중 좋은 컷을 고르고, Auto Best Take가 여러 장의 표정을 결합할 수 있다고 설명한다.
- Apple Burst mode 문서는 움직이는 피사체나 여러 고속 프레임이 필요한 상황에서 보관할 컷을 선택하는 절차를 제공한다.
- Apple Portrait mode 문서는 인물/반려동물/객체를 선명하게 두고 배경 흐림과 조명 효과를 조절하는 방식을 제공한다.

### 시나리오 수정 포인트

- `closed_eyes`는 추천의 중심 축이 아니라, `best_expression_frame_selection`을 활성화하는 guardrail이다.
- 그룹샷은 트렌드보다 추억 보존 성격이 강하므로 자연 표정 preference를 높은 우선순위로 둔다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:group
  - trend_signal:candid_group_memory
  - preference:natural_expression
  - edit_style:clean_group_memory
  - style_recipe:best_expression_frame_selection
  - issue:closed_eyes
relationships:
  - candid_group_memory VALUES natural_expression
  - burst_or_motion_photo ENABLES best_expression_frame_selection
  - closed_eyes TRIGGERS frame_selection
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://support.google.com/pixelcamera/answer/9937175?hl=en
- https://support.apple.com/guide/iphone/take-burst-mode-shots-ipha42c55cd0/ios
- https://support.apple.com/en-us/102398
