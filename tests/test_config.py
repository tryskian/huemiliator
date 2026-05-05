from huemiliator.config import load_settings


def test_load_settings_points_to_repo_dataset_path() -> None:
    settings = load_settings()
    assert settings.app_name == "Huemiliator"
    assert settings.pantone_dataset_path.name == "pantone_colours.json"
