---
title: "Bilingual scenario matching lexicon — Korean/English scene query aliases"
category: "recommendation"
updated_at: "2026-04-18"
content_type: "scenario_matching_lexicon"
---

# Bilingual scenario matching lexicon — Korean/English scene query aliases

## 목적

사용자 질문은 한국어/영어가 섞여 들어올 수 있다. 이 문서는 장면 질의를 아래 흐름으로 안정적으로 매칭하기 위한 사전이다.

```text
[원문 질의]
→ [언어 감지 + 토큰 정규화]
→ [WHEN/WHO/WHERE/WHAT/HOW 슬롯 추출]
→ [Scenario Top-K]
→ [trend/general/personalized 추천 채널]
```

## 매칭 원칙 (최적화 버전)

1. **언어 비의존 매칭**: Korean, English, code-mixed(예: "야간 portrait 2x")를 같은 canonical token으로 정규화.
2. **5W1H 슬롯 우선**: `언제/누가/어디서/무엇을/어떻게` 슬롯이 많이 채워진 후보를 상위 랭크.
3. **이슈는 보정자 역할**: issue(`underexposed_face`, `motion_blur`)는 scenario를 덮어쓰지 않고 score 보정으로 반영.
4. **안전 fallback**: Top-1 점수가 낮으면 Top-3 scenario를 유지하고 general recommendation을 먼저 출력.

## Alias table (KR/EN 통합)

| User phrase examples | Scenario | Slot coverage | Issues / facets |
|---|---|---|---|
| 카페 창가 인물, 얼굴 한쪽 어두움, 배경 지저분 / cafe window portrait face dark cluttered background | `window_light_cafe_portrait` | when:daytime, where:cafe_window, what:portrait, how:1x/2x | `underexposed_face`, `busy_background`, `diffused_window` |
| 비 오는 밤 커플, 네온 반사 / rainy neon couple portrait at night | `rain_neon_street_portrait` | when:night_rain, where:street, what:couple_portrait, how:2x | `underexposed_face`, `blown_neon`, `color_cast` |
| 어두운 식당 파스타 노랗다 흐릿 / dim restaurant pasta yellow blur | `dim_restaurant_food` | when:night_indoor, where:restaurant, what:food, how:1x + WB | `mixed_white_balance`, `motion_blur`, `low_light_noise` |
| 디저트 플랫레이 삐뚤 / dessert flat lay tilted table | `cafe_flatlay_dessert` | when:day/indoor, where:cafe_table, what:dessert, how:1x top-down | `tilted_horizon`, `edge_distortion` |
| 한낮 해변 인물 얼굴 그림자 / noon beach portrait harsh shadow | `harsh_noon_beach_portrait` | when:noon, where:beach, what:portrait, how:2x + EV- | `harsh_shadow`, `blown_highlights` |
| 골목 OOTD 다리 짧아보임 / alley OOTD proportions look short | `fashion_ootd_portrait` | when:day/evening, where:street, what:ootd, how:1x/2x + angle | `body_distortion`, `busy_background` |
| 콘서트 무대 얼굴 뭉개짐 / concert stage subject too far | `concert_stage_low_light` | when:night, where:stage, what:performer, how:3x/5x | `highlight_clipping`, `digital_zoom_softness`, `noise` |
| 눈 오는 날 인물 칙칙 / snowy portrait looks gray | `snow_portrait_clean_winter` | when:winter_day, where:outdoor_snow, what:portrait, how:1x/2x | `underexposed_snow`, `blue_cast`, `dull_skin` |
| 강아지 뛰는 사진 흔들림 / dog running photo blurry | `pets_children_action` | when:any, where:outdoor/indoor, what:pets_kids, how:fast shutter | `motion_blur`, `focus_miss` |
| 유리창 야경 반사 지저분 / city window reflection messy | `city_window_reflection` | when:night, where:window_city, what:city_lights, how:1x/2x EV- | `messy_reflection`, `blown_city_lights` |
| 미술관 작품 앞 인물 / museum portrait no flash | `museum_gallery_portrait` | when:indoor, where:museum, what:portrait, how:no_flash + WB | `mixed_light`, `busy_background` |
| 실내 생일파티 단체 / indoor birthday group candle | `indoor_party_group` | when:night/indoor, where:party_room, what:group, how:1x wide | `low_light_group`, `motion_blur`, `warm_cast` |
| 관광지 랜드마크 사람 많음 / crowded landmark portrait | `crowded_landmark_portrait` | when:any, where:landmark, what:travel_portrait, how:2x + cleanup | `busy_background`, `scale_story` |
| 제품 판매 사진 / product listing photo for marketplace | `small_product_listing_photo` | when:any, where:home/studio, what:product, how:1x + clean bg | `background_cleanup`, `color_accuracy`, `texture_detail` |
| 거울 OOTD 셀카 왜곡 / mirror selfie OOTD distortion | `mirror_selfie_ootd` | when:any, where:elevator/mirror, what:ootd_selfie, how:1x | `mirror_distortion`, `dirty_mirror`, `body_alignment` |
| 라떼아트 케이크 접사 / latte art cake close-up | `cafe_drink_dessert_closeup` | when:indoor, where:cafe, what:drink_dessert, how:macro/1x | `macro_focus`, `texture_detail` |

## Query normalization dictionary (KR + EN)

```yaml
synonyms:
  when:
    day: ["낮", "day", "daytime", "afternoon"]
    night: ["밤", "야간", "night", "low light", "after dark"]
    morning: ["아침", "새벽", "morning", "sunrise"]

  who_device:
    iphone: ["아이폰", "iphone", "ios"]
    galaxy: ["갤럭시", "삼성폰", "samsung", "galaxy"]
    pixel: ["픽셀", "google pixel", "pixel"]
    xiaomi: ["샤오미", "xiaomi", "redmi"]
    lightroom: ["라이트룸", "lightroom", "lr"]
    photoshop: ["포토샵", "photoshop", "ps"]

  where:
    indoor: ["실내", "inside", "indoor"]
    outdoor: ["야외", "outdoor"]
    cafe: ["카페", "cafe", "coffee shop"]
    street: ["거리", "가로수길", "street", "alley"]
    beach: ["해변", "바다", "beach"]
    museum: ["미술관", "전시", "museum", "gallery"]

  what:
    instagram_post: ["인스타 업로드", "instagram upload", "ig post"]
    trendy_style: ["요즘 유행", "trendy", "viral style"]
    star_photo: ["별", "은하수", "star", "milky way", "astro"]
    portrait: ["인물", "portrait", "profile", "selfie"]
    food: ["음식", "디저트", "food", "dessert", "latte"]

  how:
    zoom_2x: ["2배", "2x", "2x zoom", "tele 2x"]
    pro_mode: ["프로모드", "pro mode", "manual mode"]
    iso_600: ["iso 600", "ISO600", "아이소 600"]
    ev_minus: ["ev -", "exposure down", "밝기 낮춤"]

  issues:
    face_dark: ["얼굴 어두움", "face dark", "underexposed face"]
    blown_highlight: ["하늘 날아감", "highlight blown", "overexposed sky"]
    busy_background: ["배경 지저분", "cluttered background", "crowded background"]
    tilted: ["삐뚤", "tilted", "horizon off", "crooked"]
    motion_blur: ["흔들림", "blur", "motion blur"]
```

## 점수 계산 힌트

```text
score =
  0.35 * slot_coverage(when/who/where/what/how)
+ 0.25 * alias_exact_or_fuzzy
+ 0.20 * issue_alignment
+ 0.10 * language_match_confidence
+ 0.10 * scenario_popularity_prior
```

- 동점 시 `where + what + how`가 모두 있는 후보를 우선.
- `who_device`가 명시되면 해당 device-friendly scenario/technique를 가중.

## 다음 개선

- 한국어 형태소 분석기 + 영어 lemmatization을 동시에 적용한 offline 정규화 파이프라인 추가.
- 한 질문이 다중 시나리오일 경우 `multi-intent split`(예: "비 오는 밤 + 커플 + 인스타 업로드")로 recommendation bundle 생성.
