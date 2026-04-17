# 1x 2x 5x

- id: `lens_1x_2x_5x`
- graph: scene-first
- labels: Lens, SceneFacet
- source_file: raw/scenarios/city_night_long_exposure.md
- source_url: 

## Properties
- **id**: lens_1x_2x_5x
- **key**: lens
- **value**: 1x_2x_5x
- **name**: 1x 2x 5x
- **source_file**: raw/scenarios/city_night_long_exposure.md

## Source-oriented graph 연결
- [[source_nodes/source__Pro Or Night__mode_pro_or_night|Pro Or Night]]
- [[source_nodes/source__City Lights__subject_city_lights|City Lights]]
- [[source_nodes/source__Low Iso__tok_low_iso|Low Iso]]
- [[source_nodes/source__Noise__tok_noise|Noise]]
- [[source_nodes/source__Noise Reduction__tok_noise_reduction|Noise Reduction]]

## Outgoing
- `TRIGGERS` → [[scene_nodes/scene__General recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_general_city_night_long_exposure|General recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]]

## Incoming
- [[scene_nodes/scene__도시 야경 장노출 — 빛줄기_스카이라인__scenario_city_night_long_exposure|도시 야경 장노출 — 빛줄기/스카이라인]] → `USES_LENS`
- [[scene_nodes/scene__General recommendation — 도시 야경 장노출 — 빛줄기_스카이라인__rec_general_city_night_long_exposure|General recommendation — 도시 야경 장노출 — 빛줄기/스카이라인]] → `USES_FACET`
