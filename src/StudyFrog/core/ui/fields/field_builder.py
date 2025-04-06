"""
Author: lodego
Date: 2025-04-06
"""

import tkinter
import traceback

from typing import *

from core.ui.fields.numeric_fields import *
from core.ui.fields.string_fields import *

from utils.base_field import BaseField
from utils.builder import BaseObjectBuilder


__all__: Final[List[str]] = [
    "FieldBuilder",
    "register_field_type",
]


FIELD_TYPE_MAPING: Final[Dict[str, Type[BaseField]]] = {
    "float_spinbox_field": FloatSpinboxField,
    "integer_spinbox_field": IntegerSpinboxField,
    "multi_line_text_field": MultiLineTextField,
    "single_line_text_field": SingleLineTextField,
}


def register_field_type(
    field_type: str,
    field_class: Type[BaseField],
) -> None:
    """
    Registers a new field type with the FieldBuilder.

    This method registers a new field type with the FieldBuilder by adding it to the
    FIELD_TYPE_MAPING dictionary.

    Args:
        field_type (str): The field type to register. Must be a valid key in
                         FIELD_TYPE_MAPING.
        field_class (Type[BaseField]): The class of the field to register.

    Returns:
        None
    """

    # Add the field type and class to the dictionary
    FIELD_TYPE_MAPING[field_type] = field_class

    # Return None
    return None


class FieldBuilder(BaseObjectBuilder):
    """
    A builder class for creating instances of subclasses of BaseField.

    This class provides a fluent interface for setting various attributes
    of a BaseField object. It inherits from BaseObjectBuilder and manages
    the configuration state for the object being built.

    Attributes:
        configuration (Dict[str, Any]): The dictionary containing the configuration
                                        of the object to be built.
    """

    def __init__(self) -> None:
        """Constructor for the FieldBuilder class.

        Initializes the FieldBuilder and its configuration.
        """

        # Call teh parent class constructor
        super().__init__()

    @override
    def build(self) -> Optional[BaseField]:
        """
        Builds a Field class based on the provided configuration.

        This method is responsible for building a Field class based on the provided
        configuration. It does this by retrieving the class from the FIELD_TYPE_MAPING
        dictionary and then calling the constructor with the configuration as keyword
        arguments.

        Args:
            None

        Returns:
            Optional[BaseField]: The built Field class or None if the field type is not
                found in the FIELD_TYPE_MAPING dictionary.
        """

        try:
            # Retrieve the field class from the FIELD_TYPE_MAPING dictionary
            field_class: Optional[Type[BaseField]] = FIELD_TYPE_MAPING.get(
                self.configuration["field_type"],
                None,
            )

            # Check if the field type is valid
            if not field_class:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to find field class for field type: '{self.configuration['field_type']}'."
                )

                # Return early
                return None

            # Build the field class with the configuration as keyword arguments
            return field_class(**self.configuration)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def field_type(
        self,
        value: str,
    ) -> Self:
        """
        Sets the field type for the FieldBuilder.

        This method sets the field type for the FieldBuilder by updating
        the 'configuration' dictionary with the specified value.

        Args:
            value (str): The field type to set. Must be a valid key in
                         FIELD_TYPE_MAPING.

        Returns:
            Self: The FieldBuilder instance with updated field type or None
                  if the field type is not valid.
        """

        # Check if the provided value is a valid field type
        if value not in FIELD_TYPE_MAPING:
            # Log a warning message
            self.logger.warning(message=f"Invalid field type: '{value}'.")

            # Return None if the field type is invalid
            return

        # Update the configuration with the valid field type
        self.configuration["field_type"] = value
        return self

    def label(
        self,
        value: str,
    ) -> Self:
        """
        Sets the label for the FieldBuilder.

        This method sets the label for the FieldBuilder by updating
        the 'configuration' dictionary with the specified value.

        Args:
            value (str): The label to set.

        Returns:
            Self: The FieldBuilder instance with updated label.
        """

        # Update the configuration with the provided label
        self.configuration["label"] = value
        return self

    def master(
        self,
        value: tkinter.Misc,
    ) -> Self:
        """
        Sets the master widget for the FieldBuilder.

        This method sets the master widget for the FieldBuilder by updating
        the 'configuration' dictionary with the specified value.

        Args:
            value (tkinter.Misc): The master widget to set.

        Returns:
            Self: The FieldBuilder instance with updated master widget.
        """

        # Update the configuration with the provided master widget
        self.configuration["master"] = value
        return self

    def namespace(
        self,
        value: str,
    ) -> Self:
        """
        Sets the namespace for the FieldBuilder.

        This method sets the namespace for the FieldBuilder by updating
        the 'configuration' dictionary with the specified value.

        Args:
            value (str): The namespace to set.

        Returns:
            Self: The FieldBuilder instance with updated namespace.
        """

        # Update the configuration with the provided namespace
        self.configuration["namespace"] = value
        return self

    def on_change_callback(
        self,
        value: Callable[[str, Any], None],
    ) -> Self:
        """
        Sets the on-change callback function for the FieldBuilder.

        This method sets the on-change callback function for the FieldBuilder by
        updating the 'configuration' dictionary with the specified value.

        The on-change callback function is called when the value of the field
        changes and is passed the display name and the value of the field.

        Args:
            value (Callable[[str, Any], None]): The on-change callback function to set.

        Returns:
            Self: The FieldBuilder instance with updated on-change callback function.
        """

        # Update the configuration with the provided on-change callback function
        self.configuration["on_change_callback"] = value
        return self

    def value(
        self,
        value: Any,
    ) -> Self:
        """
        Sets the value for the FieldBuilder.

        This method sets the value for the FieldBuilder by updating the
        'configuration' dictionary with the specified value.

        Args:
            value (Any): The value to set.

        Returns:
            Self: The FieldBuilder instance with updated value.
        """

        # Update the configuration with the provided value
        self.configuration["value"] = value
        return self
