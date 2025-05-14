"""
Author: lodego
Date: 2025-05-14
"""

from typing import *

from core.flashcard import ImmutableFlashcard, MutableFlashcard

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["FlashcardExporter"]


class FlashcardExporter(ImmutableBaseObject):
    """
    The FlashcardExporter class is a singleton class that is responsible for exporting flashcards as JSONs.
    """

    _shared_instance: Optional["FlashcardExporter"] = None

    def __new__(
        cls,
        dispatcher: Dispatcher,
    ) -> "FlashcardExporter":
        """
        Creates or returns the singleton instance of the FlashcardExporter.

        This method ensures that only one instance of the `FlashcardExporter` exists
        throughout the application runtime. If no instance exists yet, a new one is
        created and initialized with the provided dispatcher.

        Args:
            dispatcher (Dispatcher): The application's central event dispatcher.

        Returns:
            FlashcardExporter: The shared singleton instance.
        """

        if not cls._shared_instance:
            cls._shared_instance = super(FlashcardExporter, cls).__new__(cls)
            cls._shared_instance.init(dispatcher=dispatcher)
        return cls._shared_instance

    def init(
        self,
        dispatcher: Dispatcher,
    ) -> None:
        """
        Initializes the singleton instance of the FlashcardExporter.

        This method sets up the internal state of the exporter, including the dispatcher-
        It is called exactly once during the creation of the singleton instance and should not be called manually.

        Args:
            dispatcher (Dispatcher): The application's central event dispatcher.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
        )

    def export_flashcard(
        self,
        flashcard: Union[
            ImmutableFlashcard,
            int,
            MutableFlashcard,
            str,
        ],
    ) -> str:
        """
        Exports a flashcard as a JSON string.

        This method exports a flashcard as a JSON string. The flashcard can be specified as an
        `ImmutableFlashcard`, an `int` (representing the flashcard's ID), a `MutableFlashcard`,
        or a `str` (representing the flashcard's name).

        Args:
            flashcard (Union[ImmutableFlashcard, int, MutableFlashcard, str]): The flashcard to export.

        Returns:
            str: The JSON string representation of the flashcard.
        """
        try:
            # Check, if the flashcard is of an unsupported type, i.e. not one of the following:
            # - ImmutableFlashcard
            # - int
            # - MutableFlashcard
            # - str
            if not isinstance(
                flashcard,
                (
                    ImmutableFlashcard,
                    int,
                    MutableFlashcard,
                    str,
                ),
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Unsupported type of 'flashcard' argument: {type(flashcard)}"
                )

                # Raise an exception
                raise ValueError(
                    f"Unsupported type of 'flashcard' argument: {type(flashcard)}"
                )

            # Check, if the flashcard is an int
            if isinstance(
                flashcard,
                int,
            ):
                # Dispatch the 'REQUEST_FLASHCARD_LOAD' event in the 'global' namespace
                notification: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        event=Events.REQUEST_FLASHCARD_LOAD,
                        field="id",
                        namespace=Constants.GLOBAL_NAMESPACE,
                        value=flashcard,
                    )
                )

                # Check, if the notification exists or has errors
                if not notification or notification.has_errors():
                    # Log a warning message
                    self.logger.warning(
                        message=f"Failed to dispatch the 'REQUEST_FLASHCARD_LOAD' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
                    )

                    # Return early
                    return

                # Get the flashcard from the notification
                flashcard: Optional[ImmutableFlashcard] = (
                    notification.get_one_and_only_result()
                )

                # Check, if the flashcard exists
                if not flashcard:
                    # Log a warning message
                    self.logger.warning(
                        message=f"Failed to load the flashcard with ID '{flashcard}'"
                    )

                    # Return early
                    return

            # Check, if the flashcard is a str
            elif isinstance(
                flashcard,
                str,
            ):
                # Dispatch the 'REQUEST_FLASHCARD_LOAD' event in the 'global' namespace
                notification: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        event=Events.REQUEST_FLASHCARD_LOAD,
                        field="key",
                        namespace=Constants.GLOBAL_NAMESPACE,
                        value=flashcard,
                    )
                )

                # Check, if the notification exists or has errors
                if not notification or notification.has_errors():
                    # Log a warning message
                    self.logger.warning(
                        message=f"Failed to dispatch the 'REQUEST_FLASHCARD_LOAD' event in the 'global' namespace ({notification.get_errors() if notification and notification.has_errors() else None})"
                    )

                    # Return early
                    return

                # Get the flashcard from the notification
                flashcard: Optional[ImmutableFlashcard] = (
                    notification.get_one_and_only_result()
                )

                # Check, if the flashcard exists
                if not flashcard:
                    # Log a warning message
                    self.logger.warning(
                        message=f"Failed to load the flashcard with key '{flashcard}'"
                    )

                    # Return early
                    return

            # Return the flashcard as a JSON string
            return flashcard.to_json()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'export_flashcard' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
