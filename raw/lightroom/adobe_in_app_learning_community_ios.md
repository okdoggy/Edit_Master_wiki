---
title: "Adobe Help — In-app learning and inspiration / Community"
category: "lightroom"
priority: "A"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://helpx.adobe.com/lightroom-cc/using/in-app-learning-ios.html"
practical_tags:
  - "프리셋"
  - "라이트룸커뮤니티"
  - "Discover"
  - "편집리플레이"
  - "리믹스"
  - "프리셋저장"
---

# Adobe Help — In-app learning and inspiration / Community — 상황별 촬영/보정 팁

이 파일은 더 이상 단순 소스 메타데이터가 아니라, 실제 촬영/보정 때 바로 써먹는 레시피 형태로 정리한다.

## 바로 쓰는 팁 카드

### Tip 1. 라이트룸 인기글/Community에서 고수 보정법을 훔쳐 배우고 싶을 때

**촬영/작업 순서**
- 먼저 비슷한 빛/피사체의 내 사진을 준비한다.
- Community에서 비슷한 장르를 찾고 Play edits로 편집 순서를 본다.

**추천 시작값 / 조작값**
- Community → For you/New/Featured/Trending
- Play edits로 단계별 슬라이더 확인
- Save as Preset으로 저장 후 Amount 조절

**보정 루틴**
- 첫 번째로 어떤 패널을 만지는지 기록한다: Light, Color, Mask, Effects 중 무엇이 먼저인지.
- 마스크가 쓰였는지 확인하고, 단순 프리셋인지 국소 보정인지 구분한다.
- 내 사진에는 Exposure/WB를 먼저 맞춘 뒤 Preset을 적용한다.

**주의할 점**
- 인기글 슬라이더를 숫자 그대로 복사하지 않는다. 원본 노출과 색온도가 다르면 결과가 달라진다.
- HDR 지원 여부 등 Community 제한을 확인한다.

**확실성:** Adobe Help 공식 Community 기능.
**근거:** Adobe Help는 Community에서 단계별 편집 보기, Remix, Save as Preset을 설명한다.

### Tip 2. 라이트룸 인기 프리셋/Community 편집을 내 사진에 적용할 때

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

### Tip 3. 인스타그램·틱톡·블로그에 올릴 최종본을 만들 때

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
- https://helpx.adobe.com/lightroom-cc/using/in-app-learning-ios.html

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
