"""
Author: lodego
Date: 2025-03-24
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.flashcard import ImmutableFlashcard
from core.setting import SettingService

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger


__all__: Final[List[str]] = ["FlashcardLearningView"]


class FlashcardLearningView(tkinter.Frame):
    """
    Represents the flashcard learning view component.

    This class is responsible for initializing and managing the UI
    for displaying and interacting with flashcards during the learning
    process. It handles event subscriptions, grid configuration, and
    widget creation.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        flashcard (ImmutableFlashcard): The flashcard instance.
        logger (Logger): Logger instance associated with this class.
        setting_service (SettingService): The setting service instance.
        side (Literal["back", "front"]): The current side of the flashcard to display.
        subscriptions (List[str]): UUIDs of active event subscriptions.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        flashcard: ImmutableFlashcard,
        master: tkinter.Misc,
        namespace: str,
        setting_service: SettingService,
    ) -> None:
        """
        Initializes a new instance of the FlashcardLearningView class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            flashcard (ImmutableFlashcard): The flashcard instance.
            master (tkinter.Misc): The parent widget.
            namespace (str): The namespace.
            setting_service (SettingService): The setting service instance.
        """

        # Configure the grid of the master widget's 0th column to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the master widget's 0th row to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a logger instance
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize a list to store bindings
        self.bindings: Final[List[str]] = []

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed flashcard instance in an instance variable
        self.flashcard: ImmutableFlashcard = flashcard

        # Store the passed namespace in an instance variable
        self.namespace: str = namespace

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Initialize the side of the flashcard
        # The side is used to determine which side of the flashcard should be displayed
        self.side: Literal["back", "front"] = "front"

        # Initialize a list to store subscription UUIDs
        # The subscription UUIDs are used to keep track of the subscriptions to events
        self.subscriptions: List[str] = []

        # Call the parent class constructor
        super().__init__(
            master=master,
            name="flashcard_learning_view",
        )

        # Style the frame
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid of the flashcard learning form widget
        # This method is responsible for configuring the grid layout of the frame
        self.configure_grid()

        # Create the widgets of the flashcard learning form
        # This method is responsible for creating the widgets that are used to display the flashcard
        self.create_widgets()

        # Subscribe to events
        self.subscribe_to_events()

        # Bind the space key to the flip method
        self.bind_keys()

        # Place the flashcard learning form widget in the parent widget
        # This method is responsible for placing the frame in the parent widget
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def bind_keys(self) -> None:
        """
        Binds the space key to the flip method.

        This method binds the space key to the flip method, which is used to flip the flashcard.

        Returns:
            None
        """

        # Bind the space key to the flip method
        self.bindings.append(
            self.bind_all(
                func=lambda event: self.flip(),
                sequence="<space>",
            )
        )

    def clear(self) -> None:
        """
        Clears the content of the flashcard learning view widget.

        This method clears the content of the flashcard learning view widget by destroying
        all its children widgets.

        Returns:
            None
        """

        # Attempt to get a list of all children widgets
        children: Optional[List[tkinter.Misc]] = self.winfo_children()

        # Check if there are any children
        if not children:
            # Return early if there are no children
            return

        # Iterate over the children
        for child in children:
            # Destroy the child widget
            child.destroy()

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

        # Collect the subscriptions
        subscriptions: List[Dict[str, Any]] = [
            {
                "event": Events.REQUEST_FLASHCARD_LEARNING_VIEW_FLIP_FLASHCARD,
                "function": self.on_request_flashcard_learning_view_flip_flashcard,
                "namespace": self.namespace,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_FLASHCARD_LEARNING_VIEW_LOAD_FLASHCARD,
                "function": self.on_request_flashcard_learning_view_load_flashcard,
                "namespace": self.namespace,
                "persistent": True,
            },
        ]

        # Return the subscriptions
        return subscriptions

    def configure_grid(self) -> None:
        """
        Configures the grid of the flashcard learning view widget.

        This method configures the grid of the flashcard learning view widget by setting
        the weights of the columns and rows.

        Returns:
            None
        """

        # Configure the flashcard learning view widget's 1st column to weight 1.
        # This means that the 1st column will stretch when the window is resized.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the flashcard learning view widget's 0th row to weight 1.
        # This means that the 0th row will stretch when the window is resized.
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

    def create_widgets(self) -> None:
        """
        Creates and configures the widgets for the flashcard learning view.

        This method initializes the front and back frames, along with their respective
        labels and text widgets, for displaying the front and back sides of the flashcard.
        It handles exceptions and logs any issues encountered during widget creation.

        Returns:
            None
        """
        try:
            # Create the front frame widget
            self.front_frame: Optional[tkinter.Frame] = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Check if the front frame was created successfully
            if not self.front_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create front frame in '{self.__class__.__name__}'. This is likely a bug."
                )
                # Return early if creation failed
                return

            # Configure the front frame widget's 0th column to weight 1.
            # This means that the 0th column will stretch when the window is resized.
            self.front_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the front frame widget's 0th row to weight 1.
            # This means that the 0th row will stretch when the window is resized.
            self.front_frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the front frame in the grid
            self.front_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the front text label widget
            self.front_text_label: Optional[tkinter.Label] = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                disabledforeground=Constants.WHITE,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                justify=CENTER,
                master=self.front_frame,
                text=self.flashcard.front_text,
            )

            # Check if the front text label was created successfully
            if not self.front_text_label:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create front text label widget in '{self.__class__.__name__}'. This is likely a bug."
                )
                # Return early if creation failed
                return

            # Bind the front text label to the flip method
            self.front_text_label.bind(
                func=lambda event: self.flip(),
                sequence="<ButtonRelease-1>",
            )

            # Place the front text label in the grid
            self.front_text_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the back frame widget
            self.back_frame: Optional[tkinter.Frame] = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Check if the back frame was created successfully
            if not self.back_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create back frame in '{self.__class__.__name__}'. This is likely a bug."
                )
                # Return early if creation failed
                return

            # Configure the back frame widget's 0th column to weight 1.
            # This means that the 0th column will stretch when the window is resized.
            self.back_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the back frame widget's 0th row to weight 1.
            # This means that the 0th row will stretch when the window is resized.
            self.back_frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the back frame in the grid
            self.back_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            scrolled_text: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_text(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=self.back_frame,
                relief=FLAT,
                wrap=WORD,
            )

            # Check if the scrolled text was created successfully
            if not scrolled_text:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create scrolled text in '{self.__class__.__name__}'. This is likely a bug."
                )
                # Return early if creation failed
                return

            # Create the back text widget
            self.back_text_text: Optional[tkinter.Text] = scrolled_text["text"]

            # Check if the back text widget was created successfully
            if not self.back_text_text:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create back text text widget in '{self.__class__.__name__}'. This is likely a bug."
                )
                # Return early if creation failed
                return

            # Bind the back text widget to the flip method
            self.back_text_text.bind(
                func=lambda event: self.flip(),
                sequence="<ButtonRelease-1>",
            )

            # Insert the back text into the text widget
            self.back_text_text.insert(
                chars=self.flashcard.back_text,
                index="1.0",
            )

            # Disable the back text widget
            self.back_text_text.configure(state=DISABLED)

            # Place the back text widget in the grid
            scrolled_text["root"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            if self.side == "back":
                # Hide the front frame
                self.front_frame.grid_forget()
            else:
                # Hide the back frame
                self.back_frame.grid_forget()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

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
            # Unbind the space key from the flip method
            self.unbind_keys()

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

    def flip(
        self,
        dispatch: bool = True,
    ) -> None:
        """
        Flips the flashcard in the learning view.

        This method toggles the 'side' instance variable between 'front' and 'back'
        and changes the visibility of the front and back frames accordingly. Additionally
        dispatches the FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED event to notify other components of the flip action.

        Args:
            dispatch (bool): Boolean-flag, determines, if the FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED event is dispatched if true.

        Returns:
            None
        """

        # Toggle the 'side' instance variable between 'front' and 'back'
        self.side = "front" if self.side == "back" else "back"

        # Change the visibility of the front and back frames accordingly
        if self.side == "front":
            # Hide the back frame
            self.back_frame.grid_forget()

            # Show the front frame
            self.front_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )
        else:
            # Hide the front frame
            self.front_frame.grid_forget()

            # Show the back frame
            self.back_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

        if dispatch:
            # Dispatch the NOTIFY_FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED event
            self.dispatcher.dispatch(
                event=Events.NOTIFY_FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED,
                flashcard=self.flashcard,
                namespace=self.namespace,
            )

    def forget_widgets(self) -> None:
        """
        Hides the current visible frame of the flashcard learning view.

        This method checks which side of the flashcard is currently visible
        and hides the corresponding frame by removing it from the grid layout.

        Returns:
            None
        """

        # Check if the back side of the flashcard is currently visible
        if self.side == "back":
            # Hide the back frame by removing it from the grid
            self.back_frame.grid_forget()
        else:
            # Hide the front frame by removing it from the grid
            self.front_frame.grid_forget()

    def on_request_flashcard_learning_view_flip_flashcard(
        self,
        side: Optional[
            Literal[
                "front",
                "back",
            ]
        ] = None,
    ) -> None:
        """
        Handles the 'request_flashcard_learning_view_flip_flashcard' event and flips the flashcard.

        This method toggles the 'side' instance variable between 'front' and 'back'
        and changes the visibility of the front and back frames accordingly.

        Args:
            side (Optional[Literal["front", "back"]]): The side of the flashcard to be displayed.

        Returns:
            None
        """

        # Check if the side is present and if so is different from the current side
        if side and side != self.side:
            # Set the side of the flashcard
            self.side = "front" if side == "back" else "back"

        # Flip the flashcard
        self.flip(dispatch=False)

    def on_request_flashcard_learning_view_load_flashcard(
        self,
        flashcard: ImmutableFlashcard,
    ) -> None:
        """
        Handles the 'request_flashcard_learning_view_load_flashcard' event and loads a flashcard into the UI.

        This method stores the passed flashcard instance in an instance variable,
        and updates the widgets of the flashcard learning form.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be loaded into the UI.

        Returns:
            None
        """

        # Store the passed flashcard instance in an instance variable
        self.flashcard = flashcard

        # Set the side of the flashcard
        # The side is used to determine which side of the flashcard should be displayed
        self.side = "back"

        # Flip the flashcard
        self.flip(dispatch=False)

        # Update the widgets in the flashcard learning view form
        self.update_widgets()

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
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def unbind_keys(self) -> None:
        """
        Unbinds the space key from the flip method.

        This method unbinds the space key from the flip method, which is used to flip the flashcard.

        Returns:
            None
        """

        # Unbind the space key from the flip method
        for binding in self.bindings:
            self.unbind_all(binding)

        # Clear the list of bindings
        self.bindings.clear()

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
                message=f"Caught an exception while attempting to run 'unsubscribe_from_events' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def update_widgets(self) -> None:
        """
        Updates the widgets in the flashcard learning view form with the current
        flashcard's front and back text.

        This method clears the text in the back text widget and inserts the current
        flashcard's back text into it. It also updates the front text label with
        the current flashcard's front text.

        Returns:
            None
        """

        # Update the widgets in the flashcard learning view form
        self.update_idletasks()

        # Disable the back text widget
        self.back_text_text.configure(state=NORMAL)

        # Clear the back text widget
        self.back_text_text.delete(
            index1="1.0",
            index2=END,
        )

        # Insert the current flashcard's back text into the back text widget
        self.back_text_text.insert(
            chars=self.flashcard.back_text,
            index="1.0",
        )

        # Disable the back text widget
        self.back_text_text.configure(state=DISABLED)

        # Update the front text label with the current flashcard's front text
        self.front_text_label.configure(
            text=self.flashcard.front_text,
        )
