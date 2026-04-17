---
title: "Scenario Corpus Index — graphify용 촬영/보정 상황 seed"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "scenario_index"
---

# Scenario Corpus Index — graphify용 촬영/보정 상황 seed

## 추가된 scenario files

| Scenario | File | Main recommendation use |
|---|---|---|
| autumn_maple_woman_portrait | `raw/scenarios/autumn_maple_woman_portrait.md` | trend/general/personalized recommendation seed |
| cherry_blossom_flower_portrait | `raw/scenarios/cherry_blossom_flower_portrait.md` | trend/general/personalized recommendation seed |
| snow_portrait_clean_winter | `raw/scenarios/snow_portrait_clean_winter.md` | trend/general/personalized recommendation seed |
| rain_neon_street_portrait | `raw/scenarios/rain_neon_street_portrait.md` | trend/general/personalized recommendation seed |
| beach_backlit_portrait | `raw/scenarios/beach_backlit_portrait.md` | trend/general/personalized recommendation seed |
| golden_hour_travel_scale | `raw/scenarios/golden_hour_travel_scale.md` | trend/general/personalized recommendation seed |
| window_light_cafe_portrait | `raw/scenarios/window_light_cafe_portrait.md` | trend/general/personalized recommendation seed |
| backlit_silhouette_sunset | `raw/scenarios/backlit_silhouette_sunset.md` | trend/general/personalized recommendation seed |
| concert_stage_low_light | `raw/scenarios/concert_stage_low_light.md` | trend/general/personalized recommendation seed |
| group_travel_selfie | `raw/scenarios/group_travel_selfie.md` | trend/general/personalized recommendation seed |
| pets_children_action | `raw/scenarios/pets_children_action.md` | trend/general/personalized recommendation seed |
| architecture_interior_wide | `raw/scenarios/architecture_interior_wide.md` | trend/general/personalized recommendation seed |
| city_night_long_exposure | `raw/scenarios/city_night_long_exposure.md` | trend/general/personalized recommendation seed |
| fireworks_skyline | `raw/scenarios/fireworks_skyline.md` | trend/general/personalized recommendation seed |
| waterfall_silky_water | `raw/scenarios/waterfall_silky_water.md` | trend/general/personalized recommendation seed |
| flower_macro_bokeh | `raw/scenarios/flower_macro_bokeh.md` | trend/general/personalized recommendation seed |
| reflection_mirror_puddle_prism | `raw/scenarios/reflection_mirror_puddle_prism.md` | trend/general/personalized recommendation seed |
| marketplace_street_food_story | `raw/scenarios/marketplace_street_food_story.md` | trend/general/personalized recommendation seed |

| fashion_ootd_portrait | `raw/scenarios/fashion_ootd_portrait.md` | trend/general/personalized recommendation seed |

| selfie_profile_portrait | `raw/scenarios/selfie_profile_portrait.md` | trend/general/personalized recommendation seed |

| dim_restaurant_food | `raw/scenarios/dim_restaurant_food.md` | Korean alias matching + scene recommendation seed |
| cafe_flatlay_dessert | `raw/scenarios/cafe_flatlay_dessert.md` | Korean alias matching + scene recommendation seed |
| city_window_reflection | `raw/scenarios/city_window_reflection.md` | Korean alias matching + scene recommendation seed |
| harsh_noon_beach_portrait | `raw/scenarios/harsh_noon_beach_portrait.md` | Korean alias matching + scene recommendation seed |
| museum_gallery_portrait | `raw/scenarios/museum_gallery_portrait.md` | Korean alias matching + scene recommendation seed |
| indoor_party_group | `raw/scenarios/indoor_party_group.md` | Korean alias matching + scene recommendation seed |
| crowded_landmark_portrait | `raw/scenarios/crowded_landmark_portrait.md` | Korean alias matching + scene recommendation seed |
| small_product_listing_photo | `raw/scenarios/small_product_listing_photo.md` | Korean alias matching + scene recommendation seed |
| mirror_selfie_ootd | `raw/scenarios/mirror_selfie_ootd.md` | Korean alias matching + scene recommendation seed |
| cafe_drink_dessert_closeup | `raw/scenarios/cafe_drink_dessert_closeup.md` | Korean alias matching + scene recommendation seed |

## 사용법

- Graphify가 각 파일의 `graph_nodes`, `graph_edges`, `Graphify 추출 힌트`를 노드/관계로 가져가도록 설계했다.
- 입력 장면이 들어오면 `subject + environment + light + season + device + preferred_style` 기준으로 가장 가까운 scenario를 찾는다.
- scenario 파일의 `트렌드 추천`, `일반 추천`, `개인화 추천 변수`를 각각 별도 answer channel로 사용할 수 있다.
