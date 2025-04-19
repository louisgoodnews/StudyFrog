"""
Author: lodego
Date: 2025-04-19
"""

from typing import *

from core.ui.notifications.notifications import ToplevelNotification

from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["ErrorService"]


class ErrorService(ImmutableBaseObject):
    """
    """

    _shared_instance: Optional["ErrorService"] = None

    def __new__(cls) -> "ErrorService":
        """
        """

        if not cls._shared_instance:
            cls._shared_instance = super(ErrorService, cls).__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def __init__(cls) -> None:
        """
        """

        # Call the parent class constructor
        super().__init__()
