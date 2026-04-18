---
title: "Scene query slot schema — when/who/where/what/how"
category: "recommendation"
updated_at: "2026-04-18"
content_type: "scene_query_slot_schema"
---

# Scene query slot schema — when/who/where/what/how

## 목적

raw 지식과 추천 노드를 연결할 때, `언제/누가/어디서/무엇을/어떻게`를 일관된 슬롯으로 강제해 질의 매칭 성능을 높인다.

## 슬롯 정의

| Slot | 의미 | 예시 |
|---|---|---|
| when | 시간/계절/조도 | 아침, 낮, 밤, 겨울, golden hour |
| who | 기기/앱/촬영 주체 | iPhone, Galaxy, Pixel, Lightroom, Photoshop |
| where | 장소/환경 | 야외, 실내, 카페, 가로수길, 해변, 미술관 |
| what | 목표/콘텐츠 타입 | 인스타 업로드용, 유행 스타일, 별 촬영, 제품 판매 사진 |
| how | 실행 파라미터 | 2x 줌, 프로모드, ISO 600, EV -0.7, 1/125s |

## 그래프 엣지 권장안

```text
Query --MENTIONS_WHEN--> TimeFacet
Query --MENTIONS_WHO--> Device/App
Query --MENTIONS_WHERE--> PlaceFacet
Query --MENTIONS_WHAT--> IntentFacet
Query --MENTIONS_HOW--> Technique/Parameter

Scenario --COVERS_WHEN/WHO/WHERE/WHAT/HOW--> Facet
Recommendation --DERIVES_FROM--> Scenario
Technique --SETS_PARAMETER--> Parameter
Recommendation --SUPPORTED_BY--> Evidence
```

## 시나리오 최소 충족 조건

- `where` + `what` + `how`는 필수.
- `when` 또는 `who` 중 하나 이상 필수.
- issue는 보조 필드로만 허용.

## 예시 매핑

질의: "밤에 갤럭시로 가로수길에서 인스타 올릴 인물샷 2배줌으로 찍고 싶은데 ISO 600 괜찮아?"

```yaml
when: time:night
who: device:galaxy
where: place:street
what: intent:instagram_publish + intent:portrait
how:
  - lens_mode:2x
  - mode:pro
  - param:iso_600
```
