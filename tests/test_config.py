from pathlib import Path

from huemiliator.config import load_settings, resolve_state_root


def test_load_settings_points_to_repo_swatch_snapshot_path() -> None:
    settings = load_settings()
    assert settings.app_name == "Huemiliator"
    assert settings.swatch_snapshot_path.name == "margaret2_swatches.json"
    assert settings.swatch_snapshot_path.exists()
    assert settings.eval_db_path.name == "evals.sqlite"
    assert settings.eval_db_path.parent.name == ".local"


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
