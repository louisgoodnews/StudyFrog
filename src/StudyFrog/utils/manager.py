"""
Author: lodego
Date: 2024-01-24
"""

from datetime import datetime, timedelta

from typing import *

from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["BaseObjectManager"]


class BaseObjectManager:
    """
    A class for managing BaseObject instances.

    This class serves as a base class for manager classes that manage object instances.
    This class comes with a rudimentary cache system.

    Attributes:
        logger (Logger): The logger instance associated with the object.
        cache (List[Dict[str, Any]]): The cache for storing objects.
        timestamp (datetime): The timestamp of the last update.
        time_limit (int): The time limit for the cache.
    """

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the BaseObjectManager class.

        :param kwargs: keyword arguments
        :type kwargs: dict

        :return: None
        :rtype: None
        """

        # Get an instance of the logger class and store it in the object
        self.logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the cache as an empty dictionary
        self._cache: Dict[str, Any] = {}

        # Store the time limit in an instance variable
        self._time_limit: int = 3600

        # Store the timestamp in an instance variable
        self._timestamp: datetime = Miscellaneous.get_current_datetime()

    @property
    def cache(self) -> Dict[str, Any]:
        """
        Returns the cache.

        :return: The cache.
        :rtype: Dict[str, Any]
        """

        # Return the cache
        return self._cache

    @property
    def time_limit(self) -> int:
        """
        Returns the time limit for the cache.

        :return: The time limit for the cache.
        :rtype: int
        """

        # Return the time limit
        return self._time_limit

    @time_limit.setter
    def time_limit(
        self,
        value: int,
    ) -> None:
        """
        Sets the time limit for the cache.

        :param value: The time limit to set.
        :type value: int

        :return: None
        :rtype: None
        """

        # Set the time limit
        self._time_limit = value

    def add_to_cache(
        self,
        key: Union[str, List[str]],
        value: Union[Any, List[Any]],
    ) -> None:
        """
        Adds an item to the cache.

        :param key: The key of the item.
        :type key: Union[str, List[str]]

        :param value: The value of the item.
        :type value: Union[Any, List[Any]]

        :return: None
        :rtype: None
        """

        # Flush the cache, if needed
        self.flush_cache()

        # Check, if both key and value are lists of the same size
        if isinstance(
            key,
            list,
        ) and isinstance(
            value,
            list,
        ):
            # Check if the lists have the same length
            if len(key) != len(value):
                # Log an error message
                self.logger.error(
                    message="Both key and value must be lists of the same size."
                )

                # Return early
                return

            # Add each key-value pair to the cache
            for (
                k,
                v,
            ) in zip(
                key,
                value,
            ):
                # Add the key-value pair to the cache
                self.add_to_cache(
                    key=k,
                    value=v,
                )

            # Return early
            return

        # Check if the key already exists
        if key in self._cache.keys():
            # Log a warning message
            self.logger.warning(message=f"Key '{key}' already exists. Overwriting...")

        # Add the key-value pair to the cache
        self._cache[key] = value

        # Log the addition to the cache
        self.logger.info(message=f"Added to cache: {key}")

    def check_timestamp(self) -> bool:
        """
        Checks if the cache needs to be cleared.

        :return: True if the cache needs to be cleared, False otherwise.
        :rtype: bool
        """

        # Return True if the cache needs to be cleared, False otherwise
        return Miscellaneous.get_current_datetime() - self._timestamp >= timedelta(
            seconds=self._time_limit
        )

    def clear_cache(self) -> None:
        """
        Clears the cache and resets the timestamp.

        :return: None
        :rtype: None
        """

        # Check, if the cache is empty
        if len(self.cache) == 0:
            # Return early
            return

        # Clear the cache
        self.cache.clear()

        # Log the clear
        self.logger.info(message="Cache cleared.")

        # Update the timestamp
        self._timestamp = Miscellaneous.get_current_datetime()

    def flush_cache(
        self,
        force: bool = False,
    ) -> None:
        """
        Checks if the cache is valid and flushes if it is not.

        Otherwise if force is True it will flush the cache no matter what.

        :param force: Whether to flush the cache no matter what.
        :type force: bool

        :return: None
        :rtype: None
        """

        # Check if the cache is valid
        if not self.check_timestamp() or force:
            # Flush the cache
            self.cache.clear()

            # Update the timestamp
            self._timestamp = Miscellaneous.get_current_datetime()

            # Log updating the timestamp
            self.logger.info(
                message=f"Updated the timestamp to {Miscellaneous.datetime_to_string(datetime=self._timestamp)}."
            )

    def get_cache_keys(self) -> List[str]:
        """
        Returns the keys of the cache.

        :return: The keys of the cache.
        :rtype: List[str]
        """

        # Return the keys of the cache
        return list(self._cache.keys())

    def get_cache_values(self) -> List[Any]:
        """
        Returns the values of the cache.

        :return: The values of the cache.
        :rtype: List[Any]
        """

        # Return the values of the cache
        return list(self._cache.values())

    def get_key_from_cache(
        self,
        value: Any,
    ) -> Optional[str]:
        """
        Returns the key of the item with the given value from the cache.

        :param value: The value of the item.
        :type value: Any

        :return: The key of the item with the given value.
        :rtype: str
        """

        # Iterate over the keys and items in the cache
        for (
            key,
            item,
        ) in self._cache.items():
            # Check, if the current item and the passed value are equal
            if value != item:
                # Skip the current iteration
                continue

            # Return the key
            return key

        # Return None
        return None

    def get_value_from_cache(
        self,
        key: str,
    ) -> Any:
        """
        Returns the value of the item with the given key from the cache.

        :param key: The key of the item.
        :type key: str

        :return: The value of the item with the given key.
        :rtype: Any
        """

        # Iterate over the items and values in the cache
        for (
            item,
            value,
        ) in self._cache.items():
            # Check, if the current item and the passed key are equal
            if key != item:
                # Skip the current iteration
                continue

            # Return the value
            return value

        # Return None
        return None

    def is_cache_empty(self) -> bool:
        """
        Checks if the cache is empty.

        :return: True if the cache is empty, False otherwise.
        :rtype: bool
        """

        # Return True if the cache is empty, False otherwise
        return len(self._cache) == 0

    def is_cache_valid(self) -> bool:
        """
        Checks if the cache is valid.

        The cache is valid if the timestamp is less than the time limit and the cache is not empty.

        :return: True if the cache is valid, False otherwise.
        :rtype: bool
        """

        # Return True if the cache is valid, False otherwise
        return self.check_timestamp() and not self.is_cache_empty()

    def is_key_in_cache(
        self,
        key: str,
    ) -> bool:
        """
        Checks if a key exists in the cache.

        :param key: The key to check.
        :type key: str

        :return: True if the key exists, False otherwise.
        :rtype: bool
        """

        # Return True if the key exists, False otherwise
        return key in self._cache.keys()

    def is_value_in_cache(
        self,
        value: Any,
    ) -> bool:
        """
        Checks if a value exists in the cache.

        :param value: The value to check.
        :type value: Any

        :return: True if the value exists, False otherwise.
        :rtype: bool
        """

        # Return True if the value exists, False otherwise
        return value in self._cache.values()

    def remove_from_cache(
        self,
        key: str,
    ) -> None:
        """
        Removes an item from the cache by its key.

        :param key: The key of the item to remove.
        :type key: str

        :return: None
        :rtype: None
        """

        # Remove the item from the cache
        self._cache.pop(
            key,
            None,
        )

        # Log the removal
        self.logger.info(message=f"Removed key '{key}' from cache.")

    def search_cache(
        self,
        **kwargs,
    ) -> Optional[List[Any]]:
        """
        Searches the internal cache for objects matching all specified attributes.

        This method checks every cached object to determine whether all provided
        key-value pairs match the object's corresponding attributes.

        Args:
            **kwargs: Arbitrary keyword arguments representing the attribute names
                    and their expected values.

        Returns:
            Optional[List[Any]]: A list of matching objects, or None if no matches are found.
        """

        # Initialize the result list
        result: List[Any] = []

        # Iterate over unique cache values (use set to avoid duplicates)
        for cache_value in self._cache.values():
            try:
                # Check if all provided attributes match the current cache object
                if all(
                    hasattr(
                        cache_value,
                        key,
                    )
                    and getattr(
                        cache_value,
                        key,
                    )
                    == value
                    for (
                        key,
                        value,
                    ) in kwargs.items()
                ):
                    result.append(cache_value)
            except Exception as e:
                # Log an error message
                self.logger.error(
                    message=f"Caught an exception while attempting cache search on value '{cache_value}': {e}"
                )

        # Return None if no matching entries were found
        return result if result else None

    def update_in_cache(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Updates the value of the item with the given key in the cache.

        :param key: The key of the item.
        :type key: str

        :param value: The new value of the item.
        :type value: Any

        :return: None
        :rtype: None

        :raises KeyError: If the key does not exist.
        """

        self.add_to_cache(
            key=key,
            value=value,
        )
