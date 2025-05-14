"""
Author: lodego
Date: 2025-03-29
"""

import asyncio
import json
import traceback

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
    "ImmutableLearningSessionAction",
    "MutableLearningSessionAction",
    "LearningSessionActionConverter",
    "LearningSessionActionFactory",
    "LearningSessionActionBuilder",
    "LearningSessionActionManager",
    "LearningSessionActionModel",
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
        children (Optional[List[str]]): A list of child learning session item keys.
        contents (Optional[List[str]]): A list of content keys.
        created_at (Optional[datetime]): The timestamp when the learning session was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session.
        end (Optional[datetime]): The end time of the learning session.
        filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
        id (Optional[int]): The ID of the learning session.
        key (Optional[str]): The key of the learning session.
        metadata (Optional[Dict[str, Any]]): The metadata of the learning session.
        mode (Optional[str]): The mode of the learning session.
        result (Optional[int]): The result of the learning session.
        settings (Optional[Dict[str, Any]]): The settings of the learning session.
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
        metadata: Optional[Dict[str, Any]] = None,
        mode: Optional[str] = None,
        result: Optional[int] = None,
        settings: Optional[Dict[str, Any]] = None,
        stacks: Optional[List[str]] = None,
        start: Optional[datetime] = None,
        status: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableLearningSession class.

        Args:
            children (Optional[List[str]]): A list of child learning session item keys.
            contents (Optional[List[str]]): A list of content keys.
            created_at (Optional[datetime]): The timestamp when the learning session was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the learning session.
            end (Optional[datetime]): The end time of the learning session.
            filters (Optional[List[Dict[str, Any]]]): The filters applied to the learning session.
            id (Optional[int]): The ID of the learning session.
            key (Optional[str]): The key of the learning session.
            metadata (Optional[Dict[str, Any]]): The metadata of the learning session.
            mode (Optional[str]): The mode of the learning session.
            result (Optional[int]): The result of the learning session.
            settings (Optional[Dict[str, Any]]): The settings of the learning session.
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
            hide_attributes=True,
            id=id,
            key=key,
            metadata=metadata,
            mode=mode,
            result=result,
            settings=settings,
            stacks=stacks,
            start=start,
            status=status,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def children(self) -> List[str]:
        """
        Returns the children of the learning session.

        Returns:
            List[str]: The children of the learning session.
        """
        return self._children

    @property
    def contents(self) -> List[str]:
        """
        Returns the contents of the learning session.

        Returns:
            List[str]: The contents of the learning session.
        """
        return self._contents

    @property
    def created_at(self) -> Optional[datetime]:
        """
        Returns the created_at of the learning session.

        Returns:
            Optional[datetime]: The created_at of the learning session.
        """
        return self._created_at

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Returns the custom_field_values of the learning session.

        Returns:
            List[Dict[str, Any]]: The custom_field_values of the learning session.
        """
        return self._custom_field_values

    @property
    def duration(self) -> float:
        """
        Returns the duration of the learning session.

        Returns:
            float: The duration of the learning session.
        """

        return self._duration

    @property
    def end(self) -> Optional[datetime]:
        """
        Returns the end of the learning session.

        Returns:
            Optional[datetime]: The end of the learning session.
        """

        return self._end

    @property
    def filters(self) -> List[Dict[str, Any]]:
        """
        Returns the filters of the learning session.

        Returns:
            List[Dict[str, Any]]: The filters of the learning session.
        """

        return self._filters

    @property
    def id(self) -> int:
        """
        Returns the id of the learning session.

        Returns:
            int: The id of the learning session.
        """

        return self._id

    @property
    def key(self) -> str:
        """
        Returns the key of the learning session.

        Returns:
            str: The key of the learning session.
        """

        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the learning session.

        Returns:
            Dict[str, Any]: The metadata of the learning session.
        """

        return self._metadata

    @property
    def mode(self) -> str:
        """
        Returns the mode of the learning session.

        Returns:
            str: The mode of the learning session.
        """

        return self._mode

    @property
    def result(self) -> Optional[int]:
        """
        Returns the result of the learning session.

        Returns:
            Optional[int]: The result of the learning session.
        """

        return self._result

    @property
    def settings(self) -> Dict[str, Any]:
        """
        Returns the settings of the learning session.

        Returns:
            Dict[str, Any]: The settings of the learning session.
        """

        return self._settings

    @property
    def stacks(self) -> List[str]:
        """
        Returns the stacks of the learning session.

        Returns:
            List[str]: The stacks of the learning session.
        """

        return self._stacks

    @property
    def start(self) -> Optional[datetime]:
        """
        Returns the start of the learning session.

        Returns:
            Optional[datetime]: The start of the learning session.
        """

        return self._start

    @property
    def status(self) -> Optional[int]:
        """
        Returns the status of the learning session.

        Returns:
            Optional[int]: The status of the learning session.
        """

        return self._status

    @property
    def updated_at(self) -> Optional[datetime]:
        """
        Returns the updated_at of the learning session.

        Returns:
            Optional[datetime]: The updated_at of the learning session.
        """

        return self._updated_at

    @property
    def uuid(self) -> Optional[str]:
        """
        Returns the uuid of the learning session.

        Returns:
            Optional[str]: The uuid of the learning session.
        """

        return self._uuid

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

    def get_setting(
        self,
        key: str,
    ) -> Optional[Any]:
        """
        Retrieves the value of a setting by its key.

        Args:
            key (str): The key of the setting to retrieve.

        Returns:
            Optional[Any]: The value of the setting if found, otherwise None.
        """
        try:
            # Iterate over the settings and return the value for the matching key
            return next(item["value"] for item in self.settings if item["key"] == key)
        except StopIteration as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_setting' method from '{self.__class__.__name__}': {e}"
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
        metadata (Optional[Dict[str, Any]]): The metadata of the learning session.
        mode (Optional[str]): The mode of the learning session.
        result (Optional[int]): The result of the learning session.
        settings (Optional[Dict[str, Any]]): The settings of the learning session.
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
        metadata: Optional[Dict[str, Any]] = None,
        mode: Optional[str] = None,
        result: Optional[int] = None,
        settings: Optional[Dict[str, Any]] = None,
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
            metadata (Optional[Dict[str, Any]]): The metadata of the learning session.
            mode (Optional[str]): The mode of the learning session.
            result (Optional[int]): The result of the learning session.
            settings (Optional[Dict[str, Any]]): The settings of the learning session.
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
            hide_attributes=True,
            id=id,
            key=key,
            metadata=metadata,
            mode=mode,
            result=result,
            settings=settings,
            stacks=stacks,
            start=start,
            status=status,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def children(self) -> List[str]:
        """
        Returns the children of the learning session.

        Returns:
            List[str]: The children of the learning session.
        """
        return self._children

    @children.setter
    def children(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the children of the learning session.

        Args:
            value (Union[List[str], str]): The new children of the learning session.

        Returns:
            None
        """

        # Check, if the children list exists
        if not self.get(
            default=None,
            name="children",
        ):
            # Set the children of the learning session to an empty list
            self._children = []

        # Check, if the passed value is a list
        if isinstance(
            value,
            list,
        ):
            # Set the children of the learning session
            self._children = value
        # Check, if the passed value is a string
        elif isinstance(
            value,
            str,
        ):
            # Set the children of the learning session
            self._children = [value]

    @property
    def contents(self) -> List[str]:
        """
        Returns the contents of the learning session.

        Returns:
            List[str]: The contents of the learning session.
        """
        return self._contents

    @contents.setter
    def contents(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the contents of the learning session.

        Args:
            value (Union[List[str], str]): The new contents of the learning session.

        Returns:
            None
        """

        # Check, if the contents list exists
        if not self.get(
            default=None,
            name="contents",
        ):
            # Set the contents of the learning session to an empty list
            self._contents = []

        # Check, if the passed value is a list
        if isinstance(
            value,
            list,
        ):
            # Set the contents of the learning session
            self._contents = value
        # Check, if the passed value is a string
        elif isinstance(
            value,
            str,
        ):
            # Set the contents of the learning session
            self._contents = [value]

    @property
    def created_at(self) -> Optional[datetime]:
        """
        Returns the created_at of the learning session.

        Returns:
            Optional[datetime]: The created_at of the learning session.
        """
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the created_at of the learning session.

        Args:
            value (datetime): The new created_at of the learning session.

        Returns:
            None
        """
        self._created_at = value

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Returns the custom_field_values of the learning session.

        Returns:
            List[Dict[str, Any]]: The custom_field_values of the learning session.
        """
        return self._custom_field_values

    @custom_field_values.setter
    def custom_field_values(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> None:
        """
        Sets the custom field values of the learning session.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]): The new custom field values of the learning session.

        Returns:
            None
        """

        # Check, if the custom field values list exists
        if not self.get(
            default=None,
            name="custom_field_values",
        ):
            # Set the custom field values of the learning session to an empty list
            self._custom_field_values = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the passed value to the list
            self._custom_field_values.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the list with the passed value
            self._custom_field_values.extend(value)

    @property
    def duration(self) -> float:
        """
        Returns the duration of the learning session.

        Returns:
            float: The duration of the learning session.
        """

        return self._duration

    @duration.setter
    def duration(
        self,
        value: float,
    ) -> None:
        """
        Sets the duration of the learning session.

        Args:
            value (float): The new duration of the learning session.

        Returns:
            None
        """
        self._duration = value

    @property
    def end(self) -> Optional[datetime]:
        """
        Returns the end of the learning session.

        Returns:
            Optional[datetime]: The end of the learning session.
        """

        return self._end

    @end.setter
    def end(
        self,
        value: Optional[datetime],
    ) -> None:
        """
        Sets the end of the learning session.

        Args:
            value (Optional[datetime]): The new end of the learning session.

        Returns:
            None
        """
        self._end = value

    @property
    def filters(self) -> List[Dict[str, Any]]:
        """
        Returns the filters of the learning session.

        Returns:
            List[Dict[str, Any]]: The filters of the learning session.
        """

        return self._filters

    @filters.setter
    def filters(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> None:
        """
        Sets the filters of the learning session.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The new filters of the learning session.

        Returns:
            None
        """

        # Check, if the filters list exists
        if not self.get(
            default=None,
            name="filters",
        ):
            # Set the filters of the learning session to an empty list
            self._filters = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the passed value to the list
            self._filters.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the list with the passed value
            self._filters.extend(value)

    @property
    def id(self) -> int:
        """
        Returns the id of the learning session.

        Returns:
            int: The id of the learning session.
        """

        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the id of the learning session.

        Args:
            value (int): The new id of the learning session.

        Returns:
            None
        """
        self._id = value

    @property
    def key(self) -> str:
        """
        Returns the key of the learning session.

        Returns:
            str: The key of the learning session.
        """

        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the learning session.

        Args:
            value (str): The new key of the learning session.

        Returns:
            None
        """
        self._key = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the learning session.

        Returns:
            Dict[str, Any]: The metadata of the learning session.
        """

        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the metadata of the learning session.

        Args:
            **kwargs (Dict[str, Any]): The new metadata of the learning session.

        Returns:
            None
        """

        # Check, if the metadata dictionary exists
        if not self.get(
            default=None,
            name="metadata",
        ):
            # Set the metadata of the learning session to an empty dictionary
            self._metadata = {}

        # Update the metadata of the learning session
        self._metadata.update(**kwargs)

    @property
    def mode(self) -> str:
        """
        Returns the mode of the learning session.

        Returns:
            str: The mode of the learning session.
        """

        return self._mode

    @mode.setter
    def mode(
        self,
        value: str,
    ) -> None:
        """
        Sets the mode of the learning session.

        Args:
            value (str): The new mode of the learning session.

        Returns:
            None
        """
        self._mode = value

    @property
    def result(self) -> Optional[int]:
        """
        Returns the result of the learning session.

        Returns:
            Optional[int]: The result of the learning session.
        """

        return self._result

    @result.setter
    def result(
        self,
        value: int,
    ) -> None:
        """
        Sets the result of the learning session.

        Args:
            value (int): The new result of the learning session.

        Returns:
            None
        """
        self._result = value

    @property
    def settings(self) -> Dict[str, Any]:
        """
        Returns the settings of the learning session.

        Returns:
            Dict[str, Any]: The settings of the learning session.
        """

        return self._settings

    @settings.setter
    def settings(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the settings of the learning session.

        Args:
            **kwargs (Dict[str, Any]): The new settings of the learning session.

        Returns:
            None
        """

        # Check, if the settings dictionary exists
        if not self.get(
            default=None,
            name="settings",
        ):
            # Set the settings of the learning session to an empty dictionary
            self._settings = {}

        # Update the settings of the learning session
        self._settings.update(**kwargs)

    @property
    def stacks(self) -> List[str]:
        """
        Returns the stacks of the learning session.

        Returns:
            List[str]: The stacks of the learning session.
        """

        return self._stacks

    @stacks.setter
    def stacks(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the stacks of the learning session.

        Args:
            value (Union[List[str], str]): The new stacks of the learning session.

        Returns:
            None
        """

        # Check, if the stacks list exists
        if not self.get(
            default=None,
            name="stacks",
        ):
            # Set the stacks of the learning session to an empty list
            self._stacks = []

        # Check, if the passed value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the passed value to the list
            self._stacks.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the list with the passed value
            self._stacks.extend(value)

    @property
    def start(self) -> Optional[datetime]:
        """
        Returns the start of the learning session.

        Returns:
            Optional[datetime]: The start of the learning session.
        """

        return self._start

    @start.setter
    def start(
        self,
        value: Optional[datetime],
    ) -> None:
        """
        Sets the start of the learning session.

        Args:
            value (Optional[datetime]): The new start of the learning session.

        Returns:
            None
        """
        self._start = value

    @property
    def status(self) -> Optional[int]:
        """
        Returns the status of the learning session.

        Returns:
            Optional[int]: The status of the learning session.
        """

        return self._status

    @status.setter
    def status(
        self,
        value: Optional[int],
    ) -> None:
        """
        Sets the status of the learning session.

        Args:
            value (Optional[int]): The new status of the learning session.

        Returns:
            None
        """
        self._status = value

    @property
    def updated_at(self) -> Optional[datetime]:
        """
        Returns the updated_at of the learning session.

        Returns:
            Optional[datetime]: The updated_at of the learning session.
        """

        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: Optional[datetime],
    ) -> None:
        """
        Sets the updated_at of the learning session.

        Args:
            value (Optional[datetime]): The new updated_at of the learning session.

        Returns:
            None
        """
        self._updated_at = value

    @property
    def uuid(self) -> Optional[str]:
        """
        Returns the uuid of the learning session.

        Returns:
            Optional[str]: The uuid of the learning session.
        """

        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: Optional[str],
    ) -> None:
        """
        Sets the uuid of the learning session.

        Args:
            value (Optional[str]): The new uuid of the learning session.

        Returns:
            None
        """
        self._uuid = value

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

    def get_setting(
        self,
        key: str,
    ) -> Optional[Any]:
        """
        Retrieves the value of a setting by its key.

        Args:
            key (str): The key of the setting to retrieve.

        Returns:
            Optional[Any]: The value of the setting if found, otherwise None.
        """
        try:
            # Iterate over the settings and return the value for the matching key
            return next(item["value"] for item in self.settings if item["key"] == key)
        except StopIteration as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_setting' method from '{self.__class__.__name__}': {e}"
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

    def set_setting(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Sets the value of a setting by its key.

        Args:
            key (str): The key of the setting to set.
            value (Any): The value to set for the setting.

        Returns:
            None
        """
        try:
            # Iterate over the settings and update the value for the matching key
            for item in self.settings:
                if item["key"] == key:
                    item["value"] = value
                    return
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'set_setting' method from '{self.__class__.__name__}': {e}"
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
        metadata: Optional[Dict[str, Any]] = None,
        mode: Optional[str] = None,
        result: Optional[int] = None,
        settings: Optional[List[Dict[str, Any]]] = None,
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
            metadata (Optional[Dict[str, Any]], optional): The metadata of the learning session. Defaults to None.
            mode (Optional[str], optional): The mode of the learning session. Defaults to None.
            result (Optional[int], optional): The result of the learning session. Defaults to None.
            settings (Optional[List[Dict[str, Any]]], optional): The settings of the learning session. Defaults to None.
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
                metadata=metadata,
                mode=mode,
                result=result,
                settings=settings,
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

    def contents(
        self,
        value: Union[List[str], str],
    ) -> Self:
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

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the learning session.

        Args:
            value (Dict[str, Any]): The metadata of the learning session.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' key exists in the 'configuration' dictionary
        if "metadata" not in self.configuration:
            self.configuration["metadata"] = {}

        # Update the 'metadata' dictionary with the new values
        self.configuration["metadata"].update(value)

        # Return the builder instance
        return self

    def mode(
        self,
        value: str,
    ) -> Self:
        """
        Sets the mode attribute of the builder.

        Args:
            value (str): The value to set for the mode attribute.

        Returns:
            Self: The builder instance with the mode attribute set.
        """
        self.configuration["mode"] = value
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

    def settings(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the settings attribute of the builder.

        Args:
            value (Dict[str, Any]): The value to set for the settings attribute.

        Returns:
            Self: The builder instance with the settings attribute set.
        """
        # Check if the "settings" key is already present in the configuration
        if "settings" not in self.configuration:
            # Initialize the "settings" key with an empty dictionary
            self.configuration["settings"] = {}

        # Update the settings dictionary
        self.configuration["settings"].update(value)
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

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        learning_session: Union[
            ImmutableLearningSession,
            MutableLearningSession,
        ],
    ) -> MutableLearningSession:
        """
        Runs pre-create tasks for the learning_session.

        Args:
            learning_session (Union[ImmutableLearningSession, MutableLearningSession]): The learning_session to run pre-create tasks for.

        Returns:
            MutableLearningSession: The learning_session with pre-create tasks run.
        """

        # Check if the learning_session object is immutable
        if not learning_session.is_mutable():
            # If it is, convert it to a mutable learning_session
            learning_session = learning_session.to_mutable()

        # Set the created_at timestamp of the learning_session
        learning_session.created_at = Miscellaneous.get_current_datetime()

        # Set the custom_field_values of the learning_session
        learning_session.custom_field_values = (
            learning_session.custom_field_values or []
        )

        # Set the key of the learning_session
        learning_session.key = f"LEARNING_SESSION_{self.count_learning_sessions() + 1}"

        # Set the metadata of the learning_session
        learning_session.metadata = learning_session.metadata or {}

        # Set the updated_at timestamp of the learning_session
        learning_session.updated_at = Miscellaneous.get_current_datetime()

        # Set the uuid of the learning_session
        learning_session.uuid = Miscellaneous.get_uuid()

        # Return the learning_session to the caller
        return learning_session

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
            
            # Initialize the result (optional) ImmutableLearningSession to none
            result: Optional[ImmutableLearningSession] = None

            # Run pre-create tasks
            learning_session: MutableLearningSession = self._run_pre_create_tasks(
                learning_session=learning_session,
            )

            # Convert the learning_session object to a LearningSessionModel object
            model: LearningSessionModel = LearningSessionConverter.object_to_model(
                object=learning_session
            )

            # Create a new learning_session in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a learning_session ({learning_session.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the learning_session to a dictionary
            kwargs: Dict[str, Any] = learning_session.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the learning_session
            kwargs["id"] = id

            # Create a new ImmutableLearningSession object
            result = LearningSessionFactory.create_learning_session(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableLearningSession from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the learning_session to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created immutable learning_session
            return result
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
        metadata (Field): The metadata of the learning session.
        mode (Field): The mode of the learning session.
        result (Field): The result of the learning session.
        settings (Field): The settings of the learning session.
        stacks (Field): The stacks associated with the learning session.
        start (Field): The start time of the learning session.
        status (Field): The status of the learning session.
        updated_at (Field): The timestamp when the learning session was last updated.
        uuid (Field): The UUID of the learning session.
    """

    table: Final[str] = Constants.LEARNING_SESSIONS

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

    metadata: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="metadata",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    mode: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="mode",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
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

    settings: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="settings",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        metadata: Optional[Dict[str, Any]] = None,
        mode: Optional[str] = None,
        result: Optional[int] = None,
        settings: Optional[Dict[str, Any]] = None,
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
            metadata (Optional[Dict[str, Any]]): The metadata of the learning session.
            mode (Optional[str]): The mode of the learning session.
            result (Optional[int]): The result of the learning session.
            settings (Optional[Dict[str, Any]]): The settings of the learning session.
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
            metadata=metadata,
            mode=mode,
            result=result,
            settings=settings,
            stacks=stacks,
            start=start,
            status=status,
            table=Constants.LEARNING_SESSIONS,
            updated_at=updated_at,
            uuid=uuid,
        )


class ImmutableLearningSessionAction(ImmutableBaseObject):
    """
    An immutable version of the MutableLearningSessionAction class.

    This class extends the ImmutableBaseObject class and provides an immutable version of the MutableLearningSessionAction class.
    It is used to represent a learning session action in an immutable form, which cannot be modified after creation.

    Attributes:
        action_metadata (Dict[str, Any]): Metadata related to the action.
        action_type (str): The type of the action.
        created_at (Optional[datetime]): The timestamp when the item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): Custom field values.
        duration (Optional[float]): The duration of the item.
        end (Optional[datetime]): The end time of the item.
        id (Optional[int]): The ID of the item.
        key (Optional[str]): The key of the item.
        metadata (Optional[Dict[str, Any]]): The metadata of the item.
        reference (Optional[str]): The reference of the item.
        start (Optional[datetime]): The start time of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
    """

    def __init__(
        self,
        action_metadata: Dict[str, Any],
        action_type: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance with the given parameters.

        Args:
        action_metadata (Dict[str, Any]): Metadata related to the action.
        action_type (str): The type of the action.
        created_at (Optional[datetime]): The timestamp when the item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): Custom field values.
        duration (Optional[float]): The duration of the item.
        end (Optional[datetime]): The end time of the item.
        id (Optional[int]): The ID of the item.
        key (Optional[str]): The key of the item.
        metadata (Optional[Dict[str, Any]]): The metadata of the item.
        reference (Optional[str]): The reference of the item.
        start (Optional[datetime]): The start time of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
        """

        # Call the parent class constructor with the provided parameters
        super().__init__(
            action_metadata=action_metadata,
            action_type=action_type,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            metadata=metadata,
            reference=reference,
            start=start,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> Optional["MutableLearningSessionAction"]:
        """
        Converts the immutable learning session action to a mutable learning session action.

        Returns:
            Optional[MutableLearningSessionAction]: The mutable learning session action if successful, otherwise None.

        Raises:
            Exception: If an exception occurs during the conversion process.
        """
        try:
            # Attempt to create and return an instance of the MutableLearningSessionAction class
            return MutableLearningSessionAction(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback for additional debugging information
            self.logger.error(message=traceback.format_exc())

            # Return None indicating that an exception has occurred
            return None


class MutableLearningSessionAction(MutableBaseObject):
    """
    A mutable version of the ImmutableLearningSessionAction class.

    This class extends the MutableBaseObject class and provides a mutable version of the ImmutableLearningSessionAction class.
    It is used to represent a learning session action in a mutable form, which can be modified after creation.

    Attributes:
        action_metadata (Dict[str, Any]): Metadata related to the action.
        action_type (str): The type of the action.
        created_at (Optional[datetime]): The timestamp when the item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): Custom field values.
        duration (Optional[float]): The duration of the item.
        end (Optional[datetime]): The end time of the item.
        id (Optional[int]): The ID of the item.
        key (Optional[str]): The key of the item.
        metadata (Optional[Dict[str, Any]]): The metadata of the item.
        reference (Optional[str]): The reference of the item.
        start (Optional[datetime]): The start time of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
    """

    def __init__(
        self,
        action_metadata: Dict[str, Any],
        action_type: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance with the given parameters.

        Args:
        action_metadata (Dict[str, Any]): Metadata related to the action.
        action_type (str): The type of the action.
        created_at (Optional[datetime]): The timestamp when the item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): Custom field values.
        duration (Optional[float]): The duration of the item.
        end (Optional[datetime]): The end time of the item.
        id (Optional[int]): The ID of the item.
        key (Optional[str]): The key of the item.
        metadata (Optional[Dict[str, Any]]): The metadata of the item.
        reference (Optional[str]): The reference of the item.
        start (Optional[datetime]): The start time of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
        """

        # Call the parent class constructor with the provided parameters
        super().__init__(
            action_metadata=action_metadata,
            action_type=action_type,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            metadata=metadata,
            reference=reference,
            start=start,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_immutable(self) -> Optional[ImmutableLearningSessionAction]:
        """
        Converts the mutable learning session action to an immutable learning session action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The immutable learning session action if successful, otherwise None.

        Raises:
            Exception: If an exception occurs during the conversion process.
        """
        try:
            # Attempt to create and return an instance of the ImmutableLearningSessionAction class
            return ImmutableLearningSessionAction(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback for additional debugging information
            self.logger.error(message=traceback.format_exc())

            # Return None indicating that an exception has occurred
            return None


class LearningSessionActionConverter:
    """
    A converter class for transforming between LearningSessionActionModel and ImmutableLearningSessionAction instances.

    This class provides methods to convert a LearningSessionActionModel instance to an ImmutableLearningSessionAction instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the LearningSessionActionConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="LearningSessionActionConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "LearningSessionActionModel",
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Converts a given LearningSessionActionModel instance to an ImmutableLearningSessionAction instance.

        Args:
            model (LearningSessionActionModel): The LearningSessionActionModel instance to be converted.

        Returns:
            ImmutableLearningSessionAction: The converted ImmutableLearningSessionAction instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the LearningSessionActionModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSessionAction class from the dictionary representation of the LearningSessionActionModel instance
            return ImmutableLearningSessionAction(
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
        object: ImmutableLearningSessionAction,
    ) -> Optional["LearningSessionActionModel"]:
        """
        Converts a given ImmutableLearningSessionAction instance to a LearningSessionActionModel instance.

        Args:
            object (ImmutableLearningSessionAction): The ImmutableLearningSessionAction instance to be converted.

        Returns:
            LearningSessionActionModel: The converted LearningSessionActionModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableLearningSessionAction instance.
        """
        try:
            # Attempt to create and return a new instance of the LearningSessionActionModel class from the dictionary representation of the ImmutableLearningSessionAction instance
            return LearningSessionActionModel(
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


class LearningSessionActionFactory:
    """
    Provides a method to create a new learning session action.

    This class extends the BaseFactory class and provides a method to create an ImmutableLearningSessionAction object by accepting
    various parameters related to a learning session action. It uses a logger to capture and log any exceptions that may occur during the creation process.

    Attributes:
        logger (Logger): The logger instance associated with the LearningSessionActionFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="LearningSessionActionFactory")

    @classmethod
    def create_learning_session_action(
        cls,
        action_type: str,
        action_metadata: Dict[str, Any],
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Creates a new learning session action.

        Args:
            action_type (str): The type of the action.
            action_metadata (Dict[str, Any]): The metadata of the action.
            created_at (Optional[datetime]): The timestamp when the action was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the action.
            end (Optional[datetime]): The end time of the action.
            id (Optional[int]): The ID of the action.
            key (Optional[str]): The key of the action.
            metadata (Optional[Dict[str, Any]]): The metadata of the action.
            reference (Optional[str]): The reference of the action.
            start (Optional[datetime]): The start time of the action.
            updated_at (Optional[datetime]): The timestamp when the action was last updated.
            uuid (Optional[str]): The UUID of the action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The created learning session action if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSessionAction class from the dictionary representation of the MutableLearningSessionAction instance
            return ImmutableLearningSessionAction(
                action_type=action_type,
                action_metadata=action_metadata,
                created_at=created_at,
                custom_field_values=custom_field_values,
                duration=duration,
                end=end,
                id=id,
                key=key,
                metadata=metadata,
                reference=reference,
                start=start,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_session_action' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=traceback.format_exc())

            # Return None indicating an exception has occurred
            return None


class LearningSessionActionBuilder(BaseObjectBuilder):
    def __init__(self) -> None:
        """
        Initializes a new instance of the LearningSessionActionBuilder class.

        This class extends the BaseObjectBuilder class and provides a method to create an ImmutableLearningSessionAction object by accepting
        various parameters related to a learning session action. It uses a logger to capture and log any exceptions that may occur during the creation process.
        """
        super().__init__()

    @override
    def build(self) -> Optional[ImmutableLearningSessionAction]:
        """
        Builds and returns an instance of the ImmutableLearningSessionAction class using the configuration dictionary.

        This method attempts to create an instance of the ImmutableLearningSessionAction class using the configuration dictionary passed to the constructor.
        If an exception occurs while creating the instance, this method will log an error message and return None.

        Returns:
            Optional[ImmutableLearningSessionAction]: The created learning session action if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSessionAction class from the dictionary representation of the MutableLearningSessionAction instance
            learning_session_action: Optional[ImmutableLearningSessionAction] = (
                LearningSessionActionFactory.create_learning_session_action(
                    **self.configuration
                )
            )

            if not learning_session_action:
                # Log an error message indicating an exception has occurred
                self.logger.error(
                    message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
                )

                # Log the traceback of the exception
                self.logger.error(message=traceback.format_exc())

                # Return None indicating an exception has occurred
                return None

            # Return the created learning session action
            return learning_session_action
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=traceback.format_exc())

            # Return None indicating an exception has occurred
            return None

    def action_type(
        self,
        value: str,
    ) -> Self:
        """
        Sets the action_type attribute of the builder.

        Args:
            value (str): The value to set for the action_type attribute.

        Returns:
            Self: The builder instance with the action_type attribute set.
        """

        # Set the action_type value in the configuration dictionary
        self.configuration["action_type"] = value

        # Return the builder instance
        return self

    def action_metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the action_metadata attribute of the builder.

        Args:
            value (Dict[str, Any]): The value to set for the action_metadata attribute.

        Returns:
            Self: The builder instance with the action_metadata attribute set.
        """

        # Check if the "action_metadata" key is already present in the configuration
        if "action_metadata" not in self.configuration:
            # Initialize the "action_metadata" key with an empty dictionary
            self.configuration["action_metadata"] = {}

        # Set the action_metadata value in the configuration dictionary
        self.configuration["action_metadata"].update(value)

        # Return the builder instance
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

        # Set the created_at value in the configuration dictionary
        self.configuration["created_at"] = value

        # Return the builder instance
        return self

    def custom_field_values(
        self,
        value: Optional[List[Dict[str, Any]]] = None,
    ) -> Self:
        """
        Sets the custom_field_values attribute of the builder.

        Args:
            value (Optional[List[Dict[str, Any]]]): The value to set for the custom_field_values attribute.

        Returns:
            Self: The builder instance with the custom_field_values attribute set.
        """

        # Set the custom_field_values value in the configuration dictionary
        self.configuration["custom_field_values"] = value

        # Return the builder instance
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

        # Set the duration value in the configuration dictionary
        self.configuration["duration"] = value

        # Return the builder instance
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

        # Set the end value in the configuration dictionary
        self.configuration["end"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the learning session action.

        Args:
            value (Dict[str, Any]): The metadata of the learning session action.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' key exists in the 'configuration' dictionary
        if "metadata" not in self.configuration:
            self.configuration["metadata"] = {}

        # Update the 'metadata' dictionary with the new values
        self.configuration["metadata"].update(value)

        # Return the builder instance
        return self

    def reference(
        self,
        value: str,
    ) -> Self:
        """
        Sets the reference attribute of the builder.

        Args:
            value (str): The value to set for the reference attribute.

        Returns:
            Self: The builder instance with the reference attribute set.
        """

        # Set the reference value in the configuration dictionary
        self.configuration["reference"] = value

        # Return the builder instance
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

        # Set the start value in the configuration dictionary
        self.configuration["start"] = value

        # Return the builder instance
        return self

    def updated_at(
        self,
        value: Optional[datetime] = None,
    ) -> Self:
        """
        Sets the updated_at attribute of the builder.

        Args:
            value (datetime): The value to set for the updated_at attribute.

        Returns:
            Self: The builder instance with the updated_at attribute set.
        """

        # Set the updated_at value in the configuration dictionary
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self


class LearningSessionActionManager(BaseObjectManager):
    """
    A manager class for managing learning_session_actions in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for learning_session_actions.

    Attributes:
        cache: (List[Any]): The cache for storing learning_session_actions.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["LearningSessionActionManager"] = None

    def __new__(cls) -> "LearningSessionActionManager":
        """
        Creates and returns a new instance of the LearningSessionActionManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            LearningSessionActionManager: The created or existing instance of LearningSessionActionManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(LearningSessionActionManager, cls).__new__(cls)
            # Initialize the instance with the dispatcher and stacks
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the LearningSessionActionManager class.

        Returns:
            None
        """
        pass

    def count_learning_session_actions(self) -> int:
        """
        Returns the number of learning_session_actions in the database.

        Returns:
            int: The number of learning_session_actions in the database.
        """
        try:
            # Count and return the number of learning_session_actions in the database
            return asyncio.run(
                LearningSessionActionModel.count(database=Constants.DATABASE_PATH)
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_learning_session_action(
        self,
        learning_session_action: Union[
            ImmutableLearningSessionAction, MutableLearningSessionAction
        ],
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Creates a new learning_session_action in the database.

        Args:
            learning_session_action (Union[ImmutableLearningSessionAction, MutableLearningSessionAction]): The learning_session_action to be created.

        Returns:
            Optional[ImmutableLearningSessionAction]: The newly created immutable learning_session_action if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the learning_session_action.
        """
        try:
            # Check if the learning_session_action object is immutable
            if isinstance(
                learning_session_action,
                ImmutableLearningSessionAction,
            ):
                # If it is, convert it to a mutable learning_session_action
                learning_session_action = learning_session_action.to_mutable()

            # Set the created_at timestamp of the learning_session_action
            learning_session_action.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the learning_session_action
            learning_session_action.custom_field_values = (
                [] or learning_session_action.custom_field_values
            )

            # Set the key of the learning_session_action
            learning_session_action.key = (
                f"LEARNING_SESSION_ACTION_{self.count_learning_session_actions() + 1}"
            )

            # Set the updated_at timestamp of the learning_session_action
            learning_session_action.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the learning_session_action
            learning_session_action.uuid = Miscellaneous.get_uuid()

            # Convert the learning_session_action object to a LearningSessionActionModel object
            model: LearningSessionActionModel = (
                LearningSessionActionConverter.object_to_model(
                    object=learning_session_action
                )
            )

            # Create a new learning_session_action in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the learning_session_action
                learning_session_action.id = id

                # Convert the learning_session_action to an immutable learning_session_action
                learning_session_action = (
                    LearningSessionActionFactory.create_learning_session_action(
                        **learning_session_action.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                )

                # Add the learning_session_action to the cache
                self.add_to_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

                # Return the newly created immutable learning_session_action
                return learning_session_action

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a learning_session_action ({learning_session_action}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_session_action' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_learning_session_action(
        self,
        learning_session_action: Union[
            ImmutableLearningSessionAction, MutableLearningSessionAction
        ],
    ) -> bool:
        """
        Deletes a learning_session_action from the database.

        Args:
            learning_session_action (Union[ImmutableLearningSessionAction, MutableLearningSessionAction]): The learning_session_action to be deleted.

        Returns:
            bool: True if the learning_session_action was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the learning_session_action to an immutable learning_session_action and delete the learning_session_action from the database
            result: bool = asyncio.run(
                LearningSessionActionConverter.object_to_model(
                    object=LearningSessionActionFactory.create_learning_session_action(
                        **learning_session_action.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the learning_session_action from the cache
            self.remove_from_cache(key=learning_session_action.key)

            # Return True if the learning_session_action was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_learning_session_actions(
        self,
    ) -> Optional[List[ImmutableLearningSessionAction]]:
        """
        Returns a list of all learning_session_actions in the database.

        Returns:
            Optional[List[ImmutableLearningSessionAction]]: A list of all learning_session_actions in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_learning_session_actions():
                # Return the list of immutable learning_session_actions from the cache
                return self.get_cache_values()

            # Get all learning_session_actions from the database
            models: List[LearningSessionActionModel] = asyncio.run(
                LearningSessionActionModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of LearningSessionActionModel objects to a list of ImmutableLearningSessionAction objects
            learning_session_actions: List[ImmutableLearningSessionAction] = [
                LearningSessionActionFactory.create_learning_session_action(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable learning_session_actions
            for learning_session_action in learning_session_actions:
                # Add the immutable learning_session_action to the cache
                self.add_to_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

            # Return the list of immutable learning_session_actions
            return learning_session_actions
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_action_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Retrieves a learning_session_action by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableLearningSessionAction]: The learning_session_action with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_action is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the learning_session_action from the cache
                return self.get_value_from_cache(key=field)

            # Get the learning_session_action with the given field and value from the database
            model: Optional[LearningSessionActionModel] = asyncio.run(
                LearningSessionActionModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the learning_session_action if it exists
            if model is not None:
                # Convert the LearningSessionActionModel object to an ImmutableLearningSessionAction object
                learning_session_action: ImmutableLearningSessionAction = (
                    LearningSessionActionFactory.create_learning_session_action(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_action to the cache
                self.add_to_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

                # Return the learning_session_action
                return learning_session_action
            else:
                # Return None indicating that the learning_session_action does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_action_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Returns a learning_session_action with the given ID.

        Args:
            id (int): The ID of the learning_session_action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The learning_session_action with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_action is already in the cache
            if self.is_key_in_cache(key=f"LEARNING_SESSION_ACTION_{id}"):
                # Return the learning_session_action from the cache
                return self.get_value_from_cache(key=f"LEARNING_SESSION_ACTION_{id}")

            # Get the learning_session_action with the given ID from the database
            model: Optional[LearningSessionActionModel] = asyncio.run(
                LearningSessionActionModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the learning_session_action if it exists
            if model is not None:
                # Convert the LearningSessionActionModel object to an ImmutableLearningSessionAction object
                learning_session_action: ImmutableLearningSessionAction = (
                    LearningSessionActionFactory.create_learning_session_action(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_action to the cache
                self.add_to_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

                # Return the learning_session_action
                return learning_session_action
            else:
                # Return None indicating that the learning_session_action does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_action_by_key(
        self,
        key: str,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Returns a learning_session_action with the given key.

        Args:
            key (str): The key of the learning_session_action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The learning_session_action with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_action is already in the cache
            if self.is_key_in_cache(key=key):
                # Return the learning_session_action from the cache
                return self.get_value_from_cache(key=key)

            # Get the learning_session_action with the given key from the database
            model: Optional[LearningSessionActionModel] = asyncio.run(
                LearningSessionActionModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the learning_session_action if it exists
            if model is not None:
                # Convert the LearningSessionActionModel object to an ImmutableLearningSessionAction object
                learning_session_action: ImmutableLearningSessionAction = (
                    LearningSessionActionFactory.create_learning_session_action(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_action to the cache
                self.add_to_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

                # Return the learning_session_action
                return learning_session_action
            else:
                # Return None indicating that the learning_session_action does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_learning_session_action_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Returns a learning_session_action with the given UUID.

        Args:
            uuid (str): The UUID of the learning_session_action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The learning_session_action with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_action is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the learning_session_action from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the learning_session_action with the given UUID from the database
            model: Optional[LearningSessionActionModel] = asyncio.run(
                LearningSessionActionModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the learning_session_action if it exists
            if model is not None:
                # Convert the LearningSessionActionModel object to an ImmutableLearningSessionAction object
                learning_session_action: ImmutableLearningSessionAction = (
                    LearningSessionActionFactory.create_learning_session_action(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                )

                # Add the learning_session_action to the cache
                self.add_to_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

                # Return the learning_session_action
                return learning_session_action
            else:
                # Return None indicating that the learning_session_action does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_learning_session_actions(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableLearningSessionAction]]]:
        """
        Searches for learning_session_actions in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the LearningSessionActionModel class.

        Returns:
            Optional[Union[List[ImmutableLearningSessionAction]]]: The found learning_session_actions if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for learning_session_actions in the database
            models: Optional[List[LearningSessionActionModel]] = asyncio.run(
                LearningSessionActionModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found learning_session_actions if any
            if models is not None and len(models) > 0:
                learning_session_actions: List[ImmutableLearningSessionAction] = [
                    LearningSessionActionFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found learning_session_actions
                for learning_session_action in learning_session_actions:
                    # Add the learning_session_action to the cache
                    self.add_to_cache(
                        key=learning_session_action.key,
                        value=learning_session_action,
                    )

                # Return the found learning_session_actions
                return learning_session_actions
            else:
                # Return None indicating that no learning_session_actions were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_learning_session_action(
        self,
        learning_session_action: Union[
            ImmutableLearningSessionAction, MutableLearningSessionAction
        ],
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Updates a learning_session_action with the given ID.

        Args:
            learning_session_action (Union[ImmutableLearningSessionAction, MutableLearningSessionAction]): The learning_session_action to update.

        Returns:
            Optional[ImmutableLearningSessionAction]: The updated learning_session_action if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the learning_session_action object is immutable
            if isinstance(
                learning_session_action,
                ImmutableLearningSessionAction,
            ):
                # If it is, convert it to a mutable learning_session_action
                learning_session_action = learning_session_action.to_mutable()

            # Update the updated_at timestamp of the learning_session_action
            learning_session_action.updated_at = Miscellaneous.get_current_datetime()

            # Convert the learning_session_action to an immutable learning_session_action and update the learning_session_action in the database
            result: bool = asyncio.run(
                LearningSessionActionConverter.object_to_model(
                    object=LearningSessionActionFactory.create_learning_session_action(
                        **learning_session_action.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **learning_session_action.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the learning_session_action was updated successfully
            if result:
                # Update the learning_session_action in the cache
                self.update_in_cache(
                    key=learning_session_action.key,
                    value=learning_session_action,
                )

                # Return the updated learning_session_action
                return learning_session_action.to_immutable()
            else:
                # Return None indicating that the learning_session_action does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class LearningSessionActionModel(ImmutableBaseModel):
    """
    Represents the structure of the LearningSessionActionModel.

    Attributes:
        id (Field): The ID of the learning session action.
        action_type (Field): The type of action associated with the learning session action.
        action_metadata (Field): A list of custom field values.
        created_at (Field): The timestamp when the action was created.
        custom_field_values (Field): A list of custom field values.
        duration (Field): The duration of the action.
        end (Field): The end time of the action.
        key (Field): The key of the action.
        metadata (Field): A dictionary of metadata.
        reference (Field): The reference of the action.
        start (Field): The start time of the action.
        updated_at (Field): The timestamp when the action was last updated.
        uuid (Field): The UUID of the action.
    """

    table: Final[str] = Constants.LEARNING_SESSION_ACTIONS

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

    action_type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="action_type",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    action_metadata: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="action_metadata",
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

    metadata: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="metadata",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
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
        action_type: Optional[str] = None,
        action_metadata: Optional[Dict[str, Any]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionActionModel class.

        Args:
            action_type (Optional[str]): The type of action associated with the action.
            action_metadata (Optional[Dict[str, Any]]): A dictionary of metadata associated with the action.
            created_at (Optional[datetime]): The timestamp when the action was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the action.
            end (Optional[datetime]): The end time of the action.
            id (Optional[int]): The ID of the action.
            key (Optional[str]): The key of the action.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            reference (Optional[str]): The reference of the action.
            start (Optional[datetime]): The start time of the action.
            updated_at (Optional[datetime]): The timestamp when the action was last updated.
            uuid (Optional[str]): The UUID of the action.
        """

        # Call the parent class constructor
        super().__init__(
            action_type=action_type,
            action_metadata=action_metadata,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            metadata=metadata,
            reference=reference,
            start=start,
            table=Constants.LEARNING_SESSION_ACTIONS,
            updated_at=updated_at,
            uuid=uuid,
        )


class ImmutableLearningSessionItem(ImmutableBaseObject):
    """
    An immutable version of the MutableLearningSessionItem class.

    This class extends the ImmutableBaseObject class and provides an immutable version of the MutableLearningSessionItem class.
    It is used to represent a learning session item in an immutable form, which cannot be modified after creation.

    Attributes:
        actions (Optional[List[str]]): A list of actions associated with the learning session item.
        created_at (Optional[datetime]): The timestamp when the learning session item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session item.
        end (Optional[datetime]): The end time of the learning session item.
        id (Optional[int]): The ID of the learning session item.
        key (Optional[str]): The key of the learning session item.
        metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
        reference (Optional[str]): The reference of the learning session item.
        start (Optional[datetime]): The start time of the learning session item.
        updated_at (Optional[datetime]): The timestamp when the learning session item was last updated.
        uuid (Optional[str]): The UUID of the learning session item.
    """

    def __init__(
        self,
        actions: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableLearningSessionItem class.

        Args:
            actions (Optional[List[str]]): A list of actions associated with the learning session item.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the learning session item.
            end (Optional[datetime]): The end time of the learning session item.
            id (Optional[int]): The ID of the learning session item.
            key (Optional[str]): The key of the learning session item.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            reference (Optional[str]): The reference of the learning session item.
            start (Optional[datetime]): The start time of the learning session item.
            updated_at (Optional[datetime]): The timestamp when the learning session item was last updated.
            uuid (Optional[str]): The UUID of the learning session item.
        """

        # Call the parent class constructor
        super().__init__(
            actions=actions,
            custom_field_values=custom_field_values,
            created_at=created_at,
            duration=duration,
            end=end,
            id=id,
            key=key,
            metadata=metadata,
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
        actions (Optional[List[str]]): A list of actions associated with the learning session item.
        created_at (Optional[datetime]): The timestamp when the item was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        duration (Optional[float]): The duration of the learning session item.
        end (Optional[datetime]): The end time of the learning session item.
        id (Optional[int]): The ID of the learning session item.
        key (Optional[str]): The key of the learning session item.
        metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
        reference (Optional[str]): The reference of the learning session item.
        start (Optional[datetime]): The start time of the learning session item.
        updated_at (Optional[datetime]): The timestamp when the learning session item was last updated.
        uuid (Optional[str]): The UUID of the learning session item.
    """

    def __init__(
        self,
        actions: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableLearningSessionItem class.

        Args:
            actions (Optional[List[str]]): A list of actions associated with the learning session item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the item.
            end (Optional[datetime]): The end time of the item.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            reference (Optional[str]): The reference of the item.
            start (Optional[datetime]): The start time of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.
        """

        # Call the parent class constructor
        super().__init__(
            actions=actions,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            metadata=metadata,
            reference=reference,
            start=start,
            updated_at=updated_at,
            uuid=uuid,
        )

    def add_action(
        self,
        action: Any,
    ) -> None:
        """ """

        # If the learning session item currently has no actions, create an empty list
        if not self.actions:
            # Initialize the actions list as an empty list
            self.actions = []

        # Check, if the learning session item's actions is an instance of string
        if isinstance(
            self.actions,
            str,
        ):
            # Convert the actions string into a list
            self.actions = json.loads(self.descendants)

        # Append the key of the given object to the learning session item's actions
        self.actions.append(action.get(name="key"))

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
    """
    Provides a method to create a new learning session item.

    This class extends the BaseFactory class and provides a method to create an ImmutableLearningSessionItem object by accepting
    various parameters related to a learning session item. It uses a logger to capture and log any exceptions that may occur during the creation process.

    Attributes:
        logger (Logger): The logger instance associated with the LearningSessionItemFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="LearningSessionItemFactory")

    @classmethod
    def create_learning_session_item(
        cls,
        actions: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Creates a new learning session item.

        Args:
            actions (Optional[List[str]]): A list of actions associated with the learning session item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the item.
            end (Optional[datetime]): The end time of the item.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
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
                actions=actions,
                created_at=created_at,
                custom_field_values=custom_field_values,
                duration=duration,
                end=end,
                id=id,
                key=key,
                metadata=metadata,
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

            # Log the traceback of the exception
            cls.logger.error(message=traceback.format_exc())

            # Return None indicating an exception has occurred
            return None


class LearningSessionItemBuilder(BaseObjectBuilder):
    def __init__(self) -> None:
        """
        Initializes a new instance of the LearningSessionItemBuilder class.

        This class extends the BaseObjectBuilder class and provides a method to create an ImmutableLearningSessionItem object by accepting
        various parameters related to a learning session item. It uses a logger to capture and log any exceptions that may occur during the creation process.
        """
        super().__init__()

    @override
    def build(self) -> Optional[ImmutableLearningSessionItem]:
        """
        Builds and returns an instance of the ImmutableLearningSessionItem class using the configuration dictionary.

        This method attempts to create an instance of the ImmutableLearningSessionItem class using the configuration dictionary passed to the constructor.
        If an exception occurs while creating the instance, this method will log an error message and return None.

        Returns:
            Optional[ImmutableLearningSessionItem]: The created learning session item if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableLearningSessionItem class from the dictionary representation of the MutableLearningSessionItem instance
            learning_session_item: Optional[ImmutableLearningSessionItem] = (
                LearningSessionItemFactory.create_learning_session_item(
                    **self.configuration
                )
            )

            if not learning_session_item:
                # Log an error message indicating an exception has occurred
                self.logger.error(
                    message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
                )

                # Log the traceback of the exception
                self.logger.error(message=traceback.format_exc())

                # Return None indicating an exception has occurred
                return None

            # Return the created learning session item
            return learning_session_item
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=traceback.format_exc())

            # Return None indicating an exception has occurred
            return None

    def actions(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the actions attribute of the builder.

        Args:
            value (Union[List[str], str]): The value to set for the actions attribute.

        Returns:
            Self: The builder instance with the actions attribute set.
        """
        # Check if the "actions" key is already present in the configuration
        if "actions" not in self.configuration:
            # Initialize the "actions" key with an empty list
            self.configuration["actions"] = []

        # Add the value to the actions list
        if isinstance(
            value,
            str,
        ):
            # Add a single action
            self.configuration["actions"].append(value)
        else:
            # Add multiple actions
            self.configuration["actions"].extend(value)

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

        # Set the created_at value in the configuration dictionary
        self.configuration["created_at"] = value

        # Return the builder instance
        return self

    def custom_field_values(
        self,
        value: Optional[List[Dict[str, Any]]] = None,
    ) -> Self:
        """
        Sets the custom_field_values attribute of the builder.

        Args:
            value (Optional[List[Dict[str, Any]]]): The value to set for the custom_field_values attribute.

        Returns:
            Self: The builder instance with the custom_field_values attribute set.
        """

        # Set the custom_field_values value in the configuration dictionary
        self.configuration["custom_field_values"] = value

        # Return the builder instance
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

        # Set the duration value in the configuration dictionary
        self.configuration["duration"] = value

        # Return the builder instance
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

        # Set the end value in the configuration dictionary
        self.configuration["end"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the learning session item.

        Args:
            value (Dict[str, Any]): The metadata of the learning session item.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' key exists in the 'configuration' dictionary
        if "metadata" not in self.configuration:
            self.configuration["metadata"] = {}

        # Update the 'metadata' dictionary with the new values
        self.configuration["metadata"].update(value)

        # Return the builder instance
        return self

    def reference(
        self,
        value: str,
    ) -> Self:
        """
        Sets the reference attribute of the builder.

        Args:
            value (str): The value to set for the reference attribute.

        Returns:
            Self: The builder instance with the reference attribute set.
        """

        # Set the reference value in the configuration dictionary
        self.configuration["reference"] = value

        # Return the builder instance
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

        # Set the start value in the configuration dictionary
        self.configuration["start"] = value

        # Return the builder instance
        return self

    def updated_at(
        self,
        value: Optional[datetime] = None,
    ) -> Self:
        """
        Sets the updated_at attribute of the builder.

        Args:
            value (datetime): The value to set for the updated_at attribute.

        Returns:
            Self: The builder instance with the updated_at attribute set.
        """

        # Set the updated_at value in the configuration dictionary
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self


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

            # Set the actions of the learning_session_item
            learning_session_item.actions = [] or learning_session_item.actions

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
        actions (Field): A list of actions associated with the learning session item.
        created_at (Field): The timestamp when the item was created.
        custom_field_values (Field): A list of custom field values.
        duration (Field): The duration of the item.
        end (Field): The end time of the item.
        key (Field): The key of the item.
        metadata (Field): A dictionary of metadata.
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

    actions: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="actions",
        nullable=True,
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

    metadata: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="metadata",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
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
        actions: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        duration: Optional[float] = None,
        end: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        reference: Optional[str] = None,
        start: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionItemModel class.

        Args:
            actions (Optional[List[str]]): A list of actions associated with the item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            duration (Optional[float]): The duration of the item.
            end (Optional[datetime]): The end time of the item.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            reference (Optional[str]): The reference of the item.
            start (Optional[datetime]): The start time of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.
        """

        # Call the parent class constructor
        super().__init__(
            actions=actions,
            created_at=created_at,
            custom_field_values=custom_field_values,
            duration=duration,
            end=end,
            id=id,
            key=key,
            metadata=metadata,
            reference=reference,
            start=start,
            table=Constants.LEARNING_SESSION_ITEMS,
            updated_at=updated_at,
            uuid=uuid,
        )
