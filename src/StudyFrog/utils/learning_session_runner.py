"""
Author: lodego
Date: 2025-03-29
"""

from argparse import Namespace
import traceback

from typing import *

from core.learning.learning_session import (
    ImmutableLearningSession,
    MutableLearningSession,
    LearningSessionBuilder,
    ImmutableLearningSessionAction,
    MutableLearningSessionAction,
    LearningSessionActionBuilder,
    ImmutableLearningSessionItem,
    MutableLearningSessionItem,
    LearningSessionItemBuilder,
)

from core.answer import ImmutableAnswer, MutableAnswer
from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard, MutableFlashcard
from core.note import ImmutableNote, MutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion, MutableQuestion
from core.stack import ImmutableStack, MutableStack
from core.status import ImmutableStatus

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.text_analyzer import TextAnalyzer


__all__: Final[List[str]] = ["LearningSessionRunner"]


class LearningSessionRunner:
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
        mode: str,
        namespace: str,
        priorities: List[Union[ImmutablePriority]],
        settings: Dict[str, Any],
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
            mode (str): The mode to be used by the runner.
            namespace (str): The namespace to be used by the runner.
            priorities (List[Union[ImmutablePriority, MutablePriority]]): The priorities to be used by the runner.
            settings (Dict[str, Any]): The settings dictionary.
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
                mode=mode,
                namespace=namespace,
                priorities=priorities,
                settings=settings,
                stacks=stacks,
            )
        # Return the shared instance
        return cls._shared_instance

    def init(
        self,
        difficulties: List[Union[ImmutableDifficulty]],
        dispatcher: Dispatcher,
        mode: str,
        namespace: str,
        priorities: List[Union[ImmutablePriority]],
        settings: Dict[str, Any],
        stacks: List[Union[ImmutableStack, MutableStack]],
    ) -> None:
        """
        Initializes the learning session runner.

        This method is responsible for initializing the learning session runner by
        setting up the logger instance.

        Args:
            difficulties (List[Union[ImmutableDifficulty]]): The difficulties to be used by the runner.
            dispatcher (Dispatcher): The dispatcher instance.
            mode (str): The mode to be used by the runner.
            namespace (str): The namespace to be used by the runner.
            priorities (List[Union[ImmutablePriority]]): The priorities to be used by the runner.
            settings (Dict[str, Any]): The settings dictionary.
            stacks (List[Union[ImmutableStack, MutableStack]]): The stacks to be used by the runner.
        Returns:
            None
        """

        # Initialize the logger
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize an empty list to store the session's contents
        self.contents: Final[List[str]] = []

        # Initialize the current content index
        self.content_index: int = -1

        # Store the passed difficulty list in an immutable instance variable
        self.difficulties: Final[List[Union[ImmutableDifficulty]]] = difficulties

        # Store the passed dispatcher instance in an immutable instance variable
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Initialize an empty list to store the session's items
        self.items: Final[List[str]] = []

        # Initialize the current item index
        self.item_index: int = -1

        # Initialize the learning session
        self.learning_session: Optional[ImmutableLearningSession] = None

        # Initialize the learning session item
        self.learning_session_item: Optional[ImmutableLearningSessionItem] = None

        # Store the passed mode in an immutable instance variable
        self.mode: Final[str] = mode

        # Store the passed namespace in an immutable instance variable
        self.namespace: Final[str] = namespace

        # Store the passed priority list in an immutable instance variable
        self.priorities: Final[List[Union[ImmutablePriority]]] = priorities

        # Store the passed settings dictionary in an immutable instance variable
        self.settings: Final[Dict[str, Any]] = settings

        # Store the passed stack list in an immutable instance variable
        self.stacks: Final[List[Union[ImmutableStack, MutableStack]]] = stacks

        # Initialize an empty list to store the subscription UUIDs
        self.subscriptions: Final[List[str]] = []

        # Initialize the text analyzer
        self.text_analyzer: Optional[TextAnalyzer] = None

        # Subscribe to events
        self.subscribe_to_events()

        # Apply filters
        self.apply_filters()

        # Create a learning session
        self.create_learning_session()

        # Dispatch a notification to indicate that the learning session runner has been loaded
        self.dispatcher.dispatch(
            event=Events.NOTIFY_LEARNING_SESSION_RUNNER_LOADED,
            namespace=self.namespace,
        )

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
            self.contents: Final[List[str]] = []

            # Get the keys of the stacks
            keys: List[str] = []

            for stack in self.stacks:
                # Add the contents of the stack to the list
                keys.extend(stack.contents)

                # Check if the stack has descendants
                if stack.has_descendants():
                    # Add the descendants of the stack to the list
                    keys.extend(stack.descendants)

            # Dispatch a request to get the contents of the stacks
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEYS,
                namespace=Constants.GLOBAL_NAMESPACE,
                keys=keys,
            )

            if not notification:
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

            # Filter the contents based on the difficulties
            if len(self.difficulties) > 0:
                contents = [
                    content
                    for content in contents
                    if content.difficulty
                    in [difficulty.id for difficulty in self.difficulties]
                ]

            # Filter the contents based on the priorities
            if len(self.priorities) > 0:
                contents = [
                    content
                    for content in contents
                    if content.priority in [priority.id for priority in self.priorities]
                ]

            # Add the filtered contents to the list
            self.contents.extend([content.key for content in contents])
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'apply_filters' method in '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
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

        # Initialize an empty list to store subscriptions
        subscriptions: List[Dict[str, Any]] = [
            {
                "event": Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM,
                "function": self.on_request_learning_session_runner_load_next_item,
                "namespace": self.namespace,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_LEARNING_SESSION_RUNNER_LOAD_PREVIOUS_ITEM,
                "function": self.on_request_learning_session_runner_load_previous_item,
                "namespace": self.namespace,
                "persistent": True,
            },
            {
                "event": Events.NOTIFY_FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED,
                "function": self.on_notify_flashcard_learning_view_flashcard_flipped,
                "namespace": self.namespace,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_LEARNING_SESSION_RUNNER_GET_INDEX_AND_LIMIT,
                "function": self.on_request_learning_session_runner_get_index_and_limit,
                "namespace": self.namespace,
                "persistent": True,
            },
            {
                "event": Events.NOTIFY_LEARNING_SESSION_DIFFICULTY_BUTTON_CLICKED,
                "function": self.on_notify_learning_session_difficulty_button_clicked,
                "namespace": self.namespace,
                "persistent": True,
            },
        ]

        # Return the collected subscriptions
        return subscriptions

    def create_learning_session(self) -> None:
        """
        Creates a learning session.

        This method creates a learning session with the contents and filters
        specified in the class instance. It first creates a builder instance
        and then sets the contents and filters using the builder's methods.
        Finally, it attempts to build the learning session and stores the
        built learning session in the class instance.

        Returns:
            None: This method does not return any value.
        """
        try:
            # Dispatch a request to lookup the status of the learning session
            status_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STATUS_LOOKUP,
                    name="new",
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check if the notification is None
            if not status_notification:
                # Log a warning message indicating that something went wrong
                self.logger.warning(message="Failed to create learning session")

                # Return early
                return

            # Get the status of the learning session
            status: Optional[ImmutableStatus] = (
                status_notification.get_one_and_only_result()
            )

            # Check if the status is None
            if not status:
                # Log a warning message indicating that something went wrong
                self.logger.warning(message="Failed to create learning session")

                # Return early
                return

            # Create a builder instance
            builder: LearningSessionBuilder = LearningSessionBuilder()

            # Set the children of the learning session
            # The children are set to an empty list
            builder.children(value=[])

            # Set the contents of the learning session
            # The contents are set to the contents of the stacks
            builder.contents(value=self.contents)

            # Set the filters of the learning session
            # The filters are set to the difficulties and priorities
            builder.filters(
                value={
                    # Set the difficulty filter
                    "difficulty": [difficulty.id for difficulty in self.difficulties],
                    # Set the priority filter
                    "priority": [priority.id for priority in self.priorities],
                }
            )

            # Set the mode of the learning session
            # The mode is set to an empty string
            builder.mode(value=self.mode)

            # Set the settings of the learning session
            # The settings are set to the settings of the learning session
            builder.settings(value=self.settings)

            # Set the stacks of the learning session
            # The stacks are set to the stacks of the learning session
            builder.stacks(value=[stack.id for stack in self.stacks])

            # Set the start of the learning session
            # The start is set to the current datetime
            builder.start(value=Miscellaneous.get_current_datetime())

            # Set the status of the learning session
            # The status is set to the status of the learning session
            builder.status(value=status.get(name="id"))

            # Dispatch the request to create the learning session
            create_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_LEARNING_SESSION_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    learning_session=builder.build(),
                )
            )

            # Check if the notification is None
            if not create_notification:
                # Log a warning message indicating that something went wrong
                self.logger.warning(message="Failed to create learning session")

                # Return early
                return

            # The learning session is retrieved from the notification
            self.learning_session = create_notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while atttempting to run 'create_learning_session' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def create_learning_session_item(self) -> None:
        """
        Creates a learning session item in the database.

        This method dispatches a request to create the learning session item and
        updates the learning session with the newly created learning session item.

        Returns:
            None
        """
        try:
            if self.learning_session_item:
                # Convert the learning session item to a mutable object
                learning_session_item: MutableLearningSessoinItem = (
                    self.learning_session_item.to_mutable()
                )

                # Set the end time of the learning session item
                learning_session_item.set(
                    name="end", value=Miscellaneous.get_current_datetime()
                )

                # Set the duration of the learning session item
                learning_session_item.set(
                    name="duration",
                    value=(
                        self.learning_session_item.end
                        - self.learning_session_item.start
                    ).total_seconds(),
                )

                # Dispatch the request to update the learning session item
                self.dispatcher.dispatch(
                    event=Events.REQUEST_LEARNING_SESSION_ITEM_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    learning_session_item=learning_session_item,
                )

            # Create a builder instance
            builder: LearningSessionItemBuilder = LearningSessionItemBuilder()

            # Set the actions attribute of the builder
            builder.actions(value=[])

            # Set the created_at attribute of the builder
            builder.created_at(value=Miscellaneous.get_current_datetime())

            # Set the reference attribute of the builder
            builder.reference(value=self.contents[self.content_index])

            # Set the start attribute of the builder
            builder.start(value=Miscellaneous.get_current_datetime())

            # Dispatch the request to create the learning session
            create_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_LEARNING_SESSION_ITEM_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    learning_session_item=builder.build(),
                )
            )

            # Check if the notification is None
            if not create_notification:
                # Log a warning message indicating that something went wrong
                self.logger.warning(message="Failed to create learning session item")

                # Return early
                return

            # The learning session item is retrieved from the notification
            self.learning_session_item = create_notification.get_one_and_only_result()

            # Add the learning session item to the learning session
            self.learning_session.add_child(child=self.learning_session_item)

            # Dispatch the request to update the learning session
            update_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_LEARNING_SESSION_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    learning_session=self.learning_session,
                )
            )

            if not update_notification:
                # Log a warning message indicating that something went wrong
                self.logger.warning(message="Failed to update learning session")

                # Return early
                return

            # The learning session is retrieved from the notification
            self.learning_session: ImmutableLearningSession = (
                update_notification.get_one_and_only_result()
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while atttempting to run 'create_learning_session_item' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def is_running(self) -> bool:
        """
        Determines if the learning session is currently running.

        This method dispatches a request to check the status of the learning session
        and verifies if it is 'completed'. If the status lookup fails or the status
        is not 'completed', it logs a warning and returns False.

        Returns:
            bool: True if the learning session is running, False otherwise.
        """
        try:
            # Dispatch a request to lookup the 'completed' status
            status_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STATUS_LOOKUP,
                    name="completed",
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check if the notification is None
            if not status_notification:
                # Log a warning message about the failed lookup
                self.logger.warning(
                    message=f"Failed to lookup 'completed' status in {self.__class__.__name__}"
                )
                return False

            # Retrieve the status of the learning session
            status: Optional[ImmutableStatus] = (
                status_notification.get_one_and_only_result()
            )

            # Verify if the status is None
            if not status:
                # Log a warning message about the failed lookup
                self.logger.warning(
                    message=f"Failed to lookup 'completed' status in {self.__class__.__name__}"
                )
                return False

            # Check if the learning session's status matches 'completed' status
            return self.learning_session.status == status.id
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'is_running' method from '{self.__class__.__name__}' class: {e}"
            )

            # Return False indicating an exception occurred
            return False

    def on_notify_flashcard_learning_view_flashcard_flipped(
        self,
        flashcard: ImmutableFlashcard,
    ) -> None:
        """
        Handles the 'notify_flashcard_learning_view_flashcard_flipped' event and creates a new learning session action.

        This method creates a builder for the learning session action and assigns the necessary values to it.
        It then dispatches a request to create the learning session action and appends its key to the actions
        of the learning session item.

        Args:
            flashcard (ImmutableFlashcard): The flashcard that was flipped.

        Returns:
            None
        """
        try:
            # Get the current timestamp
            timestamp: datetime = Miscellaneous.get_current_datetime()

            # Create a builder for the learning session action
            builder: LearningSessionActionBuilder = LearningSessionActionBuilder()

            # Set the reference of the learning session action to the flashcard's key
            # This is necessary to identify the learning session action later on
            builder.reference(value=flashcard.key)

            # Set the start time of the learning session action
            builder.start(value=timestamp)

            # Set the action type of the learning session action
            builder.action_type(value="FLASHCARD_FLIPPED")

            # Set the action metadata of the learning session action
            # This is a dictionary with some metadata about the learning session action
            builder.action_metadata(
                value={
                    # The flashcard that was flipped
                    "flashcard": {
                        "id": flashcard.id,
                        "key": flashcard.key,
                    },
                    # The time elapsed after the start of the learning session
                    "time_elapsed_after_start": (
                        timestamp - self.learning_session_item.start
                    ).total_seconds(),
                    # The timestamp of the learning session action
                    "timestamp": Miscellaneous.datetime_to_string(datetime=timestamp),
                }
            )

            # Set the end time of the learning session action
            builder.end(value=timestamp)

            # Set the duration of the learning session action
            # This is the time difference between the end and start of the learning session action
            builder.duration(
                value=(
                    builder.configuration["end"] - builder.configuration["start"]
                ).total_seconds()
            )

            # Dispatch a request to create the learning session action
            create_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_LEARNING_SESSION_ACTION_CREATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    learning_session_action=builder.build(),
                )
            )

            # Check if the notification is None
            if not create_notification:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to dispatch request to create LearningSessionAction object in 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class"
                )

                # Return early
                return

            # The learning session action is retrieved from the notification
            learning_session_action: ImmutableLearningSessionAction = (
                create_notification.get_one_and_only_result()
            )

            # Convert the learning session item to mutable
            learning_session_item: MutableLearningSessionItem = (
                self.learning_session_item.to_mutable()
            )

            # Append the key of the learning session action to the actions of the learning session item
            learning_session_item.actions.append(learning_session_action.key)

            update_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_LEARNING_SESSION_ITEM_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    learning_session_item=learning_session_item,
                )
            )

            # Check if the notification is None
            if not update_notification:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to dispatch request to update LearningSessionItem object in 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class"
                )

                # Return early
                return

            # Convert the learning session item back to immutable
            self.learning_session_item = update_notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def on_notify_learning_session_difficulty_button_clicked(
        self,
        difficulty: Literal["easy", "medium", "hard"],
    ) -> None:
        try:
            self.logger.debug(
                message=f"{self.__class__.__name__} received notification that the difficulty button with key '{difficulty}' has been clicked"
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_notify_learning_session_difficulty_button_clicked' method from '{self.__class__.__name__}' class: {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_request_learning_session_runner_get_index_and_limit(self) -> Tuple[int, int]:
        """
        Handles the 'request_learning_session_runner_get_index_and_limit' event and gets the current index and limit of the learning session runner.

        This event is dispatched by the learning session UI when it needs to render the learning session runner.

        Returns:
            Tuple[int, int]: The index and limit of the learning session runner.
        """
        return (
            # Return the current index
            self.content_index,
            # Return the length of the contents
            len(self.contents),
        )

    def on_request_learning_session_runner_load_next_item(
        self,
    ) -> Optional[
        Union[
            ImmutableFlashcard,
            ImmutableNote,
            Tuple[ImmutableQuestion, List[ImmutableAnswer]],
        ]
    ]:
        """
        Handles the 'request_learning_session_runner_load_next_item' event and loads the next item in the learning session's item list.

        This event is dispatched by the learning session UI when the user navigates to the next item in the learning session.

        Returns:
            Optional[Union[ImmutableFlashcard, ImmutableNote, Tuple[ImmutableQuestion, List[ImmutableAnswer]]]]: The loaded item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Increment the content index
            self.content_index += 1

            # Check if the content index is out of bounds
            if self.content_index >= len(self.contents):
                # Log a warning message about the out of bounds index
                self.logger.warning(
                    message=f"Content index {self.content_index} is out of bounds in {self.__class__.__name__}. This is likely a bug."
                )

                # Reset the content index to the last valid index
                self.content_index = len(self.contents) - 1

                # Return None indicating an exception occurred
                return None

            # Dispatch a request to lookup the item by key
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEY,
                namespace=Constants.GLOBAL_NAMESPACE,
                key=self.contents[self.content_index],
            )

            # Check if the notification is None
            if not notification:
                # Log a warning message about the failed lookup
                self.logger.warning(
                    message=f"Failed to lookup item with key '{self.contents[self.content_index]}' in database in {self.__class__.__name__}. This is likely a bug."
                )

                # Return None indicating an exception occurred
                return None

            # Create a learning session item
            self.create_learning_session_item()

            # Check if the learning session is in recall mode
            if self.mode == "Recall":
                # TODO:
                #   - dispatch event to request recall view to be loaded
                pass
            elif self.mode == "Recall (at random)":
                # TODO:
                #   - implement random check for a random int to then determine, if recall with be dispatched or not
                #   - dispatch event to request recall random view to be loaded
                if Miscellaneous.get_random_int(1, 4) == 1:
                    pass

            # Return the item
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_learning_session_runner_load_next_item' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    def on_request_learning_session_runner_load_previous_item(self) -> Optional[
        Union[
            ImmutableFlashcard,
            ImmutableNote,
            Tuple[ImmutableQuestion, List[ImmutableAnswer]],
        ]
    ]:
        """
        Handles the 'request_learning_session_runner_load_previous_item' event and loads the previous item in the learning session.

        This event is dispatched by the learning session UI when the user navigates to the previous item in the learning session.

        Returns:
            Optional[Union[ImmutableFlashcard, ImmutableNote, Tuple[ImmutableQuestion, List[ImmutableAnswer]]]]: The item that was loaded if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Decrement the content index
            self.content_index -= 1

            # Check if the content index is out of bounds
            if self.content_index < 0:
                # Log a warning message about the out of bounds index
                self.logger.warning(
                    message=f"Content index {self.content_index} is out of bounds in {self.__class__.__name__}. This is likely a bug."
                )

                # Reset the content index to 0
                self.content_index = 0

                # Return None indicating an exception occurred
                return None

            # Dispatch a request to lookup the item by key
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEY,
                namespace=Constants.GLOBAL_NAMESPACE,
                key=self.contents[self.content_index],
            )

            # Check if the notification is None
            if not notification:
                # Log a warning message about the failed lookup
                self.logger.warning(
                    message=f"Failed to lookup item with key '{self.contents[self.content_index]}' in database in {self.__class__.__name__}. This is likely a bug."
                )

                # Return None indicating an exception occurred
                return None

            # Create a learning session item
            self.create_learning_session_item()

            # Return the item
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_learning_session_runner_load_previous_item' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

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
