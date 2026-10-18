#!/usr/bin/env python3
"""Check member pages and data/publications.yaml for common mistakes.

Run from the repository root: python3 scripts/check_content.py
Exits non-zero if any errors are found; warnings are printed but don't fail.
"""

import datetime
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEMBERS = ROOT / "content" / "members"
PUBLICATIONS = ROOT / "data" / "publications.yaml"

MAX_PHOTO_KB = 1024
PHOTO_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
STATUSES = {"current", "alumni"}
LINK_KEYS = {"github", "scholar", "orcid", "website"}
ANCHORS = {"Center", "Top", "Bottom", "Left", "Right", "TopLeft", "TopRight", "BottomLeft", "BottomRight", "Smart"}

errors: list[str] = []
warnings: list[str] = []


def rel(path: pathlib.Path) -> str:
    return str(path.relative_to(ROOT))


def front_matter(path: pathlib.Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{rel(path)}: must start with a '---' front matter block")
        return None
    try:
        _, block, _ = text.split("---", 2)
        data = yaml.safe_load(block) or {}
    except (ValueError, yaml.YAMLError) as exc:
        errors.append(f"{rel(path)}: could not read front matter: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{rel(path)}: front matter must be 'key: value' pairs")
        return None
    return data


def check_members() -> None:
    for stray in MEMBERS.glob("*.md"):
        if stray.name != "_index.md":
            errors.append(f"{rel(stray)}: members need their own folder, e.g. "
                          f"content/members/{stray.stem}/index.md")

    for folder in sorted(p for p in MEMBERS.iterdir() if p.is_dir()):
        page = folder / "index.md"
        if not page.exists():
            errors.append(f"{rel(folder)}: missing index.md")
            continue
        fm = front_matter(page)
        if fm is None:
            continue
        where = rel(page)

        if not str(fm.get("title") or "").strip():
            errors.append(f"{where}: 'title' (the person's name) is required")
        if not str(fm.get("role") or "").strip():
            warnings.append(f"{where}: 'role' is empty")

        status = fm.get("status", "current")
        if status not in STATUSES:
            errors.append(f"{where}: 'status' must be one of {sorted(STATUSES)}, not {status!r}")
        if status == "alumni" and not fm.get("end"):
            errors.append(f"{where}: alumni need an 'end' year")

        for key in ("start", "end"):
            value = fm.get(key)
            if value not in (None, "") and not (isinstance(value, int) and 1990 <= value <= 2100):
                errors.append(f"{where}: '{key}' should be a year like 2024, not {value!r}")

        if (anchor := fm.get("photo_anchor")) and anchor not in ANCHORS:
            errors.append(f"{where}: 'photo_anchor' must be one of {sorted(ANCHORS)}")

        links = fm.get("links") or {}
        if not isinstance(links, dict):
            errors.append(f"{where}: 'links' must be key: value pairs")
            links = {}
        for key, url in links.items():
            if key not in LINK_KEYS:
                errors.append(f"{where}: unknown link '{key}' (allowed: {sorted(LINK_KEYS)})")
            elif url and not str(url).startswith(("https://", "http://")):
                errors.append(f"{where}: link '{key}' should be a full URL starting with https://")

        if (email := fm.get("email")) and "@" not in str(email):
            errors.append(f"{where}: 'email' doesn't look like an email address")

        photos = [p for p in folder.iterdir() if p.stem == "photo"]
        for photo in photos:
            if photo.suffix.lower() not in PHOTO_TYPES:
                errors.append(f"{rel(photo)}: photo must be one of {sorted(PHOTO_TYPES)}")
            size_kb = photo.stat().st_size / 1024
            if size_kb > MAX_PHOTO_KB:
                errors.append(f"{rel(photo)}: {size_kb:.0f} KB is too large; "
                              f"please resize to under {MAX_PHOTO_KB} KB (about 800x800 px is plenty)")
        if len(photos) > 1:
            errors.append(f"{rel(folder)}: more than one photo.* file")
        other_images = [p for p in folder.iterdir()
                        if p.suffix.lower() in PHOTO_TYPES and p.stem != "photo"]
        for img in other_images:
            warnings.append(f"{rel(img)}: not used; the profile photo must be named photo{img.suffix}")


def check_publications() -> None:
    if not PUBLICATIONS.exists():
        return
    where = rel(PUBLICATIONS)
    try:
        pubs = yaml.safe_load(PUBLICATIONS.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as exc:
        errors.append(f"{where}: invalid YAML: {exc}")
        return
    if not isinstance(pubs, list):
        errors.append(f"{where}: must be a list of entries, each starting with '- title:'")
        return

    this_year = datetime.date.today().year
    seen_dois: set[str] = set()
    for i, pub in enumerate(pubs, start=1):
        label = f"{where}: entry {i}"
        if not isinstance(pub, dict):
            errors.append(f"{label}: must be key: value pairs")
            continue
        if title := str(pub.get("title") or "").strip():
            label += f" ({title[:40]!r})"
        else:
            errors.append(f"{label}: 'title' is required")

        authors = pub.get("authors")
        if not isinstance(authors, list) or not authors or not all(isinstance(a, str) and a.strip() for a in authors):
            errors.append(f"{label}: 'authors' must be a list of names, e.g. [\"Jane Doe\", \"John Smith\"]")

        year = pub.get("year")
        if not isinstance(year, int) or not 1990 <= year <= this_year + 1:
            errors.append(f"{label}: 'year' must be a year like {this_year}, not {year!r}")

        doi = str(pub.get("doi") or "").strip()
        if doi:
            if doi.startswith(("http", "doi:")):
                errors.append(f"{label}: give just the DOI (10.xxxx/...), without https://doi.org/ or doi:")
            elif not doi.startswith("10."):
                errors.append(f"{label}: DOI should start with '10.'")
            elif doi.lower() in seen_dois:
                errors.append(f"{label}: duplicate DOI {doi}")
            seen_dois.add(doi.lower())

        arxiv = str(pub.get("arxiv") or "").strip()
        if arxiv.lower().startswith(("http", "arxiv:")):
            errors.append(f"{label}: give just the arXiv ID (e.g. 2301.01234), without a URL or 'arXiv:'")

        if (url := pub.get("url")) and not str(url).startswith(("https://", "http://")):
            errors.append(f"{label}: 'url' should start with https://")


def main() -> int:
    check_members()
    check_publications()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        print(f"\n{len(errors)} problem(s) found.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
