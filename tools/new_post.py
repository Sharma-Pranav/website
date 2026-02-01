from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


POSTS_START = "<!-- POSTS:START -->"
POSTS_END = "<!-- POSTS:END -->"


def slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s).strip("-")
    return s


def ensure_blog_index_has_markers(index_path: Path) -> None:
    if not index_path.exists():
        raise FileNotFoundError(f"Missing blog index: {index_path}")
    text = index_path.read_text(encoding="utf-8")
    if POSTS_START not in text or POSTS_END not in text:
        raise ValueError(
            f"Missing markers in {index_path}. Add:\n{POSTS_START}\n{POSTS_END}"
        )


def insert_post_link(index_path: Path, link_line: str) -> None:
    text = index_path.read_text(encoding="utf-8")

    # Extract block between markers
    pattern = re.compile(
        re.escape(POSTS_START) + r"(.*?)" + re.escape(POSTS_END),
        flags=re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        raise ValueError("Could not find POSTS markers block.")

    block = m.group(1).strip("\n")

    # Avoid duplicates
    lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
    if link_line in lines:
        return

    # Prepend newest
    new_lines = [link_line] + lines
    new_block = "\n" + "\n".join(new_lines) + "\n"

    new_text = pattern.sub(POSTS_START + new_block + POSTS_END, text)
    index_path.write_text(new_text, encoding="utf-8")


def build_front_matter(
    date_str: str,
    draft: bool,
    categories: list[str],
    tags: list[str],
) -> str:
    fm = ["---", f"draft: {str(draft).lower()}", f"date: {date_str}"]
    if categories:
        fm.append("categories:")
        fm.extend([f"  - {c}" for c in categories])
    if tags:
        fm.append("tags:")
        fm.extend([f"  - {t}" for t in tags])
    fm.append("---")
    return "\n".join(fm)


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a new blog post + update index.")
    ap.add_argument("title", help="Post title")
    ap.add_argument("--category", action="append", default=["Notes"], help="Repeatable")
    ap.add_argument("--tag", action="append", default=[], help="Repeatable")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="YYYY-MM-DD")
    ap.add_argument("--draft", action=argparse.BooleanOptionalAction, default=True)
    args = ap.parse_args()

    title: str = args.title
    date_str: str = args.date
    slug = slugify(title)

    # Paths
    repo_root = Path.cwd()
    posts_dir = repo_root / "docs" / "blog" / "posts"
    index_path = repo_root / "docs" / "blog" / "index.md"
    post_filename = f"{date_str}-{slug}.md"
    post_path = posts_dir / post_filename

    # Ensure dirs
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Create post file (don't overwrite)
    if post_path.exists():
        raise FileExistsError(f"Post already exists: {post_path}")

    fm = build_front_matter(
        date_str=date_str,
        draft=bool(args.draft),
        categories=list(args.category or []),
        tags=list(args.tag or []),
    )

    template = f"""{fm}

# {title}

Hook paragraph (2–4 sentences).

<!-- more -->

## Context
## What I built
## Evidence
## Links
- Demo:
- Repo:
"""

    post_path.write_text(template, encoding="utf-8")

    # Update index
    ensure_blog_index_has_markers(index_path)
    rel_link = f"posts/{post_filename}"
    link_line = f"- **{date_str}** — [{title}]({rel_link})"
    insert_post_link(index_path, link_line)

    print(f"Created: {post_path.as_posix()}")
    print(f"Updated: {index_path.as_posix()}")


if __name__ == "__main__":
    main()
