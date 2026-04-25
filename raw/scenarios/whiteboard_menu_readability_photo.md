---
title: "화이트보드·메뉴판 가독성 사진 - 원근, 눈부심, OCR 친화 보정 seed"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-25"
scenario_tags:
  - "whiteboard"
  - "menu"
  - "readability"
  - "perspective"
  - "glare"
  - "ocr"
  - "scan"
aliases:
  - "화이트보드 글자 흐림"
  - "회의판 사진"
  - "강의 판서 찍기"
  - "메뉴판 사진 안 읽힘"
  - "메뉴 글자 선명하게"
  - "whiteboard menu readability photo"
query_aliases:
  - "화이트보드나 메뉴판을 찍었는데 비스듬하고 반사가 생겨서 글자가 잘 안 읽혀요"
  - "photo of a whiteboard or menu text needs perspective correction, glare control, and readable OCR"
graph_nodes:
  - "subject:whiteboard_or_menu_text"
  - "environment:classroom_meeting_restaurant"
  - "scenario:whiteboard_menu_readability_photo"
  - "trend_signal:clean_utility_capture"
  - "preference:shareable_notes"
  - "preference:natural_context_record"
  - "edit_style:legible_text_capture"
  - "style_recipe:perspective_glare_readability"
  - "recommendation_variant:readable_whiteboard_capture"
  - "recommendation_variant:menu_text_shareable_photo"
  - "technique:scan_mode_document_whiteboard"
  - "technique:parallel_centered_capture"
  - "technique:glare_angle_control"
  - "technique:ocr_live_text_check"
  - "parameter:guided_upright_corners"
  - "parameter:contrast_clarity_for_text"
  - "parameter:highlight_glare_reduction"
  - "image_issue:skewed_perspective"
  - "image_issue:whiteboard_glare_hotspot"
  - "image_issue:small_low_contrast_text"
  - "image_issue:menu_dim_light_noise"
  - "evidence:apple_notes_scan_documents"
  - "evidence:apple_live_text_camera"
  - "evidence:samsung_document_scan"
  - "evidence:google_drive_document_scan"
  - "evidence:microsoft_onedrive_whiteboard_scan"
  - "evidence:adobe_lightroom_perspective"
graph_edges:
  - "trend_signal:clean_utility_capture SUPPORTS edit_style:legible_text_capture"
  - "preference:shareable_notes ADAPTS_TO edit_style:legible_text_capture"
  - "preference:natural_context_record ADAPTS_TO edit_style:legible_text_capture"
  - "edit_style:legible_text_capture APPLIES_TO scenario:whiteboard_menu_readability_photo"
  - "scenario:whiteboard_menu_readability_photo HAS_VARIANT recommendation_variant:readable_whiteboard_capture"
  - "scenario:whiteboard_menu_readability_photo HAS_VARIANT recommendation_variant:menu_text_shareable_photo"
  - "recommendation_variant:readable_whiteboard_capture USES technique:scan_mode_document_whiteboard"
  - "recommendation_variant:readable_whiteboard_capture USES technique:parallel_centered_capture"
  - "recommendation_variant:readable_whiteboard_capture USES technique:glare_angle_control"
  - "recommendation_variant:menu_text_shareable_photo USES technique:ocr_live_text_check"
  - "recommendation_variant:readable_whiteboard_capture SETS parameter:guided_upright_corners"
  - "recommendation_variant:readable_whiteboard_capture SETS parameter:contrast_clarity_for_text"
  - "recommendation_variant:readable_whiteboard_capture SETS parameter:highlight_glare_reduction"
  - "image_issue:skewed_perspective ADJUSTS parameter:guided_upright_corners"
  - "image_issue:whiteboard_glare_hotspot ADJUSTS technique:glare_angle_control"
  - "image_issue:small_low_contrast_text ADJUSTS parameter:contrast_clarity_for_text"
  - "image_issue:menu_dim_light_noise CONSTRAINS technique:ocr_live_text_check"
  - "recommendation_variant:readable_whiteboard_capture SUPPORTED_BY evidence:apple_notes_scan_documents"
  - "recommendation_variant:menu_text_shareable_photo SUPPORTED_BY evidence:apple_live_text_camera"
  - "recommendation_variant:readable_whiteboard_capture SUPPORTED_BY evidence:samsung_document_scan"
  - "recommendation_variant:readable_whiteboard_capture SUPPORTED_BY evidence:google_drive_document_scan"
  - "recommendation_variant:readable_whiteboard_capture SUPPORTED_BY evidence:microsoft_onedrive_whiteboard_scan"
  - "recommendation_variant:readable_whiteboard_capture SUPPORTED_BY evidence:adobe_lightroom_perspective"
urls:
  - "https://support.apple.com/guide/iphone/scan-text-and-documents-iph653f28965/ios"
  - "https://support.apple.com/guide/iphone/use-live-text-iphcf0b71b0e/ios"
  - "https://www.samsung.com/us/support/answer/ANS10003696/"
  - "https://support.google.com/drive/answer/3145835?co=GENIE.Platform%3DAndroid&hl=en"
  - "https://support.microsoft.com/en-us/office/scan-a-whiteboard-document-business-card-or-photo-in-onedrive-for-ios-7b5425d5-754f-4201-b88f-13fc765d7d3a"
  - "https://www.adobe.com/learn/lightroom-cc/web/perspective-correction"
---

# 화이트보드·메뉴판 가독성 사진 - 원근, 눈부심, OCR 친화 보정 seed

## 추천 시스템용 요약

- **트렌드 추천:** 감성 사진보다 읽히는 결과물이 중요한 clean utility capture. 회의/강의/여행 메뉴 공유용으로 바로 검색, 번역, 공유할 수 있는 이미지를 목표로 한다.
- **일반 추천:** 스캔 모드, 정면 평행, 글자 초점, 반사 회피, 원근 보정이 우선이다.
- **개인화 추천 변수:** 사용자가 OCR/공유를 원하면 흑백·고대비로, 현장 분위기 기록을 원하면 주변 맥락과 색을 일부 남긴다.

## 촬영 레시피

- 종이 메뉴나 인쇄물은 Apple Notes, Samsung 문서 스캔, Google Drive 스캔처럼 경계 인식과 모서리 조정이 있는 스캔 흐름을 우선한다.
- 화이트보드는 가능한 한 보드 중앙에 서고, 폰을 보드와 평행하게 둔다. 네 모서리가 프레임 안에 조금 여백을 두고 들어와야 나중에 원근 보정이 쉽다.
- 광택 메뉴판이나 화이트보드에 핫스팟이 생기면 플래시를 끄고 몸 위치를 살짝 옮겨 반사점을 글자 밖으로 보낸다.
- 글자가 작으면 전체 한 장만 고집하지 말고, 전체 맥락 컷 1장과 구역별 읽기 컷을 따로 찍는다.
- 메뉴판은 항목명, 가격, 알레르기/옵션 문구가 잘리는지 확인한다. iPhone 사용자는 Live Text가 주요 문구를 감지하는지 확인하면 재촬영 판단이 빠르다.
- 어두운 식당 메뉴는 음식 사진처럼 무드보다 글자 판독이 우선이다. 폰을 테이블이나 컵에 기대어 흔들림을 줄이고, 주변 손전등/torch는 정면 반사가 아니라 측면 보조광으로 시험한다.

## 보정 레시피

- Crop/Geometry에서 Auto 또는 Guided Upright로 수평·수직 기준선을 맞춘다. Adobe Lightroom 문서처럼 Guided Upright는 장면의 선을 직접 지정할 때 유용하다.
- 글자용 버전은 Exposure를 과하게 올리기보다 Highlights -20~-60, Whites -10~-30으로 반사 영역을 먼저 줄인다.
- Contrast +10~+25, Clarity/Texture +5~+15에서 시작하고, 글자 가장자리에 halo가 생기면 낮춘다.
- 공유/OCR용은 B&W 또는 grayscale 필터가 안전할 수 있다. 메뉴판 색과 음식 사진이 함께 중요한 경우에는 색 버전을 별도로 남긴다.
- 손, 그림자, 종이 구겨짐은 스캔 앱의 경계/필터/정리 기능을 먼저 쓰고, 보정 앱에서는 핵심 글자를 해치지 않는 범위에서만 지운다.

## 스타일 / 개인화 변형

- **트렌드형:** 노트 앱에 바로 붙일 수 있는 깔끔한 utility capture. 배경 장식보다 글자 대비와 수평을 우선한다.
- **일반형:** 전체 보드/메뉴 구조를 보존하고 모서리와 제목을 살린다.
- **개인화형:** 여행 기록형은 메뉴판 주변 분위기를 남기고, 업무 공유형은 크롭을 타이트하게 하며 고대비 흑백으로 저장한다.

## 실패 방지 / 주의점

- 이 파일은 기존 `document_scan_correction`의 문서 스캔 일반론을 복제하지 않고, **화이트보드·메뉴판의 반사, 원근, 작은 글자 판독**을 분리해 다룬다.
- 원본이 너무 흔들렸거나 글자가 과노출로 사라진 경우에는 보정보다 재촬영이 낫다.
- 원근 보정을 강하게 걸면 가장자리 글자가 늘어질 수 있으므로, 중요한 텍스트는 중앙에 가깝게 한 번 더 찍는다.
- OCR 결과는 편의를 위한 것이며, 가격·공지·계약성 정보는 원본 사진을 함께 보관한다.

## 근거

### 반영한 외부 근거

- Apple Notes scan 문서는 문서가 화면에 들어오게 위치시키고, 자동 캡처/수동 캡처 후 모서리를 조정하는 흐름을 제공한다.
- Apple Live Text 문서는 카메라 프레임 안 텍스트를 감지해 복사, 번역, 검색할 수 있다고 설명한다.
- Samsung document scan 문서는 스캔이 원치 않는 그림자나 손 등을 제거하고 직사각형을 정렬해 문서를 곧고 읽기 쉽게 만든다고 설명한다.
- Google Drive scan 문서는 파란 윤곽선으로 crop 영역을 표시하고, 스캔 영역 조정과 필터를 제공한다.
- Microsoft OneDrive scan 문서는 Whiteboard, Document, Business Card, Photo 모드와 플래시 설정, crop/rotate/텍스트/하이라이트 편집 및 PDF 저장을 안내한다.
- Adobe Lightroom perspective correction 문서는 Upright와 Guided Upright로 수평·수직선 기반 원근 보정을 하는 근거를 제공한다.

### 시나리오 수정 포인트

- `whiteboard_glare_hotspot`, `skewed_perspective`, `small_low_contrast_text`는 추천의 중심축이 아니라 `legible_text_capture`를 안전하게 만들기 위한 조정 조건이다.
- 사용자가 "예쁘게"보다 "읽히게"를 원하면 색감 레시피보다 원근·반사·대비·OCR 확인 순서를 우선한다.

## Graphify 추출 힌트

```yaml
entities:
  - subject:whiteboard_or_menu_text
  - trend_signal:clean_utility_capture
  - preference:shareable_notes
  - edit_style:legible_text_capture
  - image_issue:skewed_perspective
  - image_issue:whiteboard_glare_hotspot
relationships:
  - clean_utility_capture SUPPORTS legible_text_capture
  - skewed_perspective ADJUSTS guided_upright_corners
  - whiteboard_glare_hotspot ADJUSTS glare_angle_control
  - small_low_contrast_text ADJUSTS contrast_clarity_for_text
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://support.apple.com/guide/iphone/scan-text-and-documents-iph653f28965/ios
- https://support.apple.com/guide/iphone/use-live-text-iphcf0b71b0e/ios
- https://www.samsung.com/us/support/answer/ANS10003696/
- https://support.google.com/drive/answer/3145835?co=GENIE.Platform%3DAndroid&hl=en
- https://support.microsoft.com/en-us/office/scan-a-whiteboard-document-business-card-or-photo-in-onedrive-for-ios-7b5425d5-754f-4201-b88f-13fc765d7d3a
- https://www.adobe.com/learn/lightroom-cc/web/perspective-correction
