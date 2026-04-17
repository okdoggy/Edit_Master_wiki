# 가능하면 후면 1x/2x + 타이머, 아니면 전면 카메라 왜곡을 주의.

- id: `param_mirror_selfie_ootd_가능하면_후면_1x_2x_+_타이머_아니면_전면_카메라_왜곡을_주의.`
- graph: scene-first
- labels: Parameter
- source_file: raw/scenarios/mirror_selfie_ootd.md
- source_url: 

## Properties
- **id**: param_mirror_selfie_ootd_가능하면_후면_1x_2x_+_타이머_아니면_전면_카메라_왜곡을_주의.
- **name**: 가능하면 후면 1x/2x + 타이머, 아니면 전면 카메라 왜곡을 주의.
- **source_file**: raw/scenarios/mirror_selfie_ootd.md

## Source-oriented graph 연결
- [[source_nodes/source__mirror distortion__issue_mirror_distortion|mirror distortion]]
- [[source_nodes/source__dirty mirror__issue_dirty_mirror|dirty mirror]]
- [[source_nodes/source__clean influencer__trend_clean_influencer|clean influencer]]
- [[source_nodes/source__clean influencer__pref_clean_influencer|clean influencer]]
- [[source_nodes/source__longer-looking legs__pref_longer_legs|longer-looking legs]]
- [[source_nodes/source__fashion proportion__outcome_fashion_proportion|fashion proportion]]
- [[source_nodes/source__rear camera + timer__tech_rear_camera_timer|rear camera + timer]]
- [[source_nodes/source__clean mirror__tech_clean_mirror|clean mirror]]
- [[source_nodes/source__4_5 crop__param_crop_4_5|4:5 crop]]
- [[source_nodes/source__MakeUseOf mirror selfie poses__evidence_makeuseof_mirror_selfie|MakeUseOf mirror selfie poses]]

## Outgoing

## Incoming
- [[scene_nodes/scene__Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_trend_mirror_selfie_ootd|Trend recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_TECHNIQUE`
- [[scene_nodes/scene__General recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_general_mirror_selfie_ootd|General recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_TECHNIQUE`
- [[scene_nodes/scene__Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리__rec_personalized_mirror_selfie_ootd|Personalized recommendation — 거울 셀카 OOTD — 몸 비율과 거울 반사 정리]] → `USES_TECHNIQUE`
