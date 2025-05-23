"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["BaseObjectBuilder"]


class BaseObjectBuilder(ImmutableBaseObject):
    """
    A base class for builder classes that build an object using keyword arguments.

    This class is immutable and can be used as a base class for all builder classes.

    Attributes:
        configuration (Dict[str, Any]): The configuration dictionary for the builder.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the BaseObjectBuilder class.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            configuration={},
            hide_attributes=True,
        )

    @property
    def configuration(self) -> Dict[str, Any]:
        """
        Gets the configuration dictionary for the builder.

        Returns:
            Dict[str, Any]: The configuration dictionary for the builder.
        """

        # Return the configuration dictionary
        return self._configuration

    def build(self) -> Any:
        """
        A placeholder method for building an instance of the subclass.

        This method must be implemented by the subclass. It will raise a NotImplementedError if called.

        Args:
            None

        Returns:
            Any: An instance of the subclass.
        """

        # Raise a NotImplementedError if the method is not implemented
        raise NotImplementedError(
            f"Subclass '{self.__class__.__name__}' must implement the 'build' method."
        )

    def kwargs(
        self,
        **kwargs,
    ) -> Self:
        """
        Updates the configuration dictionary with the given keyword arguments.

        Args:
            kwargs (Dict[str, Any]): The keyword arguments to be updated.

        Returns:
            Self: The builder instance with updated configuration.
        """

        # Update the configuration dictionary with the given keyword arguments
        self.configuration.update(kwargs)

        # Return the builder instance
        return self
