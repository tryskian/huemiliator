from __future__ import annotations

LOSS_LINE_BANK: dict[str, str] = {
    "neutral": "you brought beige energy.",
    "brown": "earthy is not the same as intentional.",
    "red": "the idea was right. the nerve was missing.",
    "orange": "warmth alone does not save you.",
    "yellow": "pale panic is not confidence.",
    "green": "close. still too timid.",
    "blue": "blue was right. yours just wasn't.",
    "purple": "dramatic, but undercommitted.",
    "pink": "cute. not convincing.",
}


def loss_line_for_family(family: str) -> str:
    try:
        return LOSS_LINE_BANK[family]
    except KeyError as exc:
        raise ValueError(f"Unknown family for loss line: {family!r}") from exc
