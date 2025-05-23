"""
Author: lodego
Date: 2024-01-24
"""

import json

from typing import *

from utils.logger import Logger


__all__: Final[List[str]] = [
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
        hide_attributes: bool = False,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the MutableBaseObject class.

        :param hide_attributes: Whether to hide attributes
        :type hide_attributes: bool

        :param kwargs: keyword arguments
        :type kwargs: Dict[str, Any]

        :return: None
        :rtype: None
        """

        # Get an instance of the logger class and store it in the object
        object.__setattr__(
            self,
            "_logger",
            Logger.get_logger(self.__class__.__name__),
        )

        # Iterate over the keys and values of the passed keyword arguments
        for (
            key,
            value,
        ) in kwargs.items():
            # Check, if hide_attributes is True
            if hide_attributes:
                # Format the key
                key = f"_{key}" if not key.strip().startswith("_") else key

            # Set the attribute of the object
            object.__setattr__(
                self,
                key,
                value,
            )

    @property
    def logger(self) -> Logger:
        """
        Returns the logger instance associated with the object.

        :return: The logger instance associated with the object.
        :rtype: Logger
        """
        return self._logger

    def __deep_eq__(
        self,
        other: "MutableBaseObject",
    ) -> bool:
        """
        Performs a deep equality check and logs differences between self and other.

        This method compares all attributes of the current object with another object
        of the same class and prints/logs differences field by field.

        :param other: The other object to compare with.
        :type other: MutableBaseObject

        :return: True if all attributes are equal, False otherwise.
        :rtype: bool
        """

        # Check if both objects are of the same type
        if not isinstance(
            other,
            self.__class__,
        ):
            # Log a warning message
            self.logger.warning(
                message=f"[DEEP_EQ] Type mismatch: {type(self)} != {type(other)}"
            )

            # Return False early
            return False

        # Initialize the differences list of tuples as an empty list
        differences: List[
            Tuple[
                str,
                Optional[Any],
                Optional[Any],
            ]
        ] = []

        # Iterate over the keys in the object's dictionary
        for key in self.__dict__.keys():
            # Obtain the value associated with the current key from the object's dictionary
            self_val: Optional[Any] = self.__dict__.get(key)

            # Obtain the value associated with the current key from the other object's dictionary
            other_val: Optional[Any] = other.__dict__.get(key)

            # Check, if the two values are identical
            if self_val != other_val:
                # Add the key, this object's and the other object's value to the differences list of tuples
                differences.append((key, self_val, other_val))

        # Check, if there were any differneces
        if differences:
            # Log an info message
            self.logger.info(
                message=f"[DEEP_EQ] Found {len(differences)} differences between objects:"
            )

            # Iterate over the keys, this object's and the other object's values
            for (
                key,
                self_val,
                other_val,
            ) in differences:
                # Log a warning message
                self.logger.info(
                    message=f" - {key}: self={self_val} | other={other_val}"
                )

            # Return False
            return False

        # Return True
        return True

    @override
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
        if not self.has(
            name,
        ):
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

            # Return early since the attribute is not present
            return

        # Delete the attribute
        del self.__dict__[name]

    @override
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

        # Check if the objects are equal
        return isinstance(other, MutableBaseObject) and self.__dict__ == other.__dict__

    @override
    def __getattr__(
        self,
        name: str,
    ) -> Optional[Any]:
        """
        Returns the value of the attribute with the given name.

        :param name: The name of the attribute to get.
        :type name: str

        :return: The value of the attribute with the given name.
        :rtype: Optional[Any]
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ):
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

            # Return early since the attribute is not present
            return

        # Return the value of the attribute
        return self.__dict__.get(
            name,
            self.__dict__.get(
                f"_{name}",
                None,
            ),
        )

    @override
    def __getitem__(
        self,
        name: str,
    ) -> Optional[Any]:
        """
        Returns the value of the attribute with the given name.

        :param name: The name of the attribute to get.
        :type name: str

        :return: The value of the attribute with the given name.
        :rtype: Optional[Any]
        """

        # Check if the attribute exists
        if self.has(
            name,
        ):
            # Return the value of the attribute
            return self.__dict__.get(
                name,
                self.__dict__.get(
                    f"_{name}",
                    None,
                ),
            )
        elif self.has(
            name,
        ):
            # Return the value of the attribute
            return self.__dict__.get(
                name,
                None,
            )

        # Log a warning message if the attribute does not exist
        self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

        # Return None
        return None

    @override
    def __repr__(
        self,
    ) -> str:
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """

        # Return a string representation of the object
        return f"<{self.__class__.__name__}({", ".join([f'{key}={value}' for (key, value,) in self.to_dict().items()])})>"

    @override
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

    @override
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

    @override
    def __str__(
        self,
    ) -> str:
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """

        # Return a string representation of the object
        return ", ".join(
            [
                f"{key}={value}"
                for (
                    key,
                    value,
                ) in self.to_dict(exclude=["_logger"]).items()
            ]
        )

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
        if not self.has(
            name,
        ) and not self.has(
            f"_{name}",
        ):
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

            # Return early since the attribute is not present
            return

        # Delete the attribute
        del self.__dict__[name]

    def get(
        self,
        name: str,
        default: Optional[Any] = None,
    ) -> Optional[Any]:
        """
        Returns the value of the attribute with the given name.

        :param default: The default value to return if the attribute does not exist.
        :type default: Optional[Any]

        :param name: The name of the attribute to get.
        :type name: str

        :return: The value of the attribute with the given name.
        :rtype: Optional[Any]
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ) and not self.has(
            f"_{name}",
        ):
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

            # Return the default value if the attribute is not present
            return default

        # Return the value of the attribute
        return self.__dict__.get(
            name,
            self.__dict__.get(
                f"_{name}",
                default,
            ),
        )

    def has(
        self,
        key: str,
    ) -> bool:
        """
        Checks if the object has the given key.

        :param key: The key to check.
        :type key: str

        :return: True if the object has the given key, False otherwise.
        :rtype: bool
        """

        # Return True if the object has the given key
        return key in self.__dict__

    def is_mutable(self) -> bool:
        """
        Returns True if the object is mutable, False otherwise.

        Returns:
            bool: True if the object is mutable, False otherwise.
        """

        # Return True if the object is mutable
        return True

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
        exclude: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the object.

        :param exclude: An optional list of attribute names to exclude from the dictionary.
        :type exclude: Optional[List[str]]

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

        # Initialize the result dictionary as an empty dictionary
        result: Dict[str, Any] = {}

        # Iterate over the attributes of the object
        for key in sorted(self.__dict__.keys()):
            # Check, if the attribute should be excluded
            if key in exclude:
                # Skip the attribute
                continue

            # Add the attribute to the result dictionary
            result[key.strip("_")] = self.__dict__[key]

        # Return the result dictionary
        return result

    def to_json(
        self,
        exclude: Optional[List[str]] = None,
    ) -> str:
        """
        Returns a JSON string representation of the object.

        :param exclude: An optional list of attribute names to exclude from the JSON string.
        :type exclude: Optional[List[str]]

        :return: A JSON string representation of the object.
        :rtype: str
        """

        # Return the JSON string representation of the object
        return json.dumps(
            self.to_dict(exclude=exclude),
            indent=4,
        )

    def update(
        self,
        **kwargs,
    ) -> None:
        """
        Updates the attributes of the object with the given keyword arguments.

        :param kwargs: The keyword arguments representing attribute names and their new values.
        :type kwargs: Dict[str, Any]

        :return: None
        :rtype: None
        """
        # Iterate over the keyword arguments
        for (
            key,
            value,
        ) in kwargs.items():
            # Set the value of the attribute in the object
            self.set(
                name=key,
                value=value,
            )


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
        hide_attributes: bool = False,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ImmutableBaseObject class.

        :param hide_attributes: Whether to hide attributes
        :type hide_attributes: bool

        :param kwargs: Keyword arguments to be passed to the parent class constructor.
        :type kwargs: Dict[str, Any]

        :return: None
        :rtyoe: None
        """

        # Update kwargs with the 'hide_attributes' argument
        kwargs.update(
            {
                "hide_attributes": hide_attributes,
            }
        )

        # Call the parent class constructor
        super().__init__(**kwargs)

    @override
    def __delattr__(
        self,
        name: str,
    ) -> None:
        """
        Deletes the attribute with the given name if it exists.

        :param name: The name of the attribute to delete.
        :type name: str

        :return: None
        :rtyoe: None

        :raises AttributeError: If the attribute is immutable.
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ):
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

            # Return early since the attribute is not present
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot delete attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    @override
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
                f"{self.__class__.__name__}",
                f"{self.__class__.__name__}(Immutable)",
            )
        )

    @override
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

        :raises AttributeError: If the attribute is immutable.
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ):
            # Set the value of the attribute
            self.__dict__[name] = value

            # Return early since the attribute was set
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    @override
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

        :raises AttributeError: If the attribute is immutable.
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ):
            # Set the value of the attribute
            self.__dict__[name] = value

            # Return early since the attribute was set
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    @override
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

        :raises AttributeError: If the attribute is immutable.
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ):
            # Log a warning message if the attribute does not exist
            self.logger.warning(message=f"Attribute '{name.strip("_")}' does not exist.")

            # Return early since the attribute is not present
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot delete attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    @override
    def is_mutable(self) -> bool:
        """
        Returns True if the object is mutable, False otherwise.

        Returns:
            bool: True if the object is mutable, False otherwise.
        """

        # Return False if the object is immutable
        return False

    @override
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

        :raises AttributeError: If the attribute is immutable.
        """

        # Check if the attribute exists
        if not self.has(
            name,
        ):
            # Set the value of the attribute
            self.__dict__[name] = value

            # Return early since the attribute was set
            return

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute '{name}' in {self.__class__.__name__}, attribute is immutable."
        )

    @override
    def update(
        self,
        **kwargs,
    ) -> None:
        """
        Updates the attributes of the object with the given keyword arguments.

        :param kwargs: The keyword arguments representing attribute names and their new values.
        :type kwargs: Dict[str, Any]

        :return: None
        :rtype: None

        :raises AttributeError: If the attribute is immutable.
        """

        # Iterate over the keyword arguments
        for (
            key,
            value,
        ) in kwargs.items():
            # Check if the attribute exists
            if not self.has(
                key,
            ):
                # Set the value of the attribute
                self.__dict__[key] = value

        # Raise an attribute error as the attribute is immutable
        raise AttributeError(
            f"Cannot set attribute(s) '{', '.join(key for key in kwargs.keys() if key in self.__dict__)}' in {self.__class__.__name__}, attribute is immutable."
        )
