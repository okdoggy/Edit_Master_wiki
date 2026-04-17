---
title: "Evan Ranft"
category: "youtube"
priority: "B"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://www.youtube.com/@RanftEvan"
  - "https://www.youtube.com/watch?v=pnaSMvmlWnc"
  - "https://www.youtube.com/watch?v=87TEUKmnmcg"
  - "https://socialblade.com/youtube/handle/ranftevan/achievements"
practical_tags:
  - "RAW"
  - "DNG"
  - "프리셋"
  - "아이폰RAW"
  - "라이트룸모바일"
  - "프로워크플로우"
  - "보정루틴"
---

# Evan Ranft — 상황별 촬영/보정 팁

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

### Tip 3. 하늘이 하얗게 날아갔거나 노을 색이 밋밋할 때

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

## 출처에서 확인된 구체 레시피

### Evan Ranft — iPhone 카메라 기본 세팅 잠그기

**상황**
- 최신 iPhone으로 사진을 제대로 찍고 후반 편집 여지를 남기고 싶을 때.

**촬영/작업 순서**
- Settings → Camera → Formats로 이동.
- ProRaw & Resolution Control을 활성화.
- Pro Defaults에서 ProRaw Max를 켠다.
- Camera 앱에서 Grid와 Level을 켜 구도와 수평을 관리한다.
- 촬영 시 Exposure Compensation을 상황에 맞게 조절한다.
- 촬영 후 Lightroom iOS로 수동 가져와 편집하고, 공유할 때 JPEG로 변환한다.

**확인된 수치/조건**
- ProRaw Max: 최대 48MP.
- 데모 기종: iPhone 16 Pro.

**주의점**
- 대부분의 원리는 다른 Pro 모델에도 적용 가능하지만 UI/해상도 옵션은 기종별로 다를 수 있다.

## 이 소스에서 더 캐야 할 것

- 대표 영상의 챕터별 팁을 1카드 1상황으로 분해
- 영상 속 화면에 보이는 슬라이더/카메라 설정은 숫자로 기록
- Before/After가 있는 장면은 보정 순서를 따로 추출

## 출처

- https://www.shutterbug.com/content/making-most-your-iphone-camera-settings-workflow-more-video
- https://www.youtube.com/@RanftEvan
- https://www.youtube.com/watch?v=pnaSMvmlWnc
- https://www.youtube.com/watch?v=87TEUKmnmcg
- https://socialblade.com/youtube/handle/ranftevan/achievements

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
