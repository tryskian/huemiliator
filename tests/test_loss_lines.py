from __future__ import annotations

import pytest

from huemiliator.loss_lines import loss_line_for_family


def test_loss_line_for_family_returns_fixed_line() -> None:
    assert loss_line_for_family("blue") == "blue was right. yours just wasn't."


def test_loss_line_for_family_rejects_unknown_family() -> None:
    with pytest.raises(ValueError, match="Unknown family"):
        loss_line_for_family("chartreuse")
