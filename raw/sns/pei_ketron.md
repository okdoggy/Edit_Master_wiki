---
title: "Pei Ketron"
category: "sns"
priority: "A"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://santafeworkshops.com/workshop-categories/digital-printing/"
  - "https://santafeworkshops.com/workshop/pei-ketron/"
  - "https://www.instagram.com/pketron/"
practical_tags:
  - "RAW"
  - "DNG"
  - "인물"
  - "Lightroom"
  - "아이폰사진"
  - "라이트룸모바일"
  - "촬영후보정"
  - "프린트"
  - "워크플로우"
---

# Pei Ketron — 상황별 촬영/보정 팁

이 파일은 더 이상 단순 소스 메타데이터가 아니라, 실제 촬영/보정 때 바로 써먹는 레시피 형태로 정리한다.

**이 소스를 읽는 관점:** 촬영에서 Lightroom Mobile, 출력/작품화까지 이어지는 capture-to-edit 흐름으로 읽는다.

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

### Tip 2. 인물·제품은 살리고 배경은 정리하고 싶을 때

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

### Tip 3. 여행지·풍경·건축물을 스마트폰으로 고급스럽게 찍을 때

**촬영/작업 순서**
- 일출 직후/일몰 전후의 낮은 빛을 우선 노린다.
- 수평/수직선을 맞추고, 건물은 한 걸음 뒤로 물러나 1x/2x로 왜곡을 줄인다.
- 하늘이 밝으면 노출을 하늘 기준으로 낮추고, 전경은 후보정에서 살린다.
- 와이드 한 장, 망원 디테일 한 장, 사람/스케일 한 장을 세트로 찍는다.

**추천 시작값 / 조작값**
- Grid/Level: 켜기
- EV: 하늘 포함 시 -0.3~-1.0
- Lens: 0.5x는 공간감, 2x/5x는 레이어 압축
- Format: 큰 보정 예정이면 RAW/ProRAW/DNG

**보정 루틴**
- Geometry/Upright로 수직 보정
- Sky mask로 하늘만 Highlights/Dehaze 조정
- Color Mix에서 Blue/Orange를 분리해 하늘과 건물을 다듬는다.

**주의할 점**
- 초광각으로 건물을 가까이 찍으면 기울어짐이 심하다.
- HDR 느낌이 과하면 입체감이 사라진다.

**확실성:** Austin Mann/매거진형 여행·풍경 원칙 + Lightroom 공식 기능.
**근거:** Austin Mann식 현장 테스트 관점, National Geographic/Digital Camera World/PetaPixel 풍경 조언 통합.

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

## 이 소스에서 더 캐야 할 것

- 대표 게시물/Reels 5개를 골라 “상황-설정-보정” 형식으로 추가
- BTS가 있는 게시물은 카메라 위치와 소품 거리를 기록
- 수치 설정이 없는 경우 “실전 시작값”과 “출처 직접값”을 분리

## 출처

- https://santafeworkshops.com/workshop-categories/digital-printing/
- https://santafeworkshops.com/workshop/pei-ketron/
- https://www.instagram.com/pketron/

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
