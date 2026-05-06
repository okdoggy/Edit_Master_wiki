---
title: "의류 리세일 디테일 사진: 원단·택·하자 신뢰 기록"
category: "scenarios"
content_type: "graphify_ready_actionable_recipe"
updated_at: "2026-04-25"
scenario_tags:
  - "clothing"
  - "resale"
  - "marketplace"
  - "detail-photo"
  - "texture"
  - "color-accuracy"
  - "condition"
aliases:
  - "의류 중고거래 디테일 사진"
  - "옷 하자 사진"
  - "원단 질감 사진"
  - "브랜드 택 사이즈 택 사진"
  - "clothing resale detail photo"
query_aliases:
  - "중고 옷 팔 때 하자 사진 어떻게 찍어"
  - "옷 색이 실제랑 다르게 나와"
  - "빈티지 의류 원단 질감 보여주는 사진"
  - "리세일 의류 택과 소재 사진"
graph_nodes:
  - "scenario:clothing_resale_detail_photo"
  - "subject:used_clothing"
  - "subject:fabric_texture"
  - "subject:brand_size_care_tag"
  - "subject:condition_flaw"
  - "environment:home_window_flatlay"
  - "platform:vinted"
  - "platform:poshmark"
  - "platform:ebay"
  - "trend_signal:trust_first_resale_listing"
  - "trend_signal:secondhand_authenticity_detail"
  - "preference:accurate_color"
  - "preference:minimal_clean_marketplace"
  - "preference:editorial_but_honest"
  - "edit_style:true_to_item_resale"
  - "edit_style:clean_marketplace_detail"
  - "style_recipe:window_light_fabric_condition_detail"
  - "recommendation_variant:trust_first_condition"
  - "recommendation_variant:clean_marketplace_thumbnail"
  - "recommendation_variant:personalized_editorial_resale"
  - "technique:detail_sequence_front_back_tag_flaw"
  - "technique:white_balance_reference"
  - "technique:macro_fabric_stitch_closeup"
  - "technique:background_cleanup_without_item_change"
  - "parameter:front_back_tag_flaw_sequence"
  - "parameter:window_light_same_session"
  - "parameter:exposure_plus_0_05_to_0_25"
  - "parameter:texture_plus_8_to_20"
  - "parameter:vibrance_minus_5_to_plus_5"
  - "issue:color_inaccuracy"
  - "issue:hidden_flaw"
  - "issue:wrinkled_fabric"
  - "issue:personal_info_visible"
  - "issue:overedited_color"
  - "issue:busy_background"
graph_edges:
  - "TrendSignal:trust_first_resale_listing + Preference:accurate_color SELECTS EditStyle:true_to_item_resale"
  - "TrendSignal:secondhand_authenticity_detail + Preference:minimal_clean_marketplace SELECTS EditStyle:clean_marketplace_detail"
  - "EditStyle:true_to_item_resale USES StyleRecipe:window_light_fabric_condition_detail"
  - "StyleRecipe:window_light_fabric_condition_detail APPLIES_TO Scenario:clothing_resale_detail_photo"
  - "Scenario:clothing_resale_detail_photo OFFERS RecommendationVariant:trust_first_condition"
  - "Scenario:clothing_resale_detail_photo OFFERS RecommendationVariant:clean_marketplace_thumbnail"
  - "Scenario:clothing_resale_detail_photo OFFERS RecommendationVariant:personalized_editorial_resale"
  - "RecommendationVariant:trust_first_condition USES Technique:detail_sequence_front_back_tag_flaw"
  - "RecommendationVariant:clean_marketplace_thumbnail USES Technique:white_balance_reference"
  - "RecommendationVariant:personalized_editorial_resale USES Technique:background_cleanup_without_item_change"
  - "Technique:macro_fabric_stitch_closeup SETS Parameter:texture_plus_8_to_20"
  - "Technique:white_balance_reference SETS Parameter:vibrance_minus_5_to_plus_5"
  - "issue:color_inaccuracy CONSTRAINS Parameter:vibrance_minus_5_to_plus_5"
  - "issue:hidden_flaw CONSTRAINS Technique:detail_sequence_front_back_tag_flaw"
  - "issue:personal_info_visible CONSTRAINS Technique:background_cleanup_without_item_change"
  - "issue:overedited_color CONSTRAINS EditStyle:true_to_item_resale"
urls:
  - "https://www.vinted.com/catalog-rules/"
  - "https://blog.poshmark.com/photography-tips-for-poshmark/"
  - "https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4370"
  - "https://www.ebay.com/help/selling/listings/creating-managing-listings/item-conditions-category?id=4765"
  - "https://www.adobe.com/learn/lightroom-cc/web/color-adjustment"
  - "https://www.adobe.com/creativecloud/photography/discover/product-photography.html"
  - "https://support.apple.com/en-lamr/guide/iphone/iph3dc593597/ios"
---

# 의류 리세일 디테일 사진: 원단·택·하자 신뢰 기록

## 추천 시스템용 요약

- **트렌드 추천:** 의류 리세일 사진은 감성 스타일링보다 실제 상품 상태, 원단 질감, 색 정확도, 택/하자 증거를 보여주는 trust-first resale listing 방향이 우선이다.
- **일반 추천:** 앞면, 뒷면, 착용감 또는 형태, 브랜드/사이즈/케어 라벨, 원단, 단추/지퍼/봉제, 하자 부위를 한 세션의 같은 조명에서 찍는다.
- **개인화 추천 변형:** 사용자가 빠른 판매용 클린 썸네일, 빈티지 감성, 고가 브랜드 신뢰 기록 중 무엇을 원하는지에 따라 첫 장 스타일은 달라지지만, 디테일 컷은 실제 상태를 숨기지 않는다.

## 촬영 레시피

1. **사진 순서**
   - 1컷: 전체 앞면. 색과 실루엣을 한눈에 보이게 한다.
   - 2컷: 전체 뒷면. 후면 오염, 늘어남, 봉제 상태를 확인할 수 있게 한다.
   - 3컷: 브랜드/사이즈/케어 라벨. 개인정보가 적힌 영수증이나 배송 라벨은 함께 나오지 않게 한다.
   - 4컷: 원단 질감, 패턴, 니트 짜임, 데님 워싱, 가죽 결 같은 소재 정보.
   - 5컷 이후: 얼룩, 보풀, 올 풀림, 구멍, 단추/지퍼 문제, 밑단 수선 등 구매 결정에 영향을 줄 수 있는 하자.

2. **조명과 배경**
   - 창가 자연광 또는 부드러운 흰색 조명을 사용하고, 같은 물건은 같은 세션에서 모두 찍는다.
   - 흰 셔츠가 노랗게 보이거나 네이비가 검정처럼 보이면 WB를 먼저 맞춘다.
   - 배경은 흰 벽, 무지 천, 깨끗한 바닥처럼 단순한 곳을 사용한다.
   - 패턴이 강한 러그, 여러 옷이 쌓인 배경, 브랜드 쇼핑백은 색 판단과 상태 판단을 방해하므로 피한다.

3. **디테일 촬영**
   - 탭 초점으로 라벨 글자, 스티치, 얼룩 경계를 선명하게 잡는다.
   - 원단 사진은 너무 가까워 초점이 흐려지면 한 걸음 뒤로 물러나고 2x 또는 매크로를 쓴다.
   - 하자 컷은 하자만 확대하지 말고, 위치를 알 수 있는 중간 거리 컷과 근접 컷을 함께 둔다.
   - 색 비교가 어려운 옷은 한 장에 흰 종이 또는 회색/흰 배경을 같이 두어 WB 기준을 만든다. 단, 상품을 가리는 소품은 피한다.

## 보정 레시피

1. **실제 색 유지**
   - Exposure: +0.05~+0.25. 어두운 사진만 밝히고 색을 새로 만들지 않는다.
   - Highlights: -10~-25. 흰색 의류, 새틴, 가죽 반사가 날아가면 낮춘다.
   - Shadows: +5~+20. 검은 옷의 재질이 뭉개질 때만 올린다.
   - Vibrance: -5~+5. 리세일 컷에서 과한 채도는 색 오해와 반품 리스크를 만든다.
   - Color Mix: 특정 색만 다르게 보일 때 HSL로 좁게 조정한다.

2. **원단과 하자 표현**
   - Texture: +8~+20. 니트 짜임, 보풀, 데님 결, 가죽 주름을 읽기 쉽게 한다.
   - Clarity: +3~+10. 너무 올리면 오염이 과장되거나 원단이 거칠어 보이므로 제한한다.
   - Sharpness: +5~+15. 라벨 글자와 봉제선을 선명하게 보조한다.
   - 하자 부위는 지우지 않는다. 주변 먼지, 배경 얼룩, 바닥 먼지처럼 상품 상태와 무관한 요소만 정리한다.

3. **개인화 변형**
   - **Trust-first condition:** 디테일 컷 수를 늘리고, 하자 위치 설명이 가능한 중간 거리 컷을 포함한다.
   - **Clean marketplace thumbnail:** 첫 장만 밝고 단순하게 정리하되, 이후 컷은 실제 상태를 빠짐없이 보여준다.
   - **Editorial resale:** 빈티지/브랜드 무드를 살리더라도 필터가 색을 바꾸면 안 된다. 배경과 스타일링은 첫 장에만 제한하고 상세 컷은 중립 조명으로 둔다.
   - **Color-sensitive item:** 흰색, 검정, 네이비, 레드, 형광색은 보정 강도를 낮추고, 설명에 조명 조건을 함께 기록하는 변형으로 둔다.

## 실패 방지 / 주의점

- 기존 `small_product_listing_photo`처럼 일반 상품 썸네일을 만드는 파일이 아니라, 의류 리세일의 택, 소재, 하자, 색 정확도에 초점을 둔다.
- 하자를 지우거나 색을 바꾸는 편집은 신뢰를 해치므로 `overedited_color`와 `hidden_flaw`를 강한 제한 조건으로 둔다.
- 개인 주소가 적힌 배송 라벨, 영수증, QR 코드, 학생증/사원증 같은 배경 정보가 보이면 크롭하거나 다시 찍는다.
- Vinted/eBay처럼 실제 상품을 표현해야 하는 플랫폼에서는 스톡 이미지, 과한 텍스트/워터마크, 실제와 다른 보정 이미지를 피한다.
- 주름은 상품 상태의 일부일 수 있다. 판매 전 정리 가능한 주름은 스팀/정돈 후 찍고, 늘어남이나 손상은 숨기지 않는다.

## 근거

### 반영한 주요 근거

- Vinted 카탈로그 규칙은 사진이 실제 상품 상태를 나타내야 하며, 결함/스크래치/마모를 보여줄 것을 권장하고, 본인이 촬영한 선명한 사진과 첫 장 전체 상품 컷을 요구한다. 이를 `trust_first_condition`과 `front_back_tag_flaw_sequence`로 반영했다.
- Vinted 일반 규칙은 결함, 변경, 빠진 부품을 설명해야 한다고 안내한다. 의류 디테일 컷에서 하자 위치 컷과 근접 컷을 함께 요구하는 근거로 사용했다.
- Poshmark 사진 팁은 자연광, 휴대폰 조명/링라이트 테스트, 디테일을 보여주는 listing video를 제안한다. 의류 상세 컷에는 같은 조명 아래 여러 형태의 디테일 기록이 필요하다는 근거로 반영했다.
- eBay 사진 정책은 상품 상태 판단을 위해 사진이 중요하며, 실제 상품을 정확히 표현하지 않는 사진, 중고/손상/결함 상품의 스톡 사진, 텍스트/워터마크 추가를 금지한다. 실제 상태 중심 보정과 배경 정리 제한의 근거다.
- eBay 의류 상태 기준은 pre-owned 항목에서 wear와 imperfections를 보여주고 설명해야 한다고 한다. 하자 컷을 숨기지 않는 guardrail로 사용했다.
- Adobe Lightroom 색 보정 자료는 특정 색의 HSL과 Color Mixer 조정을 설명한다. 실제 색을 유지하면서 제한적으로 WB/HSL을 맞추는 편집 근거로 사용했다.
- Adobe 제품 사진 자료와 Apple 카메라 도구 문서는 조명, 초점/노출, 선명한 촬영을 위한 기술 근거로 사용했다.

### 시나리오 선정 포인트

- OOTD나 착용샷이 아니라 구매자가 확인해야 하는 `condition`, `texture`, `label`, `flaw`를 중심으로 구성했다.
- `color_inaccuracy`, `hidden_flaw`, `personal_info_visible`은 스타일 선택 이후 파라미터를 제한하는 modifier다.

## Graphify 추출 힌트

```yaml
entities:
  - scenario:clothing_resale_detail_photo
  - subject:used_clothing
  - subject:fabric_texture
  - subject:brand_size_care_tag
  - trend_signal:trust_first_resale_listing
  - preference:accurate_color
  - edit_style:true_to_item_resale
  - style_recipe:window_light_fabric_condition_detail
  - technique:detail_sequence_front_back_tag_flaw
  - technique:white_balance_reference
  - parameter:texture_plus_8_to_20
  - issue:hidden_flaw
  - issue:personal_info_visible
relationships:
  - trend_signal:trust_first_resale_listing SELECTS edit_style:true_to_item_resale
  - preference:accurate_color CONSTRAINS parameter:vibrance_minus_5_to_plus_5
  - style_recipe:window_light_fabric_condition_detail APPLIES_TO scenario:clothing_resale_detail_photo
  - issue:hidden_flaw CONSTRAINS technique:detail_sequence_front_back_tag_flaw
  - issue:personal_info_visible CONSTRAINS technique:background_cleanup_without_item_change
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

- https://www.vinted.com/catalog-rules/
- https://blog.poshmark.com/photography-tips-for-poshmark/
- https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4370
- https://www.ebay.com/help/selling/listings/creating-managing-listings/item-conditions-category?id=4765
- https://www.adobe.com/learn/lightroom-cc/web/color-adjustment
- https://www.adobe.com/creativecloud/photography/discover/product-photography.html
- https://support.apple.com/en-lamr/guide/iphone/iph3dc593597/ios
