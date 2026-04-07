from __future__ import annotations

# Import all exported variables and functions from individual modules

# Application functions
from studyfrog.core.application import (
    run_post_start_tasks,
    run_post_stop_tasks,
    run_pre_start_tasks,
    run_pre_stop_tasks,
    start_application,
    stop_application,
)

# Bootstrap functions
from studyfrog.core.bootstrap import (
    initialize_gui,
    subscribe_to_events,
    unsubscribe_from_events,
)

# Common functions
from studyfrog.core.common import (
    get_default_difficulties,
    get_default_priorities,
    get_default_user,
)

# Core module (empty, but included for completeness)
from studyfrog.core.core import *

# Export all functions and variables
__all__: list[str] = [
    # Application functions
    "run_post_start_tasks",
    "run_post_stop_tasks",
    "run_pre_start_tasks",
    "run_pre_stop_tasks",
    "start_application",
    "stop_application",
    # Bootstrap functions
    "initialize_gui",
    "subscribe_to_events",
    "unsubscribe_from_events",
    # Common functions
    "get_default_difficulties",
    "get_default_priorities",
    "get_default_user",
]
