"""
Author: lodego
Date: 2025-03-29
"""

import asyncio

from datetime import datetime

from typing import *

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableLearningSession",
    "MutableLearningSession",
    "LearningSessionConverter",
    "LearningSessionFactory",
    "LearningSessionBuilder",
    "LearningSessionManager",
    "LearningSessionModel",
    "ImmutableLearningSessionItem",
    "MutableLearningSessionItem",
    "LearningSessionItemConverter",
    "LearningSessionItemFactory",
    "LearningSessionItemBuilder",
    "LearningSessionItemManager",
    "LearningSessionItemModel",
]


class ImmutableLearningSession(ImmutableBaseObject):
    """
    Represents an immutable learning session.

    This class is responsible for encapsulating the properties of an immutable learning session.

    Attributes:
        children (Optional[List[str]]): A list of child learning sessions.
        contents (Optional[List[str]]): A list of contents.
        created_at (Optional[datetime]): The timestamp when the learning session was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session.
        end (Optional[datetime]): The end time of the learning session.
        filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
        id (Optional[int]): The ID of the learning session.
        key (Optional[str]): The key of the learning session.
        result (Optional[int]): The result of the learning session.
        stacks (Optional[List[str]]): The stacks associated with the learning session.
        start (Optional[datetime]): The start time of the learning session.
        status (Optional[int]): The status of the learning session.
        updated_at (Optional[datetime]): The timestamp when the learning session was last updated.
        uuid (Optional[str]): The UUID of the learning session.
    """

    def __init__(
        self,
        children: Optional[List[str]] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        result: Optional[int] = None,
        stacks: Optional[List[str]] = None,
        start: Optional[datetime] = None,
        status: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableLearningSession class.

        Args:
            children (Optional[List[str]]): A list of child learning session keys.
            contents (Optional[List[str]]): A list of content keys.
            created_at (Optional[datetime]): The timestamp when the learning session was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the learning session.
            end (Optional[datetime]): The end time of the learning session.
            filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
            id (Optional[int]): The ID of the learning session.
            key (Optional[str]): The key of the learning session.
            result (Optional[int]): The result of the learning session.
            stacks (Optional[List[str]]): The stacks associated with the learning session.
            start (Optional[datetime]): The start time of the learning session.
            status (Optional[int]): The status of the learning session.
            updated_at (Optional[datetime]): The timestamp when the learning session was last updated.
            uuid (Optional[str]): The UUID of the learning session.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            children=children,
            contents=contents,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            filters=filters,
            id=id,
            key=key,
            result=result,
            stacks=stacks,
            start=start,
            status=status,
            updated_at=updated_at,
            uuid=uuid,
        )

    def get_custom_field_value(
        self,
        customfield_id: str,
    ) -> Optional[Any]:
        """
        Retrieves the value of a custom field by its ID.

        Args:
            customfield_id (str): The ID of the custom field to retrieve.

        Returns:
            Optional[Any]: The value of the custom field if found, otherwise None.
        """
        try:
            # Iterate over the custom field values and return the value for the matching customfield_id
            return next(
                item["value"]
                for item in self.custom_field_values
                if item["customfield_id"] == customfield_id
            )
        except StopIteration as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def to_mutable(self) -> Optional["MutableLearningSession"]:
        """
        Converts the ImmutableLearningSession instance to a MutableLearningSession instance.

        This method is responsible for creating a mutable copy of the ImmutableLearningSession instance.

        Returns:
            Optional[MutableLearningSession]: A mutable copy of the ImmutableLearningSession instance if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a mutable copy of this ImmutableLearningSession object
            return MutableLearningSession(**self.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an error has occurred
            return None


class MutableLearningSession(MutableBaseObject):
    """
    Represents a mutable learning session.

    This class is responsible for encapsulating the properties of a mutable learning session.

    Attributes:
        children (Optional[List[str]]): A list of child learning session keys.
        contents (Optional[List[str]]): A list of content keys.
        created_at (Optional[datetime]): The timestamp when the learning session was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session.
        end (Optional[datetime]): The end time of the learning session.
        filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
        id (Optional[int]): The ID of the learning session.
        key (Optional[str]): The key of the learning session.
        result (Optional[int]): The result of the learning session.
        stacks (Optional[List[str]]): The stacks associated with the learning session.
        start (Optional[datetime]): The start time of the learning session.
        status (Optional[int]): The status of the learning session.
        updated_at (Optional[datetime]): The timestamp when the learning session was last updated.
        uuid (Optional[str]): The UUID of the learning session.
    """

    def __init__(
        self,
        children: Optional[List[str]] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        result: Optional[int] = None,
        stacks: Optional[List[str]] = None,
        start: Optional[datetime] = None,
        status: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableLearningSession class.

        Args:
            children (Optional[List[str]]): A list of child learning session keys.
            contents (Optional[List[str]]): A list of content keys.
            created_at (Optional[datetime]): The timestamp when the learning session was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the learning session.
            end (Optional[datetime]): The end time of the learning session.
            filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
            id (Optional[int]): The ID of the learning session.
            key (Optional[str]): The key of the learning session.
            result (Optional[int]): The result of the learning session.
            stacks (Optional[List[str]]): The stacks associated with the learning session.
            start (Optional[datetime]): The start time of the learning session.
            status (Optional[int]): The status of the learning session.
            updated_at (Optional[datetime]): The timestamp when the learning session was last updated.
            uuid (Optional[str]): The UUID of the learning session.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            children=children,
            contents=contents,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            filters=filters,
            id=id,
            key=key,
            result=result,
            stacks=stacks,
            start=start,
            status=status,
            updated_at=updated_at,
            uuid=uuid,
        )

    def add_child(
        self,
        child: Union[
            "ImmutableLearningSessionItem",
            "MutableLearningSessionItem",
        ],
    ) -> bool:
        """
        Adds a child to the learning session.

        Args:
            child (Union["ImmutableLearningSessionItem", "MutableLearningSessionItem"]: The child to add.

        Returns:
            bool: True if the child was successfully added, False otherwise.
        """
        try:
            # Check, if the child's key attribute is not already in the children list
            if child.key in self.children:
                # Return False indicating the child was not added
                return False

            # Add the child to the learning session
            self.children.append(child.key)

            # Return True indicating the child was added
            return True
        except Exception as e:
            # Log an error indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'add_child' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an error has occurred
            return False

    def calculate_duration(self) -> None:
        """
        Calculates the duration of the learning session.

        Returns:
            None
        """

        # Check, if the duration has not already been calculated
        if self.duration is not None:
            # Return indicating the duration has already been calculated
            return

        # Calculate the duration of the learning session
        self.duration = (self.end - self.start).total_seconds()

    def get_custom_field_value(
        self,
        customfield_id: str,
    ) -> Optional[Any]:
        """
        Retrieves the value of a custom field by its ID.

        Args:
            customfield_id (str): The ID of the custom field to retrieve.

        Returns:
            Optional[Any]: The value of the custom field if found, otherwise None.
        """
        try:
            # Iterate over the custom field values and return the value for the matching customfield_id
            return next(
                item["value"]
                for item in self.custom_field_values
                if item["customfield_id"] == customfield_id
            )
        except StopIteration as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def set_custom_field_value(
        self,
        customfield_id: str,
        value: Any,
    ) -> None:
        """
        Sets the value of a custom field by its ID.

        Args:
            customfield_id (str): The ID of the custom field to set.
            value (Any): The value to set for the custom field.

        Returns:
            None
        """
        try:
            # Iterate over the custom field values and update the value for the matching customfield_id
            for item in self.custom_field_values:
                if item["customfield_id"] == customfield_id:
                    item["value"] = value
                    return
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'set_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Return indicating an error has occurred
            return

    def to_immutable(self) -> Optional[ImmutableLearningSession]:
        """
        Converts the MutableLearningSession instance to an ImmutableLearningSession instance.

        This method is responsible for creating an immutable copy of the MutableLearningSession instance.

        Returns:
            Optional[ImmutableLearningSession]: An immutable copy of the MutableLearningSession instance if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return an immutable copy of this MutableLearningSession object
            return ImmutableLearningSession(**self.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an error has occurred
            return None


class LearningSessionConverter:
    """
    A converter class for transforming between LearningSessionModel and ImmutableLearningSession instances.

    This class provides methods to convert a LearningSessionModel instance to an ImmutableLearningSession instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the LearningSessionConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="LearningSessionConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "LearningSessionModel",
    ) -> Optional[ImmutableLearningSession]:
        """
        Converts a given LearningSessionModel instance to an ImmutableLearningSession instance.

        Args:
            model (LearningSessionModel): The LearningSessionModel instance to be converted.

        Returns:
            ImmutableLearningSession: The converted ImmutableLearningSession instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the LearningSessionModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSession class from the dictionary representation of the LearningSessionModel instance
            return ImmutableLearningSession(
                **model.to_dict(
                    exclude=[
                        "_logger",
                        "table",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'model_to_object' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def object_to_model(
        cls,
        object: ImmutableLearningSession,
    ) -> Optional["LearningSessionModel"]:
        """
        Converts a given ImmutableLearningSession instance to a LearningSessionModel instance.

        Args:
            object (ImmutableLearningSession): The ImmutableLearningSession instance to be converted.

        Returns:
            LearningSessionModel: The converted LearningSessionModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableLearningSession instance.
        """
        try:
            # Attempt to create and return a new instance of the LearningSessionModel class from the dictionary representation of the ImmutableLearningSession instance
            return LearningSessionModel(
                **object.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionFactory:
    """
    Factory class for creating ImmutableLearningSession instances.

    This class provides a method to create an ImmutableLearningSession object by accepting
    various parameters related to a learning session. It uses a logger to capture and log any
    exceptions that may occur during the creation process.

    Attributes:
        logger (Logger): The logger instance associated with the class.
    """

    logger: Final[Logger] = Logger.get_logger(name="LearningSessionFactory")

    @classmethod
    def create_learning_session(
        cls,
        children: Optional[List[str]] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        result: Optional[int] = None,
        stacks: Optional[List[str]] = None,
        start: Optional[datetime] = None,
        status: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableLearningSession]:
        """
        Creates and returns an ImmutableLearningSession object from the given parameters.

        Args:
            children (Optional[List[str]], optional): The children of the learning session. Defaults to None.
            contents (Optional[List[str]], optional): The contents of the learning session. Defaults to None.
            created_at (Optional[datetime], optional): The timestamp when the learning session was created. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the learning session. Defaults to None.
            duration (Optional[float], optional): The duration of the learning session. Defaults to None.
            end (Optional[datetime], optional): The end time of the learning session. Defaults to None.
            filters (Optional[List[Dict[str, Any]]], optional): The filters applied to the learning session. Defaults to None.
            id (Optional[int], optional): The ID of the learning session. Defaults to None.
            key (Optional[str], optional): The key of the learning session. Defaults to None.
            result (Optional[int], optional): The result of the learning session. Defaults to None.
            stacks (Optional[List[str]], optional): The stacks associated with the learning session. Defaults to None.
            start (Optional[datetime], optional): The start time of the learning session. Defaults to None.
            status (Optional[int], optional): The status of the learning session. Defaults to None.
            updated_at (Optional[datetime], optional): The timestamp when the learning session was last updated. Defaults to None.
            uuid (Optional[str], optional): The UUID of the learning session. Defaults to None.

        Returns:
            Optional[ImmutableLearningSession]: The created ImmutableLearningSession object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the learning session.
        """
        try:
            # Attempt to create and return an ImmutableLearningSession object
            return ImmutableLearningSession(
                children=children,
                contents=contents,
                created_at=created_at,
                custom_field_values=custom_field_values,
                duration=duration,
                end=end,
                filters=filters,
                id=id,
                key=key,
                result=result,
                stacks=stacks,
                start=start,
                status=status,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_session' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionBuilder(BaseObjectBuilder):
    """
    Builder class for creating ImmutableLearningSession instances.

    This class provides a method to create an ImmutableLearningSession object by accepting
    various parameters related to a learning session. It uses a logger to capture and log any
    exceptions that may occur during the creation process.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the LearningSessionBuilder class.

        This class provides a method to create an ImmutableLearningSession object by accepting
        various parameters related to a learning session. It uses a logger to capture and log any
        exceptions that may occur during the creation process.
        """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(self) -> Optional[ImmutableLearningSession]:
        """
        Builds an ImmutableLearningSession object using the configuration dictionary.

        This method attempts to create an instance of the ImmutableLearningSession class
        using the configuration provided to the builder. If the creation fails, it logs an error
        and returns None.

        Returns:
            Optional[ImmutableLearningSession]: The created ImmutableLearningSession object if successful,
            otherwise None.

        Raises:
            Exception: If an exception occurs while attempting to create the ImmutableLearningSession object.
        """
        try:
            # Attempt to create an ImmutableLearningSession object using the configuration
            learning_session: Optional[ImmutableLearningSession] = (
                LearningSessionFactory.create_learning_session(**self.configuration)
            )

            # Check if the learning_session was successfully created
            if not learning_session:
                # Log an error message indicating the creation failed
                self.logger.error(
                    message=f"Failed to create an ImmutableLearningSession object from configuration: {self.configuration}"
                )

                # Return None indicating a failure in creation
                return None

            # Return the successfully created ImmutableLearningSession object
            return learning_session
        except Exception as e:
            # Log an error message indicating an exception occurred during the build process
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def children(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the children attribute of the builder.

        Args:
            value (Union[List[str], str]): The value to set for the children attribute.

        Returns:
            Self: The builder instance with the children attribute set.
        """
        # Check if the "children" key is already present in the configuration
        if "children" not in self.configuration:
            # Initialize the "children" key with an empty list
            self.configuration["children"] = []

        # Add the value to the children list
        self.configuration["children"].extend(
            value
            if isinstance(
                value,
                list,
            )
            else self.configuration["children"].append(value)
        )
        return self
    
    def contents(self, value: Union[List[str], str],) -> Self:
        """
        Sets the contents attribute of the builder.

        Args:
            value (Union[List[str], str]): The value to set for the contents attribute.

        Returns:
            Self: The builder instance with the contents attribute set.
        """
        # Check if the "contents" key is already present in the configuration
        if "contents" not in self.configuration:
            # Initialize the "contents" key with an empty list
            self.configuration["contents"] = []

        # Add the value to the contents list
        self.configuration["contents"].extend(
            value
            if isinstance(
                value,
                list,
            )
            else self.configuration["contents"].append(value)
        )
        return self

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the created_at attribute of the builder.

        Args:
            value (datetime): The value to set for the created_at attribute.

        Returns:
            Self: The builder instance with the created_at attribute set.
        """
        self.configuration["created_at"] = value
        return self

    def duration(
        self,
        value: float,
    ) -> Self:
        """
        Sets the duration attribute of the builder.

        Args:
            value (float): The value to set for the duration attribute.

        Returns:
            Self: The builder instance with the duration attribute set.
        """
        self.configuration["duration"] = value
        return self

    def end(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the end attribute of the builder.

        Args:
            value (datetime): The value to set for the end attribute.

        Returns:
            Self: The builder instance with the end attribute set.
        """
        self.configuration["end"] = value
        return self

    def filters(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> Self:
        """
        Sets the filters attribute of the builder.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The value to set for the filters attribute.

        Returns:
            Self: The builder instance with the filters attribute set.
        """
        # Check if the "filters" key is already present in the configuration
        if "filters" not in self.configuration:
            # Initialize the "filters" key with an empty list
            self.configuration["filters"] = []

        # Add the value to the filters list
        (
            self.configuration["filters"].append(value)
            if isinstance(value, dict)
            else self.configuration["filters"].extend(value)
        )
        return self

    def id(
        self,
        value: int,
    ) -> Self:
        """
        Sets the id attribute of the builder.

        Args:
            value (int): The value to set for the id attribute.

        Returns:
            Self: The builder instance with the id attribute set.
        """
        self.configuration["id"] = value
        return self

    def key(
        self,
        value: str,
    ) -> Self:
        """
        Sets the key attribute of the builder.

        Args:
            value (str): The value to set for the key attribute.

        Returns:
            Self: The builder instance with the key attribute set.
        """
        self.configuration["key"] = value
        return self

    def result(
        self,
        value: str,
    ) -> Self:
        """
        Sets the result attribute of the builder.

        Args:
            value (str): The value to set for the result attribute.

        Returns:
            Self: The builder instance with the result attribute set.
        """
        self.configuration["result"] = value
        return self

    def stacks(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the stacks attribute of the builder.

        Args:
            value (Union[List[str], str]): The value to set for the stacks attribute.

        Returns:
            Self: The builder instance with the stacks attribute set.
        """
        # Check if the "stacks" key is already present in the configuration
        if "stacks" not in self.configuration:
            # Initialize the "stacks" key with an empty list
            self.configuration["stacks"] = []

        # Add the value to the stacks list
        (
            self.configuration["stacks"].append(value)
            if isinstance(
                value,
                str,
            )
            else self.configuration["stacks"].extend(value)
        )
        return self

    def start(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the start attribute of the builder.

        Args:
            value (datetime): The value to set for the start attribute.

        Returns:
            Self: The builder instance with the start attribute set.
        """
        self.configuration["start"] = value
        return self

    def status(
        self,
        value: int,
    ) -> Self:
        """
        Sets the status attribute of the builder.

        Args:
            value (int): The value to set for the status attribute.

        Returns:
            Self: The builder instance with the status attribute set.
        """
        self.configuration["status"] = value
        return self

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the updated_at attribute of the builder.

        Args:
            value (datetime): The value to set for the updated_at attribute.

        Returns:
            Self: The builder instance with the updated_at attribute set.
        """
        self.configuration["updated_at"] = value
        return self

    def uuid(
        self,
        value: str,
    ) -> Self:
        """
        Sets the uuid attribute of the builder.

        Args:
            value (str): The value to set for the uuid attribute.

        Returns:
            Self: The builder instance with the uuid attribute set.
        """
        self.configuration["uuid"] = value
        return self


class LearningSessionManager(BaseObjectManager):
    """
    A manager class for managing learning_sessions in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for learning_sessions.

    Attributes:
        cache: (List[Any]): The cache for storing learning_sessions.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["LearningSessionManager"] = None

    def __new__(cls) -> "LearningSessionManager":
        """
        Creates and returns a new instance of the LearningSessionManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            LearningSessionManager: The created or existing instance of LearningSessionManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(LearningSessionManager, cls).__new__(cls)
            # Initialize the instance with the dispatcher and stacks
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the LearningSessionManager class.

        Returns:
            None
        """
        pass

    def count_learning_sessions(self) -> int:
        """
        Returns the number of learning_sessions in the database.

        Returns:
            int: The number of learning_sessions in the database.
        """
        try:
            # Count and return the number of learning_sessions in the database
            return asyncio.run(
                LearningSessionModel.count(database=Constants.DATABASE_PATH)
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_learning_session(
        self,
        learning_session: Union[ImmutableLearningSession, MutableLearningSession],
    ) -> Optional[ImmutableLearningSession]:
        """
        Creates a new learning_session in the database.

        Args:
            learning_session (Union[ImmutableLearningSession, MutableLearningSession]): The learning_session to be created.

        Returns:
            Optional[ImmutableLearningSession]: The newly created immutable learning_session if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the learning_session.
        """
        try:
            # Check if the learning_session object is immutable
            if isinstance(
                learning_session,
                ImmutableLearningSession,
            ):
                # If it is, convert it to a mutable learning_session
                learning_session = learning_session.to_mutable()

            # Set the created_at timestamp of the learning_session
            learning_session.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the learning_session
            learning_session.custom_field_values = (
                [] or learning_session.custom_field_values
            )

            # Set the key of the learning_session
            learning_session.key = (
                f"LEARNING_SESSION_{self.count_learning_sessions() + 1}"
            )

            # Set the updated_at timestamp of the learning_session
            learning_session.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the learning_session
            learning_session.uuid = Miscellaneous.get_uuid()

            # Convert the learning_session object to a LearningSessionModel object
            model: LearningSessionModel = LearningSessionConverter.object_to_model(
                object=learning_session
            )

            # Create a new learning_session in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the learning_session
                learning_session.id = id

                # Convert the learning_session to an immutable learning_session
                learning_session = LearningSessionFactory.create_learning_session(
                    **learning_session.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the learning_session to the cache
                self.add_to_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

                # Return the newly created immutable learning_session
                return learning_session

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a learning_session ({learning_session}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_session' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_learning_session(
        self,
        learning_session: Union[ImmutableLearningSession, MutableLearningSession],
    ) -> bool:
        """
        Deletes a learning_session from the database.

        Args:
            learning_session (Union[ImmutableLearningSession, MutableLearningSession]): The learning_session to be deleted.

        Returns:
            bool: True if the learning_session was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the learning_session to an immutable learning_session and delete the learning_session from the database
            result: bool = asyncio.run(
                LearningSessionConverter.object_to_model(
                    object=LearningSessionFactory.create_learning_session(
                        **learning_session.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the learning_session from the cache
            self.remove_from_cache(key=learning_session.key)

            # Return True if the learning_session was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_learning_sessions(self) -> Optional[List[ImmutableLearningSession]]:
        """
        Returns a list of all learning_sessions in the database.

        Returns:
            Optional[List[ImmutableLearningSession]]: A list of all learning_sessions in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_learning_sessions():
                # Return the list of immutable learning_sessions from the cache
                return self.get_cache_values()

            # Get all learning_sessions from the database
            models: List[LearningSessionModel] = asyncio.run(
                LearningSessionModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of LearningSessionModel objects to a list of ImmutableLearningSession objects
            learning_sessions: List[ImmutableLearningSession] = [
                LearningSessionFactory.create_learning_session(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable learning_sessions
            for learning_session in learning_sessions:
                # Add the immutable learning_session to the cache
                self.add_to_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

            # Return the list of immutable learning_sessions
            return learning_sessions
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableLearningSession]:
        """
        Retrieves a learning_session by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableLearningSession]: The learning_session with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the learning_session from the cache
                return self.get_value_from_cache(key=field)

            # Get the learning_session with the given field and value from the database
            model: Optional[LearningSessionModel] = asyncio.run(
                LearningSessionModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the learning_session if it exists
            if model is not None:
                # Convert the LearningSessionModel object to an ImmutableLearningSession object
                learning_session: ImmutableLearningSession = (
                    LearningSessionFactory.create_learning_session(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session to the cache
                self.add_to_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

                # Return the learning_session
                return learning_session
            else:
                # Return None indicating that the learning_session does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableLearningSession]:
        """
        Returns a learning_session with the given ID.

        Args:
            id (int): The ID of the learning_session.

        Returns:
            Optional[ImmutableLearningSession]: The learning_session with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session is already in the cache
            if self.is_key_in_cache(key=f"LEARNING_SESSION_{id}"):
                # Return the learning_session from the cache
                return self.get_value_from_cache(key=f"LEARNING_SESSION_{id}")

            # Get the learning_session with the given ID from the database
            model: Optional[LearningSessionModel] = asyncio.run(
                LearningSessionModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the learning_session if it exists
            if model is not None:
                # Convert the LearningSessionModel object to an ImmutableLearningSession object
                learning_session: ImmutableLearningSession = (
                    LearningSessionFactory.create_learning_session(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session to the cache
                self.add_to_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

                # Return the learning_session
                return learning_session
            else:
                # Return None indicating that the learning_session does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_by_key(
        self,
        key: str,
    ) -> Optional[ImmutableLearningSession]:
        """
        Returns a learning_session with the given key.

        Args:
            key (str): The key of the learning_session.

        Returns:
            Optional[ImmutableLearningSession]: The learning_session with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session is already in the cache
            if self.is_key_in_cache(key=key):
                # Return the learning_session from the cache
                return self.get_value_from_cache(key=key)

            # Get the learning_session with the given key from the database
            model: Optional[LearningSessionModel] = asyncio.run(
                LearningSessionModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the learning_session if it exists
            if model is not None:
                # Convert the LearningSessionModel object to an ImmutableLearningSession object
                learning_session: ImmutableLearningSession = (
                    LearningSessionFactory.create_learning_session(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session to the cache
                self.add_to_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

                # Return the learning_session
                return learning_session
            else:
                # Return None indicating that the learning_session does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableLearningSession]:
        """
        Returns a learning_session with the given UUID.

        Args:
            uuid (str): The UUID of the learning_session.

        Returns:
            Optional[ImmutableLearningSession]: The learning_session with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the learning_session from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the learning_session with the given UUID from the database
            model: Optional[LearningSessionModel] = asyncio.run(
                LearningSessionModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the learning_session if it exists
            if model is not None:
                # Convert the LearningSessionModel object to an ImmutableLearningSession object
                learning_session: ImmutableLearningSession = (
                    LearningSessionFactory.create_learning_session(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session to the cache
                self.add_to_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

                # Return the learning_session
                return learning_session
            else:
                # Return None indicating that the learning_session does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_learning_sessions(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableLearningSession]]]:
        """
        Searches for learning_sessions in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the LearningSessionModel class.

        Returns:
            Optional[Union[List[ImmutableLearningSession]]]: The found learning_sessions if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for learning_sessions in the database
            models: Optional[List[LearningSessionModel]] = asyncio.run(
                LearningSessionModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found learning_sessions if any
            if models is not None and len(models) > 0:
                learning_sessions: List[ImmutableLearningSession] = [
                    LearningSessionFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found learning_sessions
                for learning_session in learning_sessions:
                    # Add the learning_session to the cache
                    self.add_to_cache(
                        key=learning_session.key,
                        value=learning_session,
                    )

                # Return the found learning_sessions
                return learning_sessions
            else:
                # Return None indicating that no learning_sessions were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_learning_session(
        self,
        learning_session: Union[ImmutableLearningSession, MutableLearningSession],
    ) -> Optional[ImmutableLearningSession]:
        """
        Updates a learning_session with the given ID.

        Args:
            learning_session (Union[ImmutableLearningSession, MutableLearningSession]): The learning_session to update.

        Returns:
            Optional[ImmutableLearningSession]: The updated learning_session if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session object is immutable
            if isinstance(
                learning_session,
                ImmutableLearningSession,
            ):
                # If it is, convert it to a mutable learning_session
                learning_session = learning_session.to_mutable()

            # Update the updated_at timestamp of the learning_session
            learning_session.updated_at = Miscellaneous.get_current_datetime()

            # Convert the learning_session to an immutable learning_session and update the learning_session in the database
            result: bool = asyncio.run(
                LearningSessionConverter.object_to_model(
                    object=LearningSessionFactory.create_learning_session(
                        **learning_session.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **learning_session.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the learning_session was updated successfully
            if result:
                # Update the learning_session in the cache
                self.update_in_cache(
                    key=learning_session.key,
                    value=learning_session,
                )

                # Return the updated learning_session
                return learning_session.to_immutable()
            else:
                # Return None indicating that the learning_session does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionModel(ImmutableBaseModel):
    """
    Represents the structure of a learning session model.

    Attributes:
        children (Field): A list of child learning sessions.
        contents (Field): A list of contents of the learning session.
        created_at (Field): The timestamp when the learning session was created.
        custom_field_values (Field): A list of custom field values.
        duration (Field): The duration of the learning session.
        end (Field): The end time of the learning session.
        filters (Field): The filters applied to the learning session.
        id (Field): The ID of the learning session.
        key (Field): The key of the learning session.
        result (Field): The result of the learning session.
        stacks (Field): The stacks associated with the learning session.
        start (Field): The start time of the learning session.
        status (Field): The status of the learning session.
        updated_at (Field): The timestamp when the learning session was last updated.
        uuid (Field): The UUID of the learning session.
    """

    table: str = Constants.LEARNING_SESSIONS

    id: Field = Field(
        autoincrement=True,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="id",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=True,
        size=None,
        type="INTEGER",
        unique=False,
    )

    children: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="children",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    contents: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="contents",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    created_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="created_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    custom_field_values: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="custom_field_values",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    duration: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="duration",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="FLOAT",
        unique=False,
    )

    end: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="end",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    filters: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="filters",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    id: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="id",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=True,
        size=None,
        type="INTEGER",
        unique=False,
    )

    key: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="key",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    result: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.LEARNING_SESSION_ITEMS}(id)",
        index=False,
        name="result",
        nullable=True,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    stacks: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="stacks",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    start: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="start",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    status: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.STATUSES}(id)",
        index=False,
        name="status",
        nullable=True,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    updated_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="updated_at",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    uuid: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="uuid",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    def __init__(
        self,
        children: Optional[List[str]] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        result: Optional[int] = None,
        stacks: Optional[List[str]] = None,
        start: Optional[datetime] = None,
        status: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableLearningSessionModel class.

        Args:
            children (Optional[List[str]]): A list of child learning sessions.
            contents (Optional[List[str]]): A list of contents of the learning session.
            created_at (Optional[datetime]): The timestamp when the learning session was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the learning session.
            end (Optional[datetime]): The end time of the learning session.
            filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
            id (Optional[int]): The ID of the learning session.
            key (Optional[str]): The key of the learning session.
            result (Optional[int]): The result of the learning session.
            stacks (Optional[List[str]]): The stacks associated with the learning session.
            start (Optional[datetime]): The start time of the learning session.
            status (Optional[int]): The status of the learning session.
            updated_at (Optional[datetime]): The timestamp when the learning session was last updated.
            uuid (Optional[str]): The UUID of the learning session.
        """

        # Call the parent class constructor
        super().__init__(
            children=children,
            contents=contents,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            filters=filters,
            id=id,
            key=key,
            result=result,
            stacks=stacks,
            start=start,
            status=status,
            table=Constants.LEARNING_SESSIONS,
            updated_at=updated_at,
            uuid=uuid,
        )


class ImmutableLearningSessionItem(ImmutableBaseObject):
    """
    An immutable version of the MutableLearningSessionItem class.

    This class extends the ImmutableBaseObject class and provides an immutable version of the MutableLearningSessionItem class.
    It is used to represent a learning session item in an immutable form, which cannot be modified after creation.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the learning session item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session item.
        end (Optional[datetime]): The end time of the learning session item.
        id (Optional[int]): The ID of the learning session item.
        key (Optional[str]): The key of the learning session item.
        reference (Optional[str]): The reference of the learning session item.
        start (Optional[datetime]): The start time of the learning session item.
        updated_at (Optional[datetime]): The timestamp when the learning session item was last updated.
        uuid (Optional[str]): The UUID of the learning session item.
    """

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableLearningSessionItem class.

        Args:
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the learning session item.
            end (Optional[datetime]): The end time of the learning session item.
            id (Optional[int]): The ID of the learning session item.
            key (Optional[str]): The key of the learning session item.
            reference (Optional[str]): The reference of the learning session item.
            start (Optional[datetime]): The start time of the learning session item.
            updated_at (Optional[datetime]): The timestamp when the learning session item was last updated.
            uuid (Optional[str]): The UUID of the learning session item.
        """

        # Call the parent class constructor
        super().__init__(
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            reference=reference,
            start=start,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> Optional["MutableLearningSessionItem"]:
        """
        Converts the ImmutableLearningSessionItem instance to a MutableLearningSessionItem instance.

        This method is responsible for creating a mutable copy of the ImmutableLearningSessionItem instance.

        Returns:
            Optional[MutableLearningSessionItem]: A mutable copy of the ImmutableLearningSessionItem instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the mutable copy.
        """
        try:
            # Attempt to create and return a new MutableLearningSessionItem instance
            return MutableLearningSessionItem(**self.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method in '{self.__class__.__name__}': {e}"
            )

            # Return None indicating that an exception has occurred
            return None


class MutableLearningSessionItem(MutableBaseObject):
    """
    A mutable version of the ImmutableLearningSessionItem class.

    This class extends the MutableBaseObject class and provides a mutable version of the ImmutableLearningSessionItem class.
    It is used to represent a learning session item in a mutable form, which can be modified and updated.

    Attributes:
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session item.
        end (Optional[datetime]): The end time of the learning session item.
        id (Optional[int]): The ID of the learning session item.
        key (Optional[str]): The key of the learning session item.
        reference (Optional[str]): The reference of the learning session item.
        start (Optional[datetime]): The start time of the learning session item.
        updated_at (Optional[datetime]): The timestamp when the learning session item was last updated.
        uuid (Optional[str]): The UUID of the learning session item.
    """

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableLearningSessionItem class.

        Args:
            created_at (Optional[datetime]): The timestamp when the item was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the item.
            end (Optional[datetime]): The end time of the item.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            reference (Optional[str]): The reference of the item.
            start (Optional[datetime]): The start time of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            reference=reference,
            start=start,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_immutable(self) -> Optional[ImmutableLearningSessionItem]:
        """
        Converts the MutableLearningSessionItem instance to an ImmutableLearningSessionItem instance.

        This method is responsible for creating an immutable copy of the MutableLearningSessionItem instance.

        Returns:
            Optional[ImmutableLearningSessionItem]: An immutable copy of the MutableLearningSessionItem instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the immutable copy.
        """
        try:
            # Attempt to create and return a new ImmutableLearningSessionItem instance
            return ImmutableLearningSessionItem(**self.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method in '{self.__class__.__name__}': {e}"
            )

            # Return None indicating that an exception has occurred
            return None


class LearningSessionItemConverter:
    """
    A converter class for transforming between LearningSessionItemModel and ImmutableLearningSessionItem instances.

    This class provides methods to convert a LearningSessionItemModel instance to an ImmutableLearningSessionItem instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the LearningSessionItemConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="LearningSessionItemConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "LearningSessionItemModel",
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Converts a given LearningSessionItemModel instance to an ImmutableLearningSessionItem instance.

        Args:
            model (LearningSessionItemModel): The LearningSessionItemModel instance to be converted.

        Returns:
            ImmutableLearningSessionItem: The converted ImmutableLearningSessionItem instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the LearningSessionItemModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSessionItem class from the dictionary representation of the LearningSessionItemModel instance
            return ImmutableLearningSessionItem(
                **model.to_dict(
                    exclude=[
                        "_logger",
                        "table",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'model_to_object' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def object_to_model(
        cls,
        object: ImmutableLearningSessionItem,
    ) -> Optional["LearningSessionItemModel"]:
        """
        Converts a given ImmutableLearningSessionItem instance to a LearningSessionItemModel instance.

        Args:
            object (ImmutableLearningSessionItem): The ImmutableLearningSessionItem instance to be converted.

        Returns:
            LearningSessionItemModel: The converted LearningSessionItemModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableLearningSessionItem instance.
        """
        try:
            # Attempt to create and return a new instance of the LearningSessionItemModel class from the dictionary representation of the ImmutableLearningSessionItem instance
            return LearningSessionItemModel(
                **object.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionItemFactory:
    logger: Final[Logger] = Logger.get_logger(name="LearningSessionItemFactory")

    @classmethod
    def create_learning_session_item(
        cls,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Creates a new learning session item.

        Args:
            created_at (Optional[datetime]): The timestamp when the item was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the item.
            end (Optional[datetime]): The end time of the item.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            reference (Optional[str]): The reference of the item.
            start (Optional[datetime]): The start time of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.

        Returns:
            Optional[ImmutableLearningSessionItem]: The created learning session item if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSessionItem class from the dictionary representation of the MutableLearningSessionItem instance
            return ImmutableLearningSessionItem(
                created_at=created_at,
                custom_field_values=custom_field_values,
                duration=duration,
                end=end,
                id=id,
                key=key,
                reference=reference,
                start=start,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_session_item' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionItemManager(BaseObjectManager):
    """
    A manager class for managing learning_session_items in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for learning_session_items.

    Attributes:
        cache: (List[Any]): The cache for storing learning_session_items.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["LearningSessionItemManager"] = None

    def __new__(cls) -> "LearningSessionItemManager":
        """
        Creates and returns a new instance of the LearningSessionItemManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            LearningSessionItemManager: The created or existing instance of LearningSessionItemManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(LearningSessionItemManager, cls).__new__(cls)
            # Initialize the instance with the dispatcher and stacks
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the LearningSessionItemManager class.

        Returns:
            None
        """
        pass

    def count_learning_session_items(self) -> int:
        """
        Returns the number of learning_session_items in the database.

        Returns:
            int: The number of learning_session_items in the database.
        """
        try:
            # Count and return the number of learning_session_items in the database
            return asyncio.run(
                LearningSessionItemModel.count(database=Constants.DATABASE_PATH)
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_learning_session_item(
        self,
        learning_session_item: Union[
            ImmutableLearningSessionItem, MutableLearningSessionItem
        ],
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Creates a new learning_session_item in the database.

        Args:
            learning_session_item (Union[ImmutableLearningSessionItem, MutableLearningSessionItem]): The learning_session_item to be created.

        Returns:
            Optional[ImmutableLearningSessionItem]: The newly created immutable learning_session_item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the learning_session_item.
        """
        try:
            # Check if the learning_session_item object is immutable
            if isinstance(
                learning_session_item,
                ImmutableLearningSessionItem,
            ):
                # If it is, convert it to a mutable learning_session_item
                learning_session_item = learning_session_item.to_mutable()

            # Set the created_at timestamp of the learning_session_item
            learning_session_item.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the learning_session_item
            learning_session_item.custom_field_values = (
                [] or learning_session_item.custom_field_values
            )

            # Set the key of the learning_session_item
            learning_session_item.key = (
                f"LEARNING_SESSION_ITEM_{self.count_learning_session_items() + 1}"
            )

            # Set the updated_at timestamp of the learning_session_item
            learning_session_item.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the learning_session_item
            learning_session_item.uuid = Miscellaneous.get_uuid()

            # Convert the learning_session_item object to a LearningSessionItemModel object
            model: LearningSessionItemModel = (
                LearningSessionItemConverter.object_to_model(
                    object=learning_session_item
                )
            )

            # Create a new learning_session_item in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the learning_session_item
                learning_session_item.id = id

                # Convert the learning_session_item to an immutable learning_session_item
                learning_session_item = (
                    LearningSessionItemFactory.create_learning_session_item(
                        **learning_session_item.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                )

                # Add the learning_session_item to the cache
                self.add_to_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

                # Return the newly created immutable learning_session_item
                return learning_session_item

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a learning_session_item ({learning_session_item}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_session_item' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_learning_session_item(
        self,
        learning_session_item: Union[
            ImmutableLearningSessionItem, MutableLearningSessionItem
        ],
    ) -> bool:
        """
        Deletes a learning_session_item from the database.

        Args:
            learning_session_item (Union[ImmutableLearningSessionItem, MutableLearningSessionItem]): The learning_session_item to be deleted.

        Returns:
            bool: True if the learning_session_item was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the learning_session_item to an immutable learning_session_item and delete the learning_session_item from the database
            result: bool = asyncio.run(
                LearningSessionItemConverter.object_to_model(
                    object=LearningSessionItemFactory.create_learning_session_item(
                        **learning_session_item.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the learning_session_item from the cache
            self.remove_from_cache(key=learning_session_item.key)

            # Return True if the learning_session_item was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_learning_session_items(
        self,
    ) -> Optional[List[ImmutableLearningSessionItem]]:
        """
        Returns a list of all learning_session_items in the database.

        Returns:
            Optional[List[ImmutableLearningSessionItem]]: A list of all learning_session_items in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_learning_session_items():
                # Return the list of immutable learning_session_items from the cache
                return self.get_cache_values()

            # Get all learning_session_items from the database
            models: List[LearningSessionItemModel] = asyncio.run(
                LearningSessionItemModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of LearningSessionItemModel objects to a list of ImmutableLearningSessionItem objects
            learning_session_items: List[ImmutableLearningSessionItem] = [
                LearningSessionItemFactory.create_learning_session_item(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable learning_session_items
            for learning_session_item in learning_session_items:
                # Add the immutable learning_session_item to the cache
                self.add_to_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

            # Return the list of immutable learning_session_items
            return learning_session_items
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_item_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Retrieves a learning_session_item by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableLearningSessionItem]: The learning_session_item with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_item is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the learning_session_item from the cache
                return self.get_value_from_cache(key=field)

            # Get the learning_session_item with the given field and value from the database
            model: Optional[LearningSessionItemModel] = asyncio.run(
                LearningSessionItemModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the learning_session_item if it exists
            if model is not None:
                # Convert the LearningSessionItemModel object to an ImmutableLearningSessionItem object
                learning_session_item: ImmutableLearningSessionItem = (
                    LearningSessionItemFactory.create_learning_session_item(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_item to the cache
                self.add_to_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

                # Return the learning_session_item
                return learning_session_item
            else:
                # Return None indicating that the learning_session_item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_item_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Returns a learning_session_item with the given ID.

        Args:
            id (int): The ID of the learning_session_item.

        Returns:
            Optional[ImmutableLearningSessionItem]: The learning_session_item with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_item is already in the cache
            if self.is_key_in_cache(key=f"LEARNING_SESSION_ITEM_{id}"):
                # Return the learning_session_item from the cache
                return self.get_value_from_cache(key=f"LEARNING_SESSION_ITEM_{id}")

            # Get the learning_session_item with the given ID from the database
            model: Optional[LearningSessionItemModel] = asyncio.run(
                LearningSessionItemModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the learning_session_item if it exists
            if model is not None:
                # Convert the LearningSessionItemModel object to an ImmutableLearningSessionItem object
                learning_session_item: ImmutableLearningSessionItem = (
                    LearningSessionItemFactory.create_learning_session_item(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_item to the cache
                self.add_to_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

                # Return the learning_session_item
                return learning_session_item
            else:
                # Return None indicating that the learning_session_item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_item_by_key(
        self,
        key: str,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Returns a learning_session_item with the given key.

        Args:
            key (str): The key of the learning_session_item.

        Returns:
            Optional[ImmutableLearningSessionItem]: The learning_session_item with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_item is already in the cache
            if self.is_key_in_cache(key=key):
                # Return the learning_session_item from the cache
                return self.get_value_from_cache(key=key)

            # Get the learning_session_item with the given key from the database
            model: Optional[LearningSessionItemModel] = asyncio.run(
                LearningSessionItemModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the learning_session_item if it exists
            if model is not None:
                # Convert the LearningSessionItemModel object to an ImmutableLearningSessionItem object
                learning_session_item: ImmutableLearningSessionItem = (
                    LearningSessionItemFactory.create_learning_session_item(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_item to the cache
                self.add_to_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

                # Return the learning_session_item
                return learning_session_item
            else:
                # Return None indicating that the learning_session_item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_item_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Returns a learning_session_item with the given UUID.

        Args:
            uuid (str): The UUID of the learning_session_item.

        Returns:
            Optional[ImmutableLearningSessionItem]: The learning_session_item with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_item is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the learning_session_item from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the learning_session_item with the given UUID from the database
            model: Optional[LearningSessionItemModel] = asyncio.run(
                LearningSessionItemModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the learning_session_item if it exists
            if model is not None:
                # Convert the LearningSessionItemModel object to an ImmutableLearningSessionItem object
                learning_session_item: ImmutableLearningSessionItem = (
                    LearningSessionItemFactory.create_learning_session_item(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_item to the cache
                self.add_to_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

                # Return the learning_session_item
                return learning_session_item
            else:
                # Return None indicating that the learning_session_item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_learning_session_items(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableLearningSessionItem]]]:
        """
        Searches for learning_session_items in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the LearningSessionItemModel class.

        Returns:
            Optional[Union[List[ImmutableLearningSessionItem]]]: The found learning_session_items if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for learning_session_items in the database
            models: Optional[List[LearningSessionItemModel]] = asyncio.run(
                LearningSessionItemModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found learning_session_items if any
            if models is not None and len(models) > 0:
                learning_session_items: List[ImmutableLearningSessionItem] = [
                    LearningSessionItemFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found learning_session_items
                for learning_session_item in learning_session_items:
                    # Add the learning_session_item to the cache
                    self.add_to_cache(
                        key=learning_session_item.key,
                        value=learning_session_item,
                    )

                # Return the found learning_session_items
                return learning_session_items
            else:
                # Return None indicating that no learning_session_items were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_learning_session_item(
        self,
        learning_session_item: Union[
            ImmutableLearningSessionItem, MutableLearningSessionItem
        ],
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Updates a learning_session_item with the given ID.

        Args:
            learning_session_item (Union[ImmutableLearningSessionItem, MutableLearningSessionItem]): The learning_session_item to update.

        Returns:
            Optional[ImmutableLearningSessionItem]: The updated learning_session_item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_item object is immutable
            if isinstance(
                learning_session_item,
                ImmutableLearningSessionItem,
            ):
                # If it is, convert it to a mutable learning_session_item
                learning_session_item = learning_session_item.to_mutable()

            # Update the updated_at timestamp of the learning_session_item
            learning_session_item.updated_at = Miscellaneous.get_current_datetime()

            # Convert the learning_session_item to an immutable learning_session_item and update the learning_session_item in the database
            result: bool = asyncio.run(
                LearningSessionItemConverter.object_to_model(
                    object=LearningSessionItemFactory.create_learning_session_item(
                        **learning_session_item.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **learning_session_item.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the learning_session_item was updated successfully
            if result:
                # Update the learning_session_item in the cache
                self.update_in_cache(
                    key=learning_session_item.key,
                    value=learning_session_item,
                )

                # Return the updated learning_session_item
                return learning_session_item.to_immutable()
            else:
                # Return None indicating that the learning_session_item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionItemModel(ImmutableBaseModel):
    """
    Represents the structure of the LearningSessionItemModel.

    Attributes:
        id (Field): The ID of the learning session item.
        created_at (Field): The timestamp when the item was created.
        custom_field_values (Field): A list of custom field values.
        duration (Field): The duration of the item.
        end (Field): The end time of the item.
        key (Field): The key of the item.
        reference (Field): The reference of the item.
        start (Field): The start time of the item.
        updated_at (Field): The timestamp when the item was last updated.
        uuid (Field): The UUID of the item.
    """

    table: Final[str] = Constants.LEARNING_SESSION_ITEMS

    id: Field = Field(
        autoincrement=True,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="id",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=True,
        size=None,
        type="INTEGER",
        unique=False,
    )

    created_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="created_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    custom_field_values: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="custom_field_values",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    duration: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="duration",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="FLOAT",
        unique=False,
    )

    end: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="end",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    key: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="key",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    reference: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="reference",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    start: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="start",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    updated_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="updated_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    uuid: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="uuid",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionItemModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the item was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the item.
            end (Optional[datetime]): The end time of the item.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            reference (Optional[str]): The reference of the item.
            start (Optional[datetime]): The start time of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            reference=reference,
            start=start,
            table=Constants.LEARNING_SESSION_ITEMS,
            updated_at=updated_at,
            uuid=uuid,
        )
