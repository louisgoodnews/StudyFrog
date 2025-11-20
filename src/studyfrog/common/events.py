"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal


# ---------- Events ---------- #

APPLICATION_STARTED: Final[Literal["application_started"]] = "application_started"

APPLICATION_STARTING: Final[Literal["application_starting"]] = "application_starting"

APPLICATION_STOPPED: Final[Literal["application_stopped"]] = "application_stopped"

APPLICATION_STOPPING: Final[Literal["application_stopping"]] = "application_stopping"


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    name for name in globals() if not name.startswith("_") and name.isidentifier()
]
