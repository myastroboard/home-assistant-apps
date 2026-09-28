#!/usr/bin/env python3
"""Bump each app to its latest upstream release.

For every ``<app>/config.yaml`` in the repository:

1. read ``version:``, ``url:`` (upstream GitHub repo), ``image:`` (Docker Hub)
   and ``arch:``;
2. list the upstream GitHub releases newer than ``version:`` (drafts and
   pre-releases ignored);
3. check the newest one is on Docker Hub for every declared arch - the upstream
   release workflow publishes the image before the GitHub release, but the app
   must never point at a tag users cannot pull;
4. rewrite ``version:`` and prepend each new release's notes, taken from the
   upstream ``CHANGELOG.md`` at that tag, to the app's ``CHANGELOG.md``.

Standard library only. ``GITHUB_TOKEN`` is used when set (API rate limit).
Writes ``changed`` and ``message`` to ``$GITHUB_OUTPUT`` when running in
GitHub Actions.

    python scripts/update_apps.py            # update files in place
    python scripts/update_apps.py --dry-run  # only report
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Home Assistant arch name -> Docker platform architecture.
DOCKER_ARCH = {"amd64": "amd64", "aarch64": "arm64", "armv7": "arm", "armhf": "arm", "i386": "386"}

SEMVER = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")


def _request(url: str, accept: str = "application/json") -> bytes:
    headers = {"Accept": accept, "User-Agent": "myastroboard-home-assistant-apps"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as resp:
        return resp.read()


def _parse_version(text: str) -> tuple[int, int, int] | None:
    match = SEMVER.match(text.strip())
    return (int(match[1]), int(match[2]), int(match[3])) if match else None


def read_config(path: Path) -> dict:
    """Pull the few scalar/list fields we need without a YAML dependency."""
    text = path.read_text(encoding="utf-8")

    def scalar(key: str) -> str:
        match = re.search(rf"^{key}:\s*[\"']?([^\"'\n#]+?)[\"']?\s*(?:#.*)?$", text, re.M)
        if not match:
            raise ValueError(f"{path}: missing '{key}:'")
        return match[1].strip()

    arch_block = re.search(r"^arch:\s*\n((?:\s+-\s*\S+\s*\n?)+)", text, re.M)
    arches = re.findall(r"-\s*(\S+)", arch_block[1]) if arch_block else []
    repo = re.match(r"https://github\.com/([^/\s]+/[^/\s]+?)/?$", scalar("url"))
    if not repo:
        raise ValueError(f"{path}: 'url:' must be a https://github.com/<owner>/<repo> URL")
    return {
        "text": text,
        "version": scalar("version"),
        "image": scalar("image"),
        "repo": repo[1],
        "arch": arches,
    }


def newer_releases(repo: str, current: tuple[int, int, int]) -> list[tuple[tuple[int, int, int], str]]:
    """(version, tag) of published, non-prerelease releases newer than current, oldest first."""
    releases = json.loads(_request(f"https://api.github.com/repos/{repo}/releases?per_page=30"))
    found = []
    for rel in releases:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        parsed = _parse_version(rel.get("tag_name", ""))
        if parsed and parsed > current:
            found.append((parsed, rel["tag_name"]))
    return sorted(found)


def missing_arches(image: str, version: str, arches: list[str]) -> list[str]:
    """Declared arches that the Docker Hub tag does not provide (all of them if the tag is absent)."""
    try:
        data = json.loads(_request(f"https://hub.docker.com/v2/repositories/{image}/tags/{version}"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return list(arches)
        raise
    available = {img.get("architecture") for img in data.get("images", [])}
    return [a for a in arches if DOCKER_ARCH.get(a, a) not in available]


def release_notes(repo: str, tag: str, version: str) -> str:
    """The version's section of the upstream CHANGELOG.md at that tag.

    Upstream files the ``[Unreleased]`` section under a version heading only after
    the release (via a PR), so at the tag the notes are usually still under
    ``## [Unreleased]``. Both heading styles are accepted: ``## 1.6.3 (date)`` and
    ``## [0.4.2] - date``.
    """
    url = f"https://raw.githubusercontent.com/{repo}/{tag}/CHANGELOG.md"
    try:
        text = _request(url, accept="text/plain").decode("utf-8")
    except urllib.error.HTTPError:
        text = ""

    section = ""
    for heading in (rf"\[?{re.escape(version)}\]?", r"\[Unreleased\]"):
        match = re.search(rf"^## {heading}[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
        if match and match[1].strip():
            section = match[1]
            break

    # Drop empty subsections and "- None." placeholders.
    parts = re.split(r"(?m)^(### .+)$", section)
    blocks = []
    for i in range(1, len(parts), 2):
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if body and body != "- None.":
            blocks.append(f"{parts[i].strip()}\n\n{body}")
    notes = "\n\n".join(blocks) if blocks else section.strip()

    # Relative links in the upstream changelog would be dead in Home Assistant.
    notes = re.sub(
        r"\]\((?!https?:|mailto:|#)([^)\s]+)\)",
        lambda m: f"](https://github.com/{repo}/blob/{tag}/{m[1].lstrip('./')})",
        notes,
    )
    link = f"https://github.com/{repo}/releases/tag/{tag}"
    return f"{notes}\n\nRelease notes: <{link}>" if notes else f"Release notes: <{link}>"


def prepend_changelog(path: Path, entries: list[str]) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Changelog\n"
    header, _, rest = existing.partition("\n")
    new = "\n\n".join(entries)
    path.write_text(f"{header}\n\n{new}\n\n{rest.lstrip()}".rstrip() + "\n", encoding="utf-8")


def update_app(app_dir: Path, dry_run: bool) -> str | None:
    """Return a short summary when the app was (or would be) bumped."""
    cfg = read_config(app_dir / "config.yaml")
    current = _parse_version(cfg["version"])
    if current is None:
        raise ValueError(f"{app_dir.name}: version '{cfg['version']}' is not X.Y.Z")

    releases = newer_releases(cfg["repo"], current)
    if not releases:
        print(f"{app_dir.name}: {cfg['version']} is up to date")
        return None

    # Newest release whose image is fully published; a newer one still building is
    # picked up on a later run.
    target = None
    for parsed, tag in reversed(releases):
        version = ".".join(map(str, parsed))
        missing = missing_arches(cfg["image"], version, cfg["arch"])
        if not missing:
            target = parsed
            break
        print(f"{app_dir.name}: {version} released but {cfg['image']}:{version} lacks {', '.join(missing)} - skipped")
    if target is None:
        return None

    included = [(p, t) for p, t in releases if p <= target]
    new_version = ".".join(map(str, target))
    print(f"{app_dir.name}: {cfg['version']} -> {new_version}")
    if dry_run:
        return f"{app_dir.name} {new_version}"

    entries = [
        f"## {'.'.join(map(str, p))}\n\n{release_notes(cfg['repo'], t, '.'.join(map(str, p)))}"
        for p, t in reversed(included)
    ]
    text = re.sub(r'^version:.*$', f'version: "{new_version}"', cfg["text"], count=1, flags=re.M)
    (app_dir / "config.yaml").write_text(text, encoding="utf-8")
    prepend_changelog(app_dir / "CHANGELOG.md", entries)
    return f"{app_dir.name} {new_version}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="report only, do not write files")
    args = parser.parse_args()

    bumped, failed = [], False
    for config in sorted(ROOT.glob("*/config.yaml")):
        try:
            summary = update_app(config.parent, args.dry_run)
        except (ValueError, urllib.error.URLError, json.JSONDecodeError) as exc:
            # One broken app must not block the others.
            print(f"::error::{config.parent.name}: {exc}")
            failed = True
            continue
        if summary:
            bumped.append(summary)

    output = os.environ.get("GITHUB_OUTPUT")
    if output and not args.dry_run:
        with open(output, "a", encoding="utf-8") as fh:
            fh.write(f"changed={'true' if bumped else 'false'}\n")
            fh.write(f"message=chore: bump {', '.join(bumped)}\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
