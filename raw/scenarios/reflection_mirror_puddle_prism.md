---
title: "거울·웅덩이·프리즘 반사 — 창의적 SNS 컷"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-17"
scenario_tags:
  - "reflection"
  - "mirror"
  - "puddle"
  - "prism"
  - "creative"
  - "sns"
aliases:
  - "웅덩이 반사"
  - "프리즘 사진"
  - "창의적 반사 사진"
  - "거울 반사 컷"
  - "creative reflection photo"
graph_nodes:
  - "subject:person_or_city"
  - "prop:mirror_prism_puddle"
  - "environment:urban_or_nature"
  - "lens:0.5x_1x_2x"
  - "edit_style:creative_reflection"
  - "trend_signal:playful_visual_hook"
graph_edges:
  - "reflection DOUBLES_subject"
  - "low_angle ENHANCES_puddle"
  - "prism CREATES_light_leak"
  - "symmetry INCREASES_visual_interest"
urls:
  - "https://www.samsung.com/us/explore/photography/creative-photography-tricks-thatll-get-you-all-the-likes/"
  - "https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html"
  - "https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html"
  - "https://business.adobe.com/resources/creative-trends-report.html"
---

# 거울·웅덩이·프리즘 반사 — 창의적 SNS 컷

## 추천 시스템용 요약

- **트렌드 추천:** 릴스/캐러셀에서는 결과+BTS가 함께 보이는 반사/프리즘 트릭이 trend 후보.
- **일반 추천:** 일반 추천은 반사면을 렌즈 가까이에 두고 대칭/프레임을 만드는 것.
- **개인화 추천 변수:** 개인화는 미니멀 반사/화려한 프리즘/네온 반사 선호 반영.

## 촬영 레시피

- 웅덩이는 폰을 낮게 내려 반사면을 크게 만든다.
- 거울은 프레임 안 프레임처럼 사용.
- 프리즘/CD/유리컵은 렌즈 가장자리에 살짝 대고 빛 번짐을 만든다.
- 결과 컷과 BTS 컷을 함께 저장.

## 보정 레시피

- Highlights -20~-60로 반사 하이라이트 보호.
- Contrast +5~+20, Dehaze +3~+12.
- Prism 색은 Saturation +5~+15, 피부는 mask로 보호.
- 불필요한 손/소품 가장자리는 Remove/Heal.

## 실패 방지 / 주의점

- 유리/거울은 안전과 주변 반사 노출 주의.
- 효과가 얼굴을 가리면 시선이 분산.

## 근거

### 반영한 외부 근거

- Samsung creative photography tricks는 거울, 반사, 각도 같은 스마트폰 창의 촬영 아이디어의 근거가 된다.
- Adobe 스마트폰 사진 자료는 구도와 빛을 먼저 정리하고, Lightroom masking은 피사체와 반사면을 분리해 보정하는 근거를 제공한다.
- Adobe Creative Trends 자료는 반사/프리즘 같은 실험적 시각 요소를 SNS 스타일 변형으로 연결하는 근거다.

### 시나리오 수정 포인트

- 반사 장면은 효과 자체보다 주 피사체와 시선 흐름이 먼저 읽혀야 한다.
- 보정에서는 반사면의 채도/명암을 낮춰 gimmick이 피사체를 압도하지 않게 한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:person_or_city
  - prop:mirror_prism_puddle
  - environment:urban_or_nature
  - lens:0.5x_1x_2x
  - edit_style:creative_reflection
  - trend_signal:playful_visual_hook
relationships:
  - reflection DOUBLES_subject
  - low_angle ENHANCES_puddle
  - prism CREATES_light_leak
  - symmetry INCREASES_visual_interest
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://www.samsung.com/us/explore/photography/creative-photography-tricks-thatll-get-you-all-the-likes/
- https://www.adobe.com/creativecloud/photography/discover/smartphone-photography.html
- https://helpx.adobe.com/lightroom-cc/using/masking-mobile-ios.html
- https://business.adobe.com/resources/creative-trends-report.html
