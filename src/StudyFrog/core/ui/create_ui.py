"""
Author: lodego
Date: 2025-02-11
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.answer import AnswerFactory, ImmutableAnswer
from core.difficulty import ImmutableDifficulty
from core.flashcard import FlashcardFactory, ImmutableFlashcard
from core.priority import ImmutablePriority
from core.question import QuestionFactory, ImmutableQuestion
from core.setting import SettingService
from core.stack import StackFactory, ImmutableStack, MutableStack
from core.status import ImmutableStatus

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


__all__: List[str] = ["CreateUI"]


class CreateUI(tkinter.Frame):
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

        # Call the parent class constructor
        super().__init__(
            master=master,
            name="create_ui",
        )

        # Initialize the logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Create a boolean variable in an instance variable
        self.create_another: tkinter.BooleanVar = tkinter.BooleanVar(value=True)

        # Initialize the form instance variable as None
        self.form: Optional[tkinter.Misc] = None

        # Store the passed navigation item instance in an instance variable
        self.navigation_item: NavigationHistoryItem = navigation_item

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Set the background og the CreateUI to grey
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Grid the create menu widget in its master
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
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

        # Configure the "Right Frame" frame widget's 1st and 2nd column to weight 1
        right_frame.grid_columnconfigure(
            index=(
                0,
                1,
            ),
            weight=1,
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
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=W,
        )

        # Create the "Create" button widget
        create_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["500"],
            command=self.on_create_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=right_frame,
            text="Create",
        )

        # Place the "Create" button widget in the "Right Frame" frame widget
        create_button.grid(
            column=1,
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

    def handle_flashcard_creation(
        self,
        object_data: Dict[str, Any],
        related_objects: Optional[Dict[str, Any]] = None,
    ) -> None:
        try:
            # Create a new flashcard
            flashcard: ImmutableFlashcard = self.unified_manager.create_flashcard(
                flashcard=FlashcardFactory.create_flashcard(**object_data)
            )

            if related_objects.get("stack"):
                # Set the stack to be mutable
                stack: MutableStack = related_objects["stack"].to_mutable()

                # Add the flashcard key to the stack contents
                stack.contents.append(flashcard.key)

                # Update the stack in the database
                self.unified_manager.update_stack(stack=stack)
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
        try:
            # Create a new question
            question: ImmutableQuestion = QuestionFactory.create_question(**object_data)

            create_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_QUESTION_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    question=question,
                )
            )

            if create_response is None:
                # Log a warning message indicating that the creation was not successful
                self.logger.warning(
                    message=f"Attempt to create question {question} was not successfull: {create_response}."
                )

                # Return early
                return
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
        try:
            # Create a new stack
            stack: ImmutableStack = StackFactory.create_stack(**object_data)

            create_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    stack=stack,
                )
            )

            if create_response is None:
                # Log a warning message indicating that the creation was not successful
                self.logger.warning(
                    message=f"Attempt to create stack {stack} was not successfull: {create_response}."
                )

                # Return early
                return
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

        # Get the type of form
        type: str = self.combobox.get()

        # Attempt to retrieve the "new" status from the database
        new_status: Optional[ImmutableStatus] = self.unified_manager.get_status_by(
            field="name",
            value=Constants.NEW,
        )

        # Add the status to the object data
        form_data["object_data"]["status"] = new_status.id

        # Add the status to the related objects
        form_data["related_objects"]["status"] = new_status

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
