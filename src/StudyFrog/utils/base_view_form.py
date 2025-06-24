"""
Author: lodego
Date: 2025-05-14
"""

import tkinter
import traceback

from datetime import datetime
from tkinter.constants import *
from tkinter import ttk
from typing import *

from core.answer import ImmutableAnswer, MutableAnswer
from core.flashcard import ImmutableFlashcard, MutableFlashcard
from core.note import ImmutableNote, MutableNote
from core.question import ImmutableQuestion, MutableQuestion
from core.stack import ImmutableStack, MutableStack

from core.ui.fields.string_fields import ReadOnlySingleLineTextField
from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.utils import DateUtil


__all__: Final[List[str]] = ["BaseViewForm"]


class BaseViewForm(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        entity: Union[
            Union[ImmutableAnswer, MutableAnswer],
            Union[ImmutableFlashcard, MutableFlashcard],
            Union[ImmutableNote, MutableNote],
            Union[ImmutableQuestion, MutableQuestion],
            Union[ImmutableStack, MutableStack],
        ],
        master: tkinter.Misc,
        **kwargs,
    ) -> None:
        """

        Args:
            dispatcher:
            entity:
            master:
            **kwargs:

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            **kwargs,
        )

        # Store the passed Dispatcher instance as an instance variable
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Initialize the entity instance variable to None
        self._entity: Optional[
            Union[
                Union[ImmutableAnswer, MutableAnswer],
                Union[ImmutableFlashcard, MutableFlashcard],
                Union[ImmutableNote, MutableNote],
                Union[ImmutableQuestion, MutableQuestion],
                Union[ImmutableStack, MutableStack],
            ]
        ] = self._process_entity(entity=entity)

        # Initialize this instance's Logger instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the timestamp instance variable to now
        self.timestamp: datetime = DateUtil.now()

        # Initialize the list of subscription UUIDs as an empty list
        self.subscriptions: Final[List[str]] = []

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Update the idletasks
        self.update_idletasks()

        # Subscribe to events
        self.subscribe_to_events()

    @property
    def entity(self) -> Union[
        Union[
            ImmutableAnswer,
            MutableAnswer,
            ImmutableFlashcard,
            MutableFlashcard,
            ImmutableNote,
            MutableNote,
            ImmutableQuestion,
            MutableQuestion,
            ImmutableStack,
            MutableStack,
        ]
    ]:
        """
        Returns the entity.

        Returns:
            Union[
                Union[
                    ImmutableAnswer,
                    MutableAnswer,
                    ImmutableFlashcard,
                    MutableFlashcard,
                    ImmutableNote,
                    MutableNote,
                    ImmutableQuestion,
                    MutableQuestion,
                    ImmutableStack,
                    MutableStack,
                ]
            ]
        """

        # Return the entity
        return self._entity

    def _check_timestamp(self) -> bool:
        """

        Args:
            None

        Returns:
            None
        """

        # Return True, if the timestamp is more than 3 minutes old, otherwise False
        return (
            DateUtil.calculate_duration(
                start=self.timestamp,
                what="minutes",
            )
            >= 3
        )

    def _on_field_change(
        self,
        label: str,
        value: Optional[Any] = None,
    ) -> None:
        """
        Handles changes to form fields.

        This method is triggered whenever a form field's value changes. It
        normalizes the label (removes suffixes like ': ' and '*: ', converts it to
        snake_case) and stores the new value in the internal `entity` instance
        variable.

        Args:
            label (str): The label of the changed field.
            value (Optional[Any]): The new value of the field.

        Returns:
            None
        """

        # Normalize the label and convert it to snake case
        label = Miscellaneous.any_to_snake(
            string=label.strip()
            .replace(
                "*",
                "",
            )
            .replace(
                ":",
                "",
            )
        )

        # Update the entity with the new value
        self.entity.set(
            name=label,
            value=value,
        )

        # Check if the timestamp is more than 3 minutes old
        if not self._check_timestamp():
            # Return early
            return

        # Update the entity (i.e., save it to the database)
        self._update_entity()

        # Update the timestamp
        self.timestamp = DateUtil.now()

    def _process_entity(
        self,
        entity: Union[
            Union[ImmutableAnswer, MutableAnswer],
            Union[ImmutableFlashcard, MutableFlashcard],
            Union[ImmutableNote, MutableNote],
            Union[ImmutableQuestion, MutableQuestion],
            Union[ImmutableStack, MutableStack],
        ],
    ) -> Union[
        MutableAnswer,
        MutableFlashcard,
        MutableNote,
        MutableQuestion,
        MutableStack,
    ]:
        """
        Processes the entity and returns a mutable version of it.

        Args:
            entity:

        Returns:
            Union[
                MutableAnswer,
                MutableFlashcard,
                MutableNote,
                MutableQuestion,
                MutableStack,
            ]
        """

        # Check, if the entity is not mutable
        if not entity.is_mutable():
            # Convert the (immutable) entity to a mutable type
            entity = entity.to_mutable()

        # Return the entity to the caller
        return entity

    def _register_field(
        self,
        label: str,
        field: tkinter.Misc,
        required: bool = False,
    ) -> None:
        """

        Args:
            label:
            field:
            required:

        Returns:
            None
        """

        pass

    def _request_entites(
        self,
        type: Literal[
            "answer",
            "difficulty",
            "flashcard",
            "note",
            "priority",
            "question",
            "stack",
            "subject",
            "tag",
            "teacher",
        ],
    ) -> List[Any]:
        """
        Requests all entities of the specified type from the dispatcher.

        Args:
            type (Literal[str]): The type of entity to request. Can be one of the following:
                "answer"
                "difficulty"
                "flashcard"
                "note"
                "priority"
                "question"
                "stack"
                "subject"
                "tag"
                "teacher"
            ]: The type of entity to request.

        Returns:
            List[Any]: The requested entities.

        Raises:
            ValueError: If the type is not one of the allowed values.
        """
        try:
            events: Dict[str, DispatcherEvent] = {
                "answer": Events.REQUEST_GET_ALL_ANSWERS,
                "difficulty": Events.REQUEST_GET_ALL_DIFFICULTIES,
                "flashcard": Events.REQUEST_GET_ALL_FLASHCARDS,
                "note": Events.REQUEST_GET_ALL_NOTES,
                "priority": Events.REQUEST_GET_ALL_PRIORITIES,
                "question": Events.REQUEST_GET_ALL_QUESTIONS,
                "stack": Events.REQUEST_GET_ALL_STACKS,
                "subject": Events.REQUEST_GET_ALL_SUBJECTS,
                "tag": Events.REQUEST_GET_ALL_TAGS,
                "teacher": Events.REQUEST_GET_ALL_TEACHERS,
            }

            # Check, if the passed type argument is valid
            if type not in events:
                # Log an error message
                self.logger.error(message=f"Invalid type argument: {type}")

                # Raise a ValueError
                raise ValueError(f"Invalid type argument: {type}")

            # Dispatch the event corresponding to the entity's type in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=events[type],
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check, if the notification exists or has irregularities
            if not notification or notification.has_irregularities():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch request get all event in the 'global' namespace."
                )

                # Return an empty list indicating that an exception has ocurred
                return []

            # Return the list of entities to the caller
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating that an exception has ocurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_request_entites' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return an empty list indicating that an exception has ocurred
            return []

    def _update_entity(self) -> None:
        """
        Updates the entity instance variable with the updated entity.

        Args:
            None

        Returns:
            None
        """

        # Dispatch the event corresponding to the entity's type in the 'global' namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_UPDATE,
            namespace=Constants.GLOBAL_NAMESPACE,
            update=self.entity,
        )

        # Check, if the notification exists or has irregularities
        if not notification or notification.has_irregularities():
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch request update event in the 'global' namespace."
            )

            # Return early
            return

        # Update the entity instance variable with the updated entity
        self.entity = notification.get_one_and_only_result().to_mutable()

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method creates an empty list of dictionaries containing event subscription configurations.
        This method should be implemented in any subclasses, that should handle events.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        # Initialize the list of subscriptions as an empty list
        subscriptions: List[Dict[str, Any]] = []

        # Return the list to the caller
        return subscriptions

    def configure_grid(self) -> None:
        """

        Args:
            None

        Returns:
            None
        """

        # Configure the BaseViewForm widget's 0th column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the BaseViewForm widget's 0th row to weight 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the BaseViewForm widget's 1st row to weight 0
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the BaseViewForm widget's 2nd row to weight 0
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """

        Args:
            master:

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """

        Args:
            master:

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 1st column to weight 0
        master.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the 'center left frame' tkinter.Frame widget
        center_left_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Create the 'center left frame' widgets
        self.create_center_left_frame_widgets(master=center_left_frame)

        # Place the 'center left frame' tkinter.Frame widget in the grid
        center_left_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the 'center right frame' tkinter.Frame widget
        center_right_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Place the 'center right frame' tkinter.Frame widget in the grid
        center_right_frame.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the 'center right frame' widgets
        self.create_center_right_frame_widgets(master=center_right_frame)

    def create_center_left_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """

        Args:
            master:

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a TabbedFrame widget
        tabbed_frame: TabbedFrame = TabbedFrame(master=master)

        # Configure the TabbedFrame widget's top frame
        tabbed_frame.configure_top_frame(background=Constants.BLUE_GREY["700"])

        # Place the TabbedFrame widget in the grid
        tabbed_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Add the 'primary attributes tab' widgets to the TabbedFrame widget
        tabbed_frame.add(
            label="Primary Attributes",
            widget=self.create_primary_tab_widgets(master=tabbed_frame),
        )

        # Configure the 'primary attributes' tab button
        tabbed_frame.configure_button(
            name="primary_attributes",
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Add the 'secondary attributes tab' widgets to the TabbedFrame widget
        tabbed_frame.add(
            label="Secondary Attributes",
            widget=self.create_secondary_tab_widgets(master=tabbed_frame),
        )

        # Configure the 'secondary attributes' tab button
        tabbed_frame.configure_button(
            name="secondary_attributes",
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

    def create_center_right_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates the center right frame widgets.

        Args:
            master (tkinter.Frame): The master widget.

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            horizontal_scrollbar=True,
            master=master,
        )

        # Configure the ScrolledFrame widget's container
        scrolled_frame.configure_container(background=Constants.BLUE_GREY["700"])

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

        # Create the 'ID' ReadOnlySingleLineTextField widget
        id_field: ReadOnlySingleLineTextField = ReadOnlySingleLineTextField(
            display_name="ID*: ",
            master=scrolled_frame.container,
            value=self.entity.id,
        )

        # Configure the 'ID' ReadOnlySingleLineTextField widget
        id_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'ID' ReadOnlySingleLineTextField widget's button
        id_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'ID' ReadOnlySingleLineTextField widget's label
        id_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'ID' ReadOnlySingleLineTextField widget in the grid
        id_field.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 0th row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Create the 'created at' ReadOnlySingleLineTextField widget
        created_at_field: ReadOnlySingleLineTextField = ReadOnlySingleLineTextField(
            display_name="Created At*: ",
            master=scrolled_frame.container,
            value=DateUtil.object_to_string(
                datetime_or_date=self.entity.created_at,
                format="%Y-%m-%d",
            ),
        )

        # Configure the 'created at' ReadOnlySingleLineTextField widget
        created_at_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'created at' ReadOnlySingleLineTextField widget's button
        created_at_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'created at' ReadOnlySingleLineTextField widget's label
        created_at_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'created at' ReadOnlySingleLineTextField widget in the grid
        created_at_field.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 1th row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Create the 'updated at' ReadOnlySingleLineTextField widget
        updated_at_field: ReadOnlySingleLineTextField = ReadOnlySingleLineTextField(
            display_name="Updated At*: ",
            master=scrolled_frame.container,
            value=DateUtil.object_to_string(
                datetime_or_date=self.entity.updated_at,
                format="%Y-%m-%d",
            ),
        )

        # Configure the 'updated at' ReadOnlySingleLineTextField widget
        updated_at_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'updated at' ReadOnlySingleLineTextField widget's button
        updated_at_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'updated at' ReadOnlySingleLineTextField widget's label
        updated_at_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'updated at' ReadOnlySingleLineTextField widget in the grid
        updated_at_field.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 2nd row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Create the 'top separator' ttk.Separator widget
        top_separator: ttk.Separator = ttk.Separator(
            master=scrolled_frame.container,
            orient=HORIZONTAL,
        )

        # Place the 'top separator' ttk.Separator widget in the grid
        top_separator.grid(
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

        # Configure the ScrolledFrame widget's container's 4th row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=4,
            weight=0,
        )

        # Create the 'details' ttk.Label widget
        details_label: ttk.Label = ttk.Label(
            anchor=CENTER,
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            justify=LEFT,
            master=scrolled_frame.container,
            text="Details: ",
        )

        # Place the 'details' ttk.Label widget in the grid
        details_label.grid(
            column=0,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 4th row to weight 0
        scrolled_frame.container.grid_rowconfigure(
            index=4,
            weight=0,
        )

        # Create a tkinter.Frame widget
        frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=scrolled_frame.container,
        )

        # Configure the tkinter.Frame widget's 0th column to weight 1
        frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Place the tkinter.Frame widget in the grid
        frame.grid(
            column=0,
            row=5,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget's container's 5th row to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=5,
            weight=1,
        )

        # Create the 'details' frame widgets
        self.create_details_frame_widgets(master=frame)

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

        raise NotImplementedError(
            f"The 'create_details_frame_widgets' method must be implemented in the {self.__class__.__name__} class."
        )

    def create_primary_tab_widgets(
        self,
        master: TabbedFrame,
    ) -> tkinter.Frame:
        """

        Args:
            master:

        Returns:
            tkinter.Frame:
        """

        raise NotImplementedError(
            f"The 'create_primary_tab_widgets' method must be implemented in the {self.__class__.__name__} class."
        )

    def create_secondary_tab_widgets(
        self,
        master: TabbedFrame,
    ) -> tkinter.Frame:
        """

        Args:
            master:

        Returns:
            tkinter.Frame:
        """

        raise NotImplementedError(
            f"The 'create_secondary_tab_widgets' method must be implemented in the {self.__class__.__name__} class."
        )

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """

        Args:
            master:

        Returns:
            None
        """

        pass

    def create_widgets(self) -> None:
        """

        Args:
            None

        Returns:
            None
        """

        # Create the 'top frame' tkinter.Frame widget
        top_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'top frame' in the grid
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the top frame widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the 'center frame' tkinter.Frame widget
        center_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'center frame' in the grid
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the center frame widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the 'bottom frame' tkinter.Frame widget
        bottom_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'bottom frame' in the grid
        bottom_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the bottom frame widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

    @override
    def destroy(self) -> None:
        """
        Cleans up resources and unsubscribes from events.

        This method attempts to unsubscribe from all events
        and calls the parent class's destroy method to clean
        up resources. Logs any exceptions that occur.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the destroy process.
        """
        try:
            # Attempt to unsubscribe from all events
            self.unsubscribe_from_events()

            # Log an info message
            self.logger.info(
                message=f"Unsubscribed from all events. Destroying '{self.__class__.__name__}' instance..."
            )

            # Call the parent class's destroy method
            super().destroy()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'destroy' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def subscribe_to_events(self) -> None:
        """
        Subscribes to all events in the subscriptions dictionary.

        This method iterates over the events and functions in the subscriptions
        dictionary and registers them with the dispatcher. It also stores the
        UUIDs of the subscriptions in the subscriptions list.

        Returns:
            None

        Raises:
            Exception: If an error occurs while subscribing to events.
        """
        try:
            # Create a dictionary of events and functions
            subscriptions: List[Dict[str, Any]] = self.collect_subscriptions()

            # Iterate over the events and functions in the subscriptions dictionary
            for subscription in subscriptions:
                # Store the UUID of the subscription in the subscriptions list
                self.subscriptions.append(
                    self.dispatcher.register(
                        event=subscription["event"],
                        function=subscription["function"],
                        namespace=subscription["namespace"],
                        persistent=subscription["persistent"],
                    )
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def unsubscribe_from_events(self) -> None:
        """
        Unsubscribes from all events subscribed in the edit UI.

        This method iterates over the UUIDs in the subscriptions dictionary and
        unregisters the event handlers associated with each UUID.

        Returns:
            None

        Raises:
            Exception: If an error occurs while unsubscribing from events.
        """
        try:
            # Iterate over the UUIDs in the subscriptions dictionary
            for uuid in self.subscriptions:
                # Unregister the handler for the given UUID
                self.dispatcher.unregister(uuid=uuid)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unsubscribe_from_events' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e
