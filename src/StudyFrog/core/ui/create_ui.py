"""
Author: lodego
Date: 2025-02-11
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.answer import AnswerFactory, ImmutableAnswer
from core.flashcard import FlashcardFactory, ImmutableFlashcard
from core.question import MutableQuestion, QuestionFactory, ImmutableQuestion
from core.setting import SettingService
from core.stack import StackFactory, ImmutableStack, MutableStack
from core.status import ImmutableStatus

from core.ui.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder
from core.ui.form.flashcard_create_form import FlashcardCreateForm
from core.ui.form.question_create_form import QuestionCreateForm
from core.ui.form.stack_create_form import StackCreateForm

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["CreateUI"]


class CreateUI(BaseUI):
    """
    A class representing the create menu user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    create menu UI, including setting up the main frames and populating them with
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
        unified_manager: UnifiedObjectManager,
        type: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the CreateUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Create a boolean variable in an instance variable
        self.create_another: tkinter.BooleanVar = tkinter.BooleanVar(value=True)

        # Initialize the form instance variable as None
        self.form: Optional[tkinter.Misc] = None

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="create_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

        if isinstance(
            master,
            tkinter.Toplevel,
        ):
            # Configure the master Toplevel widget's geometry to 540x960
            master.geometry(newGeometry="540x960")

            # Configure the master Toplevel widget's 1st column to weight 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the master Toplevel widget's 1st row to weight 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

        # Check, if a type string was passed
        if type is not None:
            # Set the combobox value to the passed type
            self.combobox.set(value=type.capitalize())
        else:
            self.preselect_combobox_value()

        # Call the on_combobox_select method
        self.on_combobox_select()

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
        Configures the grid of the create menu widget.

        This method configures the grid of the create menu widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the create menu widget's 1st column to weight 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the create menu widget's 1st and 3rd row to weight 0.
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the create menu widget's 2nd row to weight 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main frames of the create menu UI.

        This method initializes the top, center, and bottom frames within the
        create menu UI, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the "Top Frame" frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Top Frame" frame widget's 1st column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "TOp Frame" frame widget's 1st row to weight 1
        top_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Place the "Top Frame" frame widget in the main window
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Center Frame" frame widget
        self.center_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        self.center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Center Frame" frame widget's 1st row to weight 1
        self.center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Center Frame" frame widget in the main window
        self.center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the "Bottom Frame" frame widget
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Bottom Frame" frame widget's 1st column to weight 1
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Bottom Frame" frame widget's 1st row to weight 1
        bottom_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Bottom Frame" frame widget in the main window
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the "Bottom Frame" frame widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Create the "Top Frame" frame widgets
        self.create_top_frame_widgets(master=top_frame)

    def clear(self) -> None:
        """
        Clears the content of the center frame.

        This method removes all children widgets from the center frame, clearing
        its content.

        Returns:
            None
        """

        # Get a list of all children widgets in the center frame
        children: List[tkinter.Misc] = self.center_frame.winfo_children()

        # Check if there are any children
        if not children:
            # Return early
            return

        # Iterate over the children
        for child in children:

            # Destroy the child widget
            child.destroy()

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        create menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the top frame widget's 1st and 2nd column to weight 0
        master.grid_columnconfigure(
            index=(
                0,
                1,
            ),
            weight=1,
        )

        # Configure the top frame widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the "Left Frame" frame widget
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the "Left Frame" frame widget's 1st column to weight 0
        left_frame.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the "Left Frame" frame widget's 2nd column to weight 1
        left_frame.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the "Left Frame" frame widget's 1st row to weight 1
        left_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Left Frame" frame widget in the main window
        left_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Create Another" check button widget
        create_another: tkinter.Checkbutton = UIBuilder.get_checkbutton(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
            variable=self.create_another,
        )

        # Place the "Create Another" check button widget in the "Left Frame"
        create_another.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the "Label" widget
        label: tkinter.Label = UIBuilder.get_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
            text="Create another? ",
        )

        # Place the "Label" widget in the "Left Frame"
        label.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=W,
        )

        # Create the "Right Frame" frame widget
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the "Right Frame" frame widget's 1st column to weight 1
        right_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Right Frame" frame widget's 2nd and 3rd column to weight 0
        right_frame.grid_columnconfigure(
            index=(
                1,
                2,
            ),
            weight=0,
        )

        # Configure the "Right Frame" frame widget's 1st row to weight 1
        right_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Right Frame" frame widget in the main window
        right_frame.grid(
            column=1,
            row=0,
            sticky=NSEW,
        )

        # Create the "Cancel" button widget
        cancel_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_cancel_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=right_frame,
            relief=FLAT,
            text="Cancel",
        )

        # Place the "Cancel" button widget in the "Right Frame" frame widget
        cancel_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=W,
        )

        # Create the "Create" button widget
        create_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_create_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=right_frame,
            relief=FLAT,
            text="Create",
        )

        # Place the "Create" button widget in the "Right Frame" frame widget
        create_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=W,
        )

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        create menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the top frame widget's 1st column to weight 1
        master.grid_columnconfigure(index=0, weight=1)

        # Configure the top frame widget's 1st row to weight 1
        master.grid_rowconfigure(index=0, weight=1)

        # Create the top frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the top frame widget's 1st and 2nd columns to weight 1
        top_frame.grid_columnconfigure(
            index=(
                0,
                1,
            ),
            weight=1,
        )

        # Configure the top frame widget's 1st row to weight 1
        top_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the top frame widget in the main window
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the label widget
        label: tkinter.Label = UIBuilder.get_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=top_frame,
            text="Type: ",
        )

        # Place the label widget in the top frame
        label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the combobox widget
        self.combobox: ttk.Combobox = UIBuilder.get_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            master=top_frame,
            state="readonly",
            values=[
                "Flashcard",
                "Question",
                "Stack",
            ],
        )

        # Bind the combobox widget to the on_combobox_select method
        self.combobox.bind(
            func=lambda event: self.on_combobox_select(),
            sequence="<<ComboboxSelected>>",
        )

        # Place the combobox widget in the top frame
        self.combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

    def handle_answer_creation(
        self,
        question: ImmutableQuestion,
        related_objects: Optional[Dict[str, Any]] = None,
    ) -> MutableQuestion:
        """
        Handles the creation of answers for a question.

        Args:
            question (ImmutableQuestion): The question to be associated with the answer.
            related_objects (Optional[Dict[str, Any]], optional): Related objects, if any. Defaults to None.

        Returns:
            MutableQuestion: The question with the answers associated.

        Raises:
            Exception: If an error occurs during answer creation.
        """
        try:
            if isinstance(
                question,
                ImmutableQuestion,
            ):
                # Convert the immutable question object into a mutable object
                question = question.to_mutable()

            # Handle answer creation depending on the question type
            if question["question_type"] == "MULTIPLE_CHOICE":
                # Iterate over the answers for the multiple choice question
                for answer_dict in related_objects.get(
                    "answers",
                    [],
                ):
                    # Create a new answer
                    answer: ImmutableAnswer = AnswerFactory.create_answer(
                        answer_text=answer_dict["value"]
                    )

                    # Dispatch a request to create the answer
                    create_response: Optional[DispatcherNotification] = (
                        self.dispatcher.dispatch(
                            answer=answer,
                            event=Events.REQUEST_ANSWER_CREATE,
                            namespace=Constants.GLOBAL_NAMESPACE,
                        )
                    )

                    # Retrieve the created answer
                    answer = create_response.get_result_by_key(
                        key="on_request_answer_create"
                    )

                    # Add the answer to the question
                    question.add_to_answers(answer=answer)

                    # If the answer is correct, add it to the correct answers
                    if answer_dict["is_correct"]:
                        question.add_to_correct_answers(answer=answer)

            elif question["question_type"] == "OPEN_ANSWER":
                # Create a new answer
                answer: ImmutableAnswer = AnswerFactory.create_answer(
                    answer_text=related_objects["answers"][0]
                )

                # Dispatch a request to create the answer
                create_response: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        answer=answer,
                        event=Events.REQUEST_ANSWER_CREATE,
                        namespace=Constants.GLOBAL_NAMESPACE,
                    )
                )

                # Retrieve the created answer
                answer = create_response.get_result_by_key(
                    key="on_request_answer_create"
                )

                # Add the answer to the question
                question.add_to_answers(answer=answer)

                # Add the answer to the correct answers
                question.add_to_correct_answers(answer=answer)

            elif question["question_type"] == "TRUE_FALSE":
                # Get the true answer
                true_answer_response: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        answer_text="True",
                        event=Events.REQUEST_ANSWER_LOOKUP,
                        namespace=Constants.GLOBAL_NAMESPACE,
                    )
                )

                # Get the true answer from the response
                true_answer: ImmutableAnswer = true_answer_response.get_result_by_key(
                    key="on_request_answer_lookup"
                )[0]

                # Get the false answer
                false_answer_response: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        answer_text="False",
                        event=Events.REQUEST_ANSWER_LOOKUP,
                        namespace=Constants.GLOBAL_NAMESPACE,
                    )
                )

                # Get the false answer from the response
                false_answer: ImmutableAnswer = false_answer_response.get_result_by_key(
                    key="on_request_answer_lookup"
                )[0]

                # Add the true answer to the question
                question.add_to_answers(answer=true_answer)

                # Add the false answer to the question
                question.add_to_answers(answer=false_answer)

                # Add the correct answer to the correct answers
                if related_objects["answers"][0]:
                    question.add_to_correct_answers(answer=true_answer)
                else:
                    question.add_to_correct_answers(answer=false_answer)

            # Return the question with the answers associated
            return question
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_answer_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def handle_flashcard_creation(
        self,
        object_data: Dict[str, Any],
        related_objects: Optional[Dict[str, Any]] = None,
    ) -> None:
        try:
            # Check if related objects have been provided
            if not related_objects:
                # Initialize the related objects dictionary as an empty dictionary
                related_objects = {}

            # Create a new flashcard
            flashcard: ImmutableFlashcard = FlashcardFactory.create_flashcard(
                **object_data
            )

            # Dispatch a request to create the flashcard
            create_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_FLASHCARD_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    flashcard=flashcard,
                )
            )

            # Check if the creation response is None, indicating failure
            if create_response is None:
                # Log a warning message indicating that the creation was not successful
                self.logger.warning(
                    message=f"Attempt to create flashcard {flashcard} was not successfull: {create_response}."
                )

                # Return early
                return

            # Retrieve the created flashcard
            flashcard = create_response.get_result_by_key(
                key="on_request_flashcard_create"
            )

            if related_objects.get(
                "stack",
                None,
            ):
                # Set the stack to be mutable
                stack: Optional[ImmutableStack] = related_objects.get(
                    "stack",
                    None,
                )

                # Set the stack to be mutable
                stack = stack.to_mutable()

                # Add the flashcard key to the stack contents
                stack.contents.append(flashcard.key)

                # Dispatch the REQUEST_STACK_UPDATE event in the global namespace
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    stack=stack,
                )

                # Dispatch the STACK_UPDATED event in the global namespace
                self.dispatcher.dispatch(
                    event=Events.STACK_UPDATED,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    stack=stack,
                )

            # Dispatch the FLASHCARD_CREATED event in the global namespace
            self.dispatcher.dispatch(
                event=Events.FLASHCARD_CREATED,
                namespace=Constants.GLOBAL_NAMESPACE,
                flashcard=flashcard,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_flashcard_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def handle_question_creation(
        self,
        object_data: Dict[str, Any],
        related_objects: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Handles the creation of a new question.

        Args:
            object_data (Dict[str, Any]): The data required to create a question.
            related_objects (Optional[Dict[str, Any]], optional): Related objects, if any. Defaults to None.

        Raises:
            Exception: If an error occurs during question creation.
        """
        try:
            # Check if related objects have been provided
            if not related_objects:
                # Initialize the related objects dictionary as an empty dictionary
                related_objects = {}

            # Create a new question
            question: ImmutableQuestion = QuestionFactory.create_question(**object_data)

            # Dispatch a request to create the question
            create_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_QUESTION_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    question=question,
                )
            )

            # Check if the creation response is None, indicating failure
            if create_response is None:
                # Log a warning message indicating that the creation was not successful
                self.logger.warning(
                    message=f"Attempt to create question {question} was not successfull: {create_response}."
                )

                # Return early
                return

            # Retrieve the created question
            question: ImmutableQuestion = create_response.get_result_by_key(
                key="on_request_question_create"
            )

            # Check, if the "answer" key exists in the related objects
            if related_objects.get(
                "answers",
                None,
            ):
                # Create answers and update the question
                question = self.handle_answer_creation(
                    question=question,
                    related_objects=related_objects,
                )

                # Dispatch a request to update the question
                self.dispatcher.dispatch(
                    event=Events.REQUEST_QUESTION_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    question=question,
                )

            if related_objects.get(
                "stack",
                None,
            ):
                # Retrieve the stack from related objects
                stack: ImmutableStack = related_objects["stack"]

                # Convert the stack to a mutable stack
                stack = stack.to_mutable()

                # Add the question to the contents of the stack
                stack.add_to_contents(obj=question)

                # Dispatch a request to update the stack
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    stack=stack,
                )

            # Dispatch the QUESTION_CREATED event in the global namespace
            self.dispatcher.dispatch(
                event=Events.QUESTION_CREATED,
                namespace=Constants.GLOBAL_NAMESPACE,
                question=question,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_question_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def handle_stack_creation(
        self,
        object_data: Dict[str, Any],
        related_objects: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Handles the creation of a new stack.

        Args:
            object_data (Dict[str, Any]): The data required to create a stack.
            related_objects (Optional[Dict[str, Any]]): Related objects, if any.

        Returns:
            None

        Raises:
            Exception: If an error occurs during stack creation.
        """
        try:
            # Check if related objects have been provided
            if not related_objects:
                # Initialize the related objects dictionary as an empty dictionary
                related_objects = {}

            # Create a new stack using the provided object data
            stack: ImmutableStack = StackFactory.create_stack(**object_data)

            # Dispatch a request to create the stack
            create_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    stack=stack,
                )
            )

            # Check if the creation response is None, indicating failure
            if create_response is None:
                # Log a warning message indicating that the creation was not successful
                self.logger.warning(
                    message=f"Attempt to create stack {stack} was not successful: {create_response}."
                )

                # Return early
                return

            # Retrieve the created stack
            stack = create_response.get_result_by_key(key="on_request_stack_create")

            # Check, if the "ancestor_stack" key exists in the related objects
            if related_objects.get(
                "ancestor_stack",
                None,
            ):
                # Get and convert the ancestor stack to a mutable object
                ancestor: MutableStack = related_objects["ancestor_stack"].to_mutable()

                # Add the created stack to the list of descendants
                ancestor.descendants.append(stack.key)

                # Dispatch a request to update the ancestor stack
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    stack=ancestor,
                )

            # Dispatch the STACK_CREATED event in the global namespace
            self.dispatcher.dispatch(
                event=Events.STACK_CREATED,
                namespace=Constants.GLOBAL_NAMESPACE,
                stack=stack,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_stack_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def on_combobox_select(self) -> None:
        """
        Handles the selection event of the combobox widget.

        Args:
            None

        Returns:
            None
        """

        # A dictionary mapping the selected values to the corresponding form classes
        forms: Dict[str, Any] = {
            "flashcard": FlashcardCreateForm,
            "question": QuestionCreateForm,
            "stack": StackCreateForm,
        }

        # Clear the center frame to remove any existing widgets
        self.clear()

        # Create a new form widget based on the selected value
        self.form = forms[self.combobox.get().lower()](
            dispatcher=self.dispatcher,
            master=self.center_frame,
            unified_manager=self.unified_manager,
        )

    def on_cancel_button_click(self) -> None:
        """
        Handles the click event of the "Cancel" button.

        Returns:
            None
        """

        # Check if the master widget is of type toplevel
        if isinstance(
            self.master,
            tkinter.Toplevel,
        ):
            # Destroy the toplevel widget
            self.master.destroy()

    def on_create_button_click(self) -> None:
        """
        Handles the click event of the "Create" button.

        This method first checks if a form is present. If not, it returns early.
        Then, it retrieves the data from the form and the type of form.
        It attempts to retrieve the "new" status from the database and adds it
        to the object data and related objects.
        Finally, it calls the appropriate creation method based on the form type.

        Returns:
            None
        """

        # Check if a form is present
        if not self.form:
            # Return early
            return

        # Get the data from the form
        form_data: Dict[str, Any] = self.form.get()

        if not self.form.check_required_fields(
            object_data=form_data.get(
                "object_data",
                {},
            )
        ):
            # Log an info message indicating that not all required fields were filled
            self.logger.info(message="Seems like not all required fields were filled.")

            # Return early
            return

        # Get the type of form
        type: str = self.combobox.get()

        # Attempt to retrieve the "new" status from the database
        status_response: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_STATUS_LOOKUP,
            name="New",
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Retrieve the status from the response
        status: Optional[ImmutableStatus] = status_response.get_result_by_key(
            key="on_request_status_lookup",
        )[0]

        # Add the status to the object data
        form_data["object_data"]["status"] = status["id"]

        # Add the status to the related objects
        form_data["related_objects"]["status"] = status

        # Call the appropriate creation method based on the form type
        getattr(
            self,
            f"handle_{type.lower()}_creation",
        )(
            object_data=form_data["object_data"],
            related_objects=form_data["related_objects"],
        )

        if not self.create_another.get():
            # Check if the master widget is of type toplevel
            if isinstance(
                self.master,
                tkinter.Toplevel,
            ):
                # Destroy the toplevel widget
                self.master.destroy()

    def preselect_combobox_value(self) -> None:
        """
        Preselects a random value for the combobox widget.

        This method is called after the UI has been created and
        before the toplevel widget is shown. It preselects a random
        value from the list of available values for the combobox
        widget.

        Returns:
            None
        """

        # Set the combobox value to a random value
        self.combobox.set(
            value=Miscellaneous.select_random(
                [
                    # The type of object to be created
                    "Flashcard",
                    "Question",
                    "Stack",
                ]
            )
        )
