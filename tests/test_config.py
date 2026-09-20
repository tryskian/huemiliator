from pathlib import Path

import pytest

import huemiliator.config as config
from huemiliator.config import load_settings, resolve_state_root


def test_load_settings_points_to_repo_swatch_snapshot_path() -> None:
    settings = load_settings()
    assert settings.app_name == "Huemiliator"
    assert settings.swatch_snapshot_path.name == "margaret2_swatches.json"
    assert settings.swatch_snapshot_path.exists()
    assert settings.eval_db_path.name == "evals.sqlite"
    assert settings.eval_db_path.parent.name == ".local"


def test_config_stays_structural_only() -> None:
    assert not hasattr(config, "TAGLINE")
    assert not hasattr(config, "RUNTIME_CONTRACT_LINES")
    assert not hasattr(config, "ORACLE_INSTRUCTIONS")


@pytest.mark.parametrize("model", ["gpt-5.6-luna", "another-model", "", "  "])
def test_model_setting_respects_environment_and_blank_default(
    model: str, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(config, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(config, "SOURCE_ROOT", tmp_path)
    monkeypatch.setenv("HUEMILIATOR_MODEL", model)
    assert load_settings().model == (model.strip() or "gpt-5.6-luna")


@pytest.mark.parametrize("effort", ["medium", "low", "max", "", "  "])
def test_reasoning_setting_respects_environment_and_blank_default(
    effort: str, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(config, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(config, "SOURCE_ROOT", tmp_path)
    monkeypatch.setenv("HUEMILIATOR_REASONING_EFFORT", effort)
    assert load_settings().reasoning_effort == (effort.strip() or "medium")


@pytest.mark.parametrize("verbosity", ["low", "medium", "high", "", "  "])
def test_verbosity_setting_respects_environment_and_blank_default(
    verbosity: str, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(config, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(config, "SOURCE_ROOT", tmp_path)
    monkeypatch.setenv("HUEMILIATOR_VERBOSITY", verbosity)
    assert load_settings().verbosity == (verbosity.strip() or "low")


@pytest.mark.parametrize("top_p", ["0", "1", "0.7", "", "  "])
def test_top_p_setting_respects_environment_and_blank_default(
    top_p: str, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(config, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(config, "SOURCE_ROOT", tmp_path)
    monkeypatch.setenv("HUEMILIATOR_TOP_P", top_p)
    assert load_settings().top_p == (float(top_p) if top_p.strip() else 0.98)


def test_malformed_top_p_reports_the_setting(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(config, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(config, "SOURCE_ROOT", tmp_path)
    monkeypatch.setenv("HUEMILIATOR_TOP_P", "not-a-number")
    with pytest.raises(ValueError, match="HUEMILIATOR_TOP_P"):
        load_settings()


def test_model_loads_from_local_env_with_process_precedence(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(config, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(config, "SOURCE_ROOT", tmp_path)
    monkeypatch.delenv("HUEMILIATOR_MODEL", raising=False)
    monkeypatch.delenv("HUEMILIATOR_REASONING_EFFORT", raising=False)
    monkeypatch.delenv("HUEMILIATOR_VERBOSITY", raising=False)
    monkeypatch.delenv("HUEMILIATOR_TOP_P", raising=False)
    (tmp_path / ".env").write_text(
        "HUEMILIATOR_MODEL=file-model\nHUEMILIATOR_REASONING_EFFORT=low\n"
        "HUEMILIATOR_VERBOSITY=high\nHUEMILIATOR_TOP_P=0.8\n"
    )
    assert load_settings().model == "file-model"
    assert load_settings().reasoning_effort == "low"
    assert load_settings().verbosity == "high"
    assert load_settings().top_p == 0.8
    monkeypatch.setenv("HUEMILIATOR_MODEL", "process-model")
    monkeypatch.setenv("HUEMILIATOR_REASONING_EFFORT", "high")
    monkeypatch.setenv("HUEMILIATOR_VERBOSITY", "medium")
    monkeypatch.setenv("HUEMILIATOR_TOP_P", "0.6")
    assert load_settings().model == "process-model"
    assert load_settings().reasoning_effort == "high"
    assert load_settings().verbosity == "medium"
    assert load_settings().top_p == 0.6


def test_resolve_state_root_uses_checkout_root_when_git_dir_exists(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "repo"
    (repo_root / ".git").mkdir(parents=True)
    nested = repo_root / "docs" / "runtime"
    nested.mkdir(parents=True)
    fallback = tmp_path / "fallback"

    assert resolve_state_root(nested, fallback) == repo_root


def test_resolve_state_root_uses_common_root_for_git_worktree(
    tmp_path: Path,
) -> None:
    common_root = tmp_path / "canonical-repo"
    git_worktree_dir = common_root / ".git" / "worktrees" / "sample-worktree"
    git_worktree_dir.mkdir(parents=True)

    worktree_root = tmp_path / "worktree"
    worktree_root.mkdir()
    (worktree_root / ".git").write_text(f"gitdir: {git_worktree_dir}\n")

    nested = worktree_root / "src"
    nested.mkdir()
    fallback = tmp_path / "fallback"

    assert resolve_state_root(nested, fallback) == common_root


def test_resolve_state_root_falls_back_when_no_git_marker_exists(
    tmp_path: Path,
) -> None:
    fallback = tmp_path / "fallback"
    nested = tmp_path / "plain" / "nested"
    nested.mkdir(parents=True)

    assert resolve_state_root(nested, fallback) == fallback
