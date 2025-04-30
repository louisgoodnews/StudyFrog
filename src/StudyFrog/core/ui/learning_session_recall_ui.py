"""
Author: lodego
Date: 2505-04-25
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.answer import ImmutableAnswer
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.question import ImmutableQuestion
from core.setting import SettingService

from core.ui.fields.string_fields import MultiLineTextField

from core.ui.notifications.notifications import ToplevelNotification

from utils.base_ui import BaseUI
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.text_analyzer import TextAnalyzer
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager


__all__: Final[List[str]] = ["LearningSessionRecallUI"]


class LearningSessionRecallUI(BaseUI):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        entity: Union[
            ImmutableFlashcard,
            ImmutableNote,
            Tuple[ImmutableQuestion, Tuple[ImmutableAnswer, ...]],
        ],
        master: tkinter.Misc,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        text_analyzer: TextAnalyzer,
        unified_factory: UnifiedObjectFactory,
        unified_manager: UnifiedObjectManager,
        navigation_item: Optional[NavigationHistoryItem] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionRecallUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            entity (Union[ImmutableFlashcard, ImmutableNote, Tuple[ImmutableQuestion, Tuple[ImmutableAnswer, ...]]]): The entity being recalled.
            master (tkinter.Misc): The parent widget, which must be an instance of tkinter.Toplevel.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            text_analyzer (TextAnalyzer): The text analyzer instance.
            unified_factory (UnifiedObjectFactory): The unified factory instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.
            navigation_item (Optional[NavigationHistoryItem]): The navigation history item instance. Defaults to None.
            **kwargs: Any additional keyword arguments.

        Raises:
            ValueError: If the 'master' is not an instance of tkinter.Toplevel.

        Returns:
            None
        """

        # Check, if the passed 'master' tkinter.Misc widget is an instance of tkinter.Toplevel
        if not isinstance(
            master,
            tkinter.Toplevel,
        ):
            # Raise a ValueError if the passed 'master' is not an instance of tkinter.Toplevel
            raise ValueError("Passed 'master' must be an instance of tkinter.Toplevel")

        # Configure the passed 'master' tkinter.Toplevel widget
        self.configure_master(master=master)

        # Store the passed entity in an instance variable
        self.entity: Union[
            ImmutableFlashcard,
            ImmutableNote,
            Tuple[ImmutableQuestion, Tuple[ImmutableAnswer, ...]],
        ] = entity

        # Store the passed TextAnalyzer instance in an instance variable
        self.text_analyzer: TextAnalyzer = text_analyzer

        # Initialize the 'text field' MultiLineTextField instance variable as None
        self.text_field: Optional[MultiLineTextField] = None

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_session_recall_ui",
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_factory=unified_factory,
            unified_manager=unified_manager,
            navigation_item=navigation_item,
        )

    def _on_cancel_button_click(self) -> None:
        """Handles the click event of the 'Cancel' button.

        Opens a yes/no dialog to confirm the cancellation of the learning session.
        If the user chooses 'yes', the LearningSessionUI widget is destroyed.

        Args:
            None

        Returns:
            None
        """

        # Open a yes/no dialog to confirm the cancellation of the learning session
        response: Optional[str] = ToplevelNotification.yes_no(
            message="Are you sure you want to cancel the current learning session recall?",
            message_label={
                "background": Constants.BLUE_GREY["700"],
                "font": (
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                "foreground": Constants.WHITE,
            },
            title="Confirm cancel learning session recall",
            title_label={
                "background": Constants.BLUE_GREY["700"],
                "font": (
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                "foreground": Constants.WHITE,
            },
        )

        # Check, if the response exists or if it is "no"
        if not response or response == "no":
            # Return early
            return

        # Dispatch the NOTIFY_LEARNING_SESSION_RECALL_UI_RECALL_CANCELLED event in the 'global' namespace
        self.dispatcher.dispatch(
            entity=self.entity,
            event=Events.NOTIFY_LEARNING_SESSION_RECALL_UI_RECALL_CANCELLED,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Destroy the LearningSessionUI widget's master
        self.master.destroy()

    def _on_submit_button_click(self) -> None:
        """ """

        # Obtain label and value from the 'text field' MultiLineTextField widget
        (
            label,
            value,
        ) = self.text_field.get()

        # Initialize the original text as an empty string
        original: str = ""

        # Check, if the 'entity' instance variable is an instance of ImmutableFlashcard
        if isinstance(
            self.entity,
            ImmutableFlashcard,
        ):
            # Set the original text to the flashcard's 'front_text' attribute
            original = self.entity.front_text

        # Check, if the 'entity' instance variable is an instance of ImmutableNote
        elif isinstance(
            self.entity,
            ImmutableNote,
        ):
            # Set the original text to the note's 'body_text' attribute
            original = self.entity.body_text

        # Check, if the 'entity' instance variable is an instance of Tuple of ImmutableQuestion and Tuple ImmutableAnswer
        elif isinstance(
            self.entity,
            tuple,
        ):
            # Obtain the correct answer
            answer: Optional[ImmutableAnswer] = next(
                (
                    answer
                    for answer in self.entity[1]
                    if answer.key in self.entity[0].correct_answer
                ),
                None,
            )

            # Check, if the answer exists
            if answer:
                # Set the original text to the correct answer's 'answer_text' attribute
                original = answer.answer_text

        # Analyze the Text
        similarity: float = self.text_analyzer.get_similarity(
            compare_to=value,
            original=original,
        )

        # Prompt the user about the similarity
        ToplevelNotification.okay(
            message=f"Your similarity score is {similarity}",
            message_label={
                "background": Constants.BLUE_GREY["700"],
                "font": (
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                "foreground": Constants.WHITE,
            },
            title="Similarity score",
            title_label={
                "background": Constants.BLUE_GREY["700"],
                "font": (
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                "foreground": Constants.WHITE,
            },
        )

        # Dispatch the NOTIFY_LEARNING_SESSION_RECALL_UI_RECALL_COMPLETED event in the 'global' namespace
        self.dispatcher.dispatch(
            entity=self.entity,
            event=Events.NOTIFY_LEARNING_SESSION_RECALL_UI_RECALL_COMPLETED,
            namespace=Constants.GLOBAL_NAMESPACE,
            similarity=similarity,
        )

    @override
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

        # Collect the subscriptions from the parent class
        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        # Extend the subscriptions list
        subscriptions.extend([])

        # Return the subscriptions list to the caller
        return subscriptions

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout of the LearningSessionRecallUI widget.

        This method configures the grid layout of the LearningSessionRecallUI widget by setting the weights of its columns and rows.
        It ensures proper resizing behavior of the internal widgets.

        Columns:
            - Column 0: Weight 1

        Rows:
            - Row 0: Weight 0
            - Row 1: Weight 1
            - Row 2: Weight 0

        Returns:
            None
        """

        # Configure the LearningSessionRecallUI widget's 0th column to weight 1
        self.columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the LearningSessionRecallUI widget's 0th row to weight 0
        self.rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the LearningSessionRecallUI widget's 1st row to weight 1
        self.rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the LearningSessionRecallUI widget's 2nd row to weight 0
        self.rowconfigure(
            index=2,
            weight=0,
        )

    def configure_master(
        self,
        master: tkinter.Toplevel,
    ) -> None:
        """
        Configures the master tkinter.Toplevel widget.

        This method sets the grid configuration for the columns and rows of the master widget,
        applies a background color, and sets the geometry of the window.

        Args:
            master (tkinter.Toplevel): The master widget to be configured.

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Toplevel widget's 0th column to weight 1
        master.columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Toplevel widget's 0th row to weight 1
        master.rowconfigure(
            index=0,
            weight=1,
        )

        # Style the passed 'master' tkinter.Toplevel widget
        master.configure(bg=Constants.BLUE_GREY["700"])

        # Configure the passed 'master' tkinter.Toplevel widget's geometry
        master.geometry(newGeometry="800x600")

        # Set the focus to the master tkinter.Toplevel widget
        master.grab_set()

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        learning session recall UI, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 1st column to weight 0
        master.columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the passed 'master' tkinter.Frame widget's 2nd column to weight 0
        master.columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.rowconfigure(
            index=0,
            weight=1,
        )

        # Create the 'cancel button' tkinter.Button widget
        cancel_button: tkinter.Button = tkinter.Button(
            background=Constants.RED["700"],
            command=self._on_cancel_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Cancel",
        )

        # Place the 'cancel button' tkinter.Button widget in the grid
        cancel_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        # Create the 'submit button' tkinter.Button widget
        submit_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self._on_submit_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Submit",
        )

        # Place the 'submit button' tkinter.Button widget in the grid
        submit_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        # Update the idletasks
        self.update_idletasks()

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        learning session recall menu UI, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 0
        master.rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the passed 'master' tkinter.Frame widget's 1st row to weight 1
        master.rowconfigure(
            index=1,
            weight=1,
        )

        # Create a tkinter.Label widget
        label: tkinter.Label = tkinter.Label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
        )

        # Place the tkinter.Label widget in the grid
        label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Check, if the entity instance variable is an instance of ImmutableFlashcard
        if isinstance(
            self.entity,
            ImmutableFlashcard,
        ):
            # Update the tkinter.Label widget's text with the ImmutableFlashcard's front_text attribute
            label.configure(text=self.entity.front_text)
        # Check, if the entitiy instance variable is an instance of ImmutableNote
        elif isinstance(
            self.entity,
            ImmutableNote,
        ):
            # Update the tkinter.Label widget's text with the ImmutableNote's title attribute
            label.configure(text=self.entity.title)
        # Check, if the entity instance variable is a Tuple of ImmutableQuestion and Tuple Immutable Answer
        elif isinstance(
            self.entity,
            tuple,
        ):
            # Update the tkinter.Label widget's text with the ImmutableQuestion's question_text attribute
            label.configure(text=self.entity[0].question_text)

        # Create the 'text field' MultiLineTextField widget
        self.text_field: MultiLineTextField = MultiLineTextField(
            display_name="Enter your text here: ",
            master=master,
        )

        # Place the 'text field' MultiLineTextField widget in the grid
        self.text_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Style the 'text field' MutliLineTextField widget
        self.text_field.configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the 'text field' MutliLineTextField widget' tkinter.Button widget
        self.text_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'text field' MutliLineTextField widget' tkinter.Label widget
        self.text_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )
        # Style the 'text field' MutliLineTextField widget' tkinter.Text widget
        self.text_field.configure_text(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Update the idletasks
        self.update_idletasks()

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        learning session recall menu UI, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.rowconfigure(
            index=0,
            weight=1,
        )

        # Create the instruction string
        instruction: str = (
            "Enter your text below. Click the 'submit button' once you're done to view your results."
        )

        # Create the 'instructions label' tkinter.Label widget
        instructions_label: tkinter.Label = tkinter.Label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            text=instruction,
        )

        # Place the 'instructions label' tkinter.Label widget in the grid
        instructions_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Update the idletasks
        self.update_idletasks()

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main frames of the learning session recall menu UI.

        This method initializes the top, center, and bottom frames within the
        learning session recall menu UI, setting their layout configuration and
        invoking methods to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the 'top frame' tkinter.Frame widget
        top_frame: tkinter.Frame = tkinter.Frame(master=self)

        # Place the 'top frame' tkinter.Frame widget in the grid
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the 'top frame' widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the 'center frame' tkinter.Frame widgets
        center_frame: tkinter.Frame = tkinter.Frame(master=self)

        # Place the 'center frame' tkinter.Frame widget in the grid
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the 'center frame' widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the 'bottom frame' tkinter.Frame widget
        bottom_frame: tkinter.Frame = tkinter.Frame(master=self)

        # Place the 'bottom frame' tkinter.Frame widget in the grid
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the 'bottom frame' widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Update the idletasks
        self.update_idletasks()
