"""
Author: lodego
Date: 2025-02-09
"""

import tkinter

import uuid

from tkinter.constants import *

from typing import *

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger
from utils.navigation import NavigationItem, NavigationService


__all__: List[str] = ["SettingUI"]


class SettingUI(tkinter.Frame):
    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_item: NavigationItem,
        navigation_service: NavigationService,
    ) -> None:

        # Call the parent class constructor
        super().__init__(master=master)
