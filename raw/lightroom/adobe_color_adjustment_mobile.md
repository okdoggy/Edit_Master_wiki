---
title: "Adobe Learn — Color adjustment on phone or tablet"
category: "lightroom"
priority: "A"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
practical_tags:
  - "인물"
  - "라이트룸모바일"
  - "컬러믹스"
  - "HSL"
  - "색상"
  - "채도"
  - "휘도"
---

# Adobe Learn — Color adjustment on phone or tablet — 상황별 촬영/보정 팁

이 파일은 더 이상 단순 소스 메타데이터가 아니라, 실제 촬영/보정 때 바로 써먹는 레시피 형태로 정리한다.

## 바로 쓰는 팁 카드

### Tip 1. 사진 전체 필터가 아니라 특정 색만 고치고 싶을 때

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

### Tip 3. 스마트폰으로 자연스러운 인물 사진을 찍을 때

**촬영/작업 순서**
- 직사광 아래 정면 얼굴을 피하고, 그늘·창가·건물 그림자 경계의 부드러운 빛을 찾는다.
- 배경이 복잡하면 2x/3x/5x 망원 또는 Portrait mode로 배경을 압축한다.
- 눈에 초점을 탭하고, 피부가 너무 밝게 뜨면 노출을 살짝 낮춘다.
- 인물과 배경 사이를 1~3m 이상 벌려 깊이감을 만든다.

**추천 시작값 / 조작값**
- Lens: 2x/3x/5x 망원 우선, 좁은 실내는 1x
- Portrait depth: 촬영 후 f값/블러를 약하게 조정
- EV: 피부 하이라이트 날림 시 -0.3~-0.7
- Live/Burst: 표정 변화가 빠르면 사용

**보정 루틴**
- Subject mask로 얼굴 Exposure +0.1~+0.3 정도만
- Skin tone은 Orange Saturation/Luminance를 과하게 만지지 않는다.
- 배경은 Saturation/Clarity를 낮춰 시선 분리

**주의할 점**
- 초광각으로 얼굴 가까이 찍으면 왜곡이 커진다.
- Portrait blur를 과하게 주면 머리카락/안경 경계가 부자연스럽다.

**확실성:** 일반 인물 촬영 원칙 + 스마트폰 렌즈 선택 실전 시작점.
**근거:** National Geographic의 자연광 조언, Apple/Samsung Portrait 기능, Lightroom mask 편집 흐름 통합.

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
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
