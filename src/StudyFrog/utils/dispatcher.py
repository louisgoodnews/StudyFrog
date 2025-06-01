"""
Author: lodego
Date: 2025-02-06
"""

import traceback

from datetime import datetime
from typing import *

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject
from utils.utils import DateUtil


__all__: Final[List[str]] = [
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
        data: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initializes a new instance of the DispatcherEvent class.

        Args:
            id (int): The ID of the event.
            name (str): The name of the event.
            uuid (str): The UUID of the event.
            data (Optional[Dict[str, Any]]): The data associated with the event. Defaults to None.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            data=data,
            hide_attributes=True,
            id=id,
            name=name,
            uuid=uuid,
        )

    @property
    def data(self) -> Optional[Dict[str, Any]]:
        """
        Gets the data associated with the event.

        Returns:
            Optional[Dict[str, Any]]: The data associated with the event. Defaults to None.
        """

        # Return the data associated with the event
        return self._data

    @property
    def id(self) -> int:
        """
        Gets the ID of the event.

        Returns:
            int: The ID of the event.
        """

        # Return the ID of the event
        return self._id

    @property
    def name(self) -> str:
        """
        Gets the name of the event.

        Returns:
            str: The name of the event.
        """

        # Return the name of the event
        return self._name

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the event.

        Returns:
            str: The UUID of the event.
        """

        # Return the UUID of the event
        return self._uuid

    @override
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

        # Call the parent class compare_to method
        return super().compare_to(
            key=[
                "id",
                "name",
                "uuid",
            ],
            other=other,
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

    logger: Final[Logger] = Logger.get_logger(name="DispatcherEventFactory")

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
        errors (list, optional): A list of dictionary containing information regarding exceptions.
        event (DispatcherEvent): The event associated with the notification.
        id (int): The unique identifier of the notification.
        namespace (str): The namespace under which the notification was created.
        result (Dict[str, Any]): The result of the notification.
        start (datetime): The timestamp when the notification started.
    """

    def __init__(
        self,
        duration: float,
        end: datetime,
        event: DispatcherEvent,
        id: int,
        namespace: str,
        start: datetime,
        errors: Optional[List[Dict[str, Any]]] = None,
        result: Optional[Dict[str, Any]] = None,
        warnings: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        """
        Initializes a new instance of the DispatcherNotification class.

        Args:
            duration (float): The duration of the notification in seconds.
            end (datetime): The timestamp when the notification ended.
            errors (list, optional): A list of dictionary containing information regarding exceptions.
            event (DispatcherEvent): The event associated with the notification.
            id (int): The unique identifier of the notification.
            namespace (str): The namespace under which the notification was created.
            result (Dict[str, Any]): The result of the notification.
            start (datetime): The timestamp when the notification started.
            warnings (list, optional): A list of dictionary containing information regarding warnings.

        Returns:
            None
        """

        # Call the parent constructor
        super().__init__(
            duration=duration,
            end=end,
            errors=errors,
            event=event,
            hide_attributes=True,
            id=id,
            namespace=namespace,
            result=result,
            start=start,
            warnings=warnings,
        )

    @property
    def duration(self) -> float:
        """
        Gets the duration of the notification.

        Returns:
            float: The duration of the notification.
        """

        # Return the duration of the notification
        return self._duration

    @property
    def end(self) -> datetime:
        """
        Gets the end time of the notification.

        Returns:
            datetime: The end time of the notification.
        """

        # Return the end time of the notification
        return self._end

    @property
    def event(self) -> DispatcherEvent:
        """
        Gets the event associated with the notification.

        Returns:
            DispatcherEvent: The event associated with the notification.
        """

        # Return the event associated with the notification
        return self._event

    @property
    def id(self) -> int:
        """
        Gets the unique identifier of the notification.

        Returns:
            int: The unique identifier of the notification.
        """

        # Return the unique identifier of the notification
        return self._id

    @property
    def namespace(self) -> str:
        """
        Gets the namespace under which the notification was created.

        Returns:
            str: The namespace under which the notification was created.
        """

        # Return the namespace under which the notification was created
        return self._namespace

    @property
    def result(self) -> Dict[str, Any]:
        """
        Gets the result of the notification.

        Returns:
            Dict[str, Any]: The result of the notification.
        """

        # Return the result of the notification
        return self._result

    @property
    def start(self) -> datetime:
        """
        Gets the start time of the notification.

        Returns:
            datetime: The start time of the notification.
        """

        # Return the start time of the notification
        return self._start

    @property
    def warnings(self) -> List[Dict[str, Any]]:
        """
        Gets the list of warnings associated with the notification.

        Returns:
            List[Dict[str, Any]]: The list of warnings associated with the notification.
        """

        # Return the list associated with the 'warnings' key
        return self._warnings

    def get_all_results(self) -> List[Any]:
        """
        Returns the result of the notification.

        Args:
            None

        Returns:
            List[Any]: The result of the notification.
        """

        # Get the result of the notification
        return list(self.result.values())

    def get_errors(self) -> List[Dict[str, Any]]:
        """
        Returns the list of errors associated with the notification.

        Args:
            None

        Returns:
            List[Dict[str, Any]]: The list of errors associated with the notification.
        """

        # Return the list associated with the 'errors' key or an empty list
        return self.get(
            "errors",
            [],
        )

    def get_one_and_only_result(self) -> Optional[Any]:
        """
        Returns the one and only result of the notification.

        If the result contains more than one or no value(s), a ValueError is
        raised.

        Args:
            None

        Returns:
            Optional[Any]: The one and only result of the notification if it
                contains exactly one value. Otherwise, None.
        """
        try:
            # Check if the result is empty
            if not self.result:
                # Return None if the result is empty
                return None

            # Check if the result contains more than one or no value(s)
            if len(self.result) == 1:
                # Return the one and only result
                result: Optional[Any] = self.result[next(iter(self.result))]

                # Check if the result is a list with one element
                if isinstance(result, list) and len(result) == 1:
                    # Return the first element of the list
                    return result[0]

                # Return the result
                return result
            else:
                # Raise a ValueError if the result contains more than one or no value(s)
                raise ValueError("Result contains more than one or no value(s).")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_one_and_only_result' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_result_by_key(
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
        if key not in self.result:
            # Log a warning message
            self.logger.warning(
                message=f"Key '{key}' not found in result of notification '{self.name}'"
            )

            # Return early
            return None

        # Return the result
        return self.result[key]

    def has(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the notification contains the given key, False otherwise.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the notification contains the given key, False otherwise.
        """
        return key in self.result

    def has_errors(self) -> bool:
        """
        Returns True if the notification contains an 'errors' key, False otherwise.

        Args:
            None

        Returns:
            bool: True if the notification contains an 'errors' key, False otherwise.
        """

        # Return True, if the 'errors' key is present, otherwise False
        return self.has(key="errors")

    def has_irregularities(self) -> bool:
        """
        Returns True if the notification contains any irregularities, (i.e. errors or warnings), False otherwise.

        Args:
            None

        Returns:
            bool: True if the notification contains any irregularities, False otherwise.
        """

        # Return True, if the notification contains any irregularities, False otherwise
        return any(
            [
                self.has_errors(),
                self.has_warnings(),
            ]
        )

    def has_warnings(self) -> bool:
        """
        Returns True if the notification contains a 'warnings' key, False otherwise.

        Args:
            None

        Returns:
            bool: True if the notification contains a 'warnings' key, False otherwise.
        """

        # Return True, if the 'warnings' key is present, otherwise False
        return self.has(key="warnings")

    def is_empty(self) -> bool:
        """
        Returns True if the notification is empty, False otherwise.

        Args:
            None

        Returns:
            bool: True if the notification is empty, False otherwise.
        """

        # Return True, if the notification is empty, otherwise False
        return len(self.result) == 0


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

    logger: Final[Logger] = Logger.get_logger(name="DispatcherNotificationFactory")

    @classmethod
    def create_notification(
        cls,
        duration: float,
        end: datetime,
        event: DispatcherEvent,
        namespace: str,
        start: datetime,
        errors: Optional[List[Dict[str, Any]]] = None,
        result: Optional[Dict[str, Any]] = None,
        warnings: Optional[List[Dict[str, Any]]] = None,
    ) -> Optional[DispatcherNotification]:
        """
        Creates a new instance of the DispatcherNotification class.

        Args:
            duration (float): The duration of the notification in seconds.
            end (datetime): The timestamp when the notification ended.
            errors (list, optional): A list of dictionary containing information regarding exceptions.
            event (DispatcherEvent): The event associated with the notification.
            namespace (str): The namespace under which the notification was created.
            result (Any): The result of the notification.
            start (datetime): The timestamp when the notification started.
            warnings (list, optional): A list of dictionary containing information regarding warnings.

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
                errors=errors,
                event=event,
                id=cls.index,
                namespace=namespace,
                result=result,
                start=start,
                warnings=warnings,
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

        # Set the duration of the notification
        self.configuration["duration"] = value

        # Return the builder instance
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

        # Set the end datetime of the notification
        self.configuration["end"] = value

        # Return the builder instance
        return self

    def errors(
        self: str,
        function: Callable[[Optional[Any]], Optional[Any]],
        exception: Exception,
        traceback: str,
    ) -> Self:
        """
        Sets the error associated with the notification.

        Args:
            exception (Exception): The Exception object.
            function (callable): The function who's execution resulted in an exception occurring.
            traceback (str): The traceback related to the exception.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'errors' key is already present in the configuration dictionary
        if "errors" not in self.configuration:
            # Initialize an empty list under the 'errors' key
            self.configuration["errors"] = []

        # Append a dictionary of error related information to the errors list
        self.configuration["errors"].append(
            {
                "exception": exception,
                "function": function.__name__,
                "traceback": traceback,
            }
        )

        # Return the builder instance to th caller
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

        # Set the event name associated with the notification
        self.configuration["event"] = value

        # Return the builder instance
        return self

    def has_result(self) -> bool:
        """
        Checks if the notification has a result.

        Args:
            None

        Returns:
            bool: True if the notification has a result, False otherwise.
        """

        return "result" in self.configuration

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

        # Set the namespace associated with the notification
        self.configuration["namespace"] = value

        # Return the builder instance
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

        # Check, if the 'result' key is already present in the configuration dictionary
        if "result" not in self.configuration:
            # Initialize an empty dictionary under the 'result' key
            self.configuration["result"] = {}

        # Set the result of the notification
        self.configuration["result"][key] = value

        # Return the builder instance
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

        # Set the start datetime of the notification
        self.configuration["start"] = value

        # Return the builder instance
        return self

    def warnings(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the list of warnings associated with the notification.

        Args:
            value (Dict[str, Any]): The dictionary of warning related information.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'warnings' key is already present in the configuration dictionary
        if "warnings" not in self.configuration:
            # Initialize an empty list under the 'warnings' key
            self.configuration["warnings"] = []

        # Append a dictionary of warning related information to the warnings list
        self.configuration["warnings"].append(value)

        # Return the builder instance to th caller
        return self


class DispatcherEventSubscription(ImmutableBaseObject):
    """
    A class representing a subscription to an event.

    Attributes:
        event (DispatcherEvent): The event associated with the subscription.
        id (int): The ID of the subscription.
        subscriptions (Dict[str, Dict[str, Any]]): The subscriptions dictionary.
    """

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
            hide_attributes=True,
            id=id,
            subscriptions={},
        )

    @property
    def event(self) -> DispatcherEvent:
        """
        Gets the event associated with the subscription.

        Returns:
            DispatcherEvent: The event associated with the subscription.
        """

        # Return the event associated with the subscription
        return self._event

    @property
    def id(self) -> int:
        """
        Gets the ID of the subscription.

        Returns:
            int: The ID of the subscription.
        """

        # Return the ID of the subscription
        return self._id

    @property
    def subscriptions(self) -> Dict[str, Dict[str, Any]]:
        """
        Gets the subscriptions dictionary.

        Returns:
            Dict[str, Dict[str, Any]]: The subscriptions dictionary.
        """

        # Return the subscriptions dictionary
        return self._subscriptions

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

    def contains_namespace(
        self,
        namespace: str,
    ) -> bool:
        """
        Checks if a namespace exists in the subscriptions dictionary.

        Args:
            namespace (str): The namespace to check.

        Returns:
            bool: True if the namespace exists, False otherwise.
        """

        # Return whether the namespace exists in the subscriptions dictionary
        return namespace in self.subscriptions.keys()

    def notify_subscriptions(
        self,
        builder: DispatcherNotificationBuilder,
        namespace: str,
        *args,
        **kwargs,
    ) -> Optional[DispatcherNotification]:
        """
        Notifies all subscriptions associated with a given namespace.

        This method iterates over the subscriptions dictionary and calls the
        function associated with each subscription.

        Args:
            builder (DispatcherNotificationBuilder): The notification builder.
            namespace (str): The namespace under which the subscriptions are categorized.
            *args: The arguments to pass to the function.
            **kwargs: The keyword arguments to pass to the function.

        Returns:
            Optional[DispatcherNotification]: The notification built from the subscriptions.

        Raises:
            Exception: If an exception occurs while building the notification.
        """

        # Initialize a list to store the UUIDs of non-persistent subscriptions
        non_persistents: List[str] = []

        # Get the subscriptions in the namespace
        subscriptions: Dict[str, Any] = self.subscriptions.get(
            namespace,
            {},
        )

        # Check if the subscriptions dictionary is empty
        if not subscriptions:
            # Add the 'NaN' key with a None type value to the result to indicate an empty notification
            builder.result(
                key="NaN",
                value=None,
            )

            # Return the builder instance to the caller
            return builder

        # Iterate over the subscriptions in the namespace
        for (
            uuid,
            subscription,
        ) in subscriptions.items():
            # Check if the subscription is persistent
            if not subscription.get(
                "persistent",
                False,
            ):
                # Add the subscription to the subscriptions dictionary
                non_persistents.append(uuid)

            # Log a message indicating the function is beeing called
            self.logger.info(
                message=f"Calling function '{subscription['function'].__name__}' with arguments '{args}' and '{kwargs}' in namespace '{namespace}'."
            )

            try:
                # Call the function associated with the subscription
                builder.result(
                    key=subscription["function"].__name__,
                    value=subscription["function"](
                        *args,
                        **kwargs,
                    ),
                )
            except Exception as exception:
                # Log an error message indicating that an exception has occurred
                self.logger.error(
                    message=f"Caught an exception while attempting to run '{subscription["function"].__name__}' 'notify_subscription' from '{self.__class__.__name__}' class : {exception}"
                )

                # Log the traceback
                self.logger.error(message=traceback.format_exc())

                # Add the function to the result with a Nonetype value
                builder.result(
                    key=subscription["function"].__name__,
                    value=None,
                )

                # Add the error to the result indicating that an exception has occurred
                builder.errors(
                    exception=exception,
                    function=subscription["function"],
                    traceback=traceback.format_exc(),
                )

        # Iterate over the non-persistent subscriptions
        for uuid in non_persistents:
            # Remove the subscription from the dispatcher
            self.remove_subscription(uuid=uuid)

        # Return the notification
        return builder

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
                if uuid not in self.subscriptions[namespace].keys():
                    # Skip to the next namespace
                    continue

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

    logger: Final[Logger] = Logger.get_logger(name="DispatcherEventSubscriptionFactory")

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


class Dispatcher(ImmutableBaseObject):
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

        If the instance does not exist, it creates a new one by calling the parent
        class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, it returns the existing instance.

        Returns:
            Dispatcher: The created or existing instance of Dispatcher class.
        """
        # Check if the shared instance already exists
        if cls._shared_instance is None:
            # Create a new instance of the Dispatcher class
            cls._shared_instance = super(Dispatcher, cls).__new__(cls)
            # Initialize the new instance
            cls._shared_instance.init()
        # Return the shared instance
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

        # Call the parent class constructor
        super().__init__(
            hide_attributes=True,
            subscriptions={},
        )

    @property
    def subscriptions(self) -> Dict[str, DispatcherEventSubscription]:
        """
        Gets the subscriptions dictionary.

        Returns:
            Dict[str, DispatcherEventSubscription]: The subscriptions dictionary.
        """

        # Return the subscriptions dictionary
        return self._subscriptions

    def dispatch(
        self,
        event: DispatcherEvent,
        namespace: str,
        *args,
        **kwargs,
    ) -> DispatcherNotification:
        """
        Dispatches an event to all registered subscriptions.

        Args:
            event (DispatcherEvent): The event to be dispatched.
            namespace (str): The namespace under which the subscriptions are categorized.
            *args: Additional positional arguments to be passed to the event handler.
            **kwargs: Additional keyword arguments to be passed to the event handler.

        Returns:
            DispatcherNotification: The notification object.
        """

        # Initialize a new notification builder
        builder: DispatcherNotificationBuilder = DispatcherNotificationBuilder()

        # Set the event of the notification builder
        builder.event(value=event)

        # Set the namespace of the notification builder
        builder.namespace(value=namespace)

        # Get the current datetime
        start: datetime = DateUtil.now()

        # Set the start time of the notification builder
        builder.start(value=start)

        try:
            # Check if the event exists in the subscriptions dictionary
            if not self.is_event_registered(event=event):
                # Log a warning message indicating the event was not found
                self.logger.warning(
                    message=f"Event '{event.name}' not found in namespace '{namespace}'."
                )

                # Set the result of the notification builder
                builder.result(
                    key="NaN",
                    value=None,
                )

                # Add a warning to the notification builder
                builder.warnings(
                    value={
                        "args": args,
                        "event": event,
                        "kwargs": kwargs,
                        "message": f"Event '{event.name}' not found in namespace '{namespace}'.",
                        "namespace": namespace,
                        "timestamp": DateUtil.now(),
                    }
                )
            else:
                # Attempt to dispatch the event
                builder = self.subscriptions[event.name].notify_subscriptions(
                    builder=builder,
                    namespace=namespace,
                    *args,
                    **kwargs,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to dispatch event '{event.name}' in namespace '{namespace}': {e}",
            )

            # Log additional information about the exception
            self.logger.error(
                message=f"An error occurred while dispatching event '{event.name}' in namespace '{namespace}' with arguments '{args}' and '{kwargs}'.",
            )
        finally:
            # Set the end time of the notification builder
            builder.end(value=DateUtil.now())

            # Set the duration of the notification builder
            builder.duration(value=DateUtil.calculate_duration(start=start))

            # Return the notification
            return builder.build()

    def is_event_registered(
        self,
        event: Union[DispatcherEvent, str],
    ) -> bool:
        """
        Checks if a given event is registered.

        Args:
            event (Union[DispatcherEvent, str]): The event to check.

        Returns:
            bool: True if the event is registered, False otherwise.
        """

        # Check, if the event is a DispatcherEvent instance
        if isinstance(
            event,
            DispatcherEvent,
        ):
            # Extract the event name
            event = event.name

        # Check, if the event is registered
        return event in self.subscriptions.keys()

    def is_namespace_registered(
        self,
        namespace: str,
    ) -> bool:
        """
        Checks if a given namespace is registered.

        Args:
            namespace (str): The namespace to check.

        Returns:
            bool: True if the namespace is registered, False otherwise.
        """

        # Check, if the subscriptions dictionary is empty
        if not self.subscriptions:
            # Return False if the subscriptions dictionary is empty
            return False

        # Iterate over the subscriptions dictionary
        for subscription in self.subscriptions.values():
            # Check, if the subscription contains the namespace
            if not subscription.contains_namespace(namespace=namespace):
                # Skip to the next subscription
                continue

            # Return True if the namespace is registered
            return True

        # Return False if the namespace is not registered
        return False

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
            # Check if the event is already registered
            if not self.is_event_registered(event=event):
                # Create a new dictionary for the event if it doesn't exist
                self.subscriptions[event.name] = {}

            # Attempt to create a new subscription
            subscription: Optional[DispatcherEventSubscription] = (
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
        """
        Unregisters event handlers from the subscriptions dictionary.

        This method can be used to bulk remove subscriptions by event, namespace,
        or UUID.

        Args:
            event (Optional[DispatcherEvent]): The event whose subscriptions are to be removed.
            namespace (Optional[str]): The namespace whose subscriptions are to be removed.
            uuid (Optional[str]): The UUID of the subscription to be removed.

        Returns:
            Optional[bool]: True if the subscriptions were removed, False if the event was not found, or None if an exception occurred.
        """
        try:
            if all([not event, not namespace, not uuid]):
                raise ValueError(
                    "At least one of event, namespace, and uuid must be specified."
                )

            if event:
                # Remove the event from the subscriptions dictionary
                if self.is_event_registered(event=event):
                    self.subscriptions.pop(event.name)

                    # Log an info message indicating the subscriptions were removed
                    self.logger.info(
                        message=f"Subscriptions with event '{event.name}' successfully bulk removed from subscriptions."
                    )

                    # Return True indicating the subscriptions were removed
                    return True
                else:
                    # Log a warning message indicating the event was not found
                    self.logger.warning(
                        message=f"Event '{event.name}' not found in subscriptions."
                    )

                    # Return False indicating the event was not found
                    return False

            if namespace:
                # Remove the namespace from the subscriptions dictionary
                for subscription in self.subscriptions.values():
                    if namespace in subscription.subscriptions.keys():
                        subscription.subscriptions.pop(namespace)

                # Log an info message indicating the subscriptions were removed
                self.logger.info(
                    message=f"Subscriptions with namespace '{namespace}' successfully bulk removed from subscriptions."
                )

                # Return True indicating the subscriptions were removed
                return True

            if uuid:
                # Remove the subscription from the subscriptions dictionary
                for subscription in self.subscriptions.values():
                    for namespace in subscription.subscriptions.keys():
                        if uuid in subscription.subscriptions[namespace]:
                            subscription.subscriptions[namespace].pop(uuid)

                            # Log an info message indicating the subscription was removed
                            self.logger.info(
                                message=f"Subscription with UUID '{uuid}' successfully removed from '{namespace}' namespace subscriptions."
                            )

                            # Return True indicating the subscription was removed
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
