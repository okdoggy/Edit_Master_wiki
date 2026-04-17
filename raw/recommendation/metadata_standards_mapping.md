---
title: "Photo metadata standards mapping — Schema.org/IPTC/Exif to recommender graph"
category: "recommendation"
updated_at: "2026-04-17"
content_type: "metadata_standards_mapping"
---

# Photo metadata standards mapping — Schema.org/IPTC/Exif to recommender graph

## 왜 필요한가

Graphify로 raw 촬영/보정 기법을 wiki화한 뒤 추천 시스템에 연결하려면, 사진 1장과 추천 노드를 표준 메타데이터와 연결해야 한다. 이 파일은 공식 표준에서 온 필드와 추천용 추론 필드를 분리한다.

## 표준 기반 필드

### Schema.org ImageObject / Photograph

- `ImageObject`: 이미지 자산을 표현.
- `Photograph`: 사진 타입.
- `contentLocation`: 사진 안에 묘사된 위치.
- `exifData`: 이미지에 붙는 EXIF 정보.
- `spatialCoverage`, `sdPublisher` 등도 연결 가능.

### IPTC Photo Metadata

- `Keywords`: 자유 텍스트 키워드.
- `Subject Code` / Media Topics: 제어 어휘 기반 주제.
- `Location Created`: 사진이 만들어진 위치.
- `Location Shown in Image`: 사진에 묘사된 위치.
- `Model Release Status`: 인물 공개/동의 상태.
- `Image Rating`: 품질/만족 신호 후보.

### Exif / CIPA

- 촬영 기기, 렌즈, 초점거리, 노출, ISO, 셔터, 조리개, 날짜 등 원천 촬영값.
- 현재 공식 표준 축은 Exif 3.1 계열.

## 추천 그래프 필드로 매핑

| Standard/source | Raw field | Graph node/edge | Recommendation use |
|---|---|---|---|
| Exif | focal_length | lens:0.5x/1x/2x/tele | 줌별 일반 추천 |
| Exif | ISO/shutter | capture_setting | 야간/장노출 적합성 |
| IPTC | Keywords | free_tag | 검색/graphify seed |
| IPTC | Subject Code/Media Topic | controlled_subject | 표준 주제 분류 |
| IPTC | Model Release Status | privacy_level/model_release | 인물 추천 안전성 |
| IPTC | Image Rating | satisfaction_signal | 일반 추천/랭킹 |
| Schema.org | contentLocation | location_shown | 여행/장소 추천 |
| User actions | save/like/share/edit reuse | satisfaction_signal | 개인화/일반 선호 |
| CV model | subject/env/light | scenario facet | scene matching |

## 추천용 추론 필드

아래는 표준에 직접 있는 값이 아니라 추천 시스템을 위한 파생 노드다.

- `ScenarioNode`
- `TrendSignalNode`
- `PersonalizationSignalNode`
- `SatisfactionSignalNode`
- `EditStyleNode`
- `TechniqueNode`

## Privacy / safety rules

- `subject:adult_woman` 같은 세부 인물 태그는 동의/정책을 고려한다.
- 인물 사진은 `model_release_status`, `privacy_level`, `location_shown`을 분리 저장한다.
- 추천은 민감 속성을 직접 추론하기보다 사용자가 명시한 취향/스타일 중심으로 한다.

## 최소 JSON 형태 예시

```json
{
  "photo_id": "photo_001",
  "source": {"device": "iPhone", "lens": "2x", "mode": "portrait"},
  "standard_metadata": {
    "schema_org_type": "Photograph",
    "contentLocation": "park",
    "iptc_keywords": ["autumn", "portrait", "maple"],
    "model_release_status": "unknown"
  },
  "graph_facets": {
    "subject": ["person"],
    "environment": ["autumn", "maple_tree"],
    "light": ["golden_hour"],
    "technique": ["backlight", "subject_mask"],
    "edit_style": ["warm_foliage"]
  },
  "signals": {
    "trend": ["fall_foliage_peak"],
    "general": ["face_sharp", "background_separation"],
    "personal": ["prefers_warm_tone"]
  }
}
```

## 출처

- https://schema.org/ImageObject
- https://schema.org/Photograph
- https://www.iptc.org/std/photometadata/documentation/userguide/
- https://iptc.org/news/photo-metadata-standard-updated-to-version-2024-1/
- https://iptc.org/standards/media-topics/
- https://iptc.org/standards/subject-codes/
- https://www.cipa.jp/e/std/std-sec.html
- https://qingyuguo.github.io/files/docs/tkde2020_kgrs_survey.pdf
- https://www.mdpi.com/2079-9292/11/7/1003
