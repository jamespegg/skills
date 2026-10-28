#!/usr/bin/env python3
"""Version and package all skills together, using only the Python standard library."""

import argparse
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\Z")
FRONTMATTER = re.compile(r"\A---\r?\n(?P<header>.*?)\r?\n---\r?\n", re.DOTALL)
VERSION = re.compile(
    r"^(?P<prefix>  version:[ \t]*)(?P<quote>['\"]?)(?P<old>\d+\.\d+\.\d+)(?P=quote)[ \t]*$",
    re.MULTILINE,
)
NAME = re.compile(r"^name:[ \t]*(?P<name>[a-z0-9-]+)[ \t]*$", re.MULTILINE)


def skills_in(root: Path) -> list[Path]:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        raise ValueError("Missing skills/ directory")
    skills = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skills:
        raise ValueError("No skills found")
    for skill in skills:
        if skill.is_symlink() or not (skill / "SKILL.md").is_file():
            raise ValueError(f"Invalid skill directory: {skill}")
    return skills


def versioned_content(skill: Path, version: str) -> str:
    content = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = FRONTMATTER.match(content)
    if not match:
        raise ValueError(f"Missing YAML frontmatter: {skill}")
    header = match.group("header")
    names = list(NAME.finditer(header))
    versions = list(VERSION.finditer(header))
    if len(names) != 1 or names[0].group("name") != skill.name:
        raise ValueError(f"Skill name must match directory: {skill}")
    if len(versions) != 1 or not re.search(r"^metadata:[ \t]*$", header, re.MULTILINE):
        raise ValueError(f"Expected exactly one metadata.version: {skill}")
    updated = VERSION.sub(
        lambda m: f'{m.group("prefix")}{m.group("quote")}{version}{m.group("quote")}',
        header,
        count=1,
    )
    return content[: match.start("header")] + updated + content[match.end("header") :]


def stage_release(root: Path, version: str, output: Path) -> list[Path]:
    """Validate all skills, then rewrite their metadata and build root-level ZIPs."""
    if not SEMVER.fullmatch(version):
        raise ValueError(f"Invalid release version: {version}")
    skills = skills_in(root)
    updates = {skill / "SKILL.md": versioned_content(skill, version) for skill in skills}

    # Reject symlinks so archives cannot capture files outside an individual skill.
    for skill in skills:
        for path in skill.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Symlinks are not allowed in skill packages: {path}")

    for path, content in updates.items():
        path.write_text(content, encoding="utf-8")

    output.mkdir(parents=True, exist_ok=True)
    archives = []
    for skill in skills:
        archive = output / f"{skill.name}-v{version}.zip"
        with ZipFile(archive, "w", compression=ZIP_DEFLATED) as zipped:
            for path in sorted(p for p in skill.rglob("*") if p.is_file()):
                # The archive root is the skill's content, not an enclosing folder.
                entry = ZipInfo(path.relative_to(skill).as_posix(), (1980, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                zipped.writestr(entry, path.read_bytes())
        with ZipFile(archive) as verified:
            if "SKILL.md" not in verified.namelist() or verified.testzip() is not None:
                raise ValueError(f"Invalid archive: {archive}")
        archives.append(archive)
    return archives


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Release version, without v prefix")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    for archive in stage_release(args.root, args.version, args.output):
        print(f"Prepared {archive}")


if __name__ == "__main__":
    main()
