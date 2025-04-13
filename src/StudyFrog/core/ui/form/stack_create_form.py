"""
Author: lodego
Date: 2025-04-13
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.ui.fields.boolean_fields import CheckbuttonField
from core.ui.fields.datetime_fields import DateSelectField
from core.ui.fields.select_fields import ComboboxField
from core.ui.fields.string_fields import MultiSelectAnswerField, MultiLineTextField

from core.ui.frames.frames import ScrolledFrame

from core.ui.notifications.notifications import ToplevelNotification

from utils.base_create_form import BaseCreateForm
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["StackCreateForm"]


class StackCreateForm(BaseCreateForm):
    """
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        **kwargs,
    ) -> None:
        """
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            namespace=namespace,
            **kwargs,
        )

    @override
    def _on_field_change(
        self,
        label: str,
        value: Any,
    ) -> None:
        """
        """

        # Call the super class' '_on_field_change' method with the passed arguments
        super()._on_field_change(
            label=label,
            value=value,
        )

    @override
    def create_primary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
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

        # Configure the weight of the 1st row to 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the weight of the 1st row to 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the weight of the 3rd row to 0
        master.grid_rowconfigure(
            index=3,
            weight=0,
        )

        # Configure the weight of the 4th row to 1
        master.grid_rowconfigure(
            index=4,
            weight=1,
        )

        # Dispatch the REQUEST_GET_ALL_STACKS event in the global namespace
        stack_notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_STACKS,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists
        if not stack_notification:
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
            values=[stack.name for stack in stack_notification.get_one_and_only_result()],
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

        # Dispatch the REQUEST_GET_ALL_DIFFICULTIES event in the global namespace
        difficulty_notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_DIFFICULTIES,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists
        if not difficulty_notification:
            # Log a warning message
            self.logger.warning(message=f"Failed to dispatch the REQUEST_GET_ALL_DIFFICULTIES event in the global namespace.")

            # Return early
            return

        # Create the 'difficulty' ComboboxField widget
        difficulty_field: ComboboxField = ComboboxField(
            label="Difficulty*: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[difficulty.name for difficulty in difficulty_notification.get_one_and_only_result()],
        )

        # Place the 'difficulty' ComboboxField widget in the grid
        difficulty_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=1,
            sticky=NSEW,
        )

        # Style the 'difficulty' ComboboxField widget
        difficulty_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'difficulty' ComboboxField widget's button
        difficulty_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'difficulty' ComboboxField widget's combobox
        difficulty_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'difficulty' ComboboxField widget
        self._register_field(
            label="Difficulty*: ",
            field=stack_field,
            required=True,
        )

        # Dispatch the REQUEST_GET_ALL_PRIORITIES event in the global namespace
        priority_notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_PRIORITIES,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists
        if not priority_notification:
            # Log a warning message
            self.logger.warning(message=f"Failed to dispatch the REQUEST_GET_ALL_PRIORITIES event in the global namespace.")

            # Return early
            return

        # Create the 'priority' ComboboxField widget
        priority_field: ComboboxField = ComboboxField(
            label="Priority*: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[priority.name for priority in priority_notification.get_one_and_only_result()],
        )

        # Place the 'priority' ComboboxField widget in the grid
        priority_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=2,
            sticky=NSEW,
        )

        # Style the 'priority' ComboboxField widget
        priority_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'priority' ComboboxField widget's button
        priority_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'priority' ComboboxField widget's combobox
        priority_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'priority' ComboboxField widget
        self._register_field(
            label="Priority*: ",
            field=stack_field,
            required=True,
        )

        # Create the 'due by' DateSelectField widget
        due_by_field: DateSelectField = DateSelectField(
            label="Due By*: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'due by' DateSelectField widget in the grid
        due_by_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=3,
            sticky=NSEW,
        )

        # Style the 'due by' DateSelectField widget
        due_by_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'due by' DateSelectField widget's 'clear button'
        due_by_field.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'due by' DateSelectField widget's entry
        due_by_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Style the 'due by' DateSelectField widget's label
        due_by_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the 'due by' DateSelectField widget's 'select button'
        due_by_field.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Register the 'due by' DateSelectField widget
        self._register_field(
            label="Due By*: ",
            field=due_by_field,
            required=True,
        )

        # Create the 'description' MultiLineTextField widget
        description_field: MultiLineTextField = MultiLineTextField(
            label="Description: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'description' MultiLineTextField widget in the grid
        description_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=4,
            sticky=NSEW,
        )

        # Style the 'description' MultiLineTextField widget
        description_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'description' MultiLineTextField widget's button
        description_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'description' MultiLineTextField widget's text
        description_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'description' MultiLineTextField widget
        self._register_field(
            label="Description: ",
            field=description_field,
            required=False,
        )

    @override
    def create_secondary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
        """

        pass
