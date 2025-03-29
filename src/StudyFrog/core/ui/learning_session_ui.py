"""
Author: lodego
Date: 2025-03-15
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.difficulty import ImmutableDifficulty
from core.priority import ImmutablePriority
from core.setting import SettingService
from core.stack import ImmutableStack, MutableStack

from core.ui.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.learning_session_runner import LearningSessionRunner
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["LearningSessionUI"]


class LearningSessionUI(BaseUI):
    """
    A class representing the learning session user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    learning session UI, including setting up the main frames and populating them with
    respective widgets. It extends the tkinter.Frame class and utilizes various
    utility classes for managing navigation, logging, and other functionalities.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        stacks: List[ImmutableStack],
        unified_manager: UnifiedObjectManager,
        difficulties: Optional[List[ImmutableDifficulty]] = None,
        priorities: Optional[List[ImmutablePriority]] = None,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionUI class.

        Args:
            difficulties (Optional[List[ImmutableDifficulty]]): The list of difficulty instances. Defaults to None.
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            priorities (Optional[List[ImmutablePriority]]): The list of priority instances. Defaults to None.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            stacks (List[ImmutableStack]): The stacks instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_session_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

        # Store the passed difficulty list as an instance variable
        self.difficulties: Optional[List[ImmutableDifficulty]] = difficulties

        # Store the passed priority list as an instance variable
        self.priorities: Optional[List[ImmutablePriority]] = priorities

        # Initialize the learning session runner as an instance variable
        self.runner: LearningSessionRunner = LearningSessionRunner(
            difficulties=difficulties,
            dispatcher=dispatcher,
            priorities=priorities,
            stacks=stacks,
        )

        # Store the passed stacks ImmutableStack list as an instance variable
        self.stacks: List[ImmutableStack] = stacks

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        return subscriptions

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the learning session user interface.

        This method configures the grid of the learning session user interface by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the weight of the 0th column to 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the 1st row to 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the weight of the 2nd row to 0.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the learning session user interface.

        This method creates and configures the main widgets of the learning session user
        interface, setting their layout configuration and invoking methods to populate
        each frame with its respective widgets.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation or configuration of the widgets.
        """
        try:
            # Create the top frame widget
            top_frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Create the center frame widget
            center_frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Create the bottom frame widget
            bottom_frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Place the top frame widget in the main window
            top_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Place the center frame widget in the main window
            center_frame.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Place the bottom frame widget in the main window
            bottom_frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Check if all frames were created successfully
            if not all(
                [
                    top_frame,
                    center_frame,
                    bottom_frame,
                ]
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create frames in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Create and configure the top frame widgets
            self.create_top_frame_widgets(master=top_frame)

            # Create and configure the center frame widgets
            self.create_center_frame_widgets(master=center_frame)

            # Create and configure the bottom frame widgets
            self.create_bottom_frame_widgets(master=bottom_frame)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        learning session UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        try:
            # Configure the bottom frame's 0th column to weight 1
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the bottom frame's 1st column to weight 1
            master.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the bottom frame's 2nd column to weight 1
            master.grid_columnconfigure(
                index=2,
                weight=1,
            )

            # Configure the bottom frame's 0th row to weight 1
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Left Frame" frame widget
            left_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=master,
            )

            if not left_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create left frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Configure the left frame's 0th column to weight 1
            left_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the left frame's 0th row to weight 1
            left_frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Grid the "Left Frame" frame widget in the bottom frame
            left_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Previous Button" button widget
            self.previous_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=lambda: self.on_navigation_button_click(direction="previous"),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=left_frame,
                relief=FLAT,
                text="Previous",
                width=15,
            )

            if not self.previous_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create previous button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the "Previous Button" button widget in the left frame
            self.previous_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
            )

            # Create the "Center Frame" frame widget
            center_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=master,
            )

            if not center_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create center frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the "Center Frame" frame widget in the bottom frame
            center_frame.grid(
                column=1,
                row=0,
                sticky=NSEW,
            )

            # Configure the weight of the 0th column to 1.
            center_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 1st column to 1.
            center_frame.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the weight of the 2nd column to 1.
            center_frame.grid_columnconfigure(
                index=2,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            center_frame.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Create the "Easy Button" button widget
            self.easy_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.GREEN["700"],
                command=lambda: self.on_difficulty_button_click(difficulty="easy"),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=center_frame,
                relief=FLAT,
                text="Easy",
                width=15,
            )

            if not self.easy_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create easy button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the "Easy Button" button widget in the center frame
            self.easy_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
            )

            # Create the "Medium Button" button widget
            self.medium_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.ORANGE["700"],
                command=lambda: self.on_difficulty_button_click(difficulty="medium"),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=center_frame,
                relief=FLAT,
                text="Medium",
                width=15,
            )

            if not self.medium_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create medium button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the "Medium Button" button widget in the center frame
            self.medium_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
            )

            # Create the "Hard Button" button widget
            self.hard_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.RED["700"],
                command=lambda: self.on_difficulty_button_click(difficulty="hard"),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=center_frame,
                relief=FLAT,
                text="Hard",
                width=15,
            )

            if not self.hard_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create hard button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the "Hard Button" button widget in the center frame
            self.hard_button.grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
            )

            # Create the "Right Frame" frame widget
            right_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=master,
            )

            if not right_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create right frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Configure the weight of the 0th column to 1.
            right_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            right_frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Grid the "Right Frame" frame widget in the bottom frame
            right_frame.grid(
                column=2,
                row=0,
                sticky=NSEW,
            )

            # Create the "Next Button" button widget
            self.next_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=lambda: self.on_navigation_button_click(direction="next"),
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=right_frame,
                relief=FLAT,
                text="Next",
                width=15,
            )

            if not self.next_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create next button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the "Next Button" button widget in the right frame
            self.next_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_bottom_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_center_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 1st column to 0.
            master.grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            label: Optional[tkinter.Label] = UIBuilder.get_label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                text="You are currently viewing item x of X.",
            )

            if not label:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create label in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the label widget in the top frame
            label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            options_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=self.on_options_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Options",
            )

            if not options_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create options button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the options button widget in the top frame
            options_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_top_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_difficulty_button_click(
        self,
        difficulty: Literal[
            "easy",
            "medium",
            "hard",
        ],
    ) -> None:
        pass

    def on_navigation_button_click(
        self,
        direction: Literal[
            "next",
            "previous",
        ],
    ) -> None:
        pass

    def on_options_button_click(self) -> None:
        pass

    def toggle_difficulty_buttons(
        self,
        difficultly: Optional[Literal["easy", "medium", "hard"]] = None,
    ) -> None:
        pass

    def toggle_navigation_buttons(
        self,
        direction: Optional[Literal["next", "previouis"]] = None,
    ) -> None:
        pass
