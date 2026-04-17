---
title: "Adobe Learn — AI-assisted masking in Lightroom Mobile"
category: "lightroom"
priority: "A"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://www.adobe.com/learn/lightroom-cc/web/ai-assisted-masking-lightroom-mobile"
practical_tags:
  - "인물"
  - "Lightroom"
  - "프리셋"
  - "라이트룸모바일"
  - "AI마스킹"
  - "피사체선택"
  - "하늘선택"
  - "로컬보정"
---

# Adobe Learn — AI-assisted masking in Lightroom Mobile — 상황별 촬영/보정 팁

이 파일은 더 이상 단순 소스 메타데이터가 아니라, 실제 촬영/보정 때 바로 써먹는 레시피 형태로 정리한다.

## 바로 쓰는 팁 카드

### Tip 1. 인물·제품은 살리고 배경은 정리하고 싶을 때

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

### Tip 2. 하늘이 하얗게 날아갔거나 노을 색이 밋밋할 때

**촬영/작업 순서**
- 촬영할 때 하늘 기준으로 노출을 약간 낮춰 RAW/ProRAW/DNG로 저장한다.
- 태양을 직접 넣을 때는 렌즈 플레어 위치를 화면 가장자리로 조절한다.

**추천 시작값 / 조작값**
- Masking → Select Sky
- Highlights -20~-70 시작
- Dehaze +5~+20 시작
- Temp 노을은 +, 파란 하늘은 Blue Luminance -5~-20 시작

**보정 루틴**
- Sky mask로 하늘만 복구한다.
- Color Mix에서 Blue/Orange의 Saturation과 Luminance를 따로 만진다.
- 전경은 별도 Linear Gradient 또는 Subject/Background mask로 분리한다.

**주의할 점**
- 하늘만 과하게 파랗게 만들면 합성처럼 보인다.
- Dehaze를 과하게 올리면 노이즈와 띠 현상이 생긴다.

**확실성:** Adobe Masking/Color Mix 공식 기능 + 실전 시작점.
**근거:** Adobe Learn은 Select Sky/Background, Color Mix, Hue/Saturation/Luminance 조정을 설명한다.

### Tip 3. 사진 속 작은 방해물·먼지·사람·쓰레기를 지우고 싶을 때

**촬영/작업 순서**
- 촬영 단계에서 배경 가장자리를 먼저 확인하고 한 걸음 옆으로 이동해 방해물을 줄인다.
- 그래도 지울 대상이 있으면 주변 질감이 단순한 위치에서 찍는 편이 보정 성공률이 높다.

**추천 시작값 / 조작값**
- Lightroom/Photos Remove/Clean Up: 작은 물체부터 처리
- 복잡한 경계는 확대해서 여러 번 나눠 지우기

**보정 루틴**
- 큰 물체는 한 번에 지우지 말고 작은 영역으로 나눠 처리한다.
- 지운 뒤 주변 반복 패턴/그림자를 확대 확인한다.
- 인물 경계가 망가지면 원본으로 되돌리고 크롭/구도 재선택을 고려한다.

**주의할 점**
- 보도/다큐 사진에서 내용 의미를 바꾸는 삭제는 하지 않는다.
- SNS용 미화와 기록용 사진을 구분한다.

**확실성:** Apple/Adobe AI 편집 기능 기반 실전 원칙.
**근거:** Apple Photos Clean Up, Adobe Remove/Masking 계열 기능.

### Tip 4. 라이트룸 인기 프리셋/Community 편집을 내 사진에 적용할 때

**촬영/작업 순서**
- 프리셋을 쓸 사진은 노출이 너무 망가지지 않게 원본을 깔끔하게 찍는다.
- 같은 장소/빛 조건 사진을 여러 장 묶어 프리셋 일관성을 확인한다.

**추천 시작값 / 조작값**
- Presets → Recommended/Premium/Yours
- Adaptive Preset은 Subject/Background 등 특정 영역에 적용 가능
- Amount slider: 40~80부터 시작해 과하면 낮춘다

**보정 루틴**
- 프리셋 적용 후 Exposure/WB를 먼저 맞춘다.
- 피부색이 망가지면 Orange/Red Color Mix를 되돌린다.
- 마음에 드는 Community 편집은 Save as Preset으로 저장한다.

**주의할 점**
- 프리셋을 완성값으로 믿지 말고 출발점으로 쓴다.
- 다른 조명에서 만든 프리셋을 그대로 복사하면 색이 틀어진다.

**확실성:** Adobe Learn/Help 공식 기능 + 실전 시작점.
**근거:** Adobe Learn은 Adaptive presets, Amount 조정, Community/Save as Preset 흐름을 설명한다.

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
- https://www.adobe.com/learn/lightroom-cc/web/ai-assisted-masking-lightroom-mobile

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
