---
title: "PHLEARN — Lightroom Mobile beginner guide"
category: "lightroom"
priority: "B"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://phlearn.com/tutorial/intro-to-lightroom-mobile/"
practical_tags:
  - "RAW"
  - "DNG"
  - "인물"
  - "Lightroom"
  - "라이트룸모바일"
  - "입문가이드"
  - "색보정"
  - "선택보정"
---

# PHLEARN — Lightroom Mobile beginner guide — 상황별 촬영/보정 팁

이 파일은 더 이상 단순 소스 메타데이터가 아니라, 실제 촬영/보정 때 바로 써먹는 레시피 형태로 정리한다.

## 바로 쓰는 팁 카드

### Tip 1. 후보정을 크게 할 사진을 찍을 때 — 노을, 야경, 실내, 공연, 역광

**촬영/작업 순서**
- 기본 JPEG/HEIC 대신 iPhone ProRAW, Samsung Expert RAW, Lightroom Mobile DNG 등 RAW 계열을 선택한다.
- 하이라이트가 날아가지 않게 살짝 어둡게 찍고, 그림자는 후보정에서 필요한 만큼만 올린다.
- 색온도가 어려운 조명에서는 Auto WB로 찍되 RAW에서 나중에 맞춘다.
- 연속 촬영이 필요한 순간은 RAW보다 일반 모드가 빠를 수 있으므로 장면별로 전환한다.

**추천 시작값 / 조작값**
- Format: ProRAW/Expert RAW/DNG
- EV: -0.3~-1.0 시작
- ISO: 가능하면 낮게
- 셔터: 움직이는 피사체는 1/125s 이상 확보

**보정 루틴**
- WB → Exposure → Highlights/Shadows → Curve → Color Mix → Mask 순서
- 노이즈가 심하면 Detail보다 먼저 Color Noise Reduction 확인
- 최종 SNS용은 JPEG/HEIC로 export

**주의할 점**
- RAW가 항상 더 좋은 것은 아니다. 용량/처리시간/연속성 손실이 있다.
- 어두운 RAW를 무리하게 밝히면 노이즈가 크게 증가한다.

**확실성:** Adobe/Envato/Samsung/Apple RAW 워크플로우 기반.
**근거:** Adobe/Envato는 Lightroom Mobile DNG 촬영과 RAW의 보정 여지를 설명하고, Samsung/Apple은 ProRAW/Expert RAW 흐름을 제공한다.

### Tip 2. 사진 전체 필터가 아니라 특정 색만 고치고 싶을 때

**촬영/작업 순서**
- 현장에서 색이 중요한 피사체를 의식하고, 같은 장소에서 밝은 컷/어두운 컷을 하나씩 확보한다.

**추천 시작값 / 조작값**
- Color → Mix
- 피부: Orange Saturation -5~+5, Luminance +0~+10부터 조심스럽게
- 하늘: Blue Saturation -10~+15, Luminance -5~-20 시작
- 잔디: Green/Yellow Saturation -10~-30로 산만함 줄이기

**보정 루틴**
- Targeted Adjustment Tool로 이미지 위 색을 직접 찍고 조정한다.
- Hue는 크게 움직이면 색이 가짜처럼 보이므로 작게 움직인다.
- Before/After를 눌러 과보정 여부를 확인한다.

**주의할 점**
- 피부색과 배경 주황/노랑이 함께 바뀔 수 있으므로 마스크와 병행한다.
- 채도만 올리면 저렴한 필터 느낌이 난다.

**확실성:** Adobe 공식 Color Mix 절차 + 실전 시작점.
**근거:** Adobe Learn은 Color Mix에서 색상별 Hue/Saturation/Luminance와 Targeted Adjustment Tool 사용을 설명한다.

### Tip 3. 인물·제품은 살리고 배경은 정리하고 싶을 때

**촬영/작업 순서**
- 촬영 때 피사체와 배경을 분리해 둔다. 최소 1~3m 거리 확보.
- 배경이 복잡하면 망원 렌즈나 Portrait mode를 먼저 활용한다.

**추천 시작값 / 조작값**
- Lightroom Mobile: Masking → Select Subject 또는 Quick Action Subject
- Subject: Exposure +0.1~+0.4, Contrast +5~+15 시작
- Background: Exposure -0.1~-0.4 또는 Saturation -5~-20 시작

**보정 루틴**
- Subject mask에서 얼굴/제품 밝기만 올린다.
- Background mask로 채도·명료도를 낮춰 시선을 분리한다.
- Add/Subtract로 머리카락·손·제품 경계를 확인한다.

**주의할 점**
- 전체 Exposure를 올려 배경까지 밝히지 않는다.
- 마스크 경계가 어색하면 효과 Amount를 줄인다.

**확실성:** Adobe Learn 공식 기능 + 실전 시작점.
**근거:** Adobe Learn은 Quick Action Subject, Select Background, Exposure/Contrast/Saturation 조정을 설명한다.

### Tip 4. 인스타그램·틱톡·블로그에 올릴 최종본을 만들 때

**촬영/작업 순서**
- 촬영 때 4:5, 1:1, 9:16 크롭 가능성을 염두에 두고 가장자리 여백을 남긴다.
- 릴스/쇼츠용이면 결과물과 BTS를 세로로 동시에 촬영한다.

**추천 시작값 / 조작값**
- Instagram Feed: 4:5 후보 크롭
- Stories/Reels/TikTok: 9:16
- Export: sRGB JPEG, 긴 변 2000~3000px 시작

**보정 루틴**
- 작은 화면에서 먼저 확인하고 밝기/대비를 조금 더 명확하게 만든다.
- 샤픈은 업로드 압축 후 halo가 생기지 않게 약하게
- 시리즈는 색온도와 대비를 통일한다.

**주의할 점**
- 원본 전체 구도만 믿고 세로 플랫폼에 올리면 핵심 피사체가 잘린다.
- 과한 HDR/Clarity는 모바일 화면에서 지저분해 보인다.

**확실성:** SNS 실전 워크플로우 시작점.
**근거:** iPhone Photography School/Instagram tips, Dan Rubin식 모바일 편집, 일반 SNS 출판 경험 통합.

## 최신 Lightroom Mobile 검증 레시피

### RAW/DNG + Adaptive Profile로 시작하기

**상황**
- 폰 사진이 평평하거나, 하이라이트/그림자 복원이 필요할 때.

**작업 순서**
- RAW/DNG 또는 ProRAW/Expert RAW 파일을 Lightroom Mobile로 가져온다.
- Edit → Profiles에서 Adaptive Color 또는 Adaptive B&W를 먼저 적용한다.
- 이후 Light 패널에서 Exposure, Highlights, Shadows를 조정한다.

**확인된 조작값 / 시작값**
- Adaptive Profile Intensity: 0~200 범위.
- 시작값: Exposure +0.3~+0.7, Highlights -30~-70, Shadows +20~+50.

**주의점**
- Adaptive Profile은 Adobe 기준으로 “다른 조정 전에 먼저” 적용하는 편이 안전하다.
- JPG보다 RAW/DNG가 여유롭지만, 완전히 날아간 하이라이트는 복구되지 않는다.

### HDR / 역광 톤 정리

**상황**
- 하늘이 날아가고 그림자가 뭉개진 역광 사진.

**작업 순서**
- Edit → Light → Edit in HDR mode를 켠다.
- 히스토그램은 두 손가락 탭으로 확인한다.
- Exposure → Contrast → Highlights → Shadows → Whites → Blacks 순서로 정리한다.

**주의점**
- HDR 효과는 HDR 지원 디스플레이/앱에서 제대로 보인다.
- Android Ultra HDR, AVIF/JXL/JPG Gain Map 등은 기기와 앱 지원 차이가 있다.

### Subject / Sky / Background 마스크 분리 보정

**상황**
- 인물은 살리고 배경은 눌러 주인공을 튀게 하고 싶을 때.

**작업 순서**
- Actions 또는 Masking에서 Subject / Sky / Background를 선택한다.
- 피사체는 Exposure를 살짝 올리고 Shadows를 보강한다.
- 하늘은 Exposure를 조금 내리고 Highlights를 회복한다.
- 배경은 Exposure 또는 Saturation을 줄여 분리감을 만든다.

**확인된 조작값 / 시작값**
- Brush 보정 Density: 약 50부터 시작.
- Subject Exposure +0.1~+0.4.
- Background Saturation -5~-20.
- Sky Highlights -30~-70.

**주의점**
- AI 마스크가 들어간 프리셋은 사진이 바뀌면 마스크 위치/수동 보정이 어긋날 수 있다.

### Color Mix / HSL로 특정 색만 정리

**상황**
- 피부가 너무 오렌지, 하늘이 과하게 시안, 잔디가 네온처럼 보일 때.

**작업 순서**
- Color → Mix 또는 HSL로 들어간다.
- Target Adjustment Tool로 사진 위 색을 직접 잡아 조정한다.
- 먼저 WB를 맞춘 뒤 HSL을 얇게 쓴다.

**시작값**
- Hue: ±5~15.
- Saturation: ±5~20.
- Luminance: ±5~15.

**주의점**
- Orange를 움직이면 피부톤 전체가 같이 움직일 수 있다. 인물 사진은 마스크와 병행한다.

### 프리셋은 완성품이 아니라 출발점

**상황**
- 같은 룩을 여러 장에 빠르게 입히고 싶을 때.

**작업 순서**
- Preset을 적용한다.
- Amount slider로 강도를 낮춰 사진에 맞춘다.
- Exposure/WB를 다시 맞춘다.
- 데스크톱 프리셋은 Import Profiles & Presets 또는 DNG 기반 이동을 사용한다.

**확인된 조작값 / 시작값**
- Preset Amount/Intensity: 기능·버전에 따라 0~100 또는 0~200 범위로 보일 수 있음. 실전 시작은 40~80.
- 실전 시작점: 40~80%.

### Export / Share 용도별 내보내기

**상황**
- 인스타, 메시지, 보관용 원본, 인쇄용 파일을 따로 만들 때.

**작업 순서**
- Export as...에서 JPG / AVIF / JXL / TIF / DNG / Original 중 선택한다.
- JPG/TIF는 Largest Available Dimensions 또는 Small(2048 px)을 선택할 수 있다.
- 인스타그램은 square 또는 4:5 크롭을 우선 고려한다.

**확인된 조작값**
- JPG 품질: 10%~100%.
- Small export: 2048 px 옵션.

## 이 소스에서 더 캐야 할 것

- 실제 Community/튜토리얼 예제에서 슬라이더 순서를 더 수집
- 마스크/프리셋/Color Mix를 각각 독립 레시피로 분리
- 사진 장르별 시작값을 테스트하며 보정 범위를 좁히기

## 출처

- https://photography.tutsplus.com/tutorials/sync-presets-from-lightroom-classic-to-lightroom-mobile--cms-38431
- https://fstoppers.com/photoshop/edit-your-images-faster-lightrooms-ai-masks-627384
- https://petapixel.com/2021/10/27/how-to-leverage-lightrooms-new-masking-tools-in-your-workflow/
- https://helpx.adobe.com/lightroom-cc/using/save-and-export-photo-ios.html
- https://helpx.adobe.com/lightroom-cc/using/actions-lightroom-ios.html
- https://helpx.adobe.com/lightroom-cc/using/hdr-ios.html
- https://helpx.adobe.com/lightroom-cc/using/edit-photos-mobile-ios.html
- https://phlearn.com/tutorial/intro-to-lightroom-mobile/

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
