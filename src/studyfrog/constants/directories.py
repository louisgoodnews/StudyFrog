"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from pathlib import Path
from typing import Final


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "ASSETS_DIR",
    "CONFIG_DIR",
    "DATA_DIR",
    "EXPORTS_DIR",
    "HOME",
    "IMPORTS_DIR",
    "LOGS_DIR",
    "RESOURCES_DIR",
    "TEMP_DIR",
]


# ---------- Constants ---------- #


_CWD: Final[Path] = Path.cwd()

_LOCAL_DIR: Final[Path] = _CWD / ".local"

ASSETS_DIR: Final[Path] = _LOCAL_DIR / "assets"

CONFIG_DIR: Final[Path] = _LOCAL_DIR / "config"

DATA_DIR: Final[Path] = _LOCAL_DIR / "data"

EXPORTS_DIR: Final[Path] = _LOCAL_DIR / "exports"

IMAGES_DIR: Final[Path] = _LOCAL_DIR / "images"

IMPORTS_DIR: Final[Path] = _LOCAL_DIR / "imports"

LOGS_DIR: Final[Path] = _LOCAL_DIR / "logs"

RESOURCES_DIR: Final[Path] = _LOCAL_DIR / "resources"

TEMP_DIR: Final[Path] = _LOCAL_DIR / "temp"

HOME: Final[Path] = Path.home()
