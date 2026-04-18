---
title: "Token normalization playbook — multilingual scene graph"
category: "recommendation"
updated_at: "2026-04-18"
content_type: "normalization_playbook"
---

# Token normalization playbook — multilingual scene graph

## 목적

그래프 분리의 주요 원인인 중복 토큰(`Woman`, `tok_woman`, `subject:woman`)을 단일 canonical token으로 통합한다.

## 정규화 파이프라인

1. **Unicode normalization**: NFKC
2. **Case folding**: lowercase
3. **Punctuation cleanup**: `_`, `-`, `/` 정규화
4. **Language-aware mapping**: KR/EN 동의어를 canonical ID로 매핑
5. **Namespace binding**: `subject:`, `environment:`, `issue:` 등 label prefix 강제
6. **Alias registry append**: 원문 표현은 alias로 보존

## Canonical token examples

| Raw token variants | Canonical token |
|---|---|
| Woman / woman / 여성 / 여자 / tok_woman | `subject:woman` |
| underexposed_face / 얼굴 어두움 / face dark | `issue:underexposed_face` |
| night / 야간 / 저조도 / after dark | `time:night` |
| samsung / galaxy / 삼성폰 | `device:galaxy` |
| 2x / 2배 / tele 2x | `lens_mode:2x` |
| 인스타 업로드 / instagram upload / ig post | `intent:instagram_publish` |

## 5W1H 노멀라이즈 키

```yaml
keys:
  when: [time:morning, time:day, time:night, season:spring, season:summer, season:autumn, season:winter]
  who: [device:iphone, device:galaxy, device:pixel, app:lightroom, app:photoshop]
  where: [place:cafe, place:street, place:beach, place:museum, place:indoor, place:outdoor]
  what: [intent:portrait, intent:food, intent:product_listing, intent:instagram_publish, intent:trendy_style, intent:astro]
  how: [lens_mode:0_5x, lens_mode:1x, lens_mode:2x, mode:pro, param:iso, param:shutter, param:ev]
```

## 그래프 적용 규칙

- Scenario 노드는 5W1H 중 최소 3개 키를 가진다.
- Recommendation 노드는 반드시 `supported_by` evidence를 가진다.
- Issue 노드는 Recommendation을 직접 생성하지 않고 `adjusts_parameter` 경로를 사용한다.

## 품질 게이트

- 정규화 커버리지 95% 이상.
- 신규 token 생성 시 canonical dictionary 충돌 검사.
- `alias -> canonical` 단방향 매핑, canonical 중복 생성 금지.
