#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_SOURCE_DIR = Path("/Users/leejeongmin/Desktop/Obsidian/Second Brain/KBO datas")
DEFAULT_ROOT_CATEGORY = "KBO Data"
DEFAULT_LAYOUT = "single"


@dataclass
class Note:
    front_matter: dict[str, object]
    body: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync KBO notes from an Obsidian vault into this Jekyll blog."
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help=f"Obsidian source directory (default: {DEFAULT_SOURCE_DIR})",
    )
    parser.add_argument(
        "--root-category",
        default=DEFAULT_ROOT_CATEGORY,
        help=f"Top-level Jekyll category (default: {DEFAULT_ROOT_CATEGORY})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files.",
    )
    return parser.parse_args()


def parse_note(raw_text: str) -> Note:
    if not raw_text.startswith("---\n"):
        return Note(front_matter={}, body=raw_text)

    parts = raw_text.split("\n---\n", 1)
    if len(parts) != 2:
        return Note(front_matter={}, body=raw_text)

    _, rest = parts
    front_matter_block = raw_text[4 : len(raw_text) - len(rest) - 5]
    front_matter = parse_simple_yaml(front_matter_block)
    return Note(front_matter=front_matter, body=rest)


def parse_simple_yaml(block: str) -> dict[str, object]:
    data: dict[str, object] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        key, sep, value = line.partition(":")
        if not sep:
            i += 1
            continue

        key = key.strip()
        value = value.strip()

        if not value:
            items: list[str] = []
            i += 1
            while i < len(lines):
                nested = lines[i]
                stripped = nested.strip()
                if stripped.startswith("- "):
                    items.append(stripped[2:].strip())
                    i += 1
                    continue
                if not stripped:
                    i += 1
                    continue
                break
            data[key] = items
            continue

        data[key] = strip_quotes(value)
        i += 1

    return data


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def clean_folder_name(name: str) -> str:
    return re.sub(r"^\d+\.\s*", "", name).strip()


def build_categories(source_dir: Path, note_path: Path, root_category: str) -> list[str]:
    relative_parent = note_path.relative_to(source_dir).parent
    categories = [root_category]
    if relative_parent != Path("."):
        categories.extend(clean_folder_name(part) for part in relative_parent.parts)
    return categories


def serialize_front_matter(note: Note, categories: list[str], source_dir: Path, note_path: Path) -> str:
    front_matter = note.front_matter
    title = str(front_matter.get("title") or derive_title(note_path))
    date_value = str(front_matter.get("date") or derive_date(note_path))
    tags = front_matter.get("tags") if isinstance(front_matter.get("tags"), list) else []
    excerpt = front_matter.get("excerpt")
    relative_source = note_path.relative_to(source_dir).as_posix()

    lines = [
        "---",
        f"layout: {DEFAULT_LAYOUT}",
        f'title: "{escape_quotes(title)}"',
        f"date: {date_value}",
        "categories:",
    ]

    for category in categories:
        lines.append(f"  - {category}")

    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {tag}")

    if excerpt:
        lines.append(f'excerpt: "{escape_quotes(str(excerpt))}"')

    lines.extend(
        [
            "comments: true",
            "share: false",
            f'source_path: "{escape_quotes(relative_source)}"',
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def escape_quotes(value: str) -> str:
    return value.replace('"', '\\"')


def derive_title(note_path: Path) -> str:
    return note_path.stem


def derive_date(note_path: Path) -> str:
    matched = re.match(r"(\d{4}-\d{2}-\d{2})", note_path.name)
    if matched:
        return f"{matched.group(1)} 09:00:00 +0900"
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S +0900")


def build_target_filename(note_path: Path) -> str:
    matched = re.match(r"^(\d{4}-\d{2}-\d{2})(.*?)(\.[^.]+)$", note_path.name)
    if not matched:
        return note_path.name

    date_prefix, raw_slug, extension = matched.groups()
    slug = raw_slug.lstrip("-_ ")
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")

    if not slug:
        return note_path.name

    return f"{date_prefix}-{slug}{extension}"


def sync_note(source_dir: Path, target_dir: Path, note_path: Path, root_category: str, dry_run: bool) -> str:
    raw_text = note_path.read_text(encoding="utf-8")
    note = parse_note(raw_text)
    categories = build_categories(source_dir, note_path, root_category)
    front_matter = serialize_front_matter(note, categories, source_dir, note_path)
    body = note.body.lstrip("\n")
    output = front_matter + body
    target_path = target_dir / build_target_filename(note_path)
    legacy_target_path = target_dir / note_path.name

    current = target_path.read_text(encoding="utf-8") if target_path.exists() else None
    if current == output:
        return f"unchanged  {target_path.relative_to(target_dir.parent)}"

    action = "update" if target_path.exists() else "create"
    if not dry_run:
        target_path.write_text(output, encoding="utf-8")
        if legacy_target_path != target_path and legacy_target_path.exists():
            legacy_target_path.unlink()
    return f"{action:<9} {target_path.relative_to(target_dir.parent)}"


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir.expanduser().resolve()
    repo_root = Path(__file__).resolve().parent.parent
    target_dir = repo_root / "_posts"

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}", file=sys.stderr)
        return 1

    note_paths = sorted(source_dir.rglob("*.md"))
    if not note_paths:
        print(f"No markdown files found in: {source_dir}", file=sys.stderr)
        return 1

    for note_path in note_paths:
        print(sync_note(source_dir, target_dir, note_path, args.root_category, args.dry_run))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
