"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter import ttk

from tkinter.constants import *

from typing import *

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.navigation import NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["TopBar"]


class TopBar(tkinter.Frame):
    """
    A frame widget that contains buttons and labels.

    The TopBar widget contains buttons and labels that are used to navigate
    between different parts of the application.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_service: NavigationHistoryService,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the TopBar class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            unified_manager (UnifiedObjectManager): The unified object manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Initialize a logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed unified object manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Configure the top bar widget's 1st column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the top bar widget's 2nd column to weight 2
        self.grid_columnconfigure(
            index=1,
            weight=2,
        )

        # Configure the top bar widget's 3rd column to weight 1
        self.grid_columnconfigure(
            index=2,
            weight=1,
        )

        # Configure the top bar widget's 1st row to weight 1
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the top bar widget to have an indigo background color
        self.configure(background=Constants.INDIGO["500"])

        # Create the "Left Frame" frame widget
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.INDIGO["500"],
            master=self,
        )

        # Configure the "Left Frame" frame widget's 1st column to weight 0
        left_frame.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the "Left Frame" frame widget's 2nd row to weight 1
        left_frame.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Grid the "Left Frame" frame widget in the top bar widget
        left_frame.grid(
            row=0,
            column=0,
            sticky=NSEW,
        )

        # Create the "Menu Button" button widget
        menu_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.INDIGO["500"],
            command=lambda: self.dispatcher.dispatch(
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=UIBuilder.get_toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                source="topbar",
                target="menu_ui",
            ),
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
                Constants.BOLD,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
            relief=FLAT,
            text="☰",
        )

        # Grid the "Menu Button" button widget in the "Left Frame" frame widget
        menu_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        # Bind the "<Enter>" and "<Leave>" events to the "Menu Button" widget
        menu_button.bind(
            func=lambda e: menu_button.config(background=Constants.INDIGO["100"]),
            sequence="<Enter>",
        )

        menu_button.bind(
            func=lambda e: menu_button.config(background=Constants.INDIGO["500"]),
            sequence="<Leave>",
        )

        #  Create the "Logo Label" label widget
        logo_label: tkinter.Label = UIBuilder.get_label(
            background=Constants.INDIGO["500"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
                Constants.BOLD,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
            text=f"{Constants.APPLICATION_NAME} - Vers. {Constants.APPLICATION_VERSION}",
        )

        # Grid the "Logo Label" label widget in the "Left Frame" frame widget
        logo_label.grid(
            column=1,
            row=0,
            sticky=NSEW,
        )

        navigations: Dict[str, Dict[str, Any]] = {
            "📚 Learning": {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "target": "learning_dashboard_ui",
            },
            "📝 Notes": {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "target": "notes_view_ui",
            },
            "📖 Flashcards": {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "target": "flashcards_view_ui",
            },
            "❓ Questions": {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "target": "questions_view_ui",
            },
            "📋 Stacks": {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "target": "stacks_view_ui",
            },
            "📊 Statistics": {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "target": "statistics_view_ui",
            },
        }

        # Iterate over the navigations and events
        for index, (
            key,
            value,
        ) in enumerate(
            iterable=navigations.items(),
            start=2,
        ):
            # Configure the "Left Frame" frame widget's current column to weight 0
            left_frame.grid_columnconfigure(
                index=index,
                weight=0,
            )

            # Create the "Button" button widget
            button: ttk.Button = UIBuilder.get_button(
                background=Constants.INDIGO["500"],
                command=lambda event=value["event"], target=value[
                    "target"
                ]: self.dispatcher.dispatch(
                    direction="forward",
                    event=event,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    source="topbar",
                    target=target,
                ),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=left_frame,
                relief=FLAT,
                text=key,
            )

            # Grid the "Button" button widget in the "Left Frame" frame widget
            button.grid(
                column=index,
                padx=5,
                pady=5,
                row=0,
            )

            # Bind the "<Enter>" and "<Leave>" events to the "Button" widget
            button.bind(
                func=lambda e, btn=button: btn.config(
                    background=Constants.INDIGO["100"]
                ),
                sequence="<Enter>",
            )

            button.bind(
                func=lambda e, btn=button: btn.config(
                    background=Constants.INDIGO["500"]
                ),
                sequence="<Leave>",
            )

        # Create the "Create Button" button widget
        create_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["500"],
            command=lambda: self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=UIBuilder.get_toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                source="topbar",
                target="create_ui",
            ),
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=self,
            relief=FLAT,
            text="Create",
        )

        # Grid the "Create Button" button widget in the "Left Frame" frame widget
        create_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Bind the "<Enter>" and "<Leave>" events to the "Create Button" widget
        create_button.bind(
            func=lambda e: create_button.config(background=Constants.INDIGO["100"]),
            sequence="<Enter>",
        )

        create_button.bind(
            func=lambda e: create_button.config(background=Constants.BLUE_GREY["500"]),
            sequence="<Leave>",
        )

        # Create the "Right Frame" frame widget
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.INDIGO["500"],
            master=self,
        )

        # Configure the "Right Frame" frame widget's 1st column to weight 1
        right_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Grid the "Right Frame" frame widget in the top bar widget
        right_frame.grid(
            row=0,
            column=2,
            sticky=NSEW,
        )

        # Create the "Search Bar" search bar widget
        search_bar: Dict[str, Any] = UIBuilder.get_searchbar(
            master=right_frame,
            command=lambda value: self.dispatcher.dispatch(
                event=Events.SEARCH_QUERY_CHANGED,
                namespace=Constants.GLOBAL_NAMESPACE,
                value=value,
            ),
        )

        # Configure the "Button" button widget
        search_bar["button"].configure(
            background=Constants.INDIGO["500"],
            command=self.on_searchbar_button_clicked,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the "Entry" entry widget
        search_bar["entry"].configure(
            font=(Constants.DEFAULT_FONT_FAMILIY, Constants.DEFAULT_FONT_SIZE),
        )

        # Grid the "Search Bar" search bar widget in the "Right Frame" frame widget
        search_bar["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the "<Enter>" and "<Leave>" events to the "Button" widget
        search_bar["button"].bind(
            func=lambda e: search_bar["button"].config(
                background=Constants.INDIGO["100"]
            ),
            sequence="<Enter>",
        )

        search_bar["button"].bind(
            func=lambda e: search_bar["button"].config(
                background=Constants.INDIGO["500"]
            ),
            sequence="<Leave>",
        )

        # Bind the "<FocusIn>" and "<FocusOut>" events to the "Entry" widget
        search_bar["entry"].bind(
            func=lambda e: search_bar["entry"].config(background="#E8EAF6"),
            sequence="<FocusIn>",
        )

        search_bar["entry"].bind(
            func=lambda e: search_bar["entry"].config(background=Constants.WHITE),
            sequence="<FocusOut>",
        )

        icons: Dict[str, Any] = {
            "🔔": "notification_ui",
            "❓": "help_ui",
            "⚙": "settings_ui",
            "👤": "user_ui",
        }

        # Iterate over the icons and target
        for index, (
            icon,
            target,
        ) in enumerate(
            iterable=icons.items(),
            start=1,
        ):
            # Configure the column of the "Right Frame" frame widget to weight 1
            right_frame.grid_columnconfigure(
                index=index,
                weight=1,
            )

            # Create the button widget
            button: tkinter.Button = UIBuilder.get_button(
                background=Constants.INDIGO["500"],
                command=lambda: self.dispatcher.dispatch(
                    direction="forward",
                    event=Events.REQUEST_VALIDATE_NAVIGATION,
                    master=UIBuilder.get_toplevel(),
                    namespace=Constants.GLOBAL_NAMESPACE,
                    source="topbar",
                    target=target,
                ),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=right_frame,
                relief=FLAT,
                text=icon,
            )

            # Grid the button widget in the "Right Frame" frame widget
            button.grid(
                column=index,
                padx=5,
                pady=5,
                row=0,
            )

            # Bind the "<Enter>" and "<Leave>" events to the button
            button.bind(
                func=lambda e, btn=button: btn.config(
                    foreground=Constants.INDIGO["100"]
                ),
                sequence="<Enter>",
            )

            button.bind(
                func=lambda e, btn=button: btn.config(foreground=Constants.WHITE),
                sequence="<Leave>",
            )

    def on_searchbar_button_clicked(self) -> None:
        """
        Handles the event when the search button is clicked in the topbar.

        This function is called when the search button is clicked in the topbar.
        It dispatches a navigation request to the global namespace with the target
        "search_ui" and the source "topbar".

        Raises:
            Exception: If an exception occurs while attempting to dispatch the
                navigation request.
        """
        try:
            # Get the root widget
            root: tkinter.Toplevel = UIBuilder.get_toplevel()

            # Configure the root toplevel widget's 0th column to weight 1
            root.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the root toplevel widget's 0th row to weight 1
            root.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Set the toplevel widget's geometry to 1920x1080
            root.wm_geometry(newGeometry="1920x1080")

            # Dispatch the navigation request
            self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=root,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="topbar",
                target="search_ui",
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_searchbar_button_clicked' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
