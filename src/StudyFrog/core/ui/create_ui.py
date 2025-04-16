"""
Author: lodego
Date: 2025-02-11
"""

import traceback
import tkinter

from tkinter.constants import *
from tkinter import ttk
from typing import *

from core.ui.notifications.notifications import (
    ToplevelNotification,
    ToplevelToastNotification,
)

from core.ui.form.flashcard_create_form import FlashcardCreateForm
from core.ui.form.question_create_form import QuestionCreateForm
from core.ui.form.stack_create_form import StackCreateForm

from core.ui.fields.select_fields import CheckbuttonField, ComboboxField

from core.ui.ui_builder import UIBuilder

from core.answer import AnswerFactory, ImmutableAnswer
from core.difficulty import ImmutableDifficulty
from core.flashcard import FlashcardFactory, ImmutableFlashcard
from core.priority import ImmutablePriority
from core.question import MutableQuestion, QuestionFactory, ImmutableQuestion
from core.setting import SettingService
from core.stack import StackFactory, ImmutableStack, MutableStack
from core.status import ImmutableStatus

from utils.base_ui import BaseUI

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager


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

        # Initialize the form instance variable as None
        self.form: Optional[tkinter.Misc] = None

        # Initialize the namespace instance variable
        self.namespace: Final[str] = "CREATE_UI"

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
            self.type_field.set(
                dispatch=False,
                value=type.capitalize(),
            )

        # Call the on_combobox_select method
        self.on_type_field_change(
            label="Type: ",
            value=self.type_field.get()[1],
        )

    def _create_entity(
        self,
        entity: Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableStack,
        ],
        event: DispatcherEvent,
    ) -> Optional[
        Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableStack,
        ]
    ]:
        """ """
        try:
            # Dispatch the passed REQUEST_CREATE event in the global namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=event,
                **{
                    Miscellaneous.any_to_snake(
                        string=entity.__class__.__name__
                    ): entity,
                },
            )

            # Check, if the notification exists or has no errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch '{event.name}' to 'global' namespace with '{entity.__repr__()}' entity."
                )

                # Return the entity
                return entity

            # Return the created entity to the caller
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to call '_create_entity' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _get_difficulty(
        self,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """ """
        try:
            # Obtain the 'difficulty' value from the kwargs dictionary
            difficulty: Optional[Union[ImmutableDifficulty, int, str]] = kwargs.get(
                "difficulty",
                None,
            )

            # Check, if the difficulty value exists and is not an empty string
            if difficulty and difficulty != "":
                # Request the difficulty ImmutableDifficulty object from the database
                difficulty = self._request_entity(
                    event=Events.REQUEST_DIFFICULTY_LOOKUP,
                    name=difficulty,
                )

                # Add the ID of the difficulty ImmutableDifficulty object to the kwargs dictionary
                kwargs["difficulty"] = difficulty.id

            # Return the kwargs to the caller
            return kwargs
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to call '_get_difficulty' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _get_priority(
        self,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """ """
        try:
            # Obtain the 'priority' value from the kwargs dictionary
            priority: Optional[Union[ImmutablePriority, int, str]] = kwargs.get(
                "priority",
                None,
            )

            # Check, if the priority value exists and is not an empty string
            if priority and priority != "":
                # Request the priority ImmutablePriority object from the database
                priority = self._request_entity(
                    event=Events.REQUEST_PRIORITY_LOOKUP,
                    name=priority,
                )

                # Add the ID of the priority ImmutablePriority object to the kwargs dictionary
                kwargs["priority"] = priority.id

            # Return the kwargs to the caller
            return kwargs
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to call '_get_priority' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _get_stack(
        self,
        field: str,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """ """
        try:
            # Obtain the 'field' value from the kwargs dictionary
            stack: Optional[Union[ImmutableStack, int, str]] = kwargs.get(
                field,
                None,
            )

            # Check, if the field value exists and is not an empty string
            if stack and stack != "":
                # Request the field ImmutableStack object from the database
                stack = self._request_entity(
                    event=Events.REQUEST_STACK_LOOKUP,
                    name=stack,
                )

                # Add the ID of the field ImmutableStack object to the kwargs dictionary
                kwargs[field] = stack.id

            # Return the kwargs to the caller
            return kwargs
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to call '_get_stack' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _get_status(
        self,
        name: str,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """ """
        try:
            # Request the ImmutableStatus object from the database
            status: Optional[Union[ImmutableStatus, int, str]] = self._request_entity(
                event=Events.REQUEST_STATUS_LOOKUP,
                name=name,
            )

            # Check, if the status ImmutableStatus object exists
            if not status:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to fetch ImmutableStatus object with name '{name}' from the database."
                )

                # Return the kwargs to the caller early
                return kwargs

            # Add the ID of the ImmutableStatus object to the kwargs dictionary
            kwargs["status"] = status.id

            # Return the kwargs to the caller
            return kwargs
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to call '_get_status' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _request_entity(
        self,
        event: DispatcherEvent,
        **kwargs,
    ) -> Optional[ImmutableDifficulty]:
        """ """
        try:
            # Dispatch the passed event in the 'global' namespace along with the passed keyword arguments
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=event,
                namespace=Constants.GLOBAL_NAMESPACE,
                **kwargs,
            )

            # Check, if the notification does not exist or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to notify {event.__repr__()} event for 'global' namespace in {self.__class__.__name__} class."
                )

                # Return early
                return

            # Return the one and only result
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_request_entity' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

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
        children: Optional[List[tkinter.Misc]] = self.center_frame.winfo_children()

        # Check if there are any children
        if not children or len(children) == 0:
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

        # Configure the top frame widget's 0th column to weight 0
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the top frame widget's 0th row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the top frame widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create a separator widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=master,
            orient=HORIZONTAL,
        )

        # Place the separator widget in the grid
        separator.grid(
            column=0,
            padx=5,
            pady=10,
            row=0,
            sticky=NSEW,
        )

        # Create a frame widget
        frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Place the frame widget in the grid
        frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        frame.grid_columnconfigure(
            index=1,
            weight=1,
        )

        frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the "Left Frame" frame widget
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=frame,
        )

        # Configure the "Left Frame" frame widget's 1st column to weight 1
        left_frame.grid_columnconfigure(
            index=0,
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
        self.create_another: CheckbuttonField = CheckbuttonField(
            label="Create another? ",
            master=left_frame,
            namespace=self.namespace,
        )

        # Configure the background of the "Create another" combobox field widget
        self.create_another.configure(background=Constants.BLUE_GREY["700"])

        # Configure the checkbutton of the "Create another" checkbutton field widget
        self.create_another.configure_checkbutton(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the label of the "Create another" checkbutton field widget
        self.create_another.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the "Create Another" check button widget in the "Left Frame"
        self.create_another.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=W,
        )

        # Create the "Right Frame" frame widget
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=frame,
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
                Constants.DEFAULT_FONT_FAMILY,
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
            sticky=E,
        )

        # Create the "Create" button widget
        create_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_create_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
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
            sticky=E,
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

        # Configure the top frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the top frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the top frame widget's 1st row to weight 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Define the values for the type field
        values: List[str] = [
            "Flashcard",
            "Question",
            "Stack",
        ]

        # Create the "Type" combobox field widget
        # This field allows the user to select the type of object to create
        self.type_field: ComboboxField = ComboboxField(
            label="Type: ",
            master=master,
            namespace=self.namespace,
            on_change_callback=self.on_type_field_change,
            readonly=True,
            value=Miscellaneous.select_random(iterable=values),
            values=values,
        )

        # Configure the background of the "Type" combobox field widget
        self.type_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the button of the "Type" combobox field widget
        self.type_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the combobox of the "Type" combobox field widget
        self.type_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            state="readonly",
        )

        # Configure the label of the "Type" combobox field widget
        self.type_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the "Type" combobox field widget in the top frame
        self.type_field.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create a separator widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=master,
            orient=HORIZONTAL,
        )

        # Place the separator widget in the grid
        separator.grid(
            column=0,
            padx=5,
            pady=10,
            row=1,
            sticky=NSEW,
        )

    def handle_answer_creation(
        self,
        **kwargs,
    ) -> Optional[ImmutableAnswer]:
        """ """
        try:
            # Obtain the type from the kwargs
            type: Optional[str] = kwargs.get("type")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_answer_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def handle_flashcard_creation(
        self,
        **kwargs,
    ) -> Optional[ImmutableFlashcard]:
        """ """
        try:
            # Obtain the type from the kwargs
            type: Optional[str] = kwargs.get("type")

            # Check, if the 'type' keyword has been passed to this method
            if not type:
                pass
            else:
                # Remove the 'type' key from the dictionary
                kwargs.pop("type")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_flashcard_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def handle_question_creation(
        self,
        **kwargs,
    ) -> Optional[ImmutableQuestion]:
        """ """
        try:
            # Obtain the type from the kwargs
            type: Optional[str] = kwargs.get("type")

            # Check, if the 'type' keyword has been passed to this method
            if not type:
                pass
            else:
                # Remove the 'type' key from the dictionary
                kwargs.pop("type")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_question_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def handle_stack_creation(
        self,
        **kwargs,
    ) -> Optional[ImmutableStack]:
        """ """
        try:
            # Obtain the type from the kwargs
            type: Optional[str] = kwargs.get(
                "type",
                None,
            )

            # Check, if the 'type' keyword has been passed to this method
            if not type:
                # Return early
                return

            # Remove the 'type' key from the dictionary
            kwargs.pop("type")

            # Check, if the 'ancestor' key is assciated to any (non-empty string) value
            if (
                kwargs.get(
                    "ancestor",
                    None,
                )
                is not None
            ):
                # Update the kwargs with the ancestor stack's ID
                kwargs.update(
                    self._get_stack(
                        field="ancestor",
                        **kwargs,
                    )
                )

            # Check, if the 'difficulty' key is assciated to any (non-empty string) value
            if (
                kwargs.get(
                    "difficulty",
                    None,
                )
                is not None
            ):
                # Update the kwargs with the difficulty's ID
                kwargs.update(
                    self._get_difficulty(
                        **kwargs,
                    )
                )

            # Check, if the 'priority' key is assciated to any (non-empty string) value
            if (
                kwargs.get(
                    "priority",
                    None,
                )
                is not None
            ):
                # Update the kwargs with the priority's ID
                kwargs.update(
                    self._get_priority(
                        **kwargs,
                    )
                )

            # Update the kwargs with the priority's ID
            kwargs.update(
                self._get_status(
                    name="",
                    **kwargs,
                )
            )

            # Attempt to create the ImmutableStack object in the database and update the reference
            stack: ImmutableStack = self._create_entity(
                entity=UnifiedObjectFactory.create_stack(**kwargs),
                event=Events.REQUEST_STACK_CREATE,
            )

            # Check, if the stack was created succcessfully (i.e. if it has an ID)
            if not stack.get(
                default=None,
                name="id",
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create ImmutableStack object in the database. This is likely due to a bug."
                )

                # Return early
                return

            # Dispatch the STACK_CREATED event in the global namespace
            self.dispatcher.dispatch(
                event=Events.STACK_CREATED,
                namespace=Constants.GLOBAL_NAMESPACE,
                stack=stack,
            )

            # Return the stack to the caller
            return stack
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'handle_stack_creation' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

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
        try:
            # Check, if form validation is successfull
            if not self.form or not self.validate_form():
                # Return early
                return

            # Get the data from the form
            form_data: Dict[str, Any] = self.form.get()

            # Obtain the type of the entity to be created
            type: str = Miscellaneous.any_to_snake(string=form_data["type"]["value"])

            # Call the handler corresponding to the type of the entity to be created
            entity: Optional[Any] = getattr(
                self,
                f"handle_{type}_creation",
            )(**{key: form_data[key]["value"] for key in sorted(form_data.keys())})

            # Check, if the entity exists
            if not entity:
                # Log a warning message
                self.logger.warning(message=f"")

                # Notify the user
                ToplevelToastNotification(
                    message=f"Failed to create {Miscellaneous.snake_to_camel(string=form_data["type"]["value"])} in the database. Please check the logs for additional information.",
                    title=f"{Miscellaneous.snake_to_camel(string=form_data["type"]["value"])} could no be created successfully",
                )

                # Return early
                return

            # Display a toast message to the user
            ToplevelToastNotification(
                title=f"{Miscellaneous.snake_to_camel(string=form_data["type"]["value"])} created successfully",
                message=f"{Miscellaneous.snake_to_camel(string=form_data["type"]["value"])} with ID {entity.id} created successfully.",
            )

            # Check, if the 'Create another' CheckbuttonField' value is False
            if not self.create_another.get()[1]:
                # Check if the master widget is of type toplevel
                if isinstance(
                    self.master,
                    tkinter.Toplevel,
                ):
                    # Destroy the toplevel widget
                    self.master.destroy()

            # Clear the current form
            self.form.clear()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_create_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def on_type_field_change(
        self,
        label: str,
        value: str,
    ) -> None:
        """
        Handles the selection event of the combobox widget.

        Args:
            label (str): The label of the combobox widget.
            value (str): The value of the combobox widget.

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

        self.center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        self.center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a new form widget based on the selected value
        self.form = forms[value.lower()](
            dispatcher=self.dispatcher,
            master=self.center_frame,
            namespace=self.namespace,
        )

        # Place the new form widget in the grid
        self.form.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Log an info message
        self.logger.info(
            message=f"Created form widget for '{value}' type based on current '{label.replace(": ", "")}' field selection."
        )

    def validate_form(self) -> None:
        """ """

        # Obtain a validation report from the form as a dictionary
        report: Dict[str, bool] = self.form.validate_form()

        # Check, if the overall result of the report is True
        if report["result"]:
            # Return True early
            return True

        # Display a notification to the user
        ToplevelNotification.okay(
            title="Error during validation",
            message=f"It seems that at least one required field has no value.\n\nPlease review:\n {"\n\t*".join([Miscellaneous.snake_to_pascal(string=key) for key in report["fields"].keys() if not report["fields"][key]])}",
        )

        # Return False
        return False
