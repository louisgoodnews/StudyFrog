"""
Author: lodego
Date: 2025-04-13
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.ui.fields.select_fields import ComboboxField
from core.ui.fields.string_fields import MultiLineTextField

from core.ui.frames.frames import ScrolledFrame

from core.ui.notifications.notifications import ToplevelNotification

from utils.base_create_form import BaseCreateForm
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events


__all__: Final[List[str]] = ["FlashcardCreateForm"]


class FlashcardCreateForm(BaseCreateForm):
    """
    A form widget for creating new Flashcards within the StudyFrog application.

    This class provides a structured interface for inputting the core attributes of a Flashcard, 
    such as the associated Stack, front text, and back text. It inherits from BaseCreateForm and 
    extends it by adding domain-specific logic, including input validation and duplicate-checking 
    for the front text value.

    Additionally, this form utilizes the Dispatcher to coordinate event-based lookups 
    (e.g., checking for existing Flashcards with the same front text).

    Attributes:
        logger (Logger): This class' Logger instance.
        dispatcher (Dispatcher): The Dispatcher instance used for event communication.
        field_dict (dict): A dictionary in which fields are registered.
        namespace (str): The namespace to dispatch events with.
        value_dict(dict): A dictionary in which the form's value is being tracked.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
    ) -> None:
        """
        Initializes a new instance of the FlashcardCreateForm class.

        This constructor sets up the FlashcardCreateForm by delegating shared setup 
        logic to the BaseCreateForm constructor. It registers the passed Dispatcher,
        master frame, and namespace, allowing the form to function as an event-driven,
        modular UI component within the application.

        Args:
            dispatcher (Dispatcher): The central dispatcher responsible for handling UI events and coordination.
            master (tkinter.Misc): The parent widget (typically a Frame or Toplevel) where the form will be rendered.
            namespace (str): A string used to group related UI events and callbacks within the Dispatcher system.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            namespace=namespace,
        )

    @override
    def _on_field_change(
        self,
        label: str,
        value: Any,
    ) -> None:
        """
        Handles field value changes and performs additional logic for specific fields.

        This method overrides the parent class' '_on_field_change' method and adds additional
        logic for specific fields. When the 'front_text' field is changed, this method will dispatch
        a REQUEST_STACK_LOOKUP event in the global namespace to determine if a Flashcard with the
        same 'front_text' already exists in the database. If so, a warning will be shown via a
        ToplevelNotification dialog.

        Args:
            label (str): The label of the field that was changed.
            value (Any): The new value of the field.

        Returns:
            None
        """

        # Call the parent class' '_on_field_change' method with the passed arguments
        super()._on_field_change(
            label=label,
            value=value,
        )

        # Check, if the changed field is not the 'Front Text' field
        if label != "front_text":
            # Return early
            return

        # Dispatch the REQUEST_STACK_LOOKUP event in the global namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_STACK_LOOKUP,
            namespace=Constants.GLOBAL_NAMESPACE,
            **{
                "name": value,
            },
        )

        # Check, if the notification exists
        if not notification:
            # Log a warning message
            self.logger.warning(message=f"Failed to dispatch the REQUEST_STACK_LOOKUP event in the global namespace.")

            # Return early
            return

        # Attempt to obtain the one and only result of the notification
        notification_result: Optional[Any] = notification.get_one_and_only_result()

        # Check, if no result could be obtained
        if not notification_result:
            # Return early
            return

        # Notify the user with a ToplevelNotification
        ToplevelNotification.okay(
            message=f"The value you entered in the 'Front Text' field is already contained in the database. At least {len(notification_result)} other Flashcard(s) were found with an identical 'Front Text'.",
            on_click_callback=self._on_front_text_warning_okay,
            title=f"'Front Text' is not unique",
        )

    def _on_front_text_warning_okay(
        self,
        message: str,
    ) -> None:
        """
        Handles the 'okay' click event from the front text warning notification.

        This method is called when the user clicks the 'okay' button in the warning notification
        that is shown when a duplicate 'front_text' was detected. It clears the field's value if
        the user confirmed the warning.

        Args:
            message (str): The message returned from the notification, e.g., "okay".

        Returns:
            None
        """

        # Check, if the message is not 'okay'
        if message != "okay":
            # Log a warning
            self.logger.warning(message=f"Unexpected response to 'stack warning okay': '{message}'.")

            # Return early
            return

        # Clear the value of the 'front_text' field
        self.field_dict["front_text"]["widget"].clear(dispatch=False)

    @override
    def create_primary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
        Creates and places the primary widgets for the Flashcard form.

        This method creates and configures the required widgets for creating a Flashcard,
        including the stack selector, front text, and back text fields. These widgets are
        placed in the provided master container using the grid layout.

        Args:
            master (ScrolledFrame): The parent frame in which the primary widgets are to be placed.

        Returns:
            None
        """

        # Configure the weight of the 0th column to 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the 1st row to 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the weight of the 2nd row to 1
        master.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Dispatch the REQUEST_GET_ALL_STACKS event in the global namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_STACKS,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists
        if not notification:
            # Log a warning message
            self.logger.warning(message=f"Failed to dispatch the REQUEST_GET_ALL_STACKS event in the global namespace.")

            # Return early
            return

        # Create the 'stack' ComboboxField widget
        stack_field: ComboboxField = ComboboxField(
            label="Stack*: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[stack.name for stack in notification.get_one_and_only_result()],
        )

        # Place the 'stack' ComboboxField widget in the grid
        stack_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=0,
            sticky=NSEW,
        )

        # Style the 'stack' ComboboxField widget
        stack_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'stack' ComboboxField widget's button
        stack_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'stack' ComboboxField widget's combobox
        stack_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'stack' ComboboxField widget
        self._register_field(
            label="Stack*: ",
            field=stack_field,
            required=True,
        )

        # Create the 'back text' MultiLineTextField widget
        back_text_field: MultiLineTextField = MultiLineTextField(
            label="Back Text*: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'back text' MultiLineTextField widget in the grid
        back_text_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=1,
            sticky=NSEW,
        )

        # Style the 'back text' MultiLineTextField widget
        back_text_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'back text' MultiLineTextField widget's button
        back_text_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'back text' MultiLineTextField widget's text
        back_text_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'back text' MultiLineTextField widget
        self._register_field(
            label="Back Text*: ",
            field=back_text_field,
            required=True,
        )

        # Create the 'front text' MultiLineTextField widget
        front_text_field: MultiLineTextField = MultiLineTextField(
            label="Front Text*: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'front text' MultiLineTextField widget in the grid
        front_text_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=2,
            sticky=NSEW,
        )

        # Style the 'front text' MultiLineTextField widget
        front_text_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'front text' MultiLineTextField widget's button
        front_text_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'front text' MultiLineTextField widget's text
        front_text_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'front text' MultiLineTextField widget
        self._register_field(
            label="Front Text*: ",
            field=front_text_field,
            required=True,
        )

    @override
    def create_secondary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
        Creates and places optional secondary widgets for the Flashcard form.

        This method is intended to be overridden to include additional widgets such as tags,
        metadata, or advanced options. It is currently left empty.

        Args:
            master (ScrolledFrame): The parent frame in which the secondary widgets would be placed.

        Returns:
            None
        """

        pass
