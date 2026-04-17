---
title: "Apple Support — iPhone Night mode"
category: "magazine"
priority: "A"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios"
practical_tags:
  - "저조도"
  - "RAW"
  - "아이폰"
  - "DNG"
  - "야간촬영"
  - "삼각대"
  - "흔들림방지"
---

# Apple Support — iPhone Night mode — 상황별 촬영/보정 팁

이 파일은 더 이상 단순 소스 메타데이터가 아니라, 실제 촬영/보정 때 바로 써먹는 레시피 형태로 정리한다.

## 바로 쓰는 팁 카드

### Tip 1. 아이폰으로 밤거리·실내 저조도·야경을 찍을 때

**촬영/작업 순서**
- 저조도에서 Night mode가 자동으로 켜지면 끄지 말고, 노란 달 아이콘/Camera Controls에서 노출 시간을 확인한다.
- 정적인 장면은 삼각대·난간·벽에 기대어 고정하고 가능한 가장 긴 Night mode 옵션을 선택한다.
- 촬영 중 십자선이 뜨면 두 십자선을 맞춰 흔들림을 줄인다.
- 사람이 움직이는 장면은 긴 노출이 번짐을 만들 수 있으므로 노출 시간을 줄이거나 Live/Burst/영상 캡처를 고려한다.

**추천 시작값 / 조작값**
- Night mode: Auto → 정적 장면은 가능한 긴 옵션/Max
- 타이머: 3초
- 노출: 네온/간판은 -0.3~-1.0 시작
- 포맷: 보정 여지가 필요하면 ProRAW 지원 모델에서 ProRAW 선택

**보정 루틴**
- Highlights -20~-60로 네온/간판 복구
- Shadows +10~+35까지만 올려 노이즈 억제
- Noise Reduction은 디테일이 죽지 않게 약하게 시작

**주의할 점**
- 손에 들고 Max 장노출을 고집하지 않는다.
- 밤하늘/야경을 무조건 밝게 만들지 말고 어두운 분위기를 남긴다.

**확실성:** Apple 공식 절차 + 보정값은 실전 시작점.
**근거:** Apple Support는 Night mode 자동 활성화, 노출 옵션, 삼각대, 십자선 정렬을 설명한다.

### Tip 2. 무엇을 찍어도 사진이 산만하고 초점/밝기가 흔들릴 때

**촬영/작업 순서**
- 렌즈를 먼저 닦고, 카메라 설정에서 격자(Grid)와 수평(Level)을 켠다.
- 주 피사체를 화면 교차점 또는 중앙보다 약간 옆에 둔다.
- 피사체를 탭해서 초점과 노출 기준을 정하고, iPhone은 길게 눌러 AE/AF Lock을 건다.
- 하이라이트가 날아가면 화면 노출 슬라이더를 살짝 내려 밝은 부분 디테일을 살린다.

**추천 시작값 / 조작값**
- EV/노출 보정: 밝은 하늘·흰 벽·네온이 있으면 -0.3~-1.0부터 테스트
- 타이머: 삼각대/거치 시 2~3초
- 줌: 가능하면 0.5x/1x/2x/3x/5x 같은 광학 배율만 사용

**보정 루틴**
- 수평/크롭을 먼저 맞춘 뒤 노출·색을 조정한다.
- 밝은 영역 복구가 필요하면 Highlights를 낮추고 Shadows는 과하게 올리지 않는다.

**주의할 점**
- 디지털 줌으로 먼저 당기지 말고, 고해상도 촬영 후 크롭한다.
- 초점 확인 없이 연속 촬영하지 않는다.

**확실성:** source-supported 일반 원칙 + 실전 시작점.
**근거:** Apple의 AE/AF/Night mode 흐름, Samsung Pro mode, TIME/PetaPixel/Digital Camera World류의 기본 팁을 통합.

### Tip 3. 후보정을 크게 할 사진을 찍을 때 — 노을, 야경, 실내, 공연, 역광

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

## 추가 검증 촬영 레시피 — iPhone

### iPhone으로 달 찍기: AE/AF Lock + 노출 낮추기

**상황**
- 달이 작고 하얗게 날아가서 표면이 보이지 않을 때.

**촬영/작업 순서**
- 망원 렌즈가 있으면 2x 이상으로 전환한다.
- 달을 길게 눌러 AE/AF Lock을 건다.
- 노출 슬라이더를 아래로 내려 달 표면이 회색으로 보일 때 촬영한다.
- 가능하면 고정하고 여러 장 찍어 가장 선명한 컷을 고른다.

**주의점**
- iPhone은 달 전용 슈퍼줌 장비가 아니므로 Galaxy Ultra류만큼 큰 달을 기대하지 않는다.

### iPhone Night mode Portrait

**상황**
- 밤에 인물을 배경 흐림과 함께 찍고 싶을 때.

**촬영/작업 순서**
- 지원 기기에서 Portrait mode로 전환한다.
- Night mode가 자동으로 켜지는지 확인한다.
- 피사체에게 몇 초간 멈추라고 안내하고, 폰을 고정한다.

**주의점**
- Night mode에서는 Live Photos/flash가 꺼질 수 있다.
- 저조도 Portrait는 지원 기기와 렌즈 조건 제한이 있다.

### iPhone Macro: 2cm 접근과 Macro Control

**상황**
- 꽃, 음식, 작은 물건을 아주 가까이 찍을 때.

**촬영/작업 순서**
- 피사체에 최대 2cm까지 접근하면 ultrawide macro로 자동 전환될 수 있다.
- 흐리면 한 발 물러나거나 0.5x 전환 상태를 확인한다.
- 원치 않는 자동 전환이 반복되면 Macro Control을 켜서 직접 제어한다.

## 이 소스에서 더 캐야 할 것

- 공식 기능 설명은 기능명 기준으로, 매거진 조언은 상황별 행동 기준으로 재분류
- 기기별(iPhone/Galaxy/Pixel)로 가능한 조작과 불가능한 조작을 분리
- 숫자 설정이 있는 팁은 출처 URL과 함께 별도 표로 모으기

## 모드별 공식 검증값 추가

### Samsung Food mode 세부 조작

**공식 경로**
- Camera → MORE → FOOD.

**촬영 절차**
- 음식이 highlighted area 안에 들어오도록 프레임을 잡는다.
- Thermometer 아이콘으로 색온도/색감을 조정한다.
- Blur effect로 음식 주변이나 배경을 흐린다.

**실전 팁**
- 흰 접시가 노랗게 뜨면 Thermometer를 차갑게 조정한다.
- 여러 접시가 있으면 Blur effect를 약하게 하거나 일반 Photo도 같이 찍는다.

### Samsung Night mode 세부 원리

**공식 경로**
- Camera → More → Night → Capture.

**공식 확인 포인트**
- Samsung Night Mode는 AI multi-frame processing으로 여러 이미지를 합성한다.
- Samsung night-mode guide는 30 images를 하나로 결합하는 설명을 제공한다.
- 안정적인 자세 또는 삼각대가 결과를 크게 좌우한다.

**실전 팁**
- 손持ち: 짧은 Night mode, 사람은 멈추게 하기.
- 삼각대/고정: 더 긴 Night mode 또는 Pro mode 장노출.
- 달/네온처럼 매우 밝은 피사체는 Night mode보다 수동 노출이 유리할 수 있다.

### Samsung Pro mode / Expert RAW 범위

**공식 확인 조작**
- ISO, shutter speed, exposure, color tone, manual focus, white balance.

**공식 예시 범위**
- ISO 50–800.
- Shutter 1/24000–10s.
- White balance 2300K–10000K.
- Manual focus: 가까운 거리부터 far away.

**Expert RAW 예시**
- 별도 다운로드 앱/기능.
- 더 세밀한 제어와 RAW 기반 편집.
- Samsung S25 자료 예시: ISO 800, 1/125s, AF-C, highlights/shadows/white balance/denoise 편집.

### iPhone Camera Control / Exposure / Depth

**공식 확인 조작**
- Camera Control에서 Exposure와 Depth 조정 가능.
- 초점/노출 잠금 기능을 활용할 수 있다.

**실전 팁**
- 인물: Depth를 너무 낮은 f값처럼 과하게 주지 말고 머리카락/안경 경계를 확인한다.
- 달/네온: 노출을 낮춰 하이라이트를 먼저 살린다.

### Pixel Night Sight 공식 조작

**공식 경로/조작**
- Photo mode에서 Night Sight 사용.
- 저조도에서는 자동으로 동작할 수 있다.
- slider를 Max → Off 범위로 조정할 수 있다.
- More light = None으로 Night Sight를 끌 수 있다.

**실전 팁**
- 음식/인물은 Max보다 짧게, 정적인 풍경은 더 길게.
- 움직이는 사람에게는 몇 초간 정지를 요청한다.

### Pixel Pro controls / Macro / 50MP

**공식 확인 기능**
- Macro Focus.
- Pro controls.
- High-Res up to 50MP on supported devices.

**실전 팁**
- 음식 질감: Macro Focus 또는 2x/Portrait 비교.
- 여행 디테일: 50MP/High-Res는 큰 크롭이 필요한 장면에만.
- WB가 틀어지는 실내 음식은 Pro controls로 white balance를 먼저 확인.

## 출처

- https://www.adobe.com/express/learn/blog/how-to-take-better-pictures-with-your-iphone
- https://support.google.com/pixelphone/answer/7158570?hl=en-Get
- https://support.google.com/pixelcamera/answer/9708795?hl=en
- https://support.apple.com/guide/iphone/use-the-camera-control-iph0c397b154/ios
- https://www.samsung.com/us/smartphones/galaxy-s25-ultra/app/
- https://www.samsung.com/us/mobile/galaxy/camera-features/
- https://www.samsung.com/ae/support/mobile-devices/how-to-use-the-cameras-pro-mode-on-samsung-galaxy-phones/
- https://www.samsung.com/ae/mobile-phone-buying-guide/samsung-night-mode-camera/
- https://support.apple.com/fr-cm/guide/iphone/iphfaacf2eb0/ios
- https://support.apple.com/en-lamr/102519
- https://support.apple.com/guide/iphone/take-portraits-iphd7d3a91a2/ios
- https://iphonephotographyschool.com/night-sky/
- https://support.apple.com/en-lamr/guide/iphone/iph1a3c5b4c3/ios

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
