"""
Author: lodego
Date: 2025-03-15
"""

import tkinter

from tkinter import ttk
from tkinter.constants import *

from typing import *

from core.answer import ImmutableAnswer
from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion
from core.setting import SettingService
from core.stack import ImmutableStack

from core.ui.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder
from core.ui.view.flashcard_learning_view import FlashcardLearningView
from core.ui.view.note_learning_view import NoteLearningView
from core.ui.view.question_learning_view import QuestionLearningView

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
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
        mode: str,
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

        # Initialize a list to store bindings
        self.bindings: Final[List[str]] = []

        # Initialize the current learning view as an empty instance variable
        self.current_learning_view: Optional[
            Literal["flashcard", "note", "question"]
        ] = None

        # Store the passed difficulty list as an instance variable
        self.difficulties: Optional[List[ImmutableDifficulty]] = difficulties

        # Initialize the flashcard learning view as an empty instance variable
        self.flashcard_learning_view: Optional[FlashcardLearningView] = None

        # Initialize the note learning view as an empty instance variable
        self.note_learning_view: Optional[NoteLearningView] = None

        # Store the passed priority list as an instance variable
        self.priorities: Optional[List[ImmutablePriority]] = priorities

        # Initialize the question learning view as an empty instance variable
        self.question_learning_view: Optional[QuestionLearningView] = None

        # Store the passed stacks ImmutableStack list as an instance variable
        self.stacks: List[ImmutableStack] = stacks

        # Load the learning session runner
        self.load_learning_session_runner()

        # Bind the left and right arrow keys to the back and forward navigation methods
        self.bind_keys()

    def bind_keys(self) -> None:
        """
        Binds the left and right arrow keys to the back and forward navigation methods.

        This method binds the left arrow key to the back navigation method and the right arrow key to the forward navigation method.

        Returns:
            None
        """

        # Bind the left arrow key to the back navigation method
        self.bindings.append(
            self.bind_all(
                func=lambda event: self.on_navigation_button_click(
                    direction="previous"
                ),
                sequence="<Left>",
            )
        )

        # Bind the right arrow key to the forward navigation method
        self.bindings.append(
            self.bind_all(
                func=lambda event: self.on_navigation_button_click(direction="next"),
                sequence="<Right>",
            )
        )

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

        subscriptions.extend(
            [
                {
                    "event": Events.NOTIFY_LEARNING_SESSION_RUNNER_LOADED,
                    "function": self.on_learning_session_runner_loaded,
                    "namespace": Constants.LEARNING_SESSION_NAMESPACE,
                    "persistent": True,
                }
            ]
        )

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

    def clear(self) -> None:
        """
        Clears the learning session user interface.

        This method clears the learning session user interface by hiding all widgets.

        Returns:
            None
        """

        # Get the list of children widgets in the center frame
        children: Optional[List[tkinter.Misc]] = self.center_frame.winfo_children()

        # Check if there are any children widgets
        if not children:
            # Return early if there are no children widgets
            return

        # Iterate over the children widgets
        for child in children:
            # Remove the child widget from the grid
            child.grid_forget()

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
            top_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            if not top_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create top frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the top frame widget in the main window
            top_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the center frame widget
            self.center_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            if not self.center_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create center frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the center frame widget in the main window
            self.center_frame.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Create the bottom frame widget
            bottom_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            if not bottom_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create bottom frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the bottom frame widget in the main window
            bottom_frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create and configure the top frame widgets
            self.create_top_frame_widgets(master=top_frame)

            # Create and configure the center frame widgets
            self.create_center_frame_widgets(master=self.center_frame)

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
                    Constants.DEFAULT_FONT_FAMILY,
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
                    Constants.DEFAULT_FONT_FAMILY,
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
                    Constants.DEFAULT_FONT_FAMILY,
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
                    Constants.DEFAULT_FONT_FAMILY,
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
                    Constants.DEFAULT_FONT_FAMILY,
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

            # Configure the weight of the 2nd column to 0.
            master.grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the weight of the 3rd column to 0.
            master.grid_columnconfigure(
                index=3,
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
                    Constants.DEFAULT_FONT_FAMILY,
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

            # Create an IntVar to store the progress value
            self.progress_var: Optional[tkinter.IntVar] = UIBuilder.get_int_variable()

            if not self.progress_var:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create int variable in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Get the style
            style: Optional[ttk.Style] = UIBuilder.get_style(master=master)

            if not style:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create style in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Use the clam theme
            style.theme_use(themename="clam")

            # Configure the style of the progressbar
            style.configure(
                "StudyFrog.Horizontal.TProgressbar",
                troughcolor=Constants.BLUE_GREY["700"],
                background=Constants.BLUE_GREY["500"],
                thickness=20,
                bordercolor=Constants.BLUE_GREY["700"],
                lightcolor=Constants.BLUE_GREY["500"],
                darkcolor=Constants.BLUE_GREY["500"],
            )

            # Create the progressbar widget
            self.progressbar: Optional[ttk.Progressbar] = UIBuilder.get_progressbar(
                master=master,
                orient=HORIZONTAL,
                style="StudyFrog.Horizontal.TProgressbar",
                variable=self.progress_var,
            )

            if not self.progressbar:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create progressbar in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Grid the progressbar widget in the top frame
            self.progressbar.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Get the options button widget
            options_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=self.on_options_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
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
                column=3,
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

    @override
    def destroy(self) -> None:
        """
        Cleans up resources and unsubscribes from events.

        This method unsubscribes from all events and calls the parent class's destroy method to clean
        up resources. Logs any exceptions that occur.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the destroy process.
        """
        try:
            # Unbind the left and right arrow keys from the back and forward navigation methods
            self.unbind_keys()

            # Call the parent class's destroy method
            super().destroy()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'destroy' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def handle_loaded_content(
        self,
        content: Union[
            ImmutableFlashcard,
            ImmutableNote,
            Tuple[ImmutableQuestion, List[ImmutableAnswer]],
        ],
    ) -> None:
        """
        Handles the loaded content by determining the appropriate learning view to load.

        This method takes the loaded content as an argument, processes it, and loads the
        appropriate learning view based on the type of content received. If the content
        is not supported, a warning message is logged. If an exception occurs, it is
        re-raised to the caller.

        Args:
            content (Union[ImmutableFlashcard, ImmutableNote, Tuple[ImmutableQuestion, List[ImmutableAnswer]]]): The loaded content.

        Raises:
            Exception: If an exception occurs while attempting to handle the loaded content.
        """
        try:
            # Process the result
            if isinstance(
                content,
                ImmutableFlashcard,
            ):
                # Load the flashcard learning view
                self.load_learning_view(
                    content=content,
                    name="flashcard",
                )
            elif isinstance(
                content,
                ImmutableNote,
            ):
                # Load the note learning view
                self.load_learning_view(
                    content=content,
                    name="note",
                )
            elif isinstance(content, tuple) and len(content) == 2:
                (
                    question,
                    answers,
                ) = content
                if isinstance(
                    question,
                    ImmutableQuestion,
                ) and isinstance(
                    answers,
                    list,
                ):
                    self.load_learning_view(content=content, name="question")
            else:
                # Log a warning message
                self.logger.warning(
                    message=f"Unsupported content type ({type(content)}) in '{self.__class__.__name__}'. This is likely due to a type not being implemented."
                )

            # Toggle the navigation buttons
            self.toggle_navigation_buttons()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_loaded_content' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def load_learning_view(
        self,
        content: Union[
            ImmutableFlashcard,
            ImmutableNote,
            Tuple[ImmutableQuestion, List[ImmutableAnswer]],
        ],
        name: Literal["flashcard", "note", "question"],
    ) -> None:
        """
        Loads a learning view in the center frame of the learning session UI.

        This method uses the specified name to determine which learning view to
        load. It then dispatches an event to load the content into the loaded
        learning view.

        Args:
            content (Union[ImmutableFlashcard, ImmutableNote, Tuple[ImmutableQuestion, List[ImmutableAnswer]]]):
                The content to be loaded into the learning view.
            name (Literal["flashcard", "note", "question"]): The name of the
                learning view to load. Can be either "flashcard", "note", or
                "question".
        """
        try:
            # Dispatch the event to load the difficulty
            difficulty_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_DIFFICULTY_LOAD,
                    field="id",
                    namespace=Constants.GLOBAL_NAMESPACE,
                    value=(
                        content.difficulty
                        if isinstance(
                            content,
                            (
                                ImmutableFlashcard,
                                ImmutableNote,
                            ),
                        )
                        else content[0].difficulty
                    ),
                )
            )

            if not difficulty_notification:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to load difficulty in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Toggle(reset) the difficulty buttons
                self.toggle_difficulty_buttons()
            else:
                # Toggle(reset) the difficulty buttons
                self.toggle_difficulty_buttons(
                    difficulty=difficulty_notification.get_one_and_only_result().name.lower(),
                )

            # Update the widgets in the learning session ui
            self.update_idletasks()

            # Determine the event to dispatch based on the specified name
            event: DispatcherEvent

            # Dispatch the event to load the content into the learning view
            if name == "flashcard":
                # Dispatch the event to load the flashcard into the flashcard learning view
                event = Events.REQUEST_FLASHCARD_LEARNING_VIEW_LOAD_FLASHCARD
            elif name == "note":
                # Dispatch the event to load the note into the note learning view
                event = Events.REQUEST_NOTE_LEARNING_VIEW_LOAD_NOTE
            elif name == "question":
                # Dispatch the event to load the question into the question learning view
                event = Events.REQUEST_QUESTION_LEARNING_VIEW_LOAD_QUESTION

            # Check if the current learning view is the same as the specified name
            if self.current_learning_view and self.current_learning_view == name:
                # Dispatch the event to load the content into the learning view
                self.dispatcher.dispatch(
                    event=event,
                    namespace=Constants.LEARNING_SESSION_NAMESPACE,
                    **{f"{name}": content},
                )

                # Return
                return
            else:
                # Clear the center frame before loading the new learning view
                self.clear()

            # Get the learning view attribute using the name
            view_instance: Optional[Any] = getattr(
                self,
                f"{name}_learning_view",
            )

            # Check if the attribute exists
            if not view_instance:
                # Create a new instance of the matching learning view class
                view_instance: Any = {
                    "flashcard": FlashcardLearningView,
                    "note": NoteLearningView,
                    "question": QuestionLearningView,
                }[name](
                    dispatcher=self.dispatcher,
                    master=self.center_frame,
                    namespace=Constants.LEARNING_SESSION_NAMESPACE,
                    setting_service=self.setting_service,
                    **{name: content},
                )

                # Set the attribute
                setattr(
                    self,
                    f"{name}_learning_view",
                    view_instance,
                )

                # Grid the learning view attribute in the center frame
                view_instance.grid(
                    column=0,
                    row=0,
                    sticky=NSEW,
                )

                # Return
                return

            # Grid the learning view attribute in the center frame
            view_instance.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Dispatch the event to load the content into the learning view
            self.dispatcher.dispatch(
                event=event,
                namespace=Constants.LEARNING_SESSION_NAMESPACE,
                **{f"{name}": content},
            )

            # Set the current learning view
            self.current_learning_view = name
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_learning_view' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def load_learning_session_runner(self) -> None:
        """Loads the learning session runner as an instance variable.

        This method attempts to create a new instance of the LearningSessionRunner
        class and assigns it to an instance variable. If an exception occurs,
        it logs an error message and re-raises the exception to the caller.

        Raises:
            Exception: If an exception occurs while attempting to create the
                LearningSessionRunner instance.
        """
        try:
            # Initialize the learning session runner as an instance variable
            self.runner: LearningSessionRunner = LearningSessionRunner(
                difficulties=self.difficulties,
                dispatcher=self.dispatcher,
                namespace=Constants.LEARNING_SESSION_NAMESPACE,
                priorities=self.priorities,
                stacks=self.stacks,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_learning_session_runner' method from '{self.__class__.__name__}': {e}"
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
        """
        Handles the event when a difficulty button is clicked.

        This function toggles the state of the difficulty buttons based on the
        specified difficulty level.

        Args:
            difficulty (Literal["easy", "medium", "hard"]): The difficulty level
            to be set.
        """
        try:
            # Toggle the difficulty buttons
            self.toggle_difficulty_buttons(difficulty=difficulty)

            # Dispatch the event
            self.dispatcher.dispatch(
                difficulty=difficulty,
                event=Events.NOTIFY_LEARNING_SESSION_DIFFICULTY_BUTTON_CLICKED,
                namespace=Constants.LEARNING_SESSION_NAMESPACE,
            )
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_difficulty_button_click' method from '{self.__class__.__name__}': {e}"
            )
            raise e

    def on_learning_session_runner_loaded(self) -> None:
        """
        Handles the 'request_learning_session_runner_load_next_item' event.

        This method dispatches the event to the learning session runner and
        processes the result returned by the event.

        Raises:
            Exception: If an exception occurs while attempting to dispatch the
                event or process the result returned by the event.
        """
        try:
            # Dispatch the event
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM,
                namespace=Constants.LEARNING_SESSION_NAMESPACE,
            )

            # Check if the notification exists
            if not notification:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch event '{Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM}' in '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Get the result from the notification
            content: Optional[Any] = notification.get_one_and_only_result()

            if not content:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get one and only result from event '{Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM}' in '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Handle the loaded content
            self.handle_loaded_content(content=content)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_learning_session_runner_loaded' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_navigation_button_click(
        self,
        direction: Optional[Literal["next", "previous"]] = None,
    ) -> None:
        """
        Handles the event when a navigation button is clicked.

        Depending on the direction specified, this function dispatches either a
        'next' or 'previous' navigation event for the learning session runner.

        Args:
            direction (Optional[Literal["next", "previous"]]): The navigation
            direction, either "next" or "previous". Defaults to "next" if not
            specified.

        Raises:
            Exception: If an exception occurs during event dispatching.
        """
        try:
            # Determine the event to dispatch based on the specified direction
            event: DispatcherEvent

            # Dispatch the event based on the direction
            if direction == "next":
                # Dispatch the next item event
                event = Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM
            elif direction == "previous":
                # Dispatch the previous item event
                event = Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_PREVIOUS_ITEM
            else:
                # Default to next item event
                event = Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM

            # Dispatch the navigation event
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=event,
                namespace=Constants.LEARNING_SESSION_NAMESPACE,
            )

            # Check if the notification exists
            if not notification:
                # Log a warning message indicating that the event was not dispatched
                self.logger.warning(
                    message=f"Failed to dispatch event '{event}' in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Get the result from the notification
            content: Optional[Any] = notification.get_one_and_only_result()

            if not content:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get one and only result from event '{Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM}' in '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Handle the loaded content
            self.handle_loaded_content(content=content)
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_navigation_button_click' method from '{self.__class__.__name__}': {e}"
            )
            raise e

    def on_options_button_click(self) -> None:
        try:
            toplevel: Optional[tkinter.Toplevel] = UIBuilder.get_toplevel()

            if not toplevel:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get toplevel in '{self.__class__.__name__}'"
                )

                # Return early
                return
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_options_button_click' method from '{self.__class__.__name__}': {e}"
            )
            raise e

    @override
    def on_request_ui_validate_navigation(self) -> bool:
        try:
            return True
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_ui_validate_navigation' method from '{self.__class__.__name__}': {e}"
            )

            # Return False
            return False

    def toggle_difficulty_buttons(
        self,
        difficulty: Optional[Literal["easy", "medium", "hard"]] = None,
    ) -> None:
        """
        Handles the event when the difficulty buttons are clicked.

        This function toggles the state of the difficulty buttons based on the specified difficulty level.
        If the specified difficulty level matches the text of a button, it disables the button. Otherwise, it enables the button.

        Args:
            difficulty (Optional[Literal["easy", "medium", "hard"]]): The difficulty level to be set. Defaults to None.
        """
        try:
            # Get all the difficulty buttons
            buttons: Dict[str, tkinter.Button] = {
                "easy": self.easy_button,
                "medium": self.medium_button,
                "hard": self.hard_button,
            }

            # Iterate over the buttons and toggle their state
            for button in buttons.values():
                # Enable the button
                button.configure(state=NORMAL)

            if difficulty:
                # Disable the button that matches the specified difficulty
                buttons[difficulty].configure(state=DISABLED)
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'toggle_difficulty_buttons' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception
            raise e

    def toggle_navigation_buttons(
        self,
    ) -> None:
        """
        Handles the event when the next or previous navigation buttons are clicked.

        This function dispatches a request to the learning session runner to get the current index and limit.
        After receiving the result, it toggles the state of the next and previous navigation buttons based on the result.

        Args:
            direction (Optional[Literal["next", "previouis"]]): The navigation direction, either "next" or "previous". Defaults to None.
        """
        try:
            # Dispatch the event to get the current index and limit of the learning session runner
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_LEARNING_SESSION_RUNNER_GET_INDEX_AND_LIMIT,
                namespace=Constants.LEARNING_SESSION_NAMESPACE,
            )

            if not notification:
                # Log a warning message indicating that the event was not dispatched
                self.logger.warning(
                    message=f"Failed to dispatch event '{Events.REQUEST_LEARNING_SESSION_RUNNER_GET_INDEX_AND_LIMIT}' in '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Get the result from the notification
            (
                index,
                limit,
            ) = notification.get_one_and_only_result()

            # Configure the progressbar
            self.progressbar.configure(
                maximum=float(limit),
                value=float(index),
            )

            # Set the progress variable
            self.progress_var.set(index)

            if index == 0:
                # Disable the previous button if the index is 0
                self.previous_button.configure(state=DISABLED)
            else:
                # Enable the previous button if the index is not 0
                self.previous_button.configure(state=NORMAL)

            if index == limit - 1:
                # Disable the next button if the index is equal to the limit
                self.next_button.configure(state=DISABLED)
            else:
                # Enable the next button if the index is not equal to the limit
                self.next_button.configure(state=NORMAL)
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'toggle_navigation_buttons' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def unbind_keys(self) -> None:
        """
        Unbinds the left and right arrow keys from the back and forward navigation methods.

        This method unbinds the left arrow key from the back navigation method and the right arrow key from the forward navigation method.

        Returns:
            None
        """

        # Unbind the left arrow key from the back navigation method
        for binding in self.bindings:
            self.unbind_all(binding)

        # Clear the list of bindings
        self.bindings.clear()
