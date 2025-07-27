"""Configuration management for the application."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from . import __application_binary__


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    """Load configuration from YAML file.

    Args:
        config_path: Optional path to config file. If None, searches for config.yaml
                    in current directory and user home directory.

    Returns:
        Configuration dictionary.
    """
    config: dict[str, Any] = {}

    if config_path:
        config_file = Path(config_path)
        if config_file.exists():
            with config_file.open(encoding="utf-8") as f:
                config.update(yaml.safe_load(f) or {})
        return config

    # Search for config files in order of preference
    config_locations = [
        Path("config.yaml"),
        Path(f"~/.{__application_binary__}.yaml").expanduser(),
        Path("config.yaml.example"),
    ]

    for config_file in config_locations:
        if config_file.exists():
            with config_file.open(encoding="utf-8") as f:
                loaded_config = yaml.safe_load(f) or {}
                config.update(loaded_config)
            break

    return config


def save_config(config: dict[str, Any], config_path: str | Path = "config.yaml") -> None:
    """Save configuration to YAML file.

    Args:
        config: Configuration dictionary to save.
        config_path: Path to save config file to.
    """
    config_file = Path(config_path)
    with config_file.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
