from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
SWATCH_SNAPSHOT_PATH = ROOT / "data" / "margaret2_swatches.json"
EVAL_DB_PATH = ROOT / ".local" / "evals.sqlite"

TAGLINE = "pick a colour. hue's is better."


@dataclass(frozen=True)
class Settings:
    app_name: str
    swatch_snapshot_path: Path
    eval_db_path: Path


def load_settings() -> Settings:
    load_dotenv(ROOT / ".env", override=False)
    return Settings(
        app_name="Huemiliator",
        swatch_snapshot_path=SWATCH_SNAPSHOT_PATH,
        eval_db_path=EVAL_DB_PATH,
    )
