"""
Author: lodego
Date: 2025-06-05
"""

import tkinter
import traceback

from datetime import datetime
from tkinter import ttk
from tkinter.constants import *
from typing import *

from core.difficulty import ImmutableDifficulty
from core.priority import ImmutablePriority
from core.stack import ImmutableStack, MutableStack
from core.subject import ImmutableSubject

from core.ui.fields.datetime_fields import DateSelectField
from core.ui.fields.select_fields import ComboboxField
from core.ui.fields.string_fields import (
    MultiLineTextField,
    SingleLineTextField,
    ReadOnlySingleLineTextField,
)
from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from utils.base_view_form import BaseViewForm
from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.utils import DateUtil


__all__: Final[List[str]] = ["StackViewForm"]


class StackViewForm(BaseViewForm):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        stack: Union[
            ImmutableStack,
            MutableStack,
        ],
        **kwargs
    ) -> None:
        """
        Initializes a new instance of the StackViewForm class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            stack (Union[ImmutableStack, MutableStack]): The stack instance.
            **kwargs: Additional keyword arguments to pass to the parent class constructor.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            entity=stack,
            master=master,
            **kwargs,
        )

    @override
    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects the subscriptions for this class.

        Args:
            None

        Returns:
            List[Dict[str, Any]]: The subscriptions for this class.
        """

        # Call the parent class' collect_subscriptions method
        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        # Return the list to the caller
        return subscriptions

    @override
    def create_details_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates the details frame widgets.

        Args:
            master (tkinter.Frame): The master widget.

        Returns:
            None
        """

        # Attempt to request all difficulties from the database via the dispatcher
        difficulties: List[ImmutableDifficulty] = self._request_entites(
            type="difficulty"
        )

        # Attempt to request all priorities from the database via the dispatcher
        priorities: List[ImmutablePriority] = self._request_entites(
            type="priority"
        )

        # Attempt to request all subjects from the database via the dispatcher
        subjects: List[ImmutableSubject] = self._request_entites(
            type="subject"
        )

        # Configure the passed tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Create the 'due by' SingleLineTextField widget
        due_by_field: DateSelectField = DateSelectField(
            display_name="Due By*: ",
            master=master,
            on_change_callback=self._on_field_change,
            value=self.entity.due_by,
        )

        # Configure the 'due by' SingleLineTextField widget
        due_by_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'due by' SingleLineTextField widget's 'clear button' widget
        due_by_field.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'due by' SingleLineTextField widget's 'select button' widget
        due_by_field.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'due by' SingleLineTextField widget's entry
        due_by_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Configure the 'due by' SingleLineTextField widget's label
        due_by_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'due by' SingleLineTextField widget in the grid
        due_by_field.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Configure the passed tkinter.Frame widget's 0th row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Register the 'due by' SingleLineTextField widget
        self._register_field(
            label="Due By*: ",
            field=due_by_field,
            required=True,
        )

        # Create the 'difficulty' ComboboxField widget
        difficulty_field: ComboboxField = ComboboxField(
            display_name="Difficulty*: ",
            master=master,
            on_change_callback=self._on_field_change,
            values=[difficulty.name for difficulty in difficulties],
            value=next(
                (
                    difficulty.name
                    for difficulty in difficulties
                    if difficulty.id == self.entity.difficulty
                ),
                None,
            ),
        )

        # Configure the 'difficulty' ComboboxField widget
        difficulty_field.configure(
            background=Constants.BLUE_GREY["700"],
        )

        # Configure the 'difficulty' ComboboxField widget's button
        difficulty_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'difficulty' ComboboxField widget's label
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
            row=1,
            sticky=NSEW,
        )

        # Configure the passed tkinter.Frame widget's 1st row to weight 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Register the 'difficulty' ComboboxField widget
        self._register_field(
            label="Difficulty*: ",
            field=difficulty_field,
            required=True,
        )

        # Create the 'priority' ComboboxField widget
        priority_field: ComboboxField = ComboboxField(
            display_name="Priority*: ",
            master=master,
            on_change_callback=self._on_field_change,
            values=[priority.name for priority in priorities],
            value=next(
                (
                    priority.name
                    for priority in priorities
                    if priority.id == self.entity.priority
                ),
                None,
            ),
        )

        # Configure the 'priority' ComboboxField widget
        priority_field.configure(
            background=Constants.BLUE_GREY["700"],
        )

        # Configure the 'priority' ComboboxField widget's button
        priority_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'priority' ComboboxField widget's label
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
            row=2,
            sticky=NSEW,
        )

        # Configure the passed tkinter.Frame widget's 2nd row to weight 0
        master.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Register the 'priority' ComboboxField widget
        self._register_field(
            label="Priority*: ",
            field=priority_field,
            required=True,
        )

        # Create the 'subject' ComboboxField widget
        subject_field: ComboboxField = ComboboxField(
            display_name="Subject*: ",
            master=master,
            on_change_callback=self._on_field_change,
            values=[subject.name for subject in subjects],
            value=next(
                (
                    subject.name
                    for subject in subjects
                    if subject.id == self.entity.subject
                ),
                None,
            ),
        )

        # Configure the 'subject' ComboboxField widget
        subject_field.configure(
            background=Constants.BLUE_GREY["700"],
        )

        # Configure the 'subject' ComboboxField widget's button
        subject_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'subject' ComboboxField widget's label
        subject_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'subject' ComboboxField widget in the grid
        subject_field.grid(
            column=0,
            row=3,
            sticky=NSEW,
        )

        # Configure the passed tkinter.Frame widget's 3rd row to weight 0
        master.grid_rowconfigure(
            index=3,
            weight=0,
        )

        # Register the 'subject' ComboboxField widget
        self._register_field(
            label="Subject*: ",
            field=subject_field,
            required=True,
        )

    @override
    def create_primary_tab_widgets(
        self,
        master: TabbedFrame,
    ) -> ScrolledFrame:
        """
        Creates the primary tab widgets.

        Args:
            master (TabbedFrame): The master widget.

        Returns:
            ScrolledFrame: The primary tab widgets.
        """

        # Configure the passed TabbedFrame widget's container's 0th column to weight 1
        master.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed TabbedFrame widget's container's 0th row to weight 1
        master.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            master=master.container,
        )

        # Configure the ScrolledFrame widget's container
        scrolled_frame.configure_container(
            background=Constants.BLUE_GREY["700"],
        )

        # Configure the ScrolledFrame widget's 0th column to weight 1
        scrolled_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the 'name' SingleLineTextField
        name_field: SingleLineTextField = SingleLineTextField(
            display_name="Name*: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            value=self.entity.name,
        )

        # Configure the 'name' SingleLineTextField's background
        name_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'name' SingleLineTextField's button
        name_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'name' SingleLineTextField's entry
        name_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Configure the 'name' SingleLineTextField's label
        name_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'name' SingleLineTextField in the grid
        name_field.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Configure the passed ScrolledFrame widget's container's 0th row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Register the 'name' SingleLineTextField
        self._register_field(
            label="Name*: ",
            field=name_field,
            required=True,
        )

        # Create the 'top' ttk.Separator widget
        top_separator: ttk.Separator = ttk.Separator(master=scrolled_frame.container)

        # Place the 'top' ttk.Separator widget in the grid
        top_separator.grid(
            column=0,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Configure the passed ScrolledFrame widget's container's 1st row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Create the 'description' MultiLineTextField
        description_field: MultiLineTextField = MultiLineTextField(
            display_name="Description: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            value=self.entity.description,
        )

        # Configure the 'description' MultiLineTextField's background
        description_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'description' MultiLineTextField's button
        description_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'description' MultiLineTextField's text
        description_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Configure the 'description' MultiLineTextField's label
        description_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'description' MultiLineTextField in the grid
        description_field.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 1st row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Register the 'description' MultiLineTextField
        self._register_field(
            label="Description: ",
            field=description_field,
        )

        # Create the 'center' ttk.Separator widget
        center_separator: ttk.Separator = ttk.Separator(master=scrolled_frame.container)

        # Place the 'center' ttk.Separator widget in the grid
        center_separator.grid(
            column=0,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 3rd row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=3,
            weight=0,
        )

        # Return the ScrolledFrame widget to the caller
        return scrolled_frame

    @override
    def create_secondary_tab_widgets(
        self,
        master: TabbedFrame,
    ) -> tkinter.Frame:
        """
        Creates the secondary tab widgets.

        Args:
            master (TabbedFrame): The master widget.

        Returns:
            tkinter.Frame: The secondary tab widgets.
        """

        # Configure the passed TabbedFrame widget's container's 0th column to weight 1
        master.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed TabbedFrame widget's container's 0th row to weight 1
        master.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            master=master.container,
        )

        # Configure the ScrolledFrame widget's container
        scrolled_frame.configure_container(
            background=Constants.BLUE_GREY["700"],
        )

        # Configure the ScrolledFrame widget's 0th column to weight 1
        scrolled_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Return the ScrolledFrame widget to the caller
        return scrolled_frame

    @override
    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates the top frame widgets.

        Args:
            master (tkinter.Frame): The master widget.

        Returns:
            ScrolledFrame: The top frame widgets.
        """

        pass
