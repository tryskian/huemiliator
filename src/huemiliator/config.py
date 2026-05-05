from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]

TAGLINE = "pick a colour. hue's is better."


@dataclass(frozen=True)
class Settings:
    app_name: str
    pantone_dataset_path: Path


def load_settings() -> Settings:
    load_dotenv(ROOT / ".env", override=False)
    return Settings(
        app_name="Huemiliator",
        pantone_dataset_path=ROOT / "data" / "pantone_colours.json",
    )
