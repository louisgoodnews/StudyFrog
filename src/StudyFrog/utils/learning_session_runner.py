"""
Author: lodego
Date: 2025-03-29
"""

import json
import tkinter
import traceback

from datetime import datetime, timedelta
from tkinter.constants import *
from typing import *

from core.answer import ImmutableAnswer
from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion
from core.stack import ImmutableStack, MutableStack
from core.status import ImmutableStatus

from core.learning.learning_session import (
    ImmutableLearningSession,
    MutableLearningSession,
    LearningSessionBuilder,
    ImmutableLearningSessionAction,
    LearningSessionActionBuilder,
    ImmutableLearningSessionItem,
    MutableLearningSessionItem,
    LearningSessionItemBuilder,
)

from core.ui.notifications.notifications import ToplevelNotification

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.text_analyzer import TextAnalyzer


__all__: List[str] = ["LearningSessionRunner"]


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
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize an empty list to store the session's contents
        self.contents: List[str] = []

        # Initialize the current content index
        self.content_index: int = -1

        # Initialize the current entity to None
        self.current_entity: Optional[Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion,]] = None

        # Store the passed difficulty list in an immutable instance variable
        self.difficulties: List[Union[ImmutableDifficulty]] = difficulties

        # Store the passed dispatcher instance in an immutable instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Initialize an empty list to store the intrasession review queue
        self.intrasession_review_queue: List[Tuple[datetime, str]] = []

        # Initialize an empty list to store the session's items
        self.items: List[str] = []

        # Initialize the current item index
        self.item_index: int = -1

        # Initialize the learning session
        self.learning_session: Optional[ImmutableLearningSession] = None

        # Initialize the learning session item
        self.learning_session_item: Optional[ImmutableLearningSessionItem] = None

        # Store the passed mode in an immutable instance variable
        self.mode: str = mode

        # Store the passed namespace in an immutable instance variable
        self.namespace: str = namespace

        # Store the passed priority list in an immutable instance variable
        self.priorities: List[Union[ImmutablePriority]] = priorities

        # Store the passed settings dictionary in an immutable instance variable
        self.settings: Dict[str, Any] = settings

        # Store the passed stack list in an immutable instance variable
        self.stacks: List[Union[ImmutableStack, MutableStack]] = stacks

        # Initialize an empty list to store the subscription UUIDs
        self.subscriptions: List[str] = []

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

    def _calculate_adaptive_interval(
        self,
        difficulty: int,
        priority: int,
        what: Literal["days", "seconds"] = "seconds",
    ) -> Union[int, float]:
        """
        Calculates a new interval based on difficulty and priority.

        Args:
            difficulty (int): The difficulty ID.
            priority (int): The priority ID.
            what (Literal["days", "seconds"], optional): Output format. Defaults to "seconds".

        Returns:
            int|float: The calculated interval.
        """

        try:
            # Request the ImmutableDifficulty object
            difficulty: Optional[ImmutableDifficulty] = self._request_entity(
                event=Events.REQUEST_DIFFICULTY_LOAD,
                field="id",
                value=difficulty,
            )

            # Check, if the difficulty object exists
            if not difficulty:
                # Log a warning message indicating that the difficulty object does not exist
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_DIFFICULTY_LOAD' event in 'global' namespace: Difficulty object does not exist"
                )

                # Return early
                return

            # Request the ImmutablePriority object
            priority: Optional[ImmutablePriority] = self._request_entity(
                event=Events.REQUEST_PRIORITY_LOAD,
                field="id",
                value=priority,
            )

            # Check, if the priority object exists
            if not priority:
                # Log a warning message indicating that the priority object does not exist
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_PRIORITY_LOAD' event in 'global' namespace: Priority object does not exist"
                )

                # Return early
                return

            # Calculate the interval
            interval: float = (
                Constants.get_base_repetition_interval(what=what)
                * (1 + difficulty.value)
                * (1 - priority.value)
            )

            # Return the interval in the specified format
            return max(
                interval,
                Constants.get_base_repetition_interval(what=what),
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'calculate_adaptive_interval' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Raise the exception to the caller
            raise e

    def _request_entity(
        self,
        event: DispatcherEvent,
        **kwargs,
    ) -> Optional[Any]:
        """
        Dispatches a request to get an entity by the passed keyword arguments.

        This method dispatches a request to get an entity by the passed keyword arguments using the
        dispatcher. It returns the result from the dispatcher.

        Args:
            event (DispatcherEvent): The event to dispatch.
            **kwargs: Additional keyword arguments to pass to the dispatcher.

        Returns:
            Optional[Any]: The result from the dispatcher.
        """

        # Initialize the result any-type object as None
        result: Optional[Any] = None

        try:
            # Dispatch the event in the 'global' namespace
            dispatcher_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=event,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    **kwargs,
                )
            )

            # Check, if the notification exists or has errors
            if not dispatcher_notification or dispatcher_notification.has_errors():
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to dispatch '{event}' event in 'global' namespace: {dispatcher_notification.get_errors() if dispatcher_notification else 'This is likely a bug.'}"
                )

                # Return early
                return

            # Get the result from the notification
            result = dispatcher_notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_request_entity' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Raise the exception to the caller
            raise e
        finally:
            # Return the result to the caller
            return result

    def _update_entity(
        self,
        update: Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableLearningSession,
            ImmutableLearningSessionAction,
            ImmutableLearningSessionItem,
            ImmutableQuestion,
            ImmutableStack,
        ],
    ) -> Optional[
        Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableLearningSession,
            ImmutableLearningSessionAction,
            ImmutableLearningSessionItem,
            ImmutableQuestion,
            ImmutableStack,
        ]
    ]:
        """
        Updates an entity in the database.

        Args:
            update (Union[ImmutableAnswer, ImmutableFlashcard, ImmutableLearningSession, ImmutableLearningSessionAction, ImmutableLearningSessionItem, ImmutableQuestion, ImmutableStack]): The entity to update.

        Returns:
            Optional[Union[ImmutableAnswer, ImmutableFlashcard, ImmutableLearningSession, ImmutableLearningSessionAction, ImmutableLearningSessionItem, ImmutableQuestion, ImmutableStack]]: The updated entity.

        Raises:
            Exception: If an exception occurs while updating the entity.
        """

        # Initialize the result Union[ImmutableAnswer, ImmutableFlashcard, ImmutableLearningSession, ImmutableLearningSessionAction, ImmutableLearningSessionItem, ImmutableQuestion, ImmutableStack] object to None
        result: Optional[
            Union[
                ImmutableAnswer,
                ImmutableFlashcard,
                ImmutableLearningSession,
                ImmutableLearningSessionAction,
                ImmutableLearningSessionItem,
                ImmutableQuestion,
                ImmutableStack,
            ]
        ] = None

        try:
            # Dispatch the event in the 'global' namespace
            dispatcher_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_UPDATE,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    update=update,
                )
            )

            # Check, if the notification exists or has errors
            if not dispatcher_notification or dispatcher_notification.has_errors():
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_UPDATE' event in 'global' namespace: {dispatcher_notification.get_errors() if dispatcher_notification else 'This is likely a bug.'}"
                )

                # Return early
                return

            # Get the result from the notification
            result = dispatcher_notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_update_entity' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Raise the exception to the caller
            raise e
        finally:
            # Return the result to the caller
            return result

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

            # Get the keys of the stacks
            keys: List[str] = []

            for stack in self.stacks:
                # Check, if the stack has contents
                if stack.has_contents():
                    # Add the contents of the stack to the list
                    keys.extend(
                        json.loads(stack.contents)
                        if not isinstance(stack.contents, list)
                        else stack.contents
                    )

                # Check, if the stack has descendants
                if not stack.has_descendants():
                    # Skip the current iteration
                    continue

                # Obtain the stack's descendants
                descendants: List[str] = (
                    json.loads(stack.descendants)
                    if not isinstance(stack.descendants, list)
                    else stack.descendants
                )

                # Iterate over the descendants of the current stack
                for key in descendants:
                    # Get the one and only result (the descendant stack) from the descendant notification
                    descendant_stack: Optional[ImmutableStack] = self._request_entity(
                        event=Events.REQUEST_STACK_LOOKUP,
                        key=key,
                    )

                    # Check, if the ImmutableStack descendant stack exists
                    if not descendant_stack:
                        # Log a warning message
                        self.logger.warning(
                            message=f"Failed to obtain ImmutableStack with key '{key}' from the database. Skipping..."
                        )

                        # Skip the current iteration
                        continue

                    # Add the contents of the descendant stack to the list
                    keys.extend(
                        json.loads(descendant_stack.contents)
                        if not isinstance(descendant_stack.contents, list)
                        else descendant_stack.contents
                    )

            # Get the contents of the stacks
            contents: Optional[
                List[
                    Union[
                        ImmutableFlashcard,
                        ImmutableNote,
                        ImmutableQuestion,
                    ]
                ]
            ] = self._request_entity(
                event=Events.REQUEST_GET_BY_KEYS,
                keys=keys,
            )

            if not contents:
                # Log a warning message indicating that no contents were found
                self.logger.warning(
                    message=f"No contents found for stacks: {', '.join(stack.__repr__() for stack in self.stacks)}"
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

            # Check, if randomisation is enabled in the settings
            if self.settings.get(
                "enable_randomisation",
                False,
            ):
                # Shuffle the contents
                Miscellaneous.shuffle(iterable=self.contents)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'apply_filters' method in '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
            # Get the status of the learning session
            status: Optional[ImmutableStatus] = self._request_entity(
                event=Events.REQUEST_STATUS_LOOKUP,
                name="new",
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

            # Initialize an empty list for the stacks
            stacks: List[str] = []

            # Iterate over the stacks in this object
            for stack in self.stacks:
                # Append the stack's key to the stacks list
                stacks.append(stack.key)

                # Check, if the stack has descendants
                if not stack.has_descendants():
                    # Skip the current iteration
                    continue

                # Extend the stacks list with the descendants of the stack
                stacks.extend(
                    json.loads(stack.descendants)
                    if not isinstance(stack.descendants, list)
                    else stack.descendants
                )

            # Set the stacks of the learning session
            # The stacks are set to the stacks of the learning session
            builder.stacks(value=stacks)

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
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_learning_session_item(
        self,
        reference: Optional[str] = None,
    ) -> None:
        """
        Creates a learning session item in the database.

        This method dispatches a request to create the learning session item and
        updates the learning session with the newly created learning session item.

        Args:
            reference (Optional[str]): The key of the entity to be associated with the learning session item.

        Returns:
            None
        """
        try:
            # Check, if the learning session item already exists
            if self.learning_session_item:
                # Check, if the learning session item is mutable
                if not self.learning_session_item.is_mutable():
                    # Convert the learning session item to a mutable object
                    self.learning_session_item = self.learning_session_item.to_mutable()

                # Set the end time of the learning session item
                self.learning_session_item.set(
                    name="end",
                    value=Miscellaneous.get_current_datetime(),
                )

                # Set the duration of the learning session item
                self.learning_session_item.set(
                    name="duration",
                    value=(
                        self.learning_session_item.end
                        - self.learning_session_item.start
                    ).total_seconds(),
                )

                # Update the learning session item
                self.learning_session_item = self._update_entity(
                    update=self.learning_session_item
                )

                # Check, if the learning session item is mutable
                if self.learning_session_item.is_mutable():
                    # Convert the learning session item back to immutable
                    self.learning_session_item = (
                        self.learning_session_item.to_immutable()
                    )

            # Create a builder instance
            builder: LearningSessionItemBuilder = LearningSessionItemBuilder()

            # Set the actions attribute of the builder
            builder.actions(value=[])

            # Set the created_at attribute of the builder
            builder.created_at(value=Miscellaneous.get_current_datetime())

            # Set the reference attribute of the builder
            builder.reference(value=reference or self.contents[self.content_index])

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

            # Check, if the learning session is mutable
            if not self.learning_session.is_mutable():
                # Convert the learning session into a mutable type
                self.learning_session = self.learning_session.to_mutable()

            # Add the learning session item to the learning session
            self.learning_session.add_child(child=self.learning_session_item)

            # Update the learning session
            self.learning_session = self._update_entity(update=self.learning_session)

            # Check, if the learning session is mutable
            if self.learning_session.is_mutable():
                # Convert the learning session back to immutable
                self.learning_session = self.learning_session.to_immutable()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while atttempting to run 'create_learning_session_item' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def get_next_intrasession_review_item(self) -> Optional[
        Union[
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
        ]
    ]:
        """
        Gets the next intrasession review item.

        This method returns the next intrasession review item from the intrasession review queue.

        Args:
            None

        Returns:
            Optional[Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion]]: The next intrasession review item.
        """

        # Check, if the intrasession review queue is empty
        if len(self.intrasession_review_queue) == 0:
            # Return early
            return None

        # Get the next intrasession review item
        item: Tuple[
            datetime,
            Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ],
        ] = self.intrasession_review_queue[0]

        # Check, if the intrasession review item's timestamp is in the future
        if item[0] > Miscellaneous.get_current_datetime():
            # Return early
            return None

        # Remove the intrasession review item from the queue and return it
        return self.intrasession_review_queue.pop(0)[1]

    def handle_end_of_run(
        self,
        mode: Literal[
            "default",
            "recall",
            "recall_at_random",
            "speed_test",
            "spaced_repetition",
        ],
    ) -> None:
        """
        Handles the end of a run.

        This method prompts the user to end the run and updates the learning session
        accordingly. It first checks if the passed mode is not 'default'. If it is not,
        it prompts the user to end the run and updates the learning session.

        Args:
            mode (Literal["default", "recall", "recall_at_random", "speed_test", "spaced_repetition"]): The mode of the run.

        Returns:
            None: This method does not return any value.

        Raises:
            Exception: If an exception occurs while handling the end of the run.
        """
        try:
            # Prompt the user to end the run
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_SHOW_YES_NO_TOPLEVEL,
                message="Congratulations! You have completed the run. Do you wish to end the run?",
                namespace=Constants.GLOBAL_NAMESPACE,
                title="Run Completed",
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to prompt user to end run in 'handle_end_of_run' method from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Check, if the user has chosen to end the run (i.e. if the response equals 'yes')
            if notification.get_one_and_only_result() != "yes":
                # Log an info message
                self.logger.info(
                    message=f"User has chosen to not end run in 'handle_end_of_run' method from '{self.__class__.__name__}' (response was '{notification.get_one_and_only_result()}')"
                )

                # Return early
                return

            # Check, if the learning session instance variable is mutable
            if not self.learning_session.is_mutable():
                # Convert the learning session object into a mutable version
                self.learning_session: MutableLearningSession = (
                    self.learning_session.to_mutable()
                )

            # Set the end timestamp of the learning session
            self.learning_session.end = Miscellaneous.get_current_datetime()

            # Calculate and set the duration of the learning session
            self.learning_session.duration = Miscellaneous.calculate_duration(
                as_="seconds",
                start=self.learning_session.start,
            )

            # Request the 'Completed' status
            status: Optional[ImmutableStatus] = self._request_entity(
                event=Events.REQUEST_STATUS_LOAD,
                field="name",
                value="Completed",
            )

            # Check, if the status exists
            if not status:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to load 'Completed' status in 'handle_end_of_run' method from {self.__class__.__name__}"
                )

                # Return early
                return

            # Set the status of the learning session
            self.learning_session.status = status.id

            # Update the learning session in the database
            self.learning_session = self._update_entity(update=self.learning_session)

            # Check, if the learning session exists
            if not self.learning_session:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to update learning session in 'handle_end_of_run' method from {self.__class__.__name__}. This is likely a bug."
                )

                # Return early
                return

            # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
            self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                learning_session=self.learning_session,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="learning_session_ui",
                target="learning_session_result_ui",
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while atttempting to run 'handle_end_of_run' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def handle_mode(self) -> None:
        """
        Handles the learning mode of the learning session runner.

        Determines the learning mode and dispatches the appropriate event to load the learning view.

        Currently supported modes are:
            - Default
            - Recall
            - Recall (at random)

        If the mode is not supported, a warning message is logged.

        Raises:
            Exception: If an exception occurs while attempting to handle the learning mode.
        """
        try:
            # Check, if the mode is set to "Default"
            if self.mode == "Default":
                # Return early
                return

            if self.mode not in ["Recall", "Recall (at random)"]:
                # Log a warning message
                self.logger.warning(
                    message=f"Got unsupported mode in 'handle_mode' method from '{self.__class__.__name__}' class: '{self.mode}'. Aborting..."
                )

                # Return early
                return

            if (
                self.mode == "Recall (at random)"
                and not Miscellaneous.get_random_bool()
            ):
                # Return early
                return

            # Check, if the 'text_analyzer' instance variable has been initialized
            if not self.text_analyzer:
                # Initialize the 'text_analyzer' instance variable
                self.text_analyzer = TextAnalyzer()

            # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
            self.dispatcher.dispatch(
                direction="forward",
                entity=self._request_entity(
                    event=Events.REQUEST_GET_BY_KEY,
                    key=self.contents[self.content_index],
                ),
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                learning_session=self.learning_session,
                master=tkinter.Toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                source="learning_session_ui",
                target="learning_session_recall_ui",
                text_analyzer=self.text_analyzer,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while atttempting to run 'handle_mode' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
            # Retrieve the status of the learning session
            status: Optional[ImmutableStatus] = self._request_entity(
                event=Events.REQUEST_STATUS_LOOKUP,
                name="completed",
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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
                    # The action number
                    "action_number": len(
                        json.loads(self.learning_session_item.actions)
                        if not isinstance(self.learning_session_item.actions, list)
                        else self.learning_session_item.actions
                    )
                    + 1,
                    # The flashcard that was flipped
                    "flashcard": {
                        "id": flashcard.id,
                        "key": flashcard.key,
                    },
                    # The learning session
                    "learning_session": {
                        "id": self.learning_session.id,
                        "key": self.learning_session.key,
                    },
                    # The learning session item
                    "learning_session_item": {
                        "id": self.learning_session_item.id,
                        "key": self.learning_session_item.key,
                    },
                    # The mode of the learning session
                    "mode": self.mode,
                    # The settings of the learning session
                    "settings": self.settings,
                    # The timestamp of the learning session action
                    "timestamp": Miscellaneous.datetime_to_string(datetime=timestamp),
                    # The time elapsed since the start of the learning session
                    "time_elapsed_since_start": (
                        timestamp - self.learning_session_item.start
                    ).total_seconds(),
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
            learning_session_action: Optional[ImmutableLearningSessionAction] = (
                create_notification.get_one_and_only_result()
            )

            # Check, if the ImmutableLearningSessionAction object exists
            if not learning_session_action:
                # Log a warning message
                self.logger.warning(
                    message=f"ImmutableLearningSessionAction does not exist in 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class."
                )

                # Return early
                return

            # Check, if the learning session item is mutable
            if not self.learning_session_item.is_mutable():
                # Convert the learning session item to mutable
                self.learning_session_item = self.learning_session_item.to_mutable()

            # Append the key of the learning session action to the actions of the learning session item
            self.learning_session_item.add_action(action=learning_session_action)

            self.learning_session_item = self._update_entity(
                update=self.learning_session_item
            )

            # Check if the notification is None
            if not self.learning_session_item:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to dispatch request to update LearningSessionItem object in 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class"
                )

                # Return early
                return

            # Check, if the learning session item is mutable
            if self.learning_session_item.is_mutable():
                # Convert the learning session item back to immutable
                self.learning_session_item = self.learning_session_item.to_immutable()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_notify_learning_session_difficulty_button_clicked(
        self,
        difficulty: Literal["easy", "medium", "hard"],
    ) -> None:
        """
        Handles the 'request_learning_session_difficulty_button_clicked' event and updates the difficulty of the current item in the learning session.

        This method is dispatched by the learning session UI when the user clicks on the difficulty button.

        Args:
            difficulty (Literal["easy", "medium", "hard"]): The difficulty level of the flashcard.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to run the method.
        """
        try:
            # Get the current timestamp
            timestamp: datetime = Miscellaneous.get_current_datetime()

            # Get the difficulty
            passed_difficulty: ImmutableDifficulty = self._request_entity(
                event=Events.REQUEST_DIFFICULTY_LOOKUP,
                name=difficulty,
            )

            # Get the content object
            content: Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ] = self._request_entity(
                event=Events.REQUEST_GET_BY_KEY,
                key=self.contents[self.content_index],
            )

            # Check, if the content object is mutable
            if not content.is_mutable():
                # Convert the Content object to mutable
                content = content.to_mutable()

            # Update the difficulty
            content.difficulty = passed_difficulty.id

            # Dispatch a request to update the Content object
            self._update_entity(update=content)

            # Get the difficulty
            content_difficulty: ImmutableDifficulty = self._request_entity(
                event=Events.REQUEST_DIFFICULTY_LOOKUP,
                id=content.difficulty,
            )

            # Create a builder for the learning session action
            builder: LearningSessionActionBuilder = LearningSessionActionBuilder()

            # Set the reference of the learning session action to the flashcard's key
            # This is necessary to identify the learning session action later on
            builder.reference(value=self.contents[self.content_index])

            # Set the start time of the learning session action
            builder.start(value=timestamp)

            # Set the action type of the learning session action
            builder.action_type(value="DIFFICULTY_CHANGED")

            # Set the action metadata of the learning session action
            # This is a dictionary with some metadata about the learning session action
            builder.action_metadata(
                value={
                    # The action number
                    "action_number": len(
                        json.loads(self.learning_session_item.actions)
                        if not isinstance(self.learning_session_item.actions, list)
                        else self.learning_session_item.actions
                    )
                    + 1,
                    "difficulty": {
                        "from": {
                            "id": content_difficulty.id,
                            "key": content_difficulty.key,
                            "name": content_difficulty.name,
                        },
                        "to": {
                            "id": passed_difficulty.id,
                            "key": passed_difficulty.key,
                            "name": passed_difficulty.name,
                        },
                    },
                    # The flashcard that was flipped
                    Miscellaneous.find_match(string=content.key).lower(): {
                        "id": content.id,
                        "key": content.key,
                    },
                    # The learning session
                    "learning_session": {
                        "id": self.learning_session.id,
                        "key": self.learning_session.key,
                    },
                    # The learning session item
                    "learning_session_item": {
                        "id": self.learning_session_item.id,
                        "key": self.learning_session_item.key,
                    },
                    # The mode of the learning session
                    "mode": self.mode,
                    # The settings of the learning session
                    "settings": self.settings,
                    # The timestamp of the learning session action
                    "timestamp": Miscellaneous.datetime_to_string(datetime=timestamp),
                    # The time elapsed since the start of the learning session
                    "time_elapsed_since_start": (
                        timestamp - self.learning_session_item.start
                    ).total_seconds(),
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

            # Check, if the learning session item is mutable
            if not self.learning_session_item.is_mutable():
                # Convert the learning session item to mutable
                self.learning_session_item = self.learning_session_item.to_mutable()

            # Append the key of the learning session action to the actions of the learning session item
            self.learning_session_item.actions.append(learning_session_action.key)

            self.learning_session_item = self._update_entity(
                update=self.learning_session_item
            )

            # Check if the notification is None
            if not self.learning_session_item:
                # Log a warning message indicating that something went wrong
                self.logger.warning(
                    message=f"Failed to dispatch request to update LearningSessionItem object in 'on_notify_flashcard_learning_view_flashcard_flipped' method from '{self.__class__.__name__}' class"
                )

                # Return early
                return

            # Schedule due by
            self.schedule_due_by(key=self.contents[self.content_index])

            # Check, if the content's difficulty is 'medium' or 'hard'
            if content_difficulty.name not in (
                "medium",
                "hard",
            ):
                # Return early
                return

            # Check, if spaced review is enabled
            if not self.settings["enable_spaced_reivew"]:
                # Return early
                return

            # Check, if the learning session item is mutable
            if self.learning_session_item.is_mutable():
                # Convert the learning session item back to immutable
                self.learning_session_item = self.learning_session_item.to_immutable()

            # Schedule for intrasession review
            self.schedule_intrasession_review(key=self.contents[self.content_index])
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_notify_learning_session_difficulty_button_clicked' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_request_learning_session_runner_get_index_and_limit(self) -> Tuple[int, int]:
        """
        Handles the 'request_learning_session_runner_get_index_and_limit' event and gets the current index and limit of the learning session runner.

        This event is dispatched by the learning session UI when it needs to render the learning session runner.

        Returns:
            Tuple[int, int]: The index and limit of the learning session runner.
        """

        # Return a tuple of the current index and the length of the contents
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
            # Initialize the entity variable to None
            entity: Optional[
                Union[
                    ImmutableFlashcard,
                    ImmutableNote,
                    ImmutableQuestion,
                ]
            ] = None

            # Check, if a previous entity exists
            if self.current_entity:
                # Log the estimated reading time
                self.logger.debug(message=Miscellaneous.estimate_reading_time(content=self.current_entity.total_word_count))

            # Check, if the 'enable_spaced_review' mode has been enabled in the settings dictionary instance variable
            if (
                self.settings.get(
                    "enable_spaced_review",
                    False,
                )
                and self.content_index >= 0
            ):
                # Schedule an intrasession review
                self.schedule_intrasession_review(key=self.contents[self.content_index])

                # Get the next intrasession review item
                entity = self.get_next_intrasession_review_item()
            else:
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

                    # Handle case 'end of run'
                    self.handle_end_of_run(
                        mode=Miscellaneous.any_to_snake(
                            string=self.learning_session.mode.strip()
                            .replace(
                                "(",
                                "",
                            )
                            .replace(
                                ")",
                                "",
                            )
                        )
                    )

                    # Return None indicating an exception occurred
                    return None

            # Schedule due by
            self.schedule_due_by(key=self.contents[self.content_index])

            # Check, if the entity exists
            if not entity:
                # Get the one an only result from the notification
                entity = self._request_entity(
                    event=Events.REQUEST_GET_BY_KEY,
                    key=self.contents[self.content_index],
                )

            # Create a learning session item
            self.create_learning_session_item(reference=entity.key if entity else None)

            # Handle mode
            self.handle_mode()

            # Check, if the entity is immutable
            if not entity.is_mutable():
                # Convert the entity to mutable
                entity = entity.to_mutable()

            # Update the 'last viewed at' field
            entity.last_viewed_at = Miscellaneous.get_current_datetime()

            # Update the entity in the database
            entity = self._update_entity(
                update=entity,
            )

            # Check, if the entity is an ImmutableQuestion
            if isinstance(
                entity,
                ImmutableQuestion,
            ):
                # Get the one an only result from the notification
                answers: List[ImmutableAnswer] = self._request_entity(
                    event=Events.REQUEST_GET_BY_KEYS,
                    keys=entity.answers,
                )

                # Set the entity to a tuple of the entity and answers
                entity = (
                    entity,
                    answers,
                )

            # Set the current entity
            self.current_entity = entity

            # Return the entity to the caller
            return entity
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_learning_session_runner_load_next_item' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

            # Create a learning session item
            self.create_learning_session_item()

            # Get the one an only result from the notification
            entity: Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ] = self._request_entity(
                event=Events.REQUEST_GET_BY_KEY,
                key=self.contents[self.content_index],
            )

            # Check, if the entity is a question
            if isinstance(entity, ImmutableQuestion):
                # Get the answers
                entity = (
                    entity,
                    self._request_entity(
                        event=Events.REQUEST_GET_BY_KEYS,
                        keys=entity.answers,
                    ),
                )

            # Set the current entity
            self.current_entity = entity

            # Return the entity
            return entity
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_learning_session_runner_load_previous_item' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception occurred
            return None

    def schedule_due_by(
        self,
        key: str,
    ) -> None:
        """
        Schedules the item with the given key for spaced repetition.

        This method dispatches a request to lookup the item by key and
        updates its due datetime according to the SuperMemo 2 algorithm.
        The item is then updated in the database.

        Args:
            key (str): The key of the item to schedule for spaced repetition.

        Returns:
            None

        Raises:
            Exception: If an error occurs while attempting to run the method.
        """
        try:
            # Get the content from the notification
            content: Optional[
                Union[
                    ImmutableFlashcard,
                    ImmutableNote,
                    ImmutableQuestion,
                ]
            ] = self._request_entity(
                event=Events.REQUEST_GET_BY_KEY,
                key=key,
            )

            # Check, if the content is None
            if content is None:
                # Log a warning message about the missing content
                self.logger.warning(
                    message=f"Content with key {key} not found in {self.__class__.__name__}. This is likely a bug."
                )

                # Return None indicating an exception occurred
                return None

            # Check, if the content object is mutable
            if not content.is_mutable():
                # Convert the Content object to mutable
                content = content.to_mutable()

            # Get the current datetime
            now: datetime = Miscellaneous.get_current_datetime()

            # Update last viewed timestamp
            content.last_viewed_at = now

            # Calculate the interval
            interval: float = self._calculate_adaptive_interval(
                difficulty=content.difficulty,
                priority=content.priority,
                what="days",
            )

            # Set the content's interval attribute
            content.interval = interval

            # Calculate due datetime
            content.due_by = now + timedelta(days=interval)

            # Update the content
            self._update_entity(update=content)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'schedule_due_by' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception occurred
            return None

    def schedule_intrasession_review(
        self,
        key: str,
    ) -> None:
        """
        Schedules an intrasession review for the passed entity.

        This method dispatches the REQUEST_PRIORITY_LOAD event to load the
        priority with the passed ID and then calculates the interval based on
        the difficulty and priority. It then adds the entity to the
        intrasession review queue with the calculated due datetime and sorts
        the queue by due datetime in ascending order.

        Args:
            difficulty (ImmutableDifficulty): The difficulty.
            entity (Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion]): The entity to schedule an intrasession review for.
        """
        try:
            # Get the entity from the notification
            entity: Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ] = self._request_entity(
                event=Events.REQUEST_GET_BY_KEY,
                key=key,
            )

            # Calculate the interval
            interval: float = self._calculate_adaptive_interval(
                difficulty=entity.difficulty,
                priority=entity.priority,
                what="seconds",
            )

            # Calculate the due datetime
            due_by: datetime = Miscellaneous.get_current_datetime() + timedelta(
                seconds=interval
            )

            # Check, if the due datetime is tomorrow
            if due_by > Constants.END_OF_DAY:

                # Check, if the entity is immutable
                if not entity.is_mutable():
                    # Update the entity to a mutable version
                    entity = entity.to_mutable()

                # Set the entity's 'due_by' attribute to the due datetime
                entity.due_by = due_by

                # Update the entity
                self._update_entity(update=entity)

                # Return early
                return None

            # Add the key to the intrasession review queue
            self.intrasession_review_queue.append(
                (
                    due_by,
                    key,
                )
            )

            # Sort the queue by due datetime in ascending order
            self.intrasession_review_queue.sort(key=lambda x: x[0])
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'schedule_intrasession_review' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
