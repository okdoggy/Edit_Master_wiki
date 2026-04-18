#!/usr/bin/env python3
"""Hourly raw-data collector for smartphone/SNS photography techniques.

The collector is intentionally dependency-free. It fetches public RSS/Atom/search
feeds, filters for recent smartphone/social/photo-editing technique signals, skips
anything already represented in raw/, and writes a Graphify-friendly markdown file
under raw/hourly/ using the existing actionable tip-card style.

It does not copy full source articles. It stores source URLs, short source cues,
and original Korean synthesis for practical use.
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "raw"
HOURLY_DIR = RAW_DIR / "hourly"
MANIFEST_DIR = RAW_DIR / "manifests"
STATE_PATH = MANIFEST_DIR / "hourly_collection_state.json"
SOURCES_CSV = MANIFEST_DIR / "sources.csv"
SOURCE_MATRIX = MANIFEST_DIR / "source_matrix.md"
README = RAW_DIR / "README.md"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "EditMasterWikiRawCollector/1.0 Safari/537.36"
)
TIMEOUT = 18
MAX_PAGE_CHARS = 650_000

PRO_FEEDS = [
    ("PetaPixel", "professional", "https://petapixel.com/feed/"),
    ("Fstoppers", "professional", "https://fstoppers.com/feed"),
    ("DIYPhotography", "professional", "https://www.diyphotography.net/feed/"),
    ("Amateur Photographer", "professional", "https://amateurphotographer.com/feed/"),
    ("Digital Photography School", "professional", "https://digital-photography-school.com/feed/"),
]

COMMUNITY_FEEDS = [
    ("Reddit r/postprocessing top/day", "community", "https://www.reddit.com/r/postprocessing/top/.rss?t=day"),
    ("Reddit r/mobilephotography top/day", "community", "https://www.reddit.com/r/mobilephotography/top/.rss?t=day"),
    ("Reddit r/iPhoneography top/day", "community", "https://www.reddit.com/r/iPhoneography/top/.rss?t=day"),
    ("Reddit r/AskPhotography top/day", "community", "https://www.reddit.com/r/AskPhotography/top/.rss?t=day"),
    ("Reddit r/Lightroom top/week", "community", "https://www.reddit.com/r/Lightroom/top/.rss?t=week"),
]

SEARCH_QUERIES = [
    "Instagram photo editing trend smartphone photography when:7d",
    "TikTok photography hack smartphone photo editing when:7d",
    "Lightroom mobile editing trend smartphone photography when:14d",
    "mobile photography community Lightroom before after when:14d",
    "Galaxy iPhone smartphone camera technique RAW Lightroom when:14d",
    "Reels Shorts photo carousel editing trend photography when:14d",
]

KEYWORDS = {
    "core": [
        "photo", "photography", "camera", "smartphone", "mobile", "iphone", "galaxy",
        "android", "pixel", "xiaomi", "oppo", "vivo", "sony xperia", "lightroom",
        "snapseed", "vsco", "instagram", "tiktok", "reels", "shorts", "sns",
    ],
    "technique": [
        "edit", "editing", "postprocessing", "post-processing", "mask", "masking",
        "raw", "proraw", "expert raw", "dng", "pro mode", "manual", "night",
        "low light", "portrait", "macro", "telephoto", "zoom", "lens", "composition",
        "color", "colour", "grade", "grading", "grain", "film", "cinematic",
        "flash", "exposure", "white balance", "shutter", "iso", "focus", "bokeh",
        "vertical", "carousel", "filter", "preset", "ai", "generative", "remove",
    ],
    "negative": [
        "deal", "coupon", "sale", "price", "leak", "rumor", "case", "screen protector",
        "privacy display", "battery", "charging", "benchmark", "firmware", "wallpaper",
        "price drop", "deal", "best deal",
    ],
}

TAG_KEYWORDS = {
    "telephoto_macro_focus_control": ["telephoto", "macro", "focus enhancer", "auto lens", "lens switching", "close-up", "close up", "3x", "5x"],
    "low_light_night_social": ["night", "low light", "concert", "festival", "nightography", "dark", "dancefloor"],
    "sns_vertical_carousel": ["instagram", "tiktok", "reels", "shorts", "carousel", "social", "vertical"],
    "lightroom_color_masking": ["lightroom", "mask", "masking", "color grade", "colour grade", "postprocessing", "before/after", "before after"],
    "ai_authenticity_guardrail": ["ai", "generative", "remove", "enhance", "authentic", "fake", "uncanny"],
    "raw_sensor_pro_mode": ["raw", "proraw", "expert raw", "dng", "sensor", "pro mode", "manual"],
    "film_grain_nostalgia": ["grain", "film", "nostalgia", "vintage", "2016", "washed", "lo-fi", "lofi"],
}


@dataclasses.dataclass
class Candidate:
    source_name: str
    source_kind: str
    feed_url: str
    title: str
    url: str
    published_at: str = ""
    summary: str = ""
    fetched_text: str = ""
    score: int = 0
    tags: list[str] = dataclasses.field(default_factory=list)

    @property
    def canonical_url(self) -> str:
        return canonicalize_url(self.url)

    @property
    def fingerprint(self) -> str:
        return title_fingerprint(self.title)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        if tag in {"script", "style", "noscript", "svg", "canvas"}:
            self.skip += 1
        if tag in {"p", "div", "li", "br", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str):
        if tag in {"script", "style", "noscript", "svg", "canvas"} and self.skip:
            self.skip -= 1
        if tag in {"p", "div", "li", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_data(self, data: str):
        if not self.skip:
            cleaned = data.strip()
            if cleaned:
                self.parts.append(cleaned)

    def text(self) -> str:
        text = html.unescape(" ".join(self.parts))
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n\s+", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


def canonicalize_url(url: str) -> str:
    url = html.unescape((url or "").strip())
    if not url:
        return ""
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=False)
    query = [(k, v) for k, v in query if not k.lower().startswith(("utm_", "fbclid", "gclid", "mc_cid", "mc_eid"))]
    normalized_query = urllib.parse.urlencode(query, doseq=True)
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")
    netloc = parsed.netloc.lower()
    return urllib.parse.urlunsplit((parsed.scheme.lower() or "https", netloc, path, normalized_query, ""))


def title_fingerprint(title: str) -> str:
    t = html.unescape(title or "").lower()
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"[^a-z0-9가-힣]+", " ", t)
    stop = {"the", "a", "an", "and", "or", "for", "with", "this", "that", "how", "to", "in", "on", "of", "is", "are"}
    tokens = [tok for tok in t.split() if tok not in stop and len(tok) > 1]
    return " ".join(tokens[:18])


def slugify(value: str, max_len: int = 70) -> str:
    value = title_fingerprint(value)
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value).strip("-")
    if not value:
        value = hashlib.sha1(str(time.time()).encode()).hexdigest()[:10]
    return value[:max_len].strip("-")


def fetch_url(url: str, accept: str = "*/*") -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
        return res.read(MAX_PAGE_CHARS)


def decode_bytes(data: bytes) -> str:
    for enc in ("utf-8", "utf-8-sig", "cp949", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def strip_html(raw: str) -> str:
    parser = TextExtractor()
    try:
        parser.feed(raw)
    except Exception:
        return re.sub(r"<[^>]+>", " ", raw)
    return parser.text()


def parse_date_to_iso(value: str) -> str:
    value = html.unescape((value or "").strip())
    if not value:
        return ""
    try:
        from email.utils import parsedate_to_datetime

        d = parsedate_to_datetime(value)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d.astimezone().isoformat(timespec="seconds")
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d", "%a, %d %b %Y %H:%M:%S %z"):
        try:
            d = dt.datetime.strptime(value, fmt)
            if d.tzinfo is None:
                d = d.replace(tzinfo=dt.timezone.utc)
            return d.astimezone().isoformat(timespec="seconds")
        except Exception:
            continue
    return value[:80]


def parse_feed(source_name: str, source_kind: str, feed_url: str) -> list[Candidate]:
    try:
        xml_text = decode_bytes(fetch_url(feed_url, accept="application/rss+xml, application/atom+xml, text/xml, */*"))
    except Exception as exc:
        print(f"WARN feed fetch failed: {source_name}: {exc}", file=sys.stderr)
        return []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        print(f"WARN feed parse failed: {source_name}: {exc}", file=sys.stderr)
        return []

    candidates: list[Candidate] = []
    # RSS 2.0
    for item in root.findall(".//item"):
        title = first_text(item, ["title"])
        link = first_text(item, ["link", "guid"])
        pub = first_text(item, ["pubDate", "published", "updated"])
        summary = first_text(item, ["description", "summary", "content"])
        if title and link:
            candidates.append(Candidate(source_name, source_kind, feed_url, clean_text(title), clean_text(link), parse_date_to_iso(pub), clean_text(strip_html(summary))))

    # Atom
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall(".//atom:entry", ns):
        title = first_text(entry, ["{http://www.w3.org/2005/Atom}title"])
        link = ""
        for lnk in entry.findall("{http://www.w3.org/2005/Atom}link"):
            href = lnk.attrib.get("href", "")
            rel = lnk.attrib.get("rel", "alternate")
            if href and rel in {"alternate", ""}:
                link = href
                break
        if not link:
            link = first_text(entry, ["{http://www.w3.org/2005/Atom}id"])
        pub = first_text(entry, ["{http://www.w3.org/2005/Atom}published", "{http://www.w3.org/2005/Atom}updated"])
        summary = first_text(entry, ["{http://www.w3.org/2005/Atom}summary", "{http://www.w3.org/2005/Atom}content"])
        if title and link:
            candidates.append(Candidate(source_name, source_kind, feed_url, clean_text(title), clean_text(link), parse_date_to_iso(pub), clean_text(strip_html(summary))))

    return candidates


def first_text(node: ET.Element, names: Iterable[str]) -> str:
    for name in names:
        found = node.find(name)
        if found is not None and found.text:
            return found.text
    return ""


def clean_text(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def google_news_feed(query: str) -> tuple[str, str, str]:
    params = urllib.parse.urlencode({"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"})
    return (f"Google News search — {query}", "search", f"https://news.google.com/rss/search?{params}")


def build_candidate_pool() -> list[Candidate]:
    pool: list[Candidate] = []
    for source_name, source_kind, feed_url in [*PRO_FEEDS, *COMMUNITY_FEEDS, *[google_news_feed(q) for q in SEARCH_QUERIES]]:
        pool.extend(parse_feed(source_name, source_kind, feed_url))
    # Deduplicate within pool by canonical URL first, fingerprint second.
    seen_urls: set[str] = set()
    seen_fps: set[str] = set()
    unique: list[Candidate] = []
    for cand in pool:
        if not cand.canonical_url or cand.canonical_url in seen_urls:
            continue
        fp = cand.fingerprint
        if fp and fp in seen_fps:
            continue
        seen_urls.add(cand.canonical_url)
        if fp:
            seen_fps.add(fp)
        unique.append(cand)
    return unique


def load_state() -> dict:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(STATE_PATH)


def existing_signatures(state: dict) -> tuple[set[str], set[str]]:
    urls: set[str] = set(state.get("seen_urls", []))
    fps: set[str] = set(state.get("seen_title_fingerprints", []))
    url_re = re.compile(r"https?://[^\s\)\]\}\>\"']+")
    for path in RAW_DIR.rglob("*.md"):
        if path.parts[-2:] and "hourly" in path.parts and path.name.startswith("_"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for url in url_re.findall(text):
            urls.add(canonicalize_url(url.rstrip(".,;")))
        # Frontmatter title + h1 headings reduce duplicate title variants.
        for match in re.findall(r"^title:\s*[\"']?(.+?)[\"']?\s*$|^#\s+(.+)$", text, flags=re.M):
            title = match[0] or match[1]
            fp = title_fingerprint(title)
            if fp:
                fps.add(fp)
    if SOURCES_CSV.exists():
        try:
            with SOURCES_CSV.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    for key in ("primary_url", "all_urls"):
                        for u in str(row.get(key, "")).split(";"):
                            if u.strip():
                                urls.add(canonicalize_url(u.strip()))
                    if row.get("title"):
                        fps.add(title_fingerprint(row["title"]))
        except Exception:
            pass
    return urls, fps


def score_candidate(cand: Candidate) -> Candidate:
    text = f"{cand.title} {cand.summary}".lower()
    score = 0
    for word in KEYWORDS["core"]:
        if word in text:
            score += 2
    for word in KEYWORDS["technique"]:
        if word in text:
            score += 3
    for word in KEYWORDS["negative"]:
        if word in text:
            score -= 3
    if cand.source_kind == "community":
        score += 3
    if cand.source_kind == "professional":
        score += 2
    if cand.source_kind == "search":
        # Search feeds are useful for discovery but weaker than direct professional/community feeds.
        score -= 4
    if "reddit" in cand.canonical_url:
        score += 2
    title_text = cand.title.lower()
    if any(w in text for w in ["before/after", "before after", "thoughts", "tips", "how to", "guide", "settings"]):
        score += 3
    if any(w in title_text for w in ["tips", "how to", "settings", "composition", "lessons", "raw photos", "moody night", "skin tones", "before/after", "before after"]):
        score += 8
    if any(w in title_text for w in ["performance", "sluggish", "memory", "subscription", "library", "new pc", "laptop", "chair", "office chair", "dailyhunt"]):
        score -= 14
    if any(w in title_text for w in ["new versions", "release", "dropped", "update"]) and not any(w in title_text for w in ["tips", "how to", "settings", "technique"]):
        score -= 40
    if any(w in text for w in ["review", "best phone", "ranking"]) and not any(w in text for w in ["settings", "tips", "technique", "raw", "lightroom"]):
        score -= 4
    tags = []
    for tag, words in TAG_KEYWORDS.items():
        if any(w in text for w in words):
            tags.append(tag)
    if not tags and score > 0:
        tags.append("general_mobile_photo_signal")
    cand.score = score
    cand.tags = tags
    return cand


def is_duplicate(cand: Candidate, existing_urls: set[str], existing_fps: set[str]) -> bool:
    if cand.canonical_url in existing_urls:
        return True
    fp = cand.fingerprint
    if not fp:
        return False
    if fp in existing_fps:
        return True
    tokens = set(fp.split())
    if len(tokens) < 4:
        return False
    for old in existing_fps:
        old_tokens = set(old.split())
        if not old_tokens:
            continue
        overlap = len(tokens & old_tokens) / max(1, min(len(tokens), len(old_tokens)))
        if overlap >= 0.86:
            return True
    return False


def fetch_candidate_text(cand: Candidate) -> None:
    try:
        raw = decode_bytes(fetch_url(cand.url, accept="text/html,application/xhtml+xml,application/xml,*/*"))
        cand.fetched_text = strip_html(raw)[:7000]
    except Exception as exc:
        print(f"WARN page fetch failed: {cand.title}: {exc}", file=sys.stderr)
        cand.fetched_text = ""


def select_candidates(pool: list[Candidate], max_items: int, min_score: int, existing_urls: set[str], existing_fps: set[str]) -> tuple[list[Candidate], dict]:
    stats = {"pool": len(pool), "duplicates": 0, "low_score": 0, "selected": 0}
    scored: list[Candidate] = []
    for cand in pool:
        score_candidate(cand)
        if is_duplicate(cand, existing_urls, existing_fps):
            stats["duplicates"] += 1
            continue
        if cand.score < min_score:
            stats["low_score"] += 1
            continue
        scored.append(cand)
    scored.sort(key=lambda c: (c.score, c.source_kind == "community", c.published_at), reverse=True)
    selected: list[Candidate] = []
    source_counts: dict[str, int] = {}
    for cand in scored:
        # Keep hourly files diverse; avoid three cards from the same subreddit/feed.
        if source_counts.get(cand.source_name, 0) >= 1:
            continue
        selected.append(cand)
        source_counts[cand.source_name] = source_counts.get(cand.source_name, 0) + 1
        if len(selected) >= max_items:
            break
    for cand in selected:
        fetch_candidate_text(cand)
    stats["selected"] = len(selected)
    return selected, stats


def quote_safe(value: str) -> str:
    return value.replace('"', '\\"')


def yaml_list(values: Iterable[str], indent: int = 2) -> str:
    pad = " " * indent
    return "\n".join(f'{pad}- "{quote_safe(v)}"' for v in values if v)


def primary_tag(cand: Candidate) -> str:
    text = f"{cand.title} {cand.summary}".lower()
    priority = [
        "low_light_night_social",
        "sns_vertical_carousel",
        "lightroom_color_masking",
        "ai_authenticity_guardrail",
        "raw_sensor_pro_mode",
        "telephoto_macro_focus_control",
        "film_grain_nostalgia",
        "general_mobile_photo_signal",
    ]
    # Telephoto/macro should only dominate when the title/summary is explicitly
    # about lens switching/focus/macro, not when a page contains incidental words.
    if "telephoto_macro_focus_control" in cand.tags and any(w in text for w in ["telephoto", "macro", "focus enhancer", "auto lens", "lens switching", "close-up", "close up"]):
        return "telephoto_macro_focus_control"
    for tag in priority:
        if tag in cand.tags:
            return tag
    return cand.tags[0] if cand.tags else "general_mobile_photo_signal"


def derive_korean_title(cand: Candidate) -> str:
    tag = primary_tag(cand)
    mapping = {
        "telephoto_macro_focus_control": "망원·매크로 자동 전환을 통제해 디테일 살리기",
        "low_light_night_social": "저조도 SNS 사진에서 흔들림·노이즈 줄이기",
        "sns_vertical_carousel": "Reels/Shorts/캐러셀 겸용 세로 사진 설계",
        "lightroom_color_masking": "Lightroom Mobile 마스크·색보정으로 과보정 줄이기",
        "ai_authenticity_guardrail": "AI 보정/제거 기능을 티 나지 않게 쓰는 안전선",
        "raw_sensor_pro_mode": "RAW/Pro mode로 후보정 여지 확보하기",
        "film_grain_nostalgia": "필름 그레인·워시드 톤을 SNS 감성으로 쓰기",
        "general_mobile_photo_signal": "스마트폰 사진 트렌드 신호를 실전 레시피로 변환",
    }
    return mapping.get(tag, mapping["general_mobile_photo_signal"])


def source_cue(cand: Candidate) -> str:
    # Do not copy source prose into raw files. Store only detected signal words and
    # the source link/title, then synthesize original Korean practice notes below.
    text = f"{cand.title} {cand.summary} {cand.fetched_text[:1200]}".lower()
    matched: list[str] = []
    for words in (KEYWORDS["core"], KEYWORDS["technique"]):
        for word in words:
            if word in text and word not in matched:
                matched.append(word)
            if len(matched) >= 12:
                break
        if len(matched) >= 12:
            break
    if matched:
        return "제목/메타/본문 일부에서 감지된 신호어: " + ", ".join(matched)
    return "제목/메타데이터 중심으로 확인된 새 링크."


def recipe_for(cand: Candidate) -> dict[str, list[str] | str]:
    tags = set(cand.tags)
    title_lower = f"{cand.title} {cand.summary}".lower()
    tag = primary_tag(cand)

    if tag == "low_light_night_social":
        return {
            "situation": "밤거리, 콘서트, 축제, 식당처럼 SNS에 바로 올리고 싶지만 흔들림·노이즈·하이라이트 날림이 동시에 생기는 장면.",
            "steps": [
                "피사체를 탭해 초점/노출 기준을 먼저 고정한다.",
                "움직이는 사람은 장노출보다 짧은 순간을 우선하고, 정적인 도시/무대는 Night mode나 고정 촬영을 쓴다.",
                "먼 피사체는 디지털 확대보다 3x/5x 같은 광학 망원부터 확인한다.",
                "네온·무대 조명은 밝게 찍기보다 살짝 어둡게 찍고 후보정에서 그림자만 조심스럽게 올린다.",
            ],
            "settings": [
                "EV: -0.3~-1.0 시작",
                "Night mode: 정적 장면만 길게, 사람/공연은 짧게",
                "ISO: Pro mode 가능 시 낮게 시작, 움직임 있으면 셔터 우선",
                "Timer/Support: 난간·벽·삼각대 + 2~3초 타이머",
            ],
            "edit": [
                "Highlights -30~-70으로 네온/조명 복구.",
                "Shadows +10~+30까지만 올리고 Noise Reduction +10~+30으로 마무리.",
                "Color Grading은 shadows cool / highlights warm으로 약하게 시작.",
            ],
            "caution": [
                "밝은 밤 사진이 항상 좋은 밤 사진은 아니다. 어두운 분위기를 남겨야 입체감이 산다.",
                "움직이는 사람에게 Max 장노출을 쓰면 얼굴이 흐려진다.",
            ],
            "confidence": "official/vendor guidance + professional/community trend synthesis.",
        }

    if tag == "telephoto_macro_focus_control":
        return {
            "situation": "음식·꽃·소품을 가까이 찍을 때 자동 매크로/렌즈 전환 때문에 디테일이 뭉개지거나 원근감이 바뀌는 장면.",
            "steps": [
                "먼저 1x 기본 렌즈와 3x/5x 망원을 각각 테스트 컷으로 비교한다.",
                "가까이 갈수록 자동 매크로/Focus Enhancer/auto lens switching이 켜지는지 화면 아이콘을 확인한다.",
                "망원 배경흐림과 압축감이 목적이면 자동 전환을 끄고, 피사체에서 한 걸음 물러나 광학 망원으로 다시 구도 잡는다.",
                "텍스트·문서처럼 선명한 평면 기록이 목적이면 매크로/초광각 전환을 허용하고 왜곡은 후보정에서 정리한다.",
            ],
            "settings": [
                "Lens: 3x/5x optical 우선, 디지털 줌 최소화",
                "Distance: 최소 초점거리보다 5~15cm 여유",
                "EV: 밝은 접시/꽃잎은 -0.3~-0.7",
                "Focus: 피사체 디테일을 탭해 고정, 흔들리면 타이머 2초",
            ],
            "edit": [
                "Texture +5~+20, Clarity +0~+10으로 디테일만 보강한다.",
                "배경은 Mask로 Saturation/Exposure를 낮춰 주 피사체를 살린다.",
                "과한 샤프닝으로 가장자리 halo가 생기면 Sharpening보다 Texture를 우선한다.",
            ],
            "caution": [
                "자동 매크로가 항상 나쁜 것은 아니다. 아주 가까운 문서/작은 물체에는 초광각 매크로가 더 안정적일 수 있다.",
                "망원 매크로는 빛이 부족하면 셔터가 느려져 흔들림이 커진다.",
            ],
            "confidence": "source-supported + community-observed. 장치별 메뉴명은 제조사/OS 버전에 따라 다를 수 있음.",
        }


    if tag == "sns_vertical_carousel":
        return {
            "situation": "같은 사진을 Instagram 피드, TikTok/Reels/Shorts 커버, 캐러셀 스토리텔링에 함께 쓰려는 장면.",
            "steps": [
                "촬영 단계에서 9:16 안전영역을 먼저 확보하고, 피사체 주변에 텍스트 여백을 남긴다.",
                "피드용 4:5와 숏폼 커버용 9:16을 별도 export할 것을 전제로 넓게 찍는다.",
                "한 장의 완성컷보다 디테일/비하인드/환경 컷을 같이 찍어 3~5장 캐러셀로 묶는다.",
                "첫 장은 얼굴·색·형태가 즉시 읽히는 컷, 뒤쪽은 맥락과 디테일 컷으로 구성한다.",
            ],
            "settings": [
                "Crop master: 9:16 + 4:5 동시 고려",
                "Negative space: 상단/좌우 10~20% 여백",
                "Contrast: +5~+20, 텍스트 영역 배경 Saturation -5~-20",
                "Export: 1080px 계열 플랫폼별 프리셋 분리",
            ],
            "edit": [
                "피사체 Mask로 얼굴/제품만 살리고 배경은 노출·채도를 낮춘다.",
                "커버 이미지는 Clarity보다 읽기 쉬운 Contrast와 Crop 우선.",
                "캐러셀 전체 WB/톤을 맞춰 피드 일관성을 만든다.",
            ],
            "caution": [
                "한 비율에서 맞춘 텍스트는 다른 비율에서 잘릴 수 있으므로 export별 검수 필요.",
                "SNS 트렌드형 효과는 원본 보존용 edit와 분리한다.",
            ],
            "confidence": "platform-trend-informed. 세부 규격은 플랫폼 변경 가능성이 있어 주기 재검증 필요.",
        }

    if tag == "ai_authenticity_guardrail":
        return {
            "situation": "AI 제거/보정/향상 기능을 쓰되, 인물의 특징이나 장면 신뢰성을 해치지 않으려는 경우.",
            "steps": [
                "먼저 기본 색·노출·크롭을 정리하고, AI 제거는 마지막 단계에서 작은 방해물만 대상으로 한다.",
                "얼굴 윤곽, 눈썹, 머리카락 방향처럼 정체성을 바꾸는 수정은 피한다.",
                "Before/After를 100% 확대해 구조가 바뀐 부분이 없는지 확인한다.",
                "게시물/상업용/커뮤니티 공유에서는 생성형 수정 여부를 명확히 적는다.",
            ],
            "settings": [
                "Skin Texture: -5~-15 이내로 약하게",
                "Remove/Generative erase: 작은 먼지·쓰레기·배경 방해물 중심",
                "Sharpening/AI enhance: 얼굴보다 의상/배경 디테일에 제한적으로",
                "Export: 원본/AI수정본 파일명을 분리",
            ],
            "edit": [
                "Subject mask로 얼굴 노출만 소폭 보정하고 피부색은 HSL Orange/Red로 따로 보호한다.",
                "배경 제거 흔적은 Grain +5~+10 또는 약한 Texture 조정으로 이질감을 줄인다.",
            ],
            "caution": [
                "커뮤니티에서는 AI처럼 보이는 과보정 자체가 신뢰도를 떨어뜨릴 수 있다.",
                "인물 특징을 바꾸는 생성형 보정은 추천 시스템에서 risk/constraint로 분리한다.",
            ],
            "confidence": "community-observed guardrail. 윤리/표기 기준은 플랫폼·용도별로 달라질 수 있음.",
        }

    if tag == "raw_sensor_pro_mode":
        return {
            "situation": "스마트폰 자동 처리보다 자연스러운 색/계조와 Lightroom 후보정 여지를 우선하는 장면.",
            "steps": [
                "RAW+JPEG 또는 ProRAW/Expert RAW/DNG를 켜고 같은 장면을 자동 JPEG와 비교한다.",
                "하이라이트가 날아가지 않게 노출을 살짝 낮춰 촬영한다.",
                "큰 센서/고해상도 모드는 저장공간과 처리시간을 고려해 중요한 컷에만 쓴다.",
                "SNS 즉시 업로드용 JPEG와 보관/보정용 RAW를 분리한다.",
            ],
            "settings": [
                "Format: RAW+JPEG / ProRAW / Expert RAW / DNG",
                "EV: -0.3~-1.0 시작",
                "ISO: 가능한 낮게, 셔터는 흔들림 없는 선에서 확보",
                "WB: 혼합광이면 Auto 촬영 후 RAW에서 조정",
            ],
            "edit": [
                "WB → Exposure → Highlights/Shadows → Curve → Color Mix → Mask 순서.",
                "Noise Reduction은 디테일을 죽이지 않게 Color NR부터 확인.",
                "SNS export 전에는 선명도보다 피부/하늘 banding을 먼저 점검.",
            ],
            "caution": [
                "RAW도 제조사 처리의 영향을 받을 수 있으므로 완전한 무가공으로 가정하지 않는다.",
                "어두운 RAW를 무리하게 밝히면 JPEG보다 노이즈가 커질 수 있다.",
            ],
            "confidence": "source-supported + enthusiast-community consensus.",
        }

    if tag == "film_grain_nostalgia":
        return {
            "situation": "완벽한 선명함보다 2010s/필름/워시드 감성으로 SNS photo dump 분위기를 만들고 싶은 장면.",
            "steps": [
                "원본을 먼저 노출/수평/화이트밸런스 기준으로 정상화한다.",
                "Tone Curve black point를 살짝 올려 matte 기반을 만든다.",
                "Grain은 전체 강도보다 크기/거칠기를 함께 조절해 작은 화면에서도 지저분하지 않게 한다.",
                "캐러셀 전체에 같은 grain/curve 기준을 적용하되, 피부 클로즈업은 강도를 낮춘다.",
            ],
            "settings": [
                "Contrast -10~+10",
                "Highlights -15~-40, Shadows +5~+25",
                "Grain +10~+35 시작",
                "Saturation -5~-15 또는 Vibrance +0~+10",
            ],
            "edit": [
                "Color Grading: highlights warm 약하게, shadows green/cool 약하게.",
                "피부는 Texture -5~-10, 배경은 Texture +5~+15로 분리.",
            ],
            "caution": [
                "노이즈가 이미 많은 저조도 사진에 grain을 더하면 지저분해 보일 수 있다.",
                "레트로 필터는 의도적 스타일일 때만 강하게 쓴다.",
            ],
            "confidence": "trend/community-observed. 수치값은 Lightroom Mobile 시작점.",
        }

    # Default: Lightroom/community color guardrail.
    return {
        "situation": "새 SNS/커뮤니티 사진 기법 신호를 기존 추천 그래프에 넣기 전, 안전한 스마트폰 촬영·보정 시작점으로 변환하는 경우.",
        "steps": [
            "출처가 실제 촬영/보정 절차를 담고 있는지 확인하고, 장비 홍보만 있는 글은 제외한다.",
            "원본 촬영에서는 초점/노출/수평을 먼저 확보한다.",
            "보정은 전체 필터보다 Subject/Sky/Background mask로 분리 적용한다.",
            "SNS 트렌드형 강한 효과는 50~70% 강도로 먼저 테스트한다.",
        ],
        "settings": [
            "EV: -0.3~+0.3 기본, 하이라이트 장면은 -1.0까지",
            "Crop: 피드 4:5, 스토리/숏폼 9:16 별도",
            "Color: WB 먼저, HSL은 피부/하늘/배경 분리",
            "Grain/Clarity: 스타일 목적일 때만 제한적으로",
        ],
        "edit": [
            "Exposure → WB → Highlights/Shadows → Mask → Color Mix 순서.",
            "과한 saturation/banding/AI 느낌은 community guardrail로 기록한다.",
        ],
        "caution": [
            "기사/커뮤니티 댓글의 표현을 원문 그대로 길게 저장하지 않는다.",
            "중복 URL·유사 제목은 raw에 새로 만들지 않는다.",
        ],
        "confidence": "source-observed signal transformed into a conservative starter recipe.",
    }


def bullets(items: Iterable[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_tip(cand: Candidate, index: int) -> str:
    recipe = recipe_for(cand)
    ktitle = derive_korean_title(cand)
    cue = source_cue(cand)
    published = cand.published_at or "unknown"
    tags = ", ".join(cand.tags) if cand.tags else "general_mobile_photo_signal"
    return f"""### Tip {index}. {ktitle}

**확인한 신호**
- Source: {cand.source_name} / `{cand.source_kind}`
- 출처 제목: {cand.title}
- 발행/수집 시각: {published}
- 관련 태그: {tags}
- 짧은 근거 cue: {cue}

**상황**
- {recipe['situation']}

**촬영/작업 순서**
{bullets(recipe['steps'])}

**추천 시작값 / 조작값**
{bullets(recipe['settings'])}

**보정 루틴**
{bullets(recipe['edit'])}

**주의할 점**
{bullets(recipe['caution'])}

**확실성:** {recipe['confidence']}
**근거:** {cand.source_name}에서 확인한 최신 항목과 연결 URL. 원문 전문은 복사하지 않고, 추천 시스템용 실전 시작값으로 재정리했다.
"""


def render_markdown(selected: list[Candidate], run_at: dt.datetime, stats: dict) -> tuple[str, str, str]:
    date = run_at.date().isoformat()
    clock = run_at.strftime("%Y-%m-%d %H:%M %Z")
    top_slug = slugify(selected[0].title if selected else "hourly")
    filename = f"{run_at.strftime('%Y-%m-%d-%H%M')}-{top_slug}.md"
    path = HOURLY_DIR / filename
    title = f"Hourly SNS/Community Photo Technique Sweep — {clock}"
    urls = [c.canonical_url for c in selected]
    tags = sorted({tag for c in selected for tag in c.tags} | {"SNS트렌드", "커뮤니티기법", "스마트폰사진", "LightroomMobile"})
    lead = derive_korean_title(selected[0]) if selected else "새 고유 항목 없음"

    source_items = "\n".join(
        f"  - source: \"{quote_safe(c.source_name)}\"\n"
        f"    kind: \"{quote_safe(c.source_kind)}\"\n"
        f"    title: \"{quote_safe(c.title)}\"\n"
        f"    published_at: \"{quote_safe(c.published_at or 'unknown')}\"\n"
        f"    url: \"{quote_safe(c.canonical_url)}\""
        for c in selected
    )

    md = f"""---
title: "{quote_safe(title)}"
category: "hourly"
priority: "B"
updated_at: "{date}"
collected_at: "{run_at.isoformat(timespec='seconds')}"
content_type: "actionable_tip_cards"
collection_mode: "internet_surfing_hourly"
dedupe_policy: "skip existing raw URLs and near-duplicate title fingerprints"
practical_tags:
{yaml_list(tags, 2)}
urls:
{yaml_list(urls, 2)}
source_items:
{source_items}
---

# {title}

이 파일은 매시간 수집되는 `raw/hourly/` 증분 데이터다. 기존 `raw/**/*.md`와 `raw/manifests/sources.csv`의 URL/제목 fingerprint를 확인해 중복 항목은 만들지 않는다.  
원문 전문을 복사하지 않고, 인터넷에서 확인한 최신 SNS·커뮤니티·전문 매체 신호를 기존 raw 폴더의 `actionable_tip_cards` 형식으로 재작성한다.

## 수집/중복 점검 요약

- 후보 pool: {stats.get('pool', 0)}개
- 기존 raw와 중복으로 제외: {stats.get('duplicates', 0)}개
- 관련도 점수 미달로 제외: {stats.get('low_score', 0)}개
- 이번 파일에 저장: {len(selected)}개

## 바로 쓰는 팁 카드

{chr(10).join(render_tip(c, i + 1) for i, c in enumerate(selected))}

## Graphify 추출 힌트

```yaml
entities:
{chr(10).join(f'  - trend_signal:{tag}' for tag in tags[:12])}
relationships:
  - hourly_source SUPPORTS recommendation_variant
  - community_feedback CONSTRAINS overediting_risk
  - sns_trend ADJUSTS crop_and_style
recommendation_modes:
  - trend
  - general
  - personalized
```

## 출처

{chr(10).join(f'- {c.canonical_url}' for c in selected)}

> 수집 원칙: 기존 raw와 겹치는 URL/유사 제목은 건너뛰고, 새 링크·새 관찰만 기록한다. 기사/게시글 전문은 저장하지 않는다.
"""
    return str(path.relative_to(REPO_ROOT)), title, md


def append_sources_csv(file_rel: str, title: str, selected: list[Candidate]) -> None:
    SOURCES_CSV.parent.mkdir(parents=True, exist_ok=True)
    exists = SOURCES_CSV.exists()
    fieldnames = ["category", "priority", "title", "content_type", "tip_card_count", "lead_tip", "file", "primary_url", "all_urls"]
    existing_files = set()
    if exists:
        try:
            with SOURCES_CSV.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row.get("file"):
                        existing_files.add(row["file"])
        except Exception:
            pass
    if file_rel in existing_files:
        return
    with SOURCES_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not exists or SOURCES_CSV.stat().st_size == 0:
            writer.writeheader()
        writer.writerow({
            "category": "hourly",
            "priority": "B",
            "title": title,
            "content_type": "actionable_tip_cards",
            "tip_card_count": str(len(selected)),
            "lead_tip": derive_korean_title(selected[0]) if selected else "새 고유 항목 없음",
            "file": file_rel,
            "primary_url": selected[0].canonical_url if selected else "",
            "all_urls": "; ".join(c.canonical_url for c in selected),
        })


def append_source_matrix(file_rel: str, title: str, selected: list[Candidate], run_at: dt.datetime) -> None:
    if not SOURCE_MATRIX.exists():
        return
    text = SOURCE_MATRIX.read_text(encoding="utf-8")
    marker = "## Hourly incremental internet sources"
    if marker not in text:
        text = text.rstrip() + f"\n\n{marker}\n\n| Collected at | Category | Priority | Source | 대표 팁 상황 | File | URL |\n|---|---|---|---|---|---|---|\n"
    row = (
        f"| {run_at.isoformat(timespec='minutes')} | hourly | B | {title.replace('|', '/')} | "
        f"{derive_korean_title(selected[0]).replace('|', '/')} | `{file_rel}` | {selected[0].canonical_url if selected else ''} |\n"
    )
    if file_rel not in text:
        text += row
        SOURCE_MATRIX.write_text(text, encoding="utf-8")


def update_readme_once() -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    marker = "## 시간 단위 증분 수집 — raw/hourly"
    if marker in text:
        return
    addition = f"""

{marker}

- 자동 수집 스크립트: `scripts/collect_hourly_raw.py`
- 저장 위치: `raw/hourly/YYYY-MM-DD-HHMM-*.md`
- 실행 주기: launchd 설정 시 1시간마다 실행
- 중복 방지: 기존 `raw/**/*.md`, `raw/manifests/sources.csv`, `raw/manifests/hourly_collection_state.json`의 URL과 제목 fingerprint를 기준으로 이미 수집된 항목을 건너뜀
- 원칙: 인터넷에서 새로 확인한 SNS/커뮤니티/전문 매체 신호만 추가하고, 기존 raw를 짜깁기하지 않음. 원문 전문은 복사하지 않고 출처 URL과 한국어 실전 팁 카드로 요약함.
"""
    README.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def run(max_items: int, min_score: int, dry_run: bool = False) -> int:
    HOURLY_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()
    existing_urls, existing_fps = existing_signatures(state)
    pool = build_candidate_pool()
    selected, stats = select_candidates(pool, max_items, min_score, existing_urls, existing_fps)
    run_at = now_local()

    state.setdefault("seen_urls", [])
    state.setdefault("seen_title_fingerprints", [])
    state.setdefault("runs", [])
    state["last_run_at"] = run_at.isoformat(timespec="seconds")
    state["last_stats"] = stats

    if not selected:
        state["runs"].append({"run_at": state["last_run_at"], "created_file": None, "stats": stats})
        state["runs"] = state["runs"][-200:]
        if not dry_run:
            save_state(state)
        print(json.dumps({"created": None, "stats": stats}, ensure_ascii=False, indent=2))
        return 0

    file_rel, title, md = render_markdown(selected, run_at, stats)
    target = REPO_ROOT / file_rel
    if dry_run:
        print(md)
        return 0

    target.write_text(md, encoding="utf-8")
    append_sources_csv(file_rel, title, selected)
    append_source_matrix(file_rel, title, selected, run_at)
    update_readme_once()

    for cand in selected:
        if cand.canonical_url not in state["seen_urls"]:
            state["seen_urls"].append(cand.canonical_url)
        fp = cand.fingerprint
        if fp and fp not in state["seen_title_fingerprints"]:
            state["seen_title_fingerprints"].append(fp)
    # Keep state compact while preserving enough history for dedupe.
    state["seen_urls"] = state["seen_urls"][-5000:]
    state["seen_title_fingerprints"] = state["seen_title_fingerprints"][-5000:]
    state["runs"].append({
        "run_at": state["last_run_at"],
        "created_file": file_rel,
        "selected": [{**dataclasses.asdict(c), "fetched_text": ""} for c in selected],
        "stats": stats,
    })
    state["runs"] = state["runs"][-200:]
    save_state(state)

    print(json.dumps({"created": file_rel, "stats": stats, "urls": [c.canonical_url for c in selected]}, ensure_ascii=False, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Collect new hourly raw markdown for SNS/community smartphone photography techniques.")
    parser.add_argument("--max-items", type=int, default=int(os.environ.get("RAW_COLLECTOR_MAX_ITEMS", "3")), help="Maximum source items per hourly markdown file.")
    parser.add_argument("--min-score", type=int, default=int(os.environ.get("RAW_COLLECTOR_MIN_SCORE", "9")), help="Minimum relevance score to write an item.")
    parser.add_argument("--dry-run", action="store_true", help="Print markdown instead of writing files.")
    args = parser.parse_args(argv)
    return run(max_items=max(1, args.max_items), min_score=args.min_score, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
