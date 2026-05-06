"""Lightweight multilingual normalization for scene-query matching.

This module deliberately stays dependency-free so it can run inside GitHub
Actions, local launchd jobs, and ad-hoc Codex checks without setup.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field


TOKEN_RE = re.compile(r"[a-z0-9가-힣]+")


@dataclass(frozen=True)
class QuerySlots:
    when: set[str] = field(default_factory=set)
    who: set[str] = field(default_factory=set)
    where: set[str] = field(default_factory=set)
    what: set[str] = field(default_factory=set)
    how: set[str] = field(default_factory=set)
    issues: set[str] = field(default_factory=set)
    preferences: set[str] = field(default_factory=set)

    def as_dict(self) -> dict[str, list[str]]:
        return {
            "when": sorted(self.when),
            "who": sorted(self.who),
            "where": sorted(self.where),
            "what": sorted(self.what),
            "how": sorted(self.how),
            "issues": sorted(self.issues),
            "preferences": sorted(self.preferences),
        }

    @property
    def filled_slot_count(self) -> int:
        return sum(1 for values in (self.when, self.who, self.where, self.what, self.how) if values)


def normalize_text(value: str) -> str:
    """Return a normalized query string while preserving Korean tokens."""

    value = unicodedata.normalize("NFKC", value or "").casefold()
    value = value.replace("×", "x")
    value = re.sub(r"[_/|·•]+", " ", value)
    value = re.sub(r"([0-9])\s*배", r"\1x", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def tokenize(value: str) -> set[str]:
    return set(TOKEN_RE.findall(normalize_text(value)))


SLOT_PATTERNS: dict[str, dict[str, tuple[str, ...]]] = {
    "when": {
        "time:day": ("낮에", "낮 시간", "주간", "day", "daytime", "afternoon"),
        "time:noon": ("정오", "한낮", "noon", "midday", "harsh sun"),
        "time:night": ("밤", "야간", "저조도", "어두운", "night", "low light", "after dark", "dim"),
        "time:golden_hour": ("골든아워", "노을", "해질녘", "sunset", "golden hour"),
        "season:spring": ("봄", "벚꽃", "spring", "cherry blossom"),
        "season:summer": ("여름", "summer"),
        "season:autumn": ("가을", "단풍", "autumn", "fall", "maple"),
        "season:winter": ("겨울", "눈 오는", "눈 내린", "눈밭", "설경", "snow", "winter"),
        "weather:rain": ("비가", "비 오는", "비오는", "rain", "rainy", "wet"),
    },
    "who": {
        "device:iphone": ("아이폰", "iphone", "ios"),
        "device:galaxy": ("갤럭시", "삼성폰", "samsung", "galaxy"),
        "device:pixel": ("픽셀", "google pixel", "pixel"),
        "app:lightroom": ("라이트룸", "lightroom", "lr"),
        "app:photoshop": ("포토샵", "photoshop", "ps"),
    },
    "where": {
        "place:cafe": ("카페", "커피숍", "cafe", "coffee shop"),
        "place:cafe_window": ("카페 창가", "창가", "창 옆", "창문 옆", "cafe window", "window light"),
        "place:restaurant": ("식당", "레스토랑", "restaurant", "dining"),
        "place:street": ("거리", "길거리", "골목", "street", "alley"),
        "place:rain_neon_street": ("네온 거리", "네온 간판", "네온 사인", "neon street", "neon sign"),
        "place:beach": ("해변", "바다", "바닷가", "beach", "seaside"),
        "place:museum": ("미술관", "전시장", "전시회", "museum", "gallery"),
        "place:market": ("재래시장", "시장 골목", "시장 음식", "마켓", "market", "street food"),
        "place:landmark": ("관광지", "랜드마크", "명소", "유명 장소", "landmark", "tourist"),
        "place:travel": ("여행", "여행지", "travel", "trip", "vacation"),
        "place:mountain": ("산 풍경", "산", "풍경", "하늘", "mountain", "landscape", "sky", "foreground"),
        "place:mirror": ("거울", "엘리베이터", "mirror", "elevator"),
        "place:city_window": ("유리창 야경", "창문에 비친", "창문 반사", "city window", "window reflection"),
        "place:stage": ("콘서트", "공연장", "공연", "무대", "concert", "stage"),
        "place:snow": ("눈 오는", "설경", "snowy"),
        "place:home": ("집", "홈", "home", "studio"),
        "place:cave": ("동굴", "석회동굴", "cave", "cavern"),
        "place:aerial_view": ("항공샷", "위에서", "내려다본", "탑다운", "top-down", "overhead", "aerial", "balcony"),
        "place:desk_table": ("책상", "테이블", "문서", "영수증", "desk", "table", "receipt"),
    },
    "what": {
        "intent:portrait": ("인물", "인물컷", "사람", "사람 사진", "얼굴", "친구를", "프로필", "portrait", "profile"),
        "intent:couple_portrait": ("커플", "couple"),
        "intent:selfie": ("셀카", "selfie"),
        "intent:group_photo": ("친구", "친구들이랑", "친구들과", "가족", "단체", "그룹", "여럿", "group photo", "group selfie", "friends"),
        "intent:ootd": ("ootd", "전신", "착장", "패션", "옷", "outfit"),
        "intent:food": ("음식", "파스타", "디저트", "케이크", "라떼", "브런치", "먹음직", "food", "pasta", "dessert", "cake", "latte"),
        "intent:flatlay": ("플랫레이", "위에서", "탑뷰", "flatlay", "flat lay", "top view", "top-down"),
        "intent:drink_dessert_closeup": ("접사", "클로즈업", "거품", "질감", "closeup", "close-up", "macro"),
        "intent:product_listing": ("제품", "상품", "중고거래", "썸네일", "product", "listing", "marketplace"),
        "intent:pets_kids": ("강아지", "반려동물", "아이", "pet", "dog", "kid", "child"),
        "intent:action_motion": ("자전거", "러너", "달리는", "달려오는", "뛰는", "역동", "액션", "cyclist", "runner", "running", "sports", "action shot"),
        "intent:flower_macro": ("꽃", "꽃사진", "식물", "flower", "flowers", "plant", "bokeh"),
        "intent:landscape": ("풍경", "산", "하늘", "전경", "landscape", "mountain", "sky", "foreground"),
        "intent:city_lights": ("야경", "도시", "city lights", "night city"),
        "intent:reflection": ("반사", "비친", "reflection", "reflected"),
        "intent:trendy_style": ("트렌디", "요즘", "유행", "sns", "instagram", "인스타", "viral"),
        "intent:story": ("스토리", "다큐", "documentary", "story"),
        "intent:document_scan": ("문서", "계약서", "화이트보드", "글자", "스캔", "스캔본", "읽기 좋은", "scan", "document", "whiteboard", "readable"),
        "intent:receipt_flatlay": ("영수증", "영수증샷", "포토덤프", "photo dump", "receipt", "receipt photo"),
        "intent:dating_profile": ("소개팅", "소개팅 프로필", "데이팅", "데이팅 앱", "dating profile", "meeting new people"),
        "intent:aerial_shot": ("항공샷", "탑다운", "위에서 내려다", "top-down", "overhead", "aerial"),
        "intent:cave_photo": ("동굴", "석회동굴", "cave", "cavern"),
        "intent:paparazzi_candid": ("파파라치", "파파라치샷", "캔디드", "candid", "paparazzi", "flashy", "editorial", "caught by a flash"),
    },
    "how": {
        "lens_mode:0_5x": ("0.5x", "초광각", "ultrawide", "wide"),
        "lens_mode:1x": ("1x", "기본렌즈"),
        "lens_mode:2x": ("2x", "2배", "망원", "telephoto"),
        "lens_mode:3x_5x": ("3x", "5x", "멀리", "줌", "zoom"),
        "mode:portrait": ("인물모드", "portrait mode"),
        "mode:night": ("야간모드", "night mode"),
        "mode:pro": ("프로모드", "pro mode", "raw", "proraw", "expert raw"),
        "mode:burst": ("연사", "버스트", "burst", "live photo", "video still"),
        "mode:panning": ("팬샷", "패닝", "배경만 흐르게", "panning", "pan shot", "motion pan"),
        "mode:no_flash": ("플래시 없이", "플래시를 켜지 않고", "플래시는 못", "플래시는 쓸 수 없", "플래시 금지", "no flash", "without flash", "flash off"),
        "light:backlight": ("역광", "뒤에서 강한 빛", "뒤에서 빛", "뒤쪽 빛", "backlight", "backlit", "back lit"),
        "light:rim_light": ("림라이트", "테두리 빛", "머리 위 테두리", "가장자리 빛", "머리카락 빛", "머리카락 테두리", "hair glow", "rim light"),
        "light:harsh_light": ("강한 햇빛", "햇빛이 강", "햇빛 너무", "직사광", "빛이 너무", "쨍한 빛", "harsh light", "harsh sun"),
        "light:flash": ("플래시", "flash", "direct flash", "on-camera flash"),
        "edit:mask": ("마스크", "mask", "subject mask"),
        "edit:white_balance": ("화이트밸런스", "wb", "white balance"),
        "edit:crop": ("크롭", "crop", "4:5", "9:16"),
        "edit:perspective": ("사다리꼴", "원근", "기하", "모서리", "비뚤", "skewed", "perspective", "straighten", "geometry", "upright"),
    },
    "issues": {
        "issue:underexposed_face": ("얼굴 어둡", "얼굴이 어둡", "얼굴이 어두", "얼굴은 어둡", "얼굴은 어두", "얼굴은 어둡게", "얼굴 반쪽", "얼굴 그림자", "얼굴 한쪽", "칙칙", "face dark", "underexposed face", "shadow on face"),
        "issue:busy_background": ("배경 지저분", "배경이 지저분", "뒤 테이블", "뒤쪽 테이블", "어수선", "관광객", "사람 많", "산만", "busy background", "cluttered", "clutter"),
        "issue:blown_highlights": ("하늘 날아", "하늘은 하얗", "하이라이트", "네온만 너무", "날아가", "날아갔", "날림", "너무 밝", "밝게 날아", "번쩍", "스포트라이트", "쨍", "쨍하게", "과노출", "하얗게", "하얗게 뭉치", "빛이 터", "blown", "clipping", "overexposed"),
        "issue:hair_highlight_clipping": ("머리 위로 쨍", "머리 위 빛", "머리 위 테두리", "머리카락 가장자리", "가장자리 빛", "머리카락만 너무 밝", "머리카락 하이라이트", "머리 하이라이트", "테두리 빛", "림라이트가 너무", "rim light too strong", "hair highlight clipping"),
        "issue:mixed_white_balance": ("노랗", "누렇", "색이 틀", "피부색이 어색", "조명이 섞", "주황빛", "화이트밸런스", "yellow", "mixed light", "color cast"),
        "issue:motion_blur": ("흐릿", "흔들", "흔들려", "blur", "blurry", "motion blur"),
        "issue:tilted_horizon": ("삐뚤", "비뚤", "수평", "수평이 틀", "tilted", "crooked"),
        "issue:edge_distortion": ("왜곡", "비율 이상", "비율이 애매", "다리 짧", "가장자리 얼굴", "늘어나", "distortion", "proportion", "edge face", "faces stretched", "wide angle face"),
        "issue:dynamic_range": ("하늘은 하얗", "전경은 어둡", "다이내믹레인지", "dynamic range", "fake hdr", "hdr", "foreground is dark", "sky is blown"),
        "issue:dirty_reflection": ("반사가 지저분", "유리 반사", "화면 반사", "dirty mirror", "messy reflection"),
        "issue:macro_focus": ("초점 안", "초점이 부드럽", "접사 초점", "focus miss", "macro focus"),
        "issue:document_skew": ("사다리꼴", "휘고", "비뚤", "모서리", "skewed", "corners", "perspective"),
        "issue:paper_shadow": ("종이 그림자", "책상 그림자", "그림자가 들어", "gray paper", "board is gray", "shadow"),
        "issue:red_eye_flash_glare": ("빨간 눈", "번들거림", "플래시 반사", "red eye", "flash glare", "shiny skin"),
    },
    "preferences": {
        "pref:warm": ("따뜻", "warm"),
        "pref:natural": ("자연스럽", "티 나지", "natural", "no filter"),
        "pref:cinematic": ("시네마틱", "cinematic", "moody"),
        "pref:clean": ("깔끔", "깨끗", "정돈", "정리", "clean"),
        "pref:film": ("필름", "grain", "그레인", "nostalgia"),
        "pref:low_retouch": ("보정 티", "티 안", "low retouch", "subtle"),
    },
}


def _contains_phrase(text: str, phrase: str) -> bool:
    normalized_phrase = normalize_text(phrase)
    if not normalized_phrase:
        return False
    return normalized_phrase in text


def extract_slots(query: str) -> QuerySlots:
    text = normalize_text(query)
    values: dict[str, set[str]] = {key: set() for key in SLOT_PATTERNS}
    for slot, mapping in SLOT_PATTERNS.items():
        for canonical, phrases in mapping.items():
            if any(_contains_phrase(text, phrase) for phrase in phrases):
                values[slot].add(canonical)
    return QuerySlots(
        when=values["when"],
        who=values["who"],
        where=values["where"],
        what=values["what"],
        how=values["how"],
        issues=values["issues"],
        preferences=values["preferences"],
    )


def canonical_terms_for_text(value: str) -> set[str]:
    terms = tokenize(value)
    slots = extract_slots(value)
    for values in slots.as_dict().values():
        terms.update(values)
    return terms
