from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _gitdir_target(git_marker: Path) -> Path | None:
    if git_marker.is_dir():
        return git_marker.resolve()
    if not git_marker.is_file():
        return None

    text = git_marker.read_text().strip()
    prefix = "gitdir:"
    if not text.startswith(prefix):
        return None

    raw_target = text[len(prefix) :].strip()
    if not raw_target:
        return None
    return (git_marker.parent / raw_target).resolve()


def _common_root_from_gitdir(gitdir: Path) -> Path | None:
    parts = gitdir.parts
    try:
        index = parts.index(".git")
    except ValueError:
        return None
    return Path(*parts[:index]).resolve()


def resolve_state_root(start: Path, fallback: Path) -> Path:
    for candidate in (start, *start.parents):
        git_marker = candidate / ".git"
        if git_marker.is_dir():
            return candidate.resolve()

        gitdir = _gitdir_target(git_marker)
        if gitdir is None:
            continue

        common_root = _common_root_from_gitdir(gitdir)
        if common_root is not None:
            return common_root
        return candidate.resolve()

    return fallback.resolve()


SOURCE_ROOT = Path(__file__).resolve().parents[2]
STATE_ROOT = resolve_state_root(Path.cwd().resolve(), SOURCE_ROOT)
ROOT = SOURCE_ROOT
SWATCH_SNAPSHOT_PATH = SOURCE_ROOT / "data" / "margaret2_swatches.json"
EVAL_DB_PATH = STATE_ROOT / ".local" / "evals.sqlite"

TAGLINE = "pick a colour. hue's is better."


@dataclass(frozen=True)
class Settings:
    app_name: str
    swatch_snapshot_path: Path
    eval_db_path: Path


def load_settings() -> Settings:
    env_paths = (STATE_ROOT / ".env", SOURCE_ROOT / ".env")
    seen: set[Path] = set()
    for env_path in env_paths:
        if env_path in seen:
            continue
        load_dotenv(env_path, override=False)
        seen.add(env_path)
    return Settings(
        app_name="Huemiliator",
        swatch_snapshot_path=SWATCH_SNAPSHOT_PATH,
        eval_db_path=EVAL_DB_PATH,
    )
