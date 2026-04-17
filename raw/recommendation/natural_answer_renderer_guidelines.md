---
title: "Natural answer renderer guidelines — graph result to user-facing photo coaching"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "answer_renderer_contract"
---

# Natural answer renderer guidelines — graph result to user-facing photo coaching

## 목적

Graph/Neo4j에서 나온 `Recommendation`, `Technique`, `Parameter` 노드는 내부적으로는 정확하지만, 그대로 사용자에게 보여주면 딱딱하다. 사용자 답변은 **사진 코치가 말하듯 자연스럽고 정리된 문장**이어야 한다.

## 답변 원칙

1. **내부 노드명을 그대로 말하지 않는다.**
   - 나쁨: `Subject mask`, `Background Saturation -5~-20`, `Recommendation general`.
   - 좋음: “얼굴만 살짝 밝히고, 뒤 테이블은 채도와 선명도를 낮춰 시선을 정리하세요.”

2. **먼저 한 줄 진단을 준다.**
   - “이 사진은 창가 빛은 좋은데, 얼굴 한쪽이 어둡고 배경이 산만한 게 핵심 문제예요.”

3. **촬영 개선과 보정 개선을 분리한다.**
   - 다시 찍을 수 있다면: 렌즈, 위치, 빛, 구도.
   - 이미 찍은 사진이면: 노출, 마스크, 색, 크롭.

4. **수치값은 ‘시작값’으로 말한다.**
   - “Exposure +0.2부터”, “Highlights -30 정도부터”, “너무 과하면 절반으로 줄이세요.”

5. **트렌드/일반/개인화는 사용자 말로 바꾼다.**
   - 트렌드: “요즘 느낌으로 가면…”
   - 일반: “가장 실패가 적은 방법은…”
   - 개인화: “평소 따뜻한 색을 좋아한다면…”

6. **답변은 4블록 이하로 제한한다.**
   - 진단
   - 다시 찍는 법
   - 보정하는 법
   - 취향별 변형 / 주의점

## 기본 출력 템플릿

```markdown
## 한 줄 진단
이 사진은 [장점]은 좋지만, [문제 1]과 [문제 2]를 잡으면 훨씬 좋아집니다.

## 다시 찍는다면
- [렌즈/거리/앵글]
- [빛/피사체 위치]
- [구도/배경 정리]

## 지금 사진을 보정한다면
- [전체 노출/WB]
- [마스크/부분 보정]
- [색/질감/크롭]

## 스타일 선택
- 자연스럽게: [낮은 강도]
- 트렌디하게: [유행 스타일]
- 시네마틱하게: [contrast/grain/color grading]
```

## 그래프 노드 → 자연어 변환 예시

| Graph phrase | User-facing phrase |
|---|---|
| `Subject mask: Exposure +0.1~+0.4` | 얼굴만 살짝 밝히세요. +0.1에서 +0.4 사이로 시작하면 안전합니다. |
| `Background Saturation -5~-20` | 배경 색을 조금 눌러서 인물이 더 잘 보이게 하세요. |
| `2x/Portrait, eye focus` | 2배 줌이나 인물 모드로 찍고 눈에 초점을 맞추세요. |
| `EV -0.3~-0.7` | 밝은 하늘이나 네온이 날아가면 촬영할 때 밝기를 조금 낮추세요. |
| `Grain +10~+25` | 필름 느낌을 원하면 입자를 아주 약하게 추가하세요. |
| `Avoid: direct sun` | 정오의 직사광은 피하고 그늘이나 창가 빛을 쓰는 편이 좋습니다. |

## 사용자 답변에서 숨겨야 할 것

- `SceneFacet`, `Recommendation`, `TrendSignal` 같은 내부 label.
- `confidence_score`, `source_file` 같은 debug 정보.
- 동일한 bullet 반복.
- “그래프가 말하길…” 같은 시스템 중심 표현.

## 사용자 답변에서 보여줘도 좋은 것

- 간단한 근거: “인물 사진에서는 얼굴과 배경을 분리하는 게 핵심입니다.”
- 출처 버튼/접기 영역: “근거 보기”에만 표시.
- 슬라이더 카드: Exposure, Highlights, Shadows, Saturation, Texture 등.

## 품질 체크리스트

- [ ] 첫 문장이 장면 진단으로 시작하는가?
- [ ] 촬영과 보정이 분리되어 있는가?
- [ ] 수치가 시작값으로 표현되는가?
- [ ] 내부 graph 용어가 노출되지 않는가?
- [ ] 사용자가 바로 따라 할 수 있는 순서인가?
