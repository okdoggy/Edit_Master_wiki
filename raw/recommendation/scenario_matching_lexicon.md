---
title: "Korean scenario matching lexicon — scene query aliases"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "scenario_matching_lexicon"
---

# Korean scenario matching lexicon — scene query aliases

## 목적

사용자는 `rain_neon_street_portrait` 같은 내부 이름을 말하지 않는다. “비 오는 밤 커플”, “카페에서 얼굴이 어둡다”, “디저트 플랫레이가 삐뚤다”처럼 말한다. 이 파일은 한국어 자연어 질문을 scenario로 매칭하기 위한 alias 사전이다.

## 매칭 원칙

1. **피사체 + 환경 + 문제점**을 우선한다.
   - 예: `친구 + 카페 창가 + 얼굴 어두움` → `window_light_cafe_portrait`
2. **문제점이 명확하면 issue를 같이 붙인다.**
   - `얼굴이 어둡다` → `underexposed_face`
   - `하늘이 날아감` → `blown_highlights`
   - `삐뚤다` → `tilted_horizon`
3. **장면이 애매하면 더 일반 scenario로 보내고, 답변에서 추가 질문하지 말고 안전한 추천을 준다.**
4. **한국어/영어/구어체/오타를 모두 alias로 둔다.**

## Alias table

| User phrase examples | Scenario | Issues / facets |
|---|---|---|
| 카페 창가, 친구 프로필, 얼굴 한쪽 어두움, 뒤 테이블 지저분 | `window_light_cafe_portrait` | `underexposed_face`, `busy_background`, `diffused_window` |
| 비 오는 밤, 네온, 커플, 얼굴 어둠, 간판만 튐 | `rain_neon_street_portrait` | `underexposed_face`, `blown_neon`, `color_cast` |
| 어두운 식당, 파스타, 노랗다, 흐릿하다, 플래시 없이 | `dim_restaurant_food` | `mixed_white_balance`, `low_light_noise`, `motion_blur` |
| 디저트 플랫레이, 커피, 위에서, 테이블 삐뚤다, 접시 왜곡 | `cafe_flatlay_dessert` | `tilted_table`, `edge_distortion`, `white_balance` |
| 한낮 해변, 얼굴 그림자, 하늘 날아감 | `harsh_noon_beach_portrait` | `harsh_shadow`, `blown_highlights` |
| 골목 OOTD, 다리 짧아 보임, 배경이 튐 | `fashion_ootd_portrait` | `body_distortion`, `busy_background`, `outfit_color_priority` |
| 콘서트, 무대, 가수 멀다, 조명 날아감, 얼굴 뭉개짐 | `concert_stage_low_light` | `highlight_clipping`, `digital_zoom_softness`, `noise` |
| 눈 오는 날, 가족, 눈이 회색, 얼굴 칙칙 | `snow_portrait_clean_winter` | `underexposed_snow`, `dull_skin`, `blue_cast` |
| 강아지 뛰어옴, 아이 뛰어노는 사진, 흔들림 | `pets_children_action` | `motion_blur`, `focus_miss` |
| 도시 야경, 유리창 반사, 산만함 | `city_window_reflection` | `messy_reflection`, `blown_city_lights`, `busy_composition` |
| 전시회, 미술관, 작품 앞 인물, 플래시 금지 | `museum_gallery_portrait` | `mixed_light`, `no_flash`, `busy_background` |
| 실내 생일파티, 단체, 케이크 촛불, 어둡다 | `indoor_party_group` | `low_light_group`, `motion_blur`, `warm_cast` |
| 랜드마크 앞 사람, 관광객 많음, 배경 지저분 | `crowded_landmark_portrait` | `busy_background`, `scale_story`, `remove_distractions` |
| 집에서 제품 판매 사진, 쇼핑몰 썸네일, 배경 지저분 | `small_product_listing_photo` | `background_cleanup`, `color_accuracy`, `texture_detail` |
| 엘리베이터/거울 셀카, OOTD, 얼굴/몸 왜곡 | `mirror_selfie_ootd` | `mirror_distortion`, `body_alignment`, `dirty_mirror` |
| 카페 라떼아트, 케이크, 접사, 크림 질감 | `cafe_drink_dessert_closeup` | `macro_focus`, `texture_detail`, `window_light` |

## Query normalization hints

```yaml
synonyms:
  face_dark: ["얼굴 어두움", "얼굴이 어둡", "얼굴 죽음", "칙칙", "그림자"]
  blown_highlight: ["하늘 날아감", "하이라이트 날림", "너무 하얗", "네온만 튐"]
  busy_background: ["배경 지저분", "뒤가 산만", "사람 많", "테이블 지저분"]
  tilted: ["삐뚤", "기울", "수평 안 맞", "테이블이 틀어짐"]
  food: ["파스타", "디저트", "커피", "케이크", "음식", "라떼", "브런치"]
  portrait: ["인물", "프로필", "친구", "커플", "여성", "남자", "셀카"]
  night: ["밤", "야간", "어두운", "저조도", "네온", "콘서트"]
```

## 다음 개선

- 한국어 형태소/임베딩 검색으로 alias table을 보완한다.
- 한 질문이 여러 scenario에 걸치면 top-3 후보를 보여주고, 가장 안전한 general recommendation을 기본 답변으로 사용한다.
