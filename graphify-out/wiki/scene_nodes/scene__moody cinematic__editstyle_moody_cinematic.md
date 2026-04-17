# moody cinematic

- id: `editstyle_moody_cinematic`
- graph: scene-first
- labels: EditStyle, SceneFacet
- source_file: raw/scenarios/rain_neon_street_portrait.md
- source_url: 

## Properties
- **id**: editstyle_moody_cinematic
- **key**: edit_style
- **value**: moody_cinematic
- **name**: moody cinematic
- **source_file**: raw/scenarios/rain_neon_street_portrait.md

## Source-oriented graph 연결
- [[source_nodes/source__Moody Cinematic__edit_style_moody_cinematic|Moody Cinematic]]
- [[source_nodes/source__Rain Neon Street__environment_rain_neon_street|Rain Neon Street]]
- [[source_nodes/source__Neon Backlight__light_neon_backlight|Neon Backlight]]
- [[source_nodes/source__Night Or Portrait__mode_night_or_portrait|Night Or Portrait]]
- [[source_nodes/source__Color Cast__tok_color_cast|Color Cast]]
- [[source_nodes/source__Exposure Time__tok_exposure_time|Exposure Time]]
- [[source_nodes/source__Reflection__tok_reflection|Reflection]]
- [[source_nodes/source__moody cinematic__pref_moody_cinematic|moody cinematic]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_trend_city_night_long_exposure|Trend recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_personalized_city_night_long_exposure|Personalized recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]]
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리__rec_trend_city_window_reflection|Trend recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리__rec_personalized_city_window_reflection|Personalized recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리]]
- `TRIGGERS` → [[scene_nodes/scene__Trend recommendation — 비 오는 밤 네온 거리 인물 — moody city look__rec_trend_rain_neon_street_portrait|Trend recommendation — 비 오는 밤 네온 거리 인물 — moody city look]]
- `TRIGGERS` → [[scene_nodes/scene__Personalized recommendation — 비 오는 밤 네온 거리 인물 — moody city l__rec_personalized_rain_neon_street_portrait|Personalized recommendation — 비 오는 밤 네온 거리 인물 — moody city look]]

## Incoming
- [[scene_nodes/scene__도시 야경 장노출 — 빛줄기_스카이라인__scenario_city_night_long_exposure|도시 야경 장노출 — 빛줄기/스카이라인]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_trend_city_night_long_exposure|Trend recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_personalized_city_night_long_exposure|Personalized recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]] → `USES_FACET`
- [[scene_nodes/scene__도시 야경 유리창 반사 — 산만한 반사 정리__scenario_city_window_reflection|도시 야경 유리창 반사 — 산만한 반사 정리]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리__rec_trend_city_window_reflection|Trend recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리__rec_personalized_city_window_reflection|Personalized recommendation — 도시 야경 유리창 반사 — 산만한 반사 정리]] → `USES_FACET`
- [[scene_nodes/scene__비 오는 밤 네온 거리 인물 — moody city look__scenario_rain_neon_street_portrait|비 오는 밤 네온 거리 인물 — moody city look]] → `HAS_EDIT_STYLE`
- [[scene_nodes/scene__Trend recommendation — 비 오는 밤 네온 거리 인물 — moody city look__rec_trend_rain_neon_street_portrait|Trend recommendation — 비 오는 밤 네온 거리 인물 — moody city look]] → `USES_FACET`
- [[scene_nodes/scene__Personalized recommendation — 비 오는 밤 네온 거리 인물 — moody city l__rec_personalized_rain_neon_street_portrait|Personalized recommendation — 비 오는 밤 네온 거리 인물 — moody city look]] → `USES_FACET`
