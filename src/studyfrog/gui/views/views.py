"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal

from gui.views.create_view import get_create_view
from gui.views.dashboard_view import get_dashboard_view
from gui.views.edit_view import get_edit_view
from utils.utils import log_exception


# ---------- Constants ---------- #

NAME: Final[Literal["gui.views.views"]] = "gui.views.views"


# ---------- Functions ---------- #


def get_view(
    name: Literal["create", "dashboard", "edit"],
    **kwargs,
) -> None:
    """
    Returns the view.

    Args:
        name (Literal["create", "dashboard", "edit"]): The name of the view.
        **kwargs: Keyword arguments to pass to the view.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    try:
        if name == "create":
            return get_create_view(**kwargs)
        elif name == "dashboard":
            return get_dashboard_view(**kwargs)
        elif name == "edit":
            return get_edit_view(**kwargs)
    except Exception as e:
        log_exception(
            exception=e,
            name=f"{NAME}.get_view",
        )
        raise e


# ---------- Auto-Export ---------- #

# Auto-Export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
