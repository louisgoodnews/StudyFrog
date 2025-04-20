"""
Author: lodego
Date: 2025-04-19
"""

import asyncio
import json
import tkinter
import traceback

from datetime import datetime
from tkinter import filedialog
from tkinter.constants import *
from typing import *

from core.difficulty import ImmutableDifficulty
from core.flashcard import (
    FlashcardBuilder,
    ImmutableFlashcard,
)
from core.priority import ImmutablePriority
from core.stack import ImmutableStack, StackFactory

from core.ui.fields.datetime_fields import DateSelectField
from core.ui.fields.select_fields import ComboboxField, ListboxField
from core.ui.fields.string_fields import MultiLineTextField, SingleLineTextField

from core.ui.frames.frames import ScrolledFrame

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.file_service import FileService
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["FlashcardImporter"]


class FlashcardImporter(ImmutableBaseObject):
    """
    Singleton class responsible for importing flashcards into the application.

    The `FlashcardImporter` provides functionality to import flashcards from a JSON file
    into a target stack. It supports both interactive use (via user dialogs) and
    programmatic integration by accepting an existing `ImmutableStack` object.

    Core features include:
    - File selection and content validation
    - JSON structure and format checking
    - Stack selection or creation (if not provided)
    - Flashcard instantiation and insertion via dispatching events
    - GUI-based interaction using custom field and frame widgets

    This class is implemented as a singleton to ensure consistent application-wide behavior
    and shared state for importing operations.

    Usage:
        importer = FlashcardImporter(dispatcher)
        importer.start(path="data/my_cards.json")

    Attributes:
        is_running (bool): Indicates whether an import is currently in progress.
    """

    _shared_instance: Optional["FlashcardImporter"] = None

    def __new__(
        cls,
        dispatcher: Dispatcher,
    ) -> "FlashcardImporter":
        """
        Creates or returns the singleton instance of the FlashcardImporter.

        This method ensures that only one instance of the `FlashcardImporter` exists 
        throughout the application runtime. If no instance exists yet, a new one is 
        created and initialized with the provided dispatcher.

        Args:
            dispatcher (Dispatcher): The application's central event dispatcher.

        Returns:
            FlashcardImporter: The shared singleton instance.
        """

        if not cls._shared_instance:
            cls._shared_instance = super(ImmutableBaseObject, cls).__new__()
            cls._shared_instance.init(dispatcher=dispatcher)
        return cls._shared_instance

    def init(
        self,
        dispatcher: Dispatcher,
    ) -> None:
        """
        Initializes the singleton instance of the FlashcardImporter.

        This method sets up the internal state of the importer, including the dispatcher-
        It is called exactly once during the creation of the singleton instance and should not be called manually.

        Args:
            dispatcher (Dispatcher): The application's central event dispatcher.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
        )

    def _ask_user_create_stack(self) -> Optional[ImmutableStack]:
        """
        Opens a dialog window that allows the user to create a new stack.

        This method builds a `tkinter.Toplevel` interface with multiple custom UI
        fields (including name, difficulty, priority, due date, and optional description)
        using custom field components like `SingleLineTextField`, `ComboboxField`,
        `DateSelectField`, and `MultiLineTextField`.

        Required fields: name, difficulty, priority, and due date.
        These must be filled in before the user can successfully create the stack.

        Upon submission, the form data is validated and passed to `StackFactory.create_stack(...)`,
        which creates the stack object. The object is then dispatched via the event
        `REQUEST_STACK_CREATE`. If successful, the created `ImmutableStack` is returned.

        Returns:
            Optional[ImmutableStack]: The created stack object if successful, or `None` if creation
            failed or the user aborted the process.
        """

        # Initialize the result (optional) ImmutableStack object as None
        result: Optional[ImmutableStack] = None

        # initialize the form dictionary as an empty dictionary
        form: Dict[str, Any] = {}

        # Create a tkinter.Toplevel widget
        toplevel: tkinter.Toplevel = tkinter.Toplevel()

        # Configure the 0th column of the tkinter.Toplevel widget to weight 1
        toplevel.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 0th row of the tkinter.Toplevel widget to weight 0
        toplevel.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the 1st row of the tkinter.Toplevel widget to weight 1
        toplevel.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the 2nd row of the tkinter.Toplevel widget to weight 0
        toplevel.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            master=toplevel,
        )

        # Place the ScrolledFrame in the grid
        scrolled_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Configure the 0th column of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 0th row of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the 1st row of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the 2nd row of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Configure the 3rd row of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=3,
            weight=1,
        )

        # Configure the 4th row of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=4,
            weight=1,
        )

        # Configure the 5ft row of the ScrolledFrame widget to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=5,
            weight=1,
        )

        # Create an instruction string to be passed to the instruction label
        instruction: str = (
            "Fields marked with an asterisk (*) are required and must be filled."
        )

        # Create the 'instruction label' tkinter.Label widget
        instruction_label: tkinter.Label = tkinter.Label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=scrolled_frame.container,
            text=instruction,
        )

        # Place the 'instruction label' tkinter.Label widget in the grid
        instruction_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        def on_field_change(
            label: str,
            value: Any,
        ) -> None:
            """
            Handles changes in input fields and updates the internal form dictionary.

            This callback is triggered whenever a form field changes its value.
            The label of the field is normalized (special characters removed, converted
            to snake_case), and the value is stored in the `form` dictionary under that key.

            Args:
                label (str): The label of the input field (may include asterisks or colons).
                value (Any): The new value provided by the user.

            Returns:
                None
            """

            # Normalize the label and convert it to snake case
            label = Miscellaneous.any_to_snake(
                string=label.strip().replace(
                    "*",
                    "",
                ).replace(
                    ":",
                    "",
                )
            )

            # Add/update the value to the form dictionary under the passed label
            form[label] = value

        # Create the 'name' SingleLineTextField widget
        name_field: SingleLineTextField = SingleLineTextField(
            display_name="Name*: ",
            master=scrolled_frame.container,
            namespace=Constants.FLASHCARD_IMPORTER_NAMESPACE,
            on_change_callback=on_field_change,
        )

        # Style the 'name' SingleLineTextField widget
        name_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'name' SingleLineTextField widget's button widget
        name_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'name' SingleLineTextField widget's entry widget
        name_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Style the 'name' SingleLineTextField widget's label widget
        name_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'name' SingleLineTextField widget in the grid
        name_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Get the difficulties
        difficulties: Optional[List[ImmutableDifficulty]] = self._get_difficulties()

        # Create the 'difficulty' ComboboxField widget
        difficulty_field: ComboboxField = ComboboxField(
            display_name="Difficulty*: ",
            master=scrolled_frame.container,
            namespace=Constants.FLASHCARD_IMPORTER_NAMESPACE,
            on_change_callback=on_field_change,
            values=(
                [difficulty.name for difficulty in difficulties] if difficulties else []
            ),
        )

        # Style the 'difficulty' ComboboxField widget
        difficulty_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'difficulty' ComboboxField widget's button widget
        difficulty_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'difficulty' ComboboxField widget's combobox widget
        difficulty_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Style the 'difficulty' ComboboxField widget's label widget
        difficulty_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'difficulty' ComboboxField widget in the grid
        difficulty_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Get the priorities
        priorities: Optional[List[ImmutablePriority]] = self._get_priorities()

        # Create the 'priority' ComboboxField widget
        priority_field: ComboboxField = ComboboxField(
            display_name="Priority*: ",
            master=scrolled_frame.container,
            namespace=Constants.FLASHCARD_IMPORTER_NAMESPACE,
            on_change_callback=on_field_change,
            values=[priority.name for priority in priorities] if priorities else [],
        )

        # Style the 'priority' ComboboxField widget
        priority_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'priority' ComboboxField widget's button widget
        priority_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'priority' ComboboxField widget's combobox widget
        priority_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Style the 'priority' ComboboxField widget's label widget
        priority_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'priority' ComboboxField widget in the grid
        priority_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        # Create the 'due by' DateSelectField widget
        due_by_field: DateSelectField = DateSelectField(
            display_name="Due By*: ",
            master=scrolled_frame.container,
            namespace=Constants.FLASHCARD_IMPORTER_NAMESPACE,
            on_change_callback=on_field_change,
            value=Miscellaneous.get_current_datetime(),
        )

        # Style the 'due by' DateSelectField widget
        due_by_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'due by' DateSelectField widget's button widget
        due_by_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'due by' DateSelectField widget's label widget
        due_by_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'due by' DateSelectField widget in the grid
        due_by_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        # Create the 'description' MultiLineTextField widget
        description_field: MultiLineTextField = MultiLineTextField(
            display_name="Description: ",
            master=scrolled_frame.container,
            namespace=Constants.FLASHCARD_IMPORTER_NAMESPACE,
            on_change_callback=on_field_change,
        )

        # Style the 'description' MultiLineTextField widget
        description_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'description' MultiLineTextField widget's button widget
        description_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'description' MultiLineTextField widget's label widget
        description_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the 'description' MultiLineTextField widget's text widget
        description_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Place the 'description' MultiLineTextField widget in the grid
        description_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        def on_button_click() -> None:
            """
            Validates the form and closes the window if all required fields are present.

            This function is triggered when the user clicks the "Create" button.
            It checks whether all required fields ('name', 'difficulty', 'priority', 'due_by')
            are filled in. If not, a warning is logged and the function returns early.

            If validation is successful, the form data is normalized (difficulty and priority
            mapped to valid internal names), and the Toplevel window is closed. The actual
            stack creation is performed after the window has been destroyed.

            Returns:
                None
            """

            # Check, if the 'name',  'difficulty', 'due by' and 'priority' values exist
            if not all(
                form.get(
                    field,
                    False,
                )
                for field in {
                    "name",
                    "difficulty",
                    "due_by",
                    "priority",
                }
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Any field of 'difficulty', 'due_by', 'name' or 'priority' is missing. Cannot create ImmutableStack object. Aborting...."
                )

                # Return early
                return

            # Get the matching ImmutableDifficulty
            form["difficulty"] = next(
                (
                    difficulty.name
                    for difficulty in difficulties
                    if difficulty.name.lower() == form["difficulty"].lower()
                ),
                difficulties[0].name,
            )

            # Get the matching ImmutablePriority
            form["priority"] = next(
                (
                    priority.name
                    for priority in priorities
                    if priority.name.lower() == form["priority"].lower()
                ),
                priorities[0].name,
            )

            # Destroy the tkinter.Toplevel widget
            toplevel.destroy()

        # Create a tkinter.Button widget
        button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=on_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=toplevel,
            relief=FLAT,
            text="Create",
        )

        # Place the tkinter.Button in the grid
        button.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=E,
        )

        # Wait until the tkinter.Toplevel widget is destroyed
        toplevel.wait_window()

        # Dispatch the REQUEST_STACK_CREATE event in the 'global' namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_STACK_CREATE,
            namespace=Constants.GLOBAL_NAMESPACE,
            stack=StackFactory.create_stack(**form),
        )

        # Check, if the notification exists or has errors
        if not notification or notification.has_errors():
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the 'REQUEST_STACK_CREATE' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
            )

        # Set the result to the one and only result of the DispatcherNotification, the stacks
        result = notification.get_one_and_only_result()

        # Return the result
        return result

    def _ask_user_select_stack(self) -> Optional[ImmutableStack]:
        """
        Opens a dialog window that allows the user to select an existing stack.

        This method displays a `tkinter.Toplevel` window containing a `ListboxField`
        filled with the names of all available stacks. The user can select one stack
        from the list. The selected value is used to look up the corresponding
        `ImmutableStack` object from the internal list of stacks.

        After the selection and closing of the window, the matching stack object is returned.

        Returns:
            Optional[ImmutableStack]: The selected stack, or `None` if no selection was made.
        """

        # Initialize the result (optional) ImmutableStack object as None
        result: Optional[ImmutableStack] = None

        # Create a tkinter.Toplevel widget
        toplevel: tkinter.Toplevel = tkinter.Toplevel()

        # Configure the 0th column of the tkinter.Toplevel widget to weight 1
        toplevel.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 0th row of the tkinter.Toplevel widget to weight 0
        toplevel.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the 1st row of the tkinter.Toplevel widget to weight 1
        toplevel.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the 2nd row of the tkinter.Toplevel widget to weight 0
        toplevel.grid_rowconfigure(
            index=2,
            weight=0,
        )

        def on_field_change(
            label: str,
            value: Any,
        ) -> None:
            """
            Handles the user's selection in the list of stacks.

            This callback is triggered when the user selects an item in the `ListboxField`.
            It searches for a stack in the internal list of available stacks (`stacks`)
            whose name matches the selected value (case-insensitive),
            and assigns the corresponding `ImmutableStack` to the outer `result` variable.

            Args:
                label (str): The label of the field triggering the event (not used here).
                value (Any): The value selected by the user (expected to be the stack's name).

            Returns:
                None
            """

            # Check, if the passed value is not empty or None
            if not value:
                # Return early
                return

            # Set the result to the ImmutableStack object with a name matching the passed value
            result = next(
                (stack for stack in stacks if stack.name.lower() == value.lower()), None
            )

        # Get the stacks
        stacks: Optional[List[ImmutableStack]] = self._get_stacks()

        # Create the 'stack' ListboxField widget
        stack_field: ListboxField = ListboxField(
            display_name="Stack*: ",
            master=toplevel,
            namespace=Constants.FLASHCARD_IMPORTER_NAMESPACE,
            on_change_callback=on_field_change,
            selectmode="single",
            values=[stack.name for stack in stacks] if stacks else [],
        )

        # Style the 'stack' ListboxField widget
        stack_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'stack' ListboxField widget
        stack_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'stack' ListboxField widget's label widget
        stack_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the 'stack' ListboxField widget's listbox widget
        stack_field.configure_listbox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Place the 'stack' ListboxField widget in the grid
        stack_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Wait until the tkinter.Toplevel widget is destroyed
        toplevel.wait_window()

        # Return the result
        return result

    def _check_import_format(
        self,
        json_content: Dict[str, Any],
    ) -> Dict[str, Any]:
        """ """

        # Get the list of dictionaries associated to the 'flashcards' key
        list_value: List[Dict[str, Any]] = json_content["flashcards"]

        # Check, if the list is empty
        if len(list_value) == 0:
            # Log a warning message
            self.logger.warning(
                message=f"Found no flashcard JSONs to import from. Aborting..."
            )

            # Return early
            return {
                "result": "illegal",
                "format": "illegal",
            }

        # Define the keys for the necessary condition
        necessary_keys: Set[str] = {
            "back_text",
            "front_text",
        }

        # Check, if the necessary condition is fulfilled
        if self._is_necessary_condition_fulfilled(
            list_value=list_value,
            necessary_keys=necessary_keys,
        ):
            # Return a corresponding result
            return {
                "result": "legal",
                "format": "necessary_fields",
            }

        # Define the keys for the sufficient condition
        sufficient_keys: Set[str] = {
            "back_text",
            "front_text",
        }

        # Check, if the necessary condition is fulfilled
        if self._is_sufficient_condition_fulfilled(
            list_value=list_value,
            sufficient_keys=sufficient_keys,
        ):
            # Return a corresponding result
            return {
                "result": "legal",
                "format": "sufficient_fields",
            }

        # Return an illegal result
        return {
            "result": "illegal",
            "format": "illegal",
        }

    def _check_stacks_exist(self) -> bool:
        """
        Checks whether any stacks currently exist in the application.

        This method calls `_get_stacks()` to retrieve all available stacks
        via the dispatcher. If at least one stack is found, it returns `True`;
        otherwise, it returns `False`.

        Returns:
            bool: `True` if at least one stack exists, `False` otherwise.
        """

        # Return True if the DispatcherNotification has a one and only result otherwise False
        return True if self._get_stacks() else False

    def _get_difficulties(self) -> Optional[List[ImmutableDifficulty]]:
        """
        Retrieves all available difficulty levels via the dispatcher.

        This method dispatches the `REQUEST_GET_ALL_DIFFICULTIES` event
        in the global namespace to obtain a list of `ImmutableDifficulty` objects.
        If the dispatch fails or returns an error, a warning is logged.

        Returns:
            Optional[List[ImmutableDifficulty]]: A list of difficulty levels if available,
            or `None` if the request failed or returned an error.
        """

        # Dispatch the REQUEST_GET_ALL_DIFFICULTIES in the 'global' namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_DIFFICULTIES,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists or has errors
        if not notification or notification.has_errors():
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the 'REQUEST_GET_ALL_DIFFICULTIES' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
            )

        # Return the one and only result of the DispatcherNotification, the stacks
        return notification.get_one_and_only_result()

    def _get_priorities(self) -> Optional[List[ImmutablePriority]]:
        """
        Retrieves all available priority levels via the dispatcher.

        This method dispatches the `REQUEST_GET_ALL_PRIORITIES` event
        in the global namespace to fetch a list of `ImmutablePriority` objects.
        If the dispatch fails or the notification contains errors, a warning is logged.

        Returns:
            Optional[List[ImmutablePriority]]: A list of priority levels if available,
            or `None` if the request failed or returned an error.
        """

        # Dispatch the REQUEST_GET_ALL_PRIORITIES in the 'global' namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_PRIORITIES,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists or has errors
        if not notification or notification.has_errors():
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the 'REQUEST_GET_ALL_PRIORITIES' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
            )

        # Return the one and only result of the DispatcherNotification, the stacks
        return notification.get_one_and_only_result()

    def _get_stacks(self) -> Optional[List[ImmutableStack]]:
        """
        Retrieves all existing stacks via the dispatcher.

        This method dispatches the `REQUEST_GET_ALL_STACKS` event in the global namespace
        to obtain a list of `ImmutableStack` objects representing the available stacks
        in the application. If the dispatch fails or the notification contains errors,
        a warning is logged.

        Returns:
            Optional[List[ImmutableStack]]: A list of existing stacks if available,
            or `None` if the request failed or returned an error.
        """

        # Dispatch the REQUEST_GET_ALL_STACKS in the 'global' namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_STACKS,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists or has errors
        if not notification or notification.has_errors():
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the 'REQUEST_GET_ALL_STACKS' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
            )

        # Return the one and only result of the DispatcherNotification, the stacks
        return notification.get_one_and_only_result()

    def _import_flashcards(
        self,
        list_value: List[Dict[str, Any]],
        stack: ImmutableStack,
    ) -> bool:
        """ """
        try:
            # Initialize the result boolean list as an empty list
            result: List[bool] = []

            # Convert the passed ImmutableStack into a MutableStack
            stack = stack.to_mutable()

            # Log an info message
            self.logger.info(message=f"Starting import of flashcards...")

            # Create a timestamp of the process' beginning
            start: datetime = Miscellaneous.get_current_datetime()

            # Iterate over the dictionaries in the passed list
            for (
                index,
                list_dict,
            ) in enumerate(
                iterable=list_value,
                start=1,
            ):
                # Set the list dictionary's 'stack' key
                list_dict["stack"] = stack.id

                # Set the list dictionary's 'difficulty' key
                list_dict["difficulty"] = stack.difficulty

                # Set the list dictionary's 'priority' key
                list_dict["priority"] = stack.priority

                # Initialize a FlashcardBuilder instance
                builder: FlashcardBuilder = FlashcardBuilder()

                # Update the the builder with the keywords from the list dictionary
                builder.kwargs(**list_dict)

                # Dispatch the REQUEST_FLASHCARD_CREATE event in the 'global' namespace
                notification: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        event=Events.REQUEST_FLASHCARD_CREATE,
                        flashcard=builder.build(),
                        namespace=Constants.GLOBAL_NAMESPACE,
                    )
                )

                # Check, if the notification exists or has errors
                if not notification or notification.has_errors():
                    # Log a warning message
                    self.logger.warning(
                        message=f"Failed to dispatch the 'REQUEST_FLASHCARD_CREATE' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
                    )

                    # Log a warning message about the FlashcardBuilder object
                    self.logger.warning(message=f"Affected FlashcardBuilder: {builder}")

                    # Append False to the result list
                    result.append(False)

                    # Skip the current iteration
                    continue

                # Get the one and only result (ImmutableFlashcard) from the DispatcherNotification
                flashcard: ImmutableFlashcard = notification.get_one_and_only_result()

                # Log an info message
                self.logger.info(
                    message=f"Successfully imported flashcard no. {index}/{len(list_value)} with ID {flashcard.id}."
                )

                # Add the ImmutableFlashcard to the MutableStack object's contents
                stack.add_to_contents(content=flashcard)

                # Append True to the result list
                result.append(True)

            # Dispatch the REQUEST_STACK_UPDATE event in the 'global' namespace
            self.dispatcher.dispatch(
                event=Events.REQUEST_STACK_UPDATE,
                stack=stack,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Create a timestamp of the process' end
            end: datetime = Miscellaneous.get_current_datetime()

            # Log an info message
            self.logger.info(
                message=f"Completed import of flashcards {"successfully" if all(result) else "unsuccessfully"}. Total time elapsed: {(end - start).total_seconds()} seconds."
            )

            # Return a boolean representation of the result list
            return all(result)
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run '_import_flashcards' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _is_necessary_condition_fulfilled(
        self,
        list_value: List[Dict[str, Any]],
        necessary_keys: Set[str],
    ) -> bool:
        """
        Checks whether all dictionaries in the list contain exactly the necessary keys.

        This method verifies that each dictionary in `list_value` has exactly the same keys
        as defined in `necessary_keys`—no more, no less. It is used to validate that the
        minimal required structure for importing flashcards is fulfilled.

        Args:
            list_value (List[Dict[str, Any]]): A list of flashcard-like dictionaries to check.
            necessary_keys (Set[str]): The exact set of keys required for a valid minimal import.

        Returns:
            bool: `True` if every dictionary contains only the necessary keys, otherwise `False`.
        """

        # Return true, if all dictionaries in the passed list_value list contain only the necessary keys otherwise False
        return all(set(value) == necessary_keys for value in list_value)

    def _is_sufficient_condition_fulfilled(
        self,
        list_value: List[Dict[str, Any]],
        sufficient_keys: Set[str],
    ) -> bool:
        """
        Checks whether all dictionaries in the list contain exactly the sufficient keys.

        This method validates that each dictionary in `list_value` includes exactly the keys
        specified in `sufficient_keys`. It is typically used to verify that an extended
        (but still valid) flashcard import format is being used, beyond the minimal structure.

        Args:
            list_value (List[Dict[str, Any]]): A list of flashcard-like dictionaries to check.
            sufficient_keys (Set[str]): The expected full set of keys for a complete import format.

        Returns:
            bool: `True` if all dictionaries contain exactly the sufficient keys, otherwise `False`.
        """

        # Return true, if all dictionaries in the passed list_value list contain the sufficient keys otherwise False
        return all(set(value) == sufficient_keys for value in list_value)

    def start(
        self,
        path: Optional[str] = None,
        stack: Optional[ImmutableStack] = None,
    ) -> None:
        """
        Starts the flashcard import process from a JSON file.

        This method performs the full import pipeline:
        - Prompts the user to select a `.json` file (if no `path` is provided)
        - Reads and validates the file content
        - Verifies the structure and import format of the JSON
        - Selects or creates a target stack (if none is passed)
        - Imports the flashcards into the specified or chosen stack

        Args:
            path (Optional[str]): The path to the `.json` file to import. If `None`, a file dialog will open.
            stack (Optional[ImmutableStack]): The target stack for the imported flashcards. If `None`, the user is prompted to select or create one.

        Returns:
            None

        Raises:
            Exception: If any unexpected error occurs during the import process.
        """
        try:
            # Check, if any path was obtained
            if not path:
                # Seclect a .json file
                path = filedialog.askopenfilename(
                    defaultextension="json",
                    filetypes=("json"),
                    initialdir=Constants.CWD,
                    mode="r",
                    title=f"Select a .json file to import into {Constants.APPLICATION_NAME}",
                )

            # Check again, if any path was obtained
            if not path:
                # Log warning message
                self.logger.warning(message=f"'{path}' does not exist. Aborting...")

                # Return early
                return

            # Attempt to read the contents of the file
            str_content: Optional[str] = asyncio.run(FileService.read(path=path))

            # Check, if the string content was obtained
            if not str_content:
                # Log a warning message
                self.logger.warning(
                    message=f"File under '{path}' contained illegal or no content. Aborting..."
                )

                # Return early
                return

            # Load the JSON content
            json_content: Dict[str, Any] = json.loads(str_content)

            # Check, if the json_content contains a
            if not json_content.get(
                "flashcards",
                None,
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"File under '{path}' contained illegal or no content. Aborting..."
                )

                # Return early
                return

            # Obtain the format report dictionary
            format_report: Dict[str, Any] = self._check_import_format(
                json_content=json_content
            )

            # Check, if the import format was deemed illegal
            if format_report["format"] == "illegal":
                # Log an error message
                self.logger.error(
                    message=f"Illegal format in {json_content}. Please adhere to the ONLY legal import format before attempting an import into {Constants.APPLICATION_NAME}! Aborting..."
                )

                # Return early
                return

            # Initialize the (optional) ImmutableStack as None
            stack: Optional[ImmutableStack] = stack

            # Obtain a flag that indicates if any stacks exist in the application
            stacks_exist: bool = self._check_stacks_exist()

            # Check, if the stacks exists
            if stacks_exist and not stack:
                # Prompt the user to select an existing stack
                stack = self._ask_user_select_stack()
            elif not stacks_exist and not stack:
                # Prompt the user to create a new stack
                stack = self._ask_user_create_stack()

            # Log an info message
            self.logger.info(
                message="All preliminary tasks have been completed successfully. Moving to flashcard import..."
            )

            # Import the flashcards into the application
            self._import_flashcards(
                list_value=json_content["flashcards"],
                stack=stack,
            )
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run 'start' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e
