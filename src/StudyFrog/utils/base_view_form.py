"""
Author: lodego
Date: 2025-05-14
"""

import tkinter

from datetime import datetime
from tkinter.constants import *
from typing import *

from core.answer import ImmutableAnswer, MutableAnswer
from core.flashcard import ImmutableFlashcard, MutableFlashcard
from core.note import ImmutableNote, MutableNote
from core.question import ImmutableQuestion, MutableQuestion
from core.stack import ImmutableStack, MutableStack

from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


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
        self.timestamp: datetime = Miscellaneous.get_current_datetime()

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

    def _check_timestamp(self) -> bool:
        """

        Args:
            None

        Returns:
            None
        """

        # Return True, if the timestamp is more than 3 minutes old, otherwise False
        return (
            Miscellaneous.calculate_duration(
                as_="minutes",
                end=Miscellaneous.get_current_datetime(),
                start=self.timestamp,
            )
            >= 3
        )

    def _on_field_change(
        self,
        label: str,
        value: Optional[Any] = None,
    ) -> None:
        """

        Args:
            label:
            value:

        Returns:
            None
        """

        pass

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
    ) -> None:
        """

        Args:
            label:
            field:

        Returns:
            None
        """

        pass

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

        # Check, if the notification exists or has errors
        if not notification or notification.has_errors():
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

        # Add the 'secondary attributes tab' widgets to the TabbedFrame widget
        tabbed_frame.add(
            label="Secondary Attributes",
            widget=self.create_secondary_tab_widgets(master=tabbed_frame),
        )

    def create_center_right_frame_widgets(
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

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
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
