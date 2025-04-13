"""
Author: lodego
Date: 2025-04-13
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.ui.fields.boolean_fields import CheckbuttonField
from core.ui.fields.select_fields import ComboboxField
from core.ui.fields.string_fields import MultiSelectAnswerField, MultiLineTextField

from core.ui.frames.frames import ScrolledFrame

from core.ui.notifications.notifications import ToplevelNotification

from utils.base_create_form import BaseCreateForm
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["QuestionCreateForm"]


class QuestionCreateForm(BaseCreateForm):
    """
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
    ) -> None:
        """
        """

        # Initialize the answer widgets dictionary instance variable as an empty dictionary
        self.answer_widgets: Final[Dict[str, Any]] = {}

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            namespace=namespace,
        )

    def _clear_answers_frame(self) -> None:
        """
        """

        # Obtain a list of child widgets from the 'answers frame' tkinter.Frame widget
        children: List[tkinter.Misc] = self.answers_frame.winfo_children()
        
        if len(children) == 0:
            # Return early
            return

        # Iterate over the list if child widget
        for child in children:
            # Destroy the child
            child.destroy()

    def _on_add_answer_button_click(self) -> None:
        """
        """

        # Create a unique label text from the number of child widgets in the 'answers frame' frame widget
        label: str = f"Answer {len(self.answers_frame.winfo_children())}*: "

        # Create a MultiSelectAnswerField widget
        multi_select_answer_field: MultiSelectAnswerField = MultiSelectAnswerField(
            label=label,
            master=self.answers_frame,
            namespace=self.namespace,
            on_change_callback=self._on_answer_change,
        )

        # Place the MultiSelectAnswerField widget in the grid
        multi_select_answer_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=len(self.answers_frame.winfo_children()),
            sticky=NSEW,
        )

        # Style the MultiSelectAnswerField widget
        multi_select_answer_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the MultiSelectAnswerField widget's button widget
        multi_select_answer_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the MultiSelectAnswerField widget's entry widget
        multi_select_answer_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Add the MultiSelectAnswerField widget to the answers widget dictionary instance variable
        self.answer_widgets["multi_select"][label] = multi_select_answer_field

    def _on_answer_change(
        self,
        label,
        value: Any,
    ) -> None:
        """
        """

        # Obtain the current question type from the 'value_dict' dictionary instance variable
        question_type: str = Miscellaneous.any_to_snake(string=self.value_dict["question_type"])

        # Check, if the 'answers' key exists in the 'value_dict' dictionary instance variable
        if "answers" not in self.value_dict:
            # Initialize an empty dictionary in the value_dict associated to the 'answers' key
            self.value_dict["answers"] = {}

        # Check, if the current question type exists under the 'answers' key in the 'value_dict' dictionary instance variable
        if question_type not in self.value_dict["answers"]:
            # Initialize an empty dictionary in the value_dict associated to the 'answers' key
            self.value_dict["answers"] = {}

        # Check, if the current question type is 'Multiple Select' or 'Single Select'
        if question_type in [
            "multi_select",
            "single_select",
        ]:
            self.value_dict["answers"][question_type][Miscellaneous.find_match(pattern=r"([0-9]+)", string=label)] = value

        # Check, if the question type is 'Open Answer' or 'True of False'
        elif question_type == [
            "open_answer",
            "true_or_false",
        ]:
            self.value_dict["answers"][question_type] = value

        # Handle any other case
        else:
            # Log a warning message
            self.logger.warning(message=f"Unsuported question type '{question_type}'.")
            
            # Return
            return

    @override
    def _on_field_change(
        self,
        label: str,
        value: Any,
    ) -> None:
        """
        """

        # Call the parent class' '_on_field_change' method with the passed arguments
        super()._on_field_change(
            label=label,
            value=value,
        )

        # Check, if the changed field is not 'question type'
        if label != "question_type" or len(self.answer_widgets) == 0:
            # Return early
            return

        # Prompt the user
        answer: bool = ToplevelNotification.yes_no(
            message="It seems as though you've already added answers. Switching the answer mode will remove any previous answers. Do you wish to proceed?",
            on_click_callback=self._on_question_type_warning_yes_no,
            title="",
        )

        # Check, if the user answered with 'cancel'
        if not answer:
            # Return early
            return

        # Process the 'question type' ComboboxField widget change
        self._on_question_type_change(question_type=value)

    def _on_question_type_change(
        self,
        question_type: str,
    ) -> None:
        """
        """

        # Clear the answers frame
        self._clear_answers_frame()

        # Clear the answers dictionary instance variable
        self.answers.clear()

        # Convert the passed question type to a snake case represenation
        question_type = Miscellaneous.any_to_snake(string=question_type)

        # Check, if the question type is 'Multiple Select' or 'Single Select'
        if question_type in [
            "multiple_select",
            "single_select",
        ]:

            # Create a tkinter.Button widget
            button: tkinter.Button = tkinter.Button(
                background=Constants.BLUE_GREY["700"],
                command=self._on_add_answer_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=self.answers_frame,
                text="Add Answer",
            )

            # Place the tkinter.Button widget in the grid
            button.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
            )

            # Initialize an empty dictionary under the passed question type
            self.answer_widgets[question_type] = {}

        # Check, if the question type is 'Open Answer'
        elif question_type == "open_answer":

            # Create a MultiLineTextField widget
            multi_line_text_field: MultiLineTextField = MultiLineTextField(
                label="Answer Text*: ",
                master=self.answers_frame,
            )

            # Place the MultiLineTextField widget in the grid
            multi_line_text_field.grid(
                column=0,
                padx=10,
                pady=10,
                row=0,
                sticky=NSEW,
            )

            # Style the MultiLineTextField widget
            multi_line_text_field.configure(background=Constants.BLUE_GREY["700"])

            # Style the MultiLineTextField widget's button widget
            multi_line_text_field.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the MultiLineTextField widget's text widget
            multi_line_text_field.configure_text(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
            )

            # Add the MultiLineTextField widget to the answers widget dictionary instance variable
            self.answer_widgets[question_type] = multi_line_text_field

        # Check, if the question type is 'True or False'
        elif question_type == "true_or_false":

            # Create a CheckbuttonField widget
            checkbutton_field: CheckbuttonField = CheckbuttonField(
                label="Is correct? ",
                master=self.answers_frame,
            )

            # Place the CheckbuttonField widget in the grid
            checkbutton_field.grid(
                column=0,
                row=0,
            )

            # Add the CheckbuttonField widget to the answers widget dictionary instance variable
            self.answer_widgets[question_type] = checkbutton_field

        # Handle any other case
        else:
            # Log a warning message
            self.logger.warning(message=f"Unsuported question type '{question_type}'.")
            
            # Return
            return

    def _on_question_type_warning_yes_no(
        self,
        message: str,
    ) -> bool:
        """
        """

        # Return True if the messge equals 'yes' otherwise False
        return message == "yes"

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

        # Configure the weight of the 1st row to 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the weight of the 2nd row to 0
        master.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Configure the weight of the 3rd row to 1
        master.grid_rowconfigure(
            index=3,
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

        # Create the 'question text' MultiLineTextField widget
        question_text_field: MultiLineTextField = MultiLineTextField(
            label="Question Text*: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'question text' MultiLineTextField widget in the grid
        question_text_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=1,
            sticky=NSEW,
        )

        # Style the 'question text' MultiLineTextField widget
        question_text_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'question text' MultiLineTextField widget's button
        question_text_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'question text' MultiLineTextField widget's text
        question_text_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'question text' MultiLineTextField widget
        self._register_field(
            label="Question Text*: ",
            field=question_text_field,
            required=True,
        )

        # Create the 'question type' ComboboxField widget
        question_type_field: ComboboxField = ComboboxField(
            label="Question Type*: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=Constants.QUESTION_TYPES,
        )

        # Place the 'question type' ComboboxField widget in the grid
        question_type_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=2,
            sticky=NSEW,
        )

        # Style the 'question type' ComboboxField widget
        question_type_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'question type' ComboboxField widget's button
        question_type_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'question type' ComboboxField widget's combobox
        question_type_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'question type' ComboboxField widget
        self._register_field(
            label="Question Type*: ",
            field=question_type_field,
            required=True,
        )

        # Create the 'answers frame' tkinter.Frame widget
        self.answers_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'answers frame' tkinter.Frame widget in the grid
        self.answers_frame.grid(
            column=0,
            padx=10,
            pady=10,
            row=3,
            sticky=NSEW,
        )

    @override
    def create_secondary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
        """

        pass
