"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter import ttk

from tkinter.constants import *

from typing import *

from ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger


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
    ) -> None:
        """
        Initializes a new instance of the TopBar class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Initialize a logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

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
        self.configure(background="#3F51B5")

        # Create the "Left Frame" frame widget
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background="#3F51B5",
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
            background="#3F51B5",
            command=self.dispatcher.dispatch(
                event=Events.MENU_BUTTON_CLICKED,
                namespace=Constants.GLOBAL_NAMESPACE,
            ),
            font=(
                "Roboto",
                16,
                "bold",
            ),
            foreground="#FFFFFF",
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
            func=lambda e: menu_button.config(background="#C5CAE9"),
            sequence="<Enter>",
        )

        menu_button.bind(
            func=lambda e: menu_button.config(background="#3F51B5"),
            sequence="<Leave>",
        )

        #  Create the "Logo Label" label widget
        logo_label: tkinter.Label = UIBuilder.get_label(
            background="#3F51B5",
            font=(
                "Roboto",
                18,
                "bold",
            ),
            foreground="#FFFFFF",
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
                "event": Events.REQUEST_FORWARD_NAVIGATION,
                "target": "LearningDashboard",
            },
            "📝 Notes": {
                "event": Events.REQUEST_FORWARD_NAVIGATION,
                "target": "NotesView",
            },
            "📖 Flashcards": {
                "event": Events.REQUEST_FORWARD_NAVIGATION,
                "target": "FlashcardsView",
            },
            "❓ Questions": {
                "event": Events.REQUEST_FORWARD_NAVIGATION,
                "target": "QuestionsView",
            },
            "📋 Stacks": {
                "event": Events.REQUEST_FORWARD_NAVIGATION,
                "target": "StacksView",
            },
            "📊 Statistics": {
                "event": Events.REQUEST_FORWARD_NAVIGATION,
                "target": "StatisticsView",
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
                background="#3F51B5",
                command=lambda event=value["event"], target=value[
                    "target"
                ]: self.dispatcher.dispatch(
                    event=event,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    target=target,
                ),
                font=(
                    "Roboto",
                    14,
                ),
                foreground="#FFFFFF",
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
                func=lambda e, btn=button: btn.config(background="#C5CAE9"),
                sequence="<Enter>",
            )

            button.bind(
                func=lambda e, btn=button: btn.config(background="#3F51B5"),
                sequence="<Leave>",
            )

        # Create the "Create Button" button widget
        create_button: tkinter.Button = UIBuilder.get_button(
            background="#3F51B5",
            command=lambda: self.dispatcher.dispatch(
                event=Events.CREATE_BUTTON_CLICKED,
                namespace=Constants.GLOBAL_NAMESPACE,
            ),
            font=(
                "Roboto",
                16,
            ),
            foreground="#FFFFFF",
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
            func=lambda e: create_button.config(background="#C5CAE9"),
            sequence="<Enter>",
        )

        create_button.bind(
            func=lambda e: create_button.config(background="#3F51B5"),
            sequence="<Leave>",
        )

        # Create the "Right Frame" frame widget
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background="#3F51B5",
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
            background="#3F51B5",
            font=(
                "Roboto",
                16,
            ),
            foreground="#FFFFFF",
            relief=FLAT,
        )

        # Configure the "Entry" entry widget
        search_bar["entry"].configure(
            font=(
                "Roboto",
                16,
            ),
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
            func=lambda e: search_bar["button"].config(background="#C5CAE9"),
            sequence="<Enter>",
        )

        search_bar["button"].bind(
            func=lambda e: search_bar["button"].config(background="#3F51B5"),
            sequence="<Leave>",
        )

        # Bind the "<FocusIn>" and "<FocusOut>" events to the "Entry" widget
        search_bar["entry"].bind(
            func=lambda e: search_bar["entry"].config(background="#E8EAF6"),
            sequence="<FocusIn>",
        )

        search_bar["entry"].bind(
            func=lambda e: search_bar["entry"].config(background="#FFFFFF"),
            sequence="<FocusOut>",
        )

        icons: Dict[str, Any] = {
            "🔔": Events.NOTIFICATIONS_BUTTON_CLICKED,
            "❓": Events.HELP_BUTTON_CLICKED,
            "⚙": Events.SETTINGS_BUTTON_CLICKED,
            "👤": Events.USER_BUTTON_CLICKED,
        }

        # Iterate over the icons and events
        for index, (
            icon,
            event,
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
                background="#3F51B5",
                command=lambda: self.dispatcher.dispatch(
                    event=event,
                    namespace=Constants.GLOBAL_NAMESPACE,
                ),
                font=(
                    "Roboto",
                    16,
                ),
                foreground="#FFFFFF",
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
                func=lambda e, btn=button: btn.config(foreground="#C5CAE9"),
                sequence="<Enter>",
            )

            button.bind(
                func=lambda e, btn=button: btn.config(foreground="#FFFFFF"),
                sequence="<Leave>",
            )
