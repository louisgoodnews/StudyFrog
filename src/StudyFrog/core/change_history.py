"""
Author: lodego
Date: 2025-02-06
"""

import uuid

from datetime import datetime

from typing import *

from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: List[str] = [
    "ChangeHistory",
    "ChangeHistoryConverter",
    "ChangeHistoryFactory",
    "ChangeHistoryManager",
    "ChangeHistoryModel",
    "ChangeHistoryItem",
    "ChangeHistoryItemConverter",
    "ChangeHistoryItemFactory",
    "ChangeHistoryItemManager",
    "ChangeHistoryItemModel",
]


class ChangeHistory(ImmutableBaseObject):
    pass


class ChangeHistoryConverter:
    pass


class ChangeHistoryFactory:
    pass


class ChangeHistoryManager(BaseObjectManager):
    pass


class ChangeHistoryModel(ImmutableBaseModel):
    pass


class ChangeHistoryItem(ImmutableBaseObject):
    pass


class ChangeHistoryItemConverter:
    pass


class ChangeHistoryItemFactory:
    pass


class ChangeHistoryItemManager(BaseObjectManager):
    pass


class ChangeHistoryItemModel(ImmutableBaseModel):
    pass
