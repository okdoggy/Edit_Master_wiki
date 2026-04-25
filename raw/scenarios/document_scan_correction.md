---
title: "문서/화이트보드 스캔 보정 - 글자 가독성과 원근 교정 추천 seed"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-25"
scenario_tags:
  - "document"
  - "scan"
  - "whiteboard"
  - "perspective"
  - "readability"
aliases:
  - "문서 스캔 보정"
  - "A4 계약서가 사다리꼴로 찍힘"
  - "화이트보드 글자 선명하게 보정"
  - "종이 그림자 제거"
  - "document scan correction"
  - "skewed notes readable document"
query_aliases:
  - "스마트폰으로 찍은 문서가 비뚤고 회색으로 보여서 깨끗한 스캔처럼 만들고 싶다"
  - "whiteboard photographed at an angle needs perspective correction and readable text"
graph_nodes:
  - "subject:document_or_whiteboard"
  - "scenario:document_scan_correction"
  - "trend_signal:clean_utility_capture"
  - "edit_style:clean_document_readability"
  - "recommendation_variant:document_readable_scan"
  - "technique:corner_detection"
  - "technique:guided_upright"
  - "parameter:contrast_clarity_for_text"
  - "image_issue:skewed_corners"
  - "image_issue:paper_shadow"
  - "evidence:apple_notes_scan_documents"
  - "evidence:samsung_document_scan"
  - "evidence:adobe_lightroom_perspective"
graph_edges:
  - "trend_signal:clean_utility_capture SUPPORTS edit_style:clean_document_readability"
  - "edit_style:clean_document_readability APPLIES_TO scenario:document_scan_correction"
  - "scenario:document_scan_correction HAS_VARIANT recommendation_variant:document_readable_scan"
  - "recommendation_variant:document_readable_scan USES technique:corner_detection"
  - "recommendation_variant:document_readable_scan USES technique:guided_upright"
  - "recommendation_variant:document_readable_scan SETS parameter:contrast_clarity_for_text"
  - "image_issue:skewed_corners ADJUSTS technique:guided_upright"
  - "image_issue:paper_shadow CONSTRAINS parameter:contrast_clarity_for_text"
  - "recommendation_variant:document_readable_scan SUPPORTED_BY evidence:apple_notes_scan_documents"
  - "recommendation_variant:document_readable_scan SUPPORTED_BY evidence:samsung_document_scan"
  - "recommendation_variant:document_readable_scan SUPPORTED_BY evidence:adobe_lightroom_perspective"
urls:
  - https://support.apple.com/guide/iphone/scan-text-and-documents-iph653f28965/ios
  - https://www.samsung.com/us/support/answer/ANS10003696/
  - https://www.adobe.com/learn/lightroom-cc/web/straighten-photos-perspective-correction
  - https://www.adobe.com/learn/lightroom-cc/web/perspective-correction
---

# 문서/화이트보드 스캔 보정 - 글자 가독성과 원근 교정 추천 seed

## 추천 시스템용 요약

- **트렌드 추천:** SNS용 감성 사진이 아니라 "읽히는 결과물"이 우선인 utility capture. 깔끔한 흑백/그레이스케일, 직각 정렬, 균일한 배경 톤을 추천한다.
- **일반 추천:** 촬영 단계에서는 문서 가장자리 네 꼭짓점이 보이게 찍고, 편집 단계에서는 원근/자르기/대비를 먼저 잡은 뒤 색을 줄인다.
- **개인화 추천 변수:** 사용자가 자연스러운 종이 질감을 원하면 흑백 강도를 낮추고, 보관/공유용이면 대비와 선명도를 더 강하게 둔다.

## 촬영 레시피

- 종이 전체와 네 모서리가 화면 안에 들어오도록 한 걸음 물러난다.
- 가능하면 iPhone Notes, Samsung Gallery/Camera의 문서 스캔 모드를 우선 사용한다.
- 그림자가 생기면 조명을 종이 옆면으로 보내고, 손이나 휴대폰 그림자가 문서 위에 닿지 않게 각도를 바꾼다.
- 화이트보드는 비스듬히 찍지 말고, 가능한 한 보드 중심에 평행하게 선다.

## 보정 레시피

- Crop/Geometry에서 Auto 또는 Guided Upright로 수평/수직 기준선을 맞춘다.
- 문서 모서리가 잘린 경우에는 과한 Full 보정보다 수동 가이드와 Constrain Crop을 사용한다.
- Exposure는 종이가 하얗게 보일 만큼만 올리고, Contrast/Clarity/Texture는 글자가 또렷해지는 지점에서 멈춘다.
- 색 번짐이 있으면 Saturation을 낮추거나 흑백/그레이스케일 필터를 적용한다.

## 실패 방지 / 주의점

- 종이를 너무 꽉 채워 찍으면 원근 보정 후 가장자리가 잘린다.
- 글자를 살리겠다고 Clarity를 과하게 올리면 종이 섬유와 그림자까지 거칠게 살아난다.
- 중요한 계약서/증빙은 감성 보정보다 원본 보존과 PDF 저장을 우선한다.

## 근거

### 반영한 외부 근거

- Apple Notes 스캔 문서는 문서 경계 감지, 모서리 조정, 필터 적용을 공식 기능으로 설명한다.
- Samsung 문서 스캔 문서는 그림자/손 등 방해 요소 제거와 사각형 정렬, PDF 저장 흐름을 안내한다.
- Adobe Lightroom 학습 문서는 Upright/Guided Upright와 Geometry 보정으로 기울어진 수직/수평선을 교정하는 방법을 제공한다.

### 시나리오 수정 포인트

- 이 시나리오는 인물/음식/제품 사진이 아니라 가독성 중심의 utility scenario로 분리한다.
- 핵심 이슈는 "예쁘게 보정"이 아니라 skewed corners, paper shadow, text readability다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:document_or_whiteboard
  - trend_signal:clean_utility_capture
  - edit_style:clean_document_readability
  - image_issue:skewed_corners
  - image_issue:paper_shadow
relationships:
  - clean_utility_capture SUPPORTS clean_document_readability
  - skewed_corners ADJUSTS guided_upright
  - paper_shadow CONSTRAINS contrast_clarity_for_text
recommendation_modes: [general, personalized]
```

## 출처

- https://support.apple.com/guide/iphone/scan-text-and-documents-iph653f28965/ios
- https://www.samsung.com/us/support/answer/ANS10003696/
- https://www.adobe.com/learn/lightroom-cc/web/straighten-photos-perspective-correction
- https://www.adobe.com/learn/lightroom-cc/web/perspective-correction
