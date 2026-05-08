from huemiliator.config import load_settings


def test_load_settings_points_to_repo_swatch_snapshot_path() -> None:
    settings = load_settings()
    assert settings.app_name == "Huemiliator"
    assert settings.swatch_snapshot_path.name == "margaret2_swatches.json"
    assert settings.swatch_snapshot_path.exists()
    assert settings.eval_db_path.name == "evals.sqlite"
    assert settings.eval_db_path.parent.name == ".local"
