"""
Author: lodego
Date: 2024-01-24
"""

from typing import *

from utils.logger import Logger


__all__: List[str] = [
    "MutableBaseObject",
    "ImmutableBaseObject",
]


class MutableBaseObject:
    """
    A base class for mutable objects.

    This class serves as a base class for objects that can be modified after creation.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the MutableBaseObject class.

        :param kwargs: keyword arguments
        :type kwargs: Dict[str, Any]

        :return: None
        :rtype: None
        """

        # Get an instance of the logger class and store it in the object
        self._logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Update the object's dictionary with the keyword arguments
        self.__dict__.update(**kwargs)

    @property
    def logger(self) -> Logger:
        """
        Returns the logger instance associated with the object.

        :return: The logger instance associated with the object.
        :rtype: Logger
        """
        return self._logger

    def __delattr__(
        self,
        name: str,
    ) -> None:
        """
        Deletes the attribute with the given name if it exists.

        :param name: The name of the attribute to delete.
        :type name: str

        :return: None
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Delete the attribute
        del self.__dict__[name]

    def __eq__(
        self,
        other: "MutableBaseObject",
    ) -> bool:
        """
        Checks if the object is equal to the given object.

        :param other: The object to compare to.
        :type other: MutableBaseObject

        :return: True if the object is equal to the given object, False otherwise.
        :rtype: bool
        """
        return self.__dict__ == other.__dict__

    def __getattr__(
        self,
        name: str,
    ) -> Any:
        """
        Returns the value of the attribute with the given name.

        :param name: The name of the attribute to get.
        :type name: str

        :return: The value of the attribute with the given name.
        :rtype: Any
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Return the value of the attribute
        return self.__dict__[name]

    def __getitem__(
        self,
        name: str,
    ) -> Any:
        """
        Returns the value of the attribute with the given name.

        :param name: The name of the attribute to get.
        :type name: str

        :return: The value of the attribute with the given name.
        :rtype: Any
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Return the value of the attribute
        return self.__dict__[name]

    def __repr__(
        self,
    ) -> str:
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """

        # Return a string representation of the object
        return f"<{self.__class__.__name__}({", ".join([f'{key}={value}' for key, value, in self.to_dict().items()])})>"

    def __setattr__(
        self,
        name: str,
        value: Any,
    ) -> None:
        """
        Sets the value of the attribute with the given name.

        :param name: The name of the attribute to set.
        :type name: str

        :param value: The value to set the attribute to.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Set the value of the attribute with the given name
        self.__dict__[name] = value

    def __setitem__(
        self,
        name: str,
        value: Any,
    ) -> None:
        """
        Sets the value of the attribute with the given name.

        :param name: The name of the attribute to set.
        :type name: str

        :param value: The value to set the attribute to.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Set the value of the attribute with the given name
        self.__dict__[name] = value

    def __str__(
        self,
    ) -> str:
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """

        # Return a string representation of the object
        return self.__repr__()

    def compare_to(
        self,
        key: Union[str, Iterable[str]],
        other: "MutableBaseObject",
    ) -> bool:
        """
        Checks, if the values associated with the given keys are equal within this and the given object.

        :param key: The key to check.
        :type key: str

        :param other: The object to compare to.
        :type other: MutableBaseObject

        :return: True if the object contains the given key, False otherwise.
        :rtype: bool
        """

        # Check if the passed key argument is not a list
        if not isinstance(
            key,
            list,
        ):
            # Convert the key to a list if it is a string
            key = [key]

        # Check if the values associated with the given keys are equal
        return all(self[key] == other[key] for key in key)

    def contains_key(
        self,
        key: str,
    ) -> bool:
        """
        Checks if the object contains the given key.

        :param key: The key to check.
        :type key: str

        :return: True if the object contains the given key, False otherwise.
        :rtype: bool
        """

        # Check if the object contains the given key
        return f"_{key}" in self.__dict__

    def contains_value(
        self,
        value: Any,
    ) -> bool:
        """
        Checks if the object contains the given value.

        :param value: The value to check.
        :type value: Any

        :return: True if the object contains the given value, False otherwise.
        :rtype: bool
        """

        # Check if the object contains the given value
        return value in self.__dict__.values()

    def delete(
        self,
        name: str,
    ) -> None:
        """
        Deletes the attribute with the given name.

        :param name: The name of the attribute to delete.
        :type name: str

        :return: None
        :rtype: None
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Delete the attribute
        del self.__dict__[name]

    def get(
        self,
        name: str,
    ) -> Any:
        """
        Returns the value of the attribute with the given name.

        :param name: The name of the attribute to get.
        :type name: str

        :return: The value of the attribute with the given name.
        :rtype: Any
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Return the value of the attribute
        return self.__dict__[name]

    def set(
        self,
        name: str,
        value: Any,
    ) -> None:
        """
        Sets the value of the attribute with the given name.

        :param name: The name of the attribute to set.
        :type name: str

        :param value: The value to set the attribute to.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Set the value of the attribute
        self.__dict__[name] = value

    def to_dict(
        self,
        exclude: Iterable[str] = None,
    ) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the object.

        :param exclude: A list of attribute names to exclude from the dictionary.
        :type exclude: Iterable[str]

        :return: A dictionary representation of the object.
        :rtype: Dict[str, Any]
        """

        # Check, if the exclude argument is None
        if not exclude:
            # Initialize an empty list
            exclude = []

        # Check, if the logger attribute should be excluded
        if "_logger" not in exclude:
            # Add "_logger" to the exclude list
            exclude.append("_logger")

        # Return a dictionary representation of the object
        return {
            key: self.__dict__[key]
            for key in sorted(self.__dict__.keys())
            if key not in exclude
        }


class ImmutableBaseObject(MutableBaseObject):
    """
    A base object that is immutable.

    This class serves as a base class for all immutable base objects.

    It inherits the MutableBaseObject class and extends it with immutability.

    Attributes:
        logger (Logger): The Logger instance associated with the object.
    """

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ImmutableBaseObject class.

        :param kwargs: Keyword arguments to be passed to the parent class constructor.
        :type kwargs: Dict[str, Any]

        :return: None
        """

        # Call the parent class constructor
        super().__init__(**kwargs)

    def __delattr__(
        self,
        name: str,
    ) -> None:
        """
        Deletes the attribute with the given name if it exists.

        :param name: The name of the attribute to delete.
        :type name: str

        :return: None
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot delete attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """

        # Return a string representation of the object
        return (
            super()
            .__repr__()
            .replace(
                f"({self.__class__.__name__})",
                f"({self.__class__.__name__}[Immutable])",
            )
        )

    def __setattr__(
        self,
        name: str,
        value: Any,
    ) -> None:
        """
        Sets the value of the attribute with the given name.

        :param name: The name of the attribute to set.
        :type name: str

        :param value: The value to set the attribute to.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Set the value of the attribute
            super().__setattr__(
                name=name,
                value=value,
            )

            # Return early since the attribute was set
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    def __setitem__(
        self,
        name: str,
        value: Any,
    ) -> None:
        """
        Sets the value of the attribute with the given name.

        :param name: The name of the attribute to set.
        :type name: str

        :param value: The value to set the attribute to.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Set the value of the attribute
            super().__setitem__(
                name=name,
                value=value,
            )

            # Return early since the attribute was set
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    def delete(
        self,
        name: str,
    ) -> None:
        """
        Deletes the attribute with the given name.

        :param name: The name of the attribute to delete.
        :type name: str

        :return: None
        :rtype: None
        """

        # Check if the attribute exists
        if name not in self.__dict__:
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name}' does not exist.")

            # Return early since the attribute is not present
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot delete attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    def set(
        self,
        name: str,
        value: Any,
    ) -> None:
        """
        Sets the value of the attribute with the given name.

        :param name: The name of the attribute to set.
        :type name: str

        :param value: The value to set the attribute to.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Check if the attribute exists
        if name in self.__dict__:
            # Set the value of the attribute
            super().set(
                name=name,
                value=value,
            )

            # Return early since the attribute was set
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )
