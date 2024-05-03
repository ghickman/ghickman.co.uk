import itertools
import re
import sys
from pathlib import Path

from first import first

image_pat = re.compile(r"\/images\/")
path_pat = re.compile(r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<name>.*)$")

old_content = Path("content.bak")
new_content = Path("content/posts")

header_template = """
---
date: {date}T00:00:00+00:00
draft: {draft}
title: {title}
tags:{tags}
aliases:{aliases}
---
"""


def get_header(header_lines: list[str], name: str) -> str:
    header = first(header_lines, key=lambda line: line.lower().strip().startswith(name))

    if header is None:
        return ""

    _, _, content = header.partition(" ")
    return content


def get_status(header_lines: list[str]) -> str:
    raw = get_header(header_lines, "status").lower()

    match raw:
        case "published":
            return "false"
        case "draft":
            return "true"
        case _:
            return "false"


def get_tags(header_lines: list[str]) -> str:
    raw = get_header(header_lines, "tags")

    if not raw:
        return ""

    tags = raw.split(", ")
    tags = [f" - {tag}" for tag in tags]

    return "\n" + "\n".join(tags)


def get_title(header_lines: list[str]) -> str:
    raw = get_header(header_lines, "title")

    if ":" not in raw:
        return raw

    return f'"{raw}"'


for path in old_content.glob("*.md"):
    lines = iter(path.read_text().split("\n"))
    header_lines = list(itertools.takewhile(lambda line: line not in ["", "\n"], lines))
    title = get_title(header_lines)
    status = get_status(header_lines)
    tags = get_tags(header_lines)

    if not (match := path_pat.match(path.stem)):
        print(f"WHAT: {path}")
        sys.exit(1)

    year = match.group("year")
    month = match.group("month")
    day = match.group("day")
    name = match.group("name")

    alias = f"\n - /{year}/{month}/{day}/{name}"
    date = f"{year}-{month}-{day}"

    header = header_template.format(
        date=date,
        draft=status,
        title=title,
        tags=tags,
        aliases=alias,
    ).strip()

    updated = "\n".join([header, *lines])
    has_images = bool(image_pat.search(updated))

    if not has_images:
        new_path = (new_content / path.stem).with_suffix(".md")
        new_path.write_text(updated)
        continue

    directory = new_content / path.stem
    directory.mkdir(exist_ok=True)
    (directory / "index.md").write_text(updated)
