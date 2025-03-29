"""
Author: lodego
Date: 2025-03-29
"""

from typing import *

from core.answer import ImmutableAnswer, MutableAnswer
from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard, MutableFlashcard
from core.note import ImmutableNote, MutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion, MutableQuestion
from core.stack import ImmutableStack, MutableStack

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["LearningSessionRunner"]


class LearningSessionRunner(ImmutableBaseObject):
    """
    A singleton class responsible for managing a learning session.

    The class provides methods to create and return a new instance of the
    LearningSessionRunner class, and initializes the instance with a dispatcher.

    The class provides a single shared instance of the LearningSessionRunner class,
    accessible using the `instance` class method.

    Attributes:
        _shared_instance (Optional[LearningSessionRunner]): The shared instance of the class.
        logger (Logger): The logger instance associated with the runner.
    """

    _shared_instance: Optional["LearningSessionRunner"] = None

    def __new__(
        cls,
        difficulties: List[Union[ImmutableDifficulty]],
        dispatcher: Dispatcher,
        priorities: List[Union[ImmutablePriority]],
        stacks: List[Union[ImmutableStack, MutableStack]],
    ) -> "LearningSessionRunner":
        """
        Creates and returns a new instance of the LearningSessionRunner class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            difficulties (List[Union[ImmutableDifficulty, MutableDifficulty]]): The difficulties to be used by the runner.
            dispatcher (Dispatcher): The dispatcher instance to be used by the runner.
            priorities (List[Union[ImmutablePriority, MutablePriority]]): The priorities to be used by the runner.
            stacks (List[Union[ImmutableStack, MutableStack]]): The stacks to be used by the runner.

        Returns:
            LearningSessionRunner: The created or existing instance of LearningSessionRunner class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(LearningSessionRunner, cls).__new__(cls)
            # Initialize the instance with the dispatcher and stacks
            cls._shared_instance.init(
                difficulties=difficulties,
                dispatcher=dispatcher,
                priorities=priorities,
                stacks=stacks,
            )
        # Return the shared instance
        return cls._shared_instance

    def init(
        self,
        difficulties: List[Union[ImmutableDifficulty]],
        dispatcher: Dispatcher,
        priorities: List[Union[ImmutablePriority]],
        stacks: List[Union[ImmutableStack, MutableStack]],
    ) -> None:
        """
        Initializes the learning session runner.

        This method is responsible for initializing the learning session runner by
        setting up the logger instance.

        Args:
            difficulties (List[Union[ImmutableDifficulty]]): The difficulties to be used by the runner.
            dispatcher (Dispatcher): The dispatcher instance.
            priorities (List[Union[ImmutablePriority]]): The priorities to be used by the runner.
            stacks (List[Union[ImmutableStack, MutableStack]]): The stacks to be used by the runner.

        Returns:
            None
        """

        # Initialize an empty list to store the session's contents
        self.contents: Final[List[str]] = []

        # Store the passed difficulty list in an immutable instance variable
        self.difficulties: Final[List[Union[ImmutableDifficulty]]] = difficulties

        # Store the passed dispatcher instance in an immutable instance variable
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Initialize an empty list to store the session's items
        self.items: Final[List[str]] = []

        # Store the passed priority list in an immutable instance variable
        self.priorities: Final[List[Union[ImmutablePriority]]] = priorities

        # Store the passed stack list in an immutable instance variable
        self.stacks: Final[List[Union[ImmutableStack, MutableStack]]] = stacks

        # Subscribe to events
        self.subscribe_to_events()

        # Apply filters
        self.apply_filters()

    def apply_filters(self) -> None:
        """
        Applies filters to the contents of the stacks.

        This method is responsible for filtering the contents of the stacks
        based on the provided difficulties and priorities.

        Returns:
            None
        """
        try:
            # Initialize an empty list to store the filtered contents
            self.contents: List[str] = []

            # Get the contents of the stacks
            keys: List[str] = []

            for stack in self.stacks:
                # Add the contents of the stack to the list
                keys.extend(stack.contents)

            # Dispatch a request to get the contents of the stacks
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEYS,
                namespace=Constants.GLOBAL_NAMESPACE,
                keys=keys,
            )

            if notification is None:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to get contents for stacks: {', '.join(stack.__repr__ for stack in self.stacks)}"
                )

                # Return early
                return

            # Get the contents of the stacks
            contents: Optional[
                List[Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion]]
            ] = notification.get_one_and_only_result()

            if not contents:
                # Log a warning message indicating that no contents were found
                self.logger.warning(
                    message=f"No contents found for stacks: {', '.join(stack.__repr__ for stack in self.stacks)}"
                )

                # Return early
                return

            if self.difficulties:
                # Filter the contents based on the difficulties
                contents = [
                    content
                    for content in contents
                    if content.difficulty
                    in [difficulty.id for difficulty in self.difficulties]
                ]

            if self.priorities:
                # Filter the contents based on the priorities
                contents = [
                    content
                    for content in contents
                    if content.priority in [priority.id for priority in self.priorities]
                ]

            # Add the filtered contents to the list
            self.contents.extend(contents)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'apply_filters' method in '{self.__class__.__name__}': {e}"
            )

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

        # Initialize an empty list to store subscriptions
        subscriptions: List[Dict[str, Any]] = []

        # Return the collected subscriptions
        return subscriptions

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
            # Get the subscriptions from the collect_subscriptions method
            subscriptions: List[Dict[str, Any]] = self.collect_subscriptions()

            # Iterate over the subscriptions
            for subscription in subscriptions:
                # Register the event handler with the dispatcher
                self.subscriptions.append(
                    self.dispatcher.register(
                        event=subscription["event"],
                        function=subscription["function"],
                        namespace=subscription["namespace"],
                        persistent=subscription["persistent"],
                    )
                )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method in '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def unsubscribe_from_events(self) -> None:
        """
        Unsubscribes from all events.

        This method iterates over the UUIDs in the subscriptions list and
        unregisters the event handlers associated with each UUID.

        Raises:
            Exception: If an error occurs while unsubscribing from events.
        """
        try:
            # Iterate over the UUIDs in the subscriptions list
            for uuid in self.subscriptions:
                # Unregister the handler for the given UUID
                self.dispatcher.unregister(uuid=uuid)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unsubscribe_from_events' method in '{self.__class__.__name__}': {e}"
            )
            # Re-raise the exception to the caller
            raise e
