---
title: "서점·도서관 독서 인물 - 조용한 북스타그램 무드"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-25"
scenario_tags:
  - "bookstore"
  - "library"
  - "reading"
  - "portrait"
  - "bookstagram"
  - "available-light"
aliases:
  - "book cafe"
  - "quiet portrait with shelves"
  - "shelves in the background"
  - "warm indoor lights"
  - "서점 독서 사진"
  - "도서관 인물 사진"
  - "책 읽는 프로필"
  - "북스타그램 인물"
  - "bookstore reading portrait"
  - "library book portrait"
  - "book cafe portrait"
  - "shelves background portrait"
  - "warm indoor book cafe photo"
query_aliases:
  - "서점 책장 앞에서 조용하고 감성적인 독서 인물 사진을 찍고 싶다"
  - "도서관에서 플래시 없이 책 읽는 모습을 자연스럽게 찍고 싶다"
  - "cozy bookstore or library reading portrait with bookstagram mood"
  - "book cafe quiet portrait with shelves in the background and warm indoor light"
graph_nodes:
  - "subject:person_with_book"
  - "object:book"
  - "environment:bookstore_or_library"
  - "light:warm_available_shelf_light"
  - "scenario:bookstore_library_reading_portrait"
  - "trend_signal:bookstagram_cozy_reading"
  - "trend_signal:quiet_lifestyle_portrait"
  - "preference:cozy_intellectual_mood"
  - "preference:quiet_low_retouch"
  - "edit_style:warm_clean_bookish_portrait"
  - "style_recipe:available_light_bookish_warmth"
  - "recommendation_variant:cozy_reading_shelf_portrait"
  - "technique:available_light_no_flash"
  - "technique:book_shelf_depth_layering"
  - "technique:quiet_candid_reading_pose"
  - "parameter:warm_neutral_white_balance"
  - "parameter:background_saturation_minus_5_to_20"
  - "parameter:subject_exposure_plus_0_1_to_0_3"
  - "image_issue:mixed_white_balance"
  - "image_issue:busy_shelves"
  - "risk:privacy_or_policy_violation"
  - "outcome:calm_bookish_identity_portrait"
  - "evidence:nlm_reading_room_policy"
  - "evidence:loc_library_photography_rules"
  - "evidence:apple_night_mode"
  - "evidence:adobe_portrait_photography"
  - "evidence:lightroom_masking_color"
graph_edges:
  - "trend_signal:bookstagram_cozy_reading SUPPORTS edit_style:warm_clean_bookish_portrait"
  - "trend_signal:quiet_lifestyle_portrait SUPPORTS recommendation_variant:cozy_reading_shelf_portrait"
  - "preference:cozy_intellectual_mood ADAPTS_TO style_recipe:available_light_bookish_warmth"
  - "preference:quiet_low_retouch CONSTRAINS subject_exposure_plus_0_1_to_0_3"
  - "edit_style:warm_clean_bookish_portrait APPLIES_TO scenario:bookstore_library_reading_portrait"
  - "scenario:bookstore_library_reading_portrait HAS_VARIANT recommendation_variant:cozy_reading_shelf_portrait"
  - "recommendation_variant:cozy_reading_shelf_portrait USES technique:available_light_no_flash"
  - "recommendation_variant:cozy_reading_shelf_portrait USES technique:book_shelf_depth_layering"
  - "recommendation_variant:cozy_reading_shelf_portrait SETS parameter:warm_neutral_white_balance"
  - "image_issue:mixed_white_balance ADJUSTS parameter:warm_neutral_white_balance"
  - "image_issue:busy_shelves CONSTRAINS technique:book_shelf_depth_layering"
  - "risk:privacy_or_policy_violation CONSTRAINS technique:quiet_candid_reading_pose"
  - "recommendation_variant:cozy_reading_shelf_portrait SUPPORTED_BY evidence:nlm_reading_room_policy"
  - "recommendation_variant:cozy_reading_shelf_portrait SUPPORTED_BY evidence:loc_library_photography_rules"
  - "recommendation_variant:cozy_reading_shelf_portrait SUPPORTED_BY evidence:apple_night_mode"
  - "recommendation_variant:cozy_reading_shelf_portrait SUPPORTED_BY evidence:adobe_portrait_photography"
  - "recommendation_variant:cozy_reading_shelf_portrait SUPPORTED_BY evidence:lightroom_masking_color"
urls:
  - "https://www.nlm.nih.gov/readingroom/rrphoto.html"
  - "https://www.loc.gov/visit/rules-of-behavior/"
  - "https://support.apple.com/guide/iphone/take-night-mode-photos-iph1a3c5b4c3/ios"
  - "https://www.adobe.com/creativecloud/photography/type/portrait-photography.html"
  - "https://helpx.adobe.com/ph_fil/lightroom-cc/using/masking-mobile-ios.html"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
---

# 서점·도서관 독서 인물 - 조용한 북스타그램 무드

## 추천 시스템용 요약

- **트렌드 추천:** Bookstagram식 cozy reading, 책장 깊이감, 자연광/따뜻한 실내광, 조용한 라이프스타일 portrait.
- **일반 추천:** 플래시 없이 사용 가능한 빛을 쓰고, 책·얼굴·책장 중 무엇을 주인공으로 할지 먼저 정한다.
- **개인화 추천 변수:** 따뜻한 감성 취향은 amber shelf tone, clean 취향은 흰 종이와 피부색을 자연스럽게, dark academia 취향은 그림자와 갈색 계열을 조금 남긴다.

## 촬영 레시피

- 도서관/서점의 촬영 규칙을 먼저 확인하고, 다른 이용자 얼굴이 들어가지 않는 각도를 고른다.
- 창가, 독서등, 밝은 책장 끝처럼 얼굴 한쪽에 부드러운 빛이 닿는 위치를 찾고 flash는 끈다.
- 공간이 허락하면 2x portrait, 좁은 통로에서는 1x로 찍되 얼굴을 프레임 가장자리에 붙이지 않는다.
- 책은 얼굴을 가리지 않게 가슴 높이에서 30~45도 기울이고, 표지는 노출할지 익명적인 독서 무드로 갈지 선택한다.
- 책장 선이 기울면 산만하므로 촬영 때 수직선을 맞추고, 배경 책 제목이 너무 복잡하면 한 걸음 옆으로 이동한다.

## 보정 레시피

- WB를 먼저 맞춰 종이가 과하게 노랗거나 초록빛으로 뜨지 않게 한다.
- Subject mask: Exposure +0.1~+0.3, Shadows +5~+15, Texture -5~0.
- Background/shelf mask: Saturation -5~-20, Clarity -5~0으로 책장 혼잡도를 낮춘다.
- 따뜻한 variant는 Temp를 약간 올리되 Orange Saturation은 +10 이상 과하게 올리지 않는다.
- Geometry/rotate로 책장과 테이블 수직·수평을 정리하고, 4:5 피드용과 9:16 스토리용을 따로 크롭한다.

## 실패 방지 / 주의점

- 공공 도서관과 열람실에서는 handheld, available light, no flash가 기본인 경우가 많으며, formal portrait는 허가가 필요할 수 있다.
- 다른 이용자, 직원, 열람 자료, 대출 정보가 식별되면 privacy risk가 생긴다.
- 책장 배경이 너무 선명하면 얼굴보다 제목이 먼저 읽히므로 배경 blur나 saturation 감소로 우선순위를 조절한다.
- 조용한 장소에서는 촬영 지시를 길게 하지 말고, 짧은 포즈 2~3개만 빠르게 확보한다.

## 근거

### 반영한 외부 근거

- NLM Reading Room 정책은 다른 이용자를 방해하지 않고 handheld camera, available light, no flash 조건을 명시한다.
- Library of Congress 촬영 규칙은 일반 방문 중 spontaneous informal photo와 formal/posed session을 구분하고, staged portrait에는 별도 절차가 필요하다고 설명한다.
- Apple Night mode 문서는 저조도에서 자동으로 밝기와 디테일을 확보하되 촬영 중 폰을 안정적으로 유지해야 한다고 안내한다.
- Adobe portrait photography는 눈 초점, 빛의 성격, 배경 분리, 긴 focal length의 인물 친화성을 강조한다.
- Lightroom masking/color 문서는 subject/background를 나눠 조정하고 Color Mix로 특정 색을 다듬는 근거를 제공한다.

### 시나리오 수정 포인트

- 이 시나리오는 `museum_gallery_portrait`와 비슷한 no-flash 실내 규칙을 공유하지만, 핵심은 작품 감상보다 bookish identity와 독서 취향 personalization이다.
- `mixed_white_balance`, `busy_shelves`, `privacy_or_policy_violation`은 추천을 막는 중심축이 아니라 조용한 북스타그램 스타일을 안전하게 조정하는 guardrail이다.

## Graphify 추출 힌트

```yaml
entities:
  - trend_signal:bookstagram_cozy_reading
  - preference:cozy_intellectual_mood
  - edit_style:warm_clean_bookish_portrait
  - recommendation_variant:cozy_reading_shelf_portrait
  - technique:available_light_no_flash
  - image_issue:mixed_white_balance
relationships:
  - bookstagram_cozy_reading SUPPORTS warm_clean_bookish_portrait
  - cozy_intellectual_mood ADAPTS_TO available_light_bookish_warmth
  - privacy_or_policy_violation CONSTRAINS quiet_candid_reading_pose
recommendation_modes: [trend, general, personalized]
```

## 출처

- https://www.nlm.nih.gov/readingroom/rrphoto.html
- https://www.loc.gov/visit/rules-of-behavior/
- https://support.apple.com/guide/iphone/take-night-mode-photos-iph1a3c5b4c3/ios
- https://www.adobe.com/creativecloud/photography/type/portrait-photography.html
- https://helpx.adobe.com/ph_fil/lightroom-cc/using/masking-mobile-ios.html
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
