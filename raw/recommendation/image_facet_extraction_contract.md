---
title: "Image facet extraction contract — photo observation to scene graph"
category: "recommendation"
updated_at: "2026-04-24"
content_type: "image_facet_extraction_contract"
---

# Image facet extraction contract — photo observation to scene graph

## 목적

Learnable Agent가 실제 사진을 받으면 먼저 사진을 추천 그래프가 이해할 수 있는 관찰값으로 바꿔야 한다.

```text
Image / user caption
→ ImageObservation
→ subject / environment / light / issue / style preference facets
→ ScenarioMatcher
→ RecommendationVariant
```

## 안정적인 출력 계약

```json
{
  "id": "obs_20260424_001",
  "source": "external_vision",
  "subjects": ["intent:portrait"],
  "environments": ["place:cafe_window"],
  "lights": ["light:diffused_window"],
  "composition": ["background:busy"],
  "technical_issues": ["issue:underexposed_face", "issue:busy_background"],
  "style_preferences": ["pref:natural"],
  "device_or_app": ["app:lightroom"],
  "confidence": {
    "subject": 0.8,
    "issues": 0.7
  }
}
```

## 추출해야 하는 facet

| Facet | 예시 | 추천에서의 역할 |
|---|---|---|
| subject | `intent:portrait`, `intent:food`, `intent:ootd` | scenario 후보의 중심 |
| environment | `place:cafe`, `place:restaurant`, `place:beach` | scenario 후보의 중심 |
| light | `light:diffused_window`, `time:night`, `light:neon` | 촬영/보정 파라미터 조정 |
| composition | `background:busy`, `crop:top_down`, `angle:low` | 렌즈/구도 조언 |
| technical_issues | `issue:underexposed_face`, `issue:motion_blur` | 추천을 덮어쓰지 않는 guardrail |
| style_preferences | `pref:natural`, `pref:cinematic`, `pref:warm` | 개인화 variant 선택 |
| device_or_app | `device:iphone`, `app:lightroom` | 기능/앱별 조작법 선택 |

## 코드 위치

- Facet contract / adapter: `scripts/recommender/image_facets.py`
- 텍스트 질의만 있을 때: `observation_from_text(...)`
- 외부 비전 모델 결과가 있을 때: `observation_from_vision_json(...)`
- matcher 연결: `observation.to_matcher_query(original_query)`

## 중요한 제한

현재 로컬 구현은 실제 컴퓨터 비전 모델이 아니다. 텍스트 질의와 외부 비전 JSON을 graph-ready payload로 정규화하는 어댑터다. 실제 이미지 분석기는 이 계약에 맞춰 나중에 연결한다.

