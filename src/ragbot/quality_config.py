from __future__ import annotations

import json
from pathlib import Path
from typing import Any, TypeVar

T = TypeVar("T")


def load_json_config(path: str | Path, default: T) -> T:
    config_path = Path(path)
    if not config_path.exists():
        return default
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default
    if isinstance(default, dict) and isinstance(data, dict):
        return data  # type: ignore[return-value]
    if isinstance(default, list) and isinstance(data, list):
        return data  # type: ignore[return-value]
    return default


def string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]
