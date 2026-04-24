---
title: "Personalization learning schema — learnable photo-coach memory"
category: "recommendation"
updated_at: "2026-04-24"
content_type: "personalization_learning_schema"
---

# Personalization learning schema — learnable photo-coach memory

## 목적

Learnable Agent는 매번 같은 정답을 주는 추천기가 아니라, 사용자가 좋아하는 사진 톤과 보정 강도에 맞춰 점점 더 잘 고르는 사진 코치여야 한다.

개인화 데이터는 원본 사진이나 민감한 대화 전문이 아니라, 추천 후 사용자가 남긴 선택/만족 신호를 작게 누적한다.

```text
User feedback
→ PreferenceProfile
→ Recommendation reranking
→ Parameter/style variant hints
→ SatisfactionSignal
```

## 저장 단위

### FeedbackEvent

```json
{
  "scenario_id": "scenario_window_light_cafe_portrait",
  "channel": "personalized",
  "rating": 1,
  "style_tags": ["natural", "clean", "low_retouch"],
  "rejected_tags": ["strong_edit"],
  "issue_tags": ["issue:busy_background"],
  "note": "피부 보정 티가 적고 배경이 깔끔한 쪽을 선호"
}
```

### UserPreferenceProfile

```json
{
  "user_id": "local_user",
  "preferences": {
    "warmth": 0.0,
    "brightness": 0.0,
    "contrast": 0.0,
    "saturation": 0.0,
    "grain": 0.0,
    "skin_retouch": 0.0,
    "background_cleanup": 0.0,
    "cinematic": 0.0,
    "natural": 0.0,
    "edit_strength": 0.0
  },
  "channel_weights": {
    "trend": 1.0,
    "general": 1.0,
    "personalized": 1.0
  },
  "scenario_affinity": {},
  "issue_sensitivity": {},
  "event_count": 0
}
```

## 개인화 적용 원칙

1. `general` 추천은 안전한 기본값으로 유지한다.
2. `personalized` 추천은 사용자 취향에 따라 rank와 파라미터 힌트를 조정한다.
3. issue는 취향보다 우선한다. 예: 얼굴이 어두우면 “낮은 보정 선호”가 있어도 얼굴 노출 보정은 유지하되 강도를 낮춘다.
4. 사용자가 싫어한 스타일은 즉시 큰 폭으로 제거하지 않고, 여러 이벤트를 통해 천천히 낮춘다.
5. 원본 이미지, 얼굴 정보, 위치 정보는 이 프로필에 저장하지 않는다.

## 코드 위치

- 개인화 프로필/피드백 업데이트: `scripts/recommender/personalization.py`
- 추천 경로: `ScenarioMatcher` 결과 → graph recommendation → `rerank_recommendations(...)`

