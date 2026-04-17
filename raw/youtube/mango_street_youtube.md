---
title: "Mango Street"
category: "youtube"
priority: "A"
updated_at: "2026-04-17"
content_type: "actionable_tip_cards"
urls:
  - "https://www.youtube.com/@MangoStreet"
  - "https://www.youtube.com/watch?v=HjVUe98mG8E"
  - "https://www.youtube.com/watch?v=6TzYOXl7tBc"
  - "https://socialblade.com/youtube/c/mangostreet/similarrank/subscribers"
practical_tags:
  - "RAW"
  - "DNG"
  - "인물"
  - "Lightroom"
  - "아이폰사진"
  - "라이트룸모바일"
  - "색보정"
  - "SNS사진"
  - "유튜브"
---

# Mango Street — 상황별 촬영/보정 팁

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

## 출처에서 확인된 구체 레시피

### Mango Street — iPhone로 3분 미만 숏필름 만들기

**상황**
- 스마트폰만으로 영화 같은 짧은 영상 프로젝트를 만들고 싶을 때.

**촬영/작업 순서**
- 먼저 서스펜스 같은 강한 장르/톤을 정한다.
- 전체 러닝타임을 3분 미만으로 제한한다.
- 모바일 폰만으로 전편 촬영한다.
- 최소 한 컷은 Moment 렌즈를 사용한다.
- 장소/세팅을 준비해 짧고 집중적으로 촬영한다.
- 편집에서 텐션과 이야기 흐름을 빠르게 정리한다.

**확인된 수치/조건**
- 3분 미만.
- Moment 렌즈 최소 1컷.
- 실제 촬영 시간 예시: 7시간.

**주의점**
- 이 자료는 노출/셔터 튜토리얼보다 제작 과정/BTS 참고용이다.

## 이 소스에서 더 캐야 할 것

- 대표 영상의 챕터별 팁을 1카드 1상황으로 분해
- 영상 속 화면에 보이는 슬라이더/카메라 설정은 숫자로 기록
- Before/After가 있는 장면은 보정 순서를 따로 추출

## 출처

- https://www.mangostreetlab.com/blog/shotoniphone
- https://www.youtube.com/@MangoStreet
- https://www.youtube.com/watch?v=HjVUe98mG8E
- https://www.youtube.com/watch?v=6TzYOXl7tBc
- https://socialblade.com/youtube/c/mangostreet/similarrank/subscribers

> 원문 전문은 복사하지 않고, 실전 팁·출처 링크·출처 기반/실전 시작값 구분만 저장한다.
