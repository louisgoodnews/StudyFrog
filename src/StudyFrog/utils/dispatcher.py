"""
Author: lodego
Date: 2025-02-06
"""

from datetime import datetime

from typing import *

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: List[str] = [
    "Dispatcher",
    "DispatcherEvent",
    "DispatcherEventFactory",
    "DispatcherEventSubscription",
    "DispatcherNotification",
    "DispatcherNotificationBuilder",
]


class DispatcherEvent(ImmutableBaseObject):
    """
    An immutable class representing an event for the Dispatcher.

    Attributes:
        id (int): The ID of the event.
        name (str): The name of the event.
        uuid (str): The UUID of the event.
    """

    def __init__(
        self,
        id: int,
        name: str,
        uuid: str,
    ) -> None:
        """
        Initializes a new instance of the DispatcherEvent class.

        Args:
            id (int): The ID of the event.
            name (str): The name of the event.
            uuid (str): The UUID of the event.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            id=id,
            name=name,
            uuid=uuid,
        )

    def compare_to(
        self,
        other: "DispatcherEvent",
    ) -> bool:
        """
        Compares this DispatcherEvent with another to determine equality.

        Args:
            other (DispatcherEvent): The event to compare against.

        Returns:
            bool: True if both events have the same id, name, and uuid; False otherwise.
        """
        return all(
            [
                self.id == other.id,
                self.name == other.name,
                self.uuid == other.uuid,
            ]
        )


class DispatcherEventFactory:
    """
    A factory class for creating instances of DispatcherEvent.

    This class provides a method to create and initialize a new DispatcherEvent
    object with a given name and a generated UUID. It utilizes a logger to
    capture and log exceptions that may occur during the creation process.

    Attributes:
        index (int): The index used to create unique IDs for events.
        logger (Logger): The logger instance associated with the object.
    """

    index: int = Constants.get_base_id()

    logger: Logger = Logger.get_logger(name="DispatcherEventFactory")

    @classmethod
    def create_event(
        cls,
        name: str,
    ) -> Optional[DispatcherEvent]:
        """
        Creates and returns a new instance of the DispatcherEvent class.

        Args:
            name (str): The name of the event.

        Returns:
            Optional[DispatcherEvent]: The created DispatcherEvent object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the event.
        """
        try:
            # Attempt to create and return a new instance of the DispatcherEvent class
            event: DispatcherEvent = DispatcherEvent(
                id=cls.index,
                name=name,
                uuid=Miscellaneous.get_uuid(),
            )

            # Increment the index for the next event
            cls.index += 1

            # Return the created event
            return event
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_event' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DispatcherNotification(ImmutableBaseObject):
    """
    A class representing a notification that is dispatched via the dispatcher.

    Attributes:
        duration (float): The duration of the notification in seconds.
        end (datetime): The timestamp when the notification ended.
        event (DispatcherEvent): The event associated with the notification.
        id (int): The unique identifier of the notification.
        namespace (str): The namespace under which the notification was created.
        result (Any): The result of the notification.
        start (datetime): The timestamp when the notification started.
    """

    def __init__(
        self,
        duration: float,
        end: datetime,
        event: DispatcherEvent,
        id: int,
        namespace: str,
        result: Any,
        start: datetime,
    ) -> None:
        """
        Initializes a new instance of the DispatcherNotification class.

        Args:
            duration (float): The duration of the notification in seconds.
            end (datetime): The timestamp when the notification ended.
            event (DispatcherEvent): The event associated with the notification.
            id (int): The unique identifier of the notification.
            namespace (str): The namespace under which the notification was created.
            result (Any): The result of the notification.
            start (datetime): The timestamp when the notification started.

        Returns:
            None
        """

        # Call the parent constructor
        super().__init__(
            duration=duration,
            end=end,
            event=event,
            id=id,
            namespace=namespace,
            result=result,
            start=start,
        )

    def get_all_results(self) -> List[Any]:
        """
        Returns the result of the notification.

        Returns:
            List[Any]: The result of the notification.
        """

        # Get the result of the notification
        return self["result"].values()

    def get_result(
        self,
        key: str,
    ) -> Optional[Any]:
        """
        Returns the result of the notification with the given key.

        If the key is not found in the result, a warning message is logged and
        None is returned.

        Args:
            key (str): The key of the result to retrieve.

        Returns:
            Optional[Any]: The result of the notification with the given key if
                the key is found. Otherwise, None.
        """

        # Check, if the key is present in the result
        if key not in self["result"].keys():
            # Log a warning message
            self.logger.warning(
                message=f"Key '{key}' not found in result of notification '{self['name']}'"
            )

            # Return early
            return

        # Return the result
        return self["result"][key]


class DispatcherNotificationFactory:
    """
    A factory class for creating instances of the DispatcherNotification class.

    The class provides a method to create and initialize a new
    DispatcherNotification object with a given set of attributes. The method
    utilizes a logger to capture and log exceptions that may occur during the
    creation process.

    Attributes:
        index (int): The index used to create unique IDs for notifications.
        logger (Logger): The logger instance associated with the object.
    """

    index: int = Constants.get_base_id()

    logger: Logger = Logger.get_logger(name="DispatcherNotificationFactory")

    @classmethod
    def create_notification(
        cls,
        duration: float,
        end: datetime,
        event: DispatcherEvent,
        namespace: str,
        result: Any,
        start: datetime,
    ) -> Optional[DispatcherNotification]:
        """
        Creates a new instance of the DispatcherNotification class.

        Args:
            duration (float): The duration of the notification in seconds.
            end (datetime): The timestamp when the notification ended.
            event (DispatcherEvent): The event associated with the notification.
            namespace (str): The namespace under which the notification was created.
            result (Any): The result of the notification.
            start (datetime): The timestamp when the notification started.

        Returns:
            Optional[DispatcherNotification]: The created notification object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the notification.
        """
        try:
            # Create a new notification object
            notification: DispatcherNotification = DispatcherNotification(
                duration=duration,
                end=end,
                event=event,
                id=cls.index,
                namespace=namespace,
                result=result,
                start=start,
            )

            # Increment the index for the next notification
            cls.index += 1

            # Return the created notification object
            return notification
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_notification' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DispatcherNotificationBuilder(BaseObjectBuilder):
    """
    A builder class for constructing DispatcherNotification objects.

    This class provides a fluent interface for setting the attributes of
    a DispatcherNotification object. It inherits from BaseObjectBuilder
    and manages the configuration state for the object being built.

    Attributes:
        configuration (Dict[str, Any]): The configuration dictionary for the builder.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DispatcherNotificationBuilder class.

        This constructor calls the parent class constructor to initialize the
        object.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def build(self) -> DispatcherNotification:
        """
        Builds an instance of the DispatcherNotification class.

        Args:
            None

        Returns:
            DispatcherNotification: An instance of the DispatcherNotification class.
        """
        try:
            # Attempt to create and return a new instance of the DispatcherNotification class
            return DispatcherNotificationFactory.create_notification(
                **self.configuration
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def duration(
        self,
        value: float,
    ) -> Self:
        """
        Sets the duration of the notification.

        Args:
            value (float): The duration of the notification.

        Returns:
            Self: The builder instance.
        """
        self.configuration["duration"] = value
        return self

    def end(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the end datetime of the notification.

        Args:
            value (datetime): The end datetime of the notification.

        Returns:
            Self: The builder instance.
        """
        self.configuration["end"] = value
        return self

    def event(
        self,
        value: str,
    ) -> Self:
        """
        Sets the event name associated with the notification.

        Args:
            value (str): The name of the event.

        Returns:
            Self: The builder instance.
        """
        self.configuration["event"] = value
        return self

    def namespace(
        self,
        value: str,
    ) -> Self:
        """
        Sets the namespace associated with the notification.

        Args:
            value (str): The namespace associated with the notification.

        Returns:
            Self: The builder instance.
        """
        self.configuration["namespace"] = value
        return self

    def result(
        self,
        key: str,
        value: Any,
    ) -> Self:
        """
        Sets the result of the notification.

        Args:
            key (str): The key of the result.
            value (Any): The value of the result.

        Returns:
            Self: The builder instance.
        """
        if "result" not in self.configuration.keys():
            self.configuration["result"] = {}

        self.configuration["result"][key] = value
        return self

    def start(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the start datetime of the notification.

        Args:
            value (datetime): The start datetime of the notification.

        Returns:
            Self: The builder instance.
        """
        self.configuration["start"] = value
        return self


class DispatcherEventSubscription(ImmutableBaseObject):
    def __init__(
        self,
        event: DispatcherEvent,
        id: int,
    ) -> None:
        """
        Initializes a new instance of the DispatcherEventSubscription class.

        Args:
            event (DispatcherEvent): The event associated with the subscription.
            id (int): The ID of the subscription.

        Returns:
            None
        """
        # Call the parent class constructor
        super().__init__(
            event=event,
            id=id,
        )

        # Initialize the subscriptions dictionary as an empty dictionary
        self.subscriptions: Dict[str, Any] = {}

    def add_subscription(
        self,
        function: Callable[..., Any],
        namespace: str,
        persistent: bool,
    ) -> Optional[str]:
        """
        Adds a subscription for a given function under a specified namespace.

        This method associates a given callable function with a namespace and
        stores it in the subscriptions dictionary, generating a unique identifier
        for the subscription. The subscription can be marked as persistent.

        Args:
            function (Callable[..., Any]): The function to be subscribed.
            namespace (str): The namespace under which the subscription is categorized.
            persistent (bool): A flag indicating whether the subscription should be persistent.

        Returns:
            Optional[str]: The UUID of the subscription if successful, otherwise None.
        """
        try:
            # Check if the namespace exists in the subscriptions dictionary
            if namespace not in self.subscriptions.keys():
                # Create a new dictionary for the namespace if it doesn't exist
                self.subscriptions[namespace] = {}

            # Generate a UUID
            code: str = Miscellaneous.get_uuid()

            # Add the subscription to the subscriptions dictionary
            self.subscriptions[namespace][code] = {
                "function": function,
                "persistent": persistent,
            }

            # Return the generated UUID
            return code
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'add_subscription' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def notify_subscriptions(
        self,
        namespace: str,
        *args,
        **kwargs,
    ) -> Optional[DispatcherNotification]:
        """
        Notifies all subscriptions associated with a given namespace.

        This method iterates over the subscriptions dictionary and calls the
        function associated with each subscription.

        Args:
            namespace (str): The namespace under which the subscriptions are categorized.

        Returns:
            Optional[DispatcherNotification]: The notification built from the subscriptions.

        Raises:
            Exception: If an exception occurs while building the notification.
        """
        try:
            # Initialize a notification builder
            result: DispatcherNotificationBuilder = DispatcherNotificationBuilder()

            # Initialize a list to store the UUIDs of non-persistent subscriptions
            non_persistents: List[str] = []

            # Set the event of the notification
            result.event(value=self.event)

            # Set the namespace of the notification
            result.namespace(value=namespace)

            # Set the start time of the notification
            result.start(value=Miscellaneous.get_current_datetime())

            # Iterate over the subscriptions in the namespace
            for (
                uuid,
                subscription,
            ) in self.subscriptions[namespace].items():
                # Check if the subscription is persistent
                if not subscription["persistent"]:
                    # Add the subscription to the subscriptions dictionary
                    non_persistents.append(uuid)

                # Log a message indicating the function is beeing called
                self.logger.info(
                    message=f"Calling function '{subscription['function'].__name__}' with arguments '{args}' and '{kwargs}' in namespace '{namespace}'."
                )

                # Call the function associated with the subscription
                result.result(
                    key=subscription["function"].__name__,
                    value=subscription["function"](
                        *args,
                        **kwargs,
                    ),
                )

            # Iterate over the non-persistent subscriptions
            for uuid in non_persistents:
                # Remove the subscription from the dispatcher
                self.remove_subscription(uuid=uuid)

            # Set the end time of the notification
            result.end(value=Miscellaneous.get_current_datetime())

            # Calculate the duration of the notification
            result.duration(
                value=result["configuration"]["end"] - result["configuration"]["start"]
            )

            # Build the notification and return it
            return result.build()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'notify_subscriptions' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def remove_subscription(
        self,
        uuid: str,
    ) -> Optional[bool]:
        """
        Removes a subscription based on its UUID.

        Args:
            uuid (str): The UUID of the subscription to be removed.

        Returns:
            Optional[bool]: True if the subscription was removed, False otherwise.
        """
        try:
            # Iterate over the namesapces in the subscriptions dictionary
            for namespace in self.subscriptions.keys():
                # Check if the UUID exists in the namespace
                if uuid in self.subscriptions[namespace].keys():
                    # Remove the subscription from the dictionary
                    del self.subscriptions[namespace][uuid]

                    # Log a message indicating the subscription was removed
                    self.logger.info(
                        message=f"Removed subscription with UUID '{uuid}' from namespace '{namespace}'."
                    )

                    # Return True if the subscription was removed
                    return True

            # Log a warning message indicating the subscription was not found
            self.logger.warning(message=f"Subscription with UUID '{uuid}' not found.")

            # Return False if the subscription was not found
            return False
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'remove_subscription' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DispatcherEventSubscriptionFactory:
    """
    A factory class used to create instances of DispatcherEventSubscription class.

    Attributes:
        index (int): The index used to create unique IDs for subscriptions.
        logger (Logger): The logger instance associated with the object.
    """

    index: int = Constants.get_base_id()

    logger: Logger = Logger.get_logger(name="DispatcherEventSubscriptionFactory")

    @classmethod
    def create_subscription(
        cls,
        event: DispatcherEvent,
    ) -> Optional[DispatcherEventSubscription]:
        try:
            # Attempt to create and return a new instance of the DispatcherEventSubscription class
            subscription: DispatcherEventSubscription = DispatcherEventSubscription(
                event=event,
                id=cls.index,
            )

            # Increment the index for the next subscription
            cls.index += 1

            # Return the created subscription
            return subscription
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_subscription' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class Dispatcher:
    """
    A class used to manage event subscriptions and dispatch events to registered handlers.

    This class provides methods to register, unregister, and dispatch events to registered handlers.
    It is designed to be used as a singleton, meaning that only one instance of the class can
    exist at any given time. The instance is accessible through the `Dispatcher.instance` property.

    The class uses a dictionary to store event subscriptions, where the key is the event name and
    the value is a dictionary containing the UUIDs of the subscriptions and the associated namespaces.

    The class provides methods to register a function to be called when an event is dispatched,
    unregister a function from an event, and dispatch an event to all registered handlers.

    The class also provides a method to log messages to the console, which can be useful for debugging.

    Attributes:
        _shared_instance (Optional[Dispatcher]): The shared instance of the class.
        logger (Logger): The logger instance associated with the object.
        subscriptions (Dict[str, DispatcherEventSubscription]): The dictionary storing event subscriptions.
    """

    _shared_instance: Optional["Dispatcher"] = None

    def __new__(cls) -> "Dispatcher":
        """
        Creates and returns a new instance of the Dispatcher class.

        If the instance does not exist, creates a new one by calling the parent class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            Dispatcher: The created or existing instance of Dispatcher class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the dispatcher by creating a logger instance and initializing an empty dictionary for subscriptions.

        This method is called when the shared instance of the dispatcher is created. It initializes an instance of the Logger class and an empty dictionary for storing event subscriptions.

        Args:
            None

        Returns:
            None
        """
        # Initialize an instance of the Logger class
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the subscriptions dictionary as an empty dictionary
        self.subscriptions: Dict[str, DispatcherEventSubscription] = {}

    def dispatch(
        self,
        event: DispatcherEvent,
        namespace: str,
        *args,
        **kwargs,
    ) -> Optional[Any]:
        """
        Dispatches an event to all registered subscriptions.

        Args:
            event (DispatcherEvent): The event to be dispatched.
            namespace (str): The namespace under which the subscriptions are categorized.
            *args: Additional positional arguments to be passed to the event handler.
            **kwargs: Additional keyword arguments to be passed to the event handler.

        Returns:
            Any: The return value of the first function that handles the event.
        """
        try:
            # Check if the event exists in the subscriptions dictionary
            if event.name in self.subscriptions.keys():
                # Attempt to dispatch the event
                return self.subscriptions[event.name].notify_subscriptions(
                    namespace=namespace,
                    *args,
                    **kwargs,
                )
            else:
                # Log a warning message indicating the event was not found
                self.logger.warning(
                    message=f"Event '{event.name}' not found in namespace '{namespace}'."
                )

                # Return None
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to dispatch event '{event.name}' in namespace '{namespace}': {e}",
            )

            # Log additional information about the exception
            self.logger.error(
                message=f"An error occurred while dispatching event '{event.name}' in namespace '{namespace}'.",
            )

            # Return None indicating an exception has occurred
            return None

    def register(
        self,
        event: DispatcherEvent,
        function: Callable[..., Any],
        namespace: str,
        persistent: bool,
    ) -> Optional[str]:
        """
        Registers a function to be called when the associated event is dispatched.

        Args:
            event (DispatcherEvent): The event to be associated with the function.
            function (Callable[..., Any]): The function to be called when the event is dispatched.
            namespace (str): The namespace under which the subscription is categorized.
            persistent (bool): A flag indicating whether the subscription should be persistent.

        Returns:
            Optional[str]: The UUID of the subscription if successful, otherwise None.
        """
        try:
            # Check if the event exists in the subscriptions dictionary
            if event.name not in self.subscriptions.keys():
                # Create a new dictionary for the event if it doesn't exist
                self.subscriptions[event.name] = {}

            # Attempt to create a new subscription
            subscription: DispatcherEventSubscription = (
                DispatcherEventSubscriptionFactory.create_subscription(
                    event=event,
                )
            )

            # Check if the subscription was created
            if subscription is None:
                # Log a warning message indicating the subscription was not created
                self.logger.warning(
                    message=f"Failed to create subscription for event '{event.name}' in namespace '{namespace}'."
                )

                # Return None indicating the subscription was not created
                return None

            # Add the subscription to the subscriptions dictionary
            self.subscriptions[event.name] = subscription

            # Attempt to add the subscription
            result: Optional[str] = subscription.add_subscription(
                function=function,
                namespace=namespace,
                persistent=persistent,
            )

            # Check if the subscription was added
            if result:
                # Log a message indicating the subscription was added
                self.logger.info(
                    message=f"Subscribed function '{function.__name__}' to event '{event.name}' in namespace '{namespace}' with UUID '{result}'."
                )

                # Return the generated UUID
                return result

            # Log a warning message indicating the subscription was not added
            self.logger.warning(
                message=f"Failed to subscribe function '{function.__name__}' to event '{event.name}' in namespace '{namespace}'."
            )

            # Return None indicating the subscription was not added
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def unregister(
        self,
        event: Optional[DispatcherEvent] = None,
        namespace: Optional[str] = None,
        uuid: Optional[str] = None,
    ) -> Optional[bool]:
        try:
            if all([not event, not namespace, not uuid]):
                raise ValueError(
                    "At least one of event, namespace, and uuid must be specified."
                )

            if event:
                if event.name not in self.subscriptions.keys():
                    # Log a warning message indicating the event was not found
                    self.logger.warning(
                        message=f"Event '{event.name}' not found in subscriptions."
                    )

                    # Return False indicating the event was not found
                    return False

                # Remove the event from the subscriptions dictionary
                self.subscriptions.pop(event.name)

                # Return True indicating the event was removed
                return True

            if namespace:
                for subscription in self.subscriptions.values():
                    if namespace in subscription.subscriptions.keys():
                        subscription.subscriptions.pop(namespace)

                # Return True indicating the namespace was removed
                return True

            if uuid:
                for subscription in self.subscriptions.values():
                    for namespace in subscription.subscriptions.keys():
                        if uuid in subscription.subscriptions[namespace]:
                            subscription.subscriptions[namespace].pop(uuid)

                            # Return True indicating the UUID was removed
                            return True

            # Return False indicating that the event was not found
            return False
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unregister' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None
