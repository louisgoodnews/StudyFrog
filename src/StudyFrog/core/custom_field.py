"""
Author: lodego
Date: 2025-02-09
"""

import asyncio
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
    "ImmutableCustomField",
    "MutableCustomField",
    "CustomFieldConverter",
    "CustomFieldFactory",
    "CustomFieldModel",
]


class ImmutableCustomField(ImmutableBaseObject):
    """
    An immutable class representing a custom field.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the custom field was created.
        description (Optional[str]): The description of the custom field.
        id (Optional[int]): The ID of the custom field.
        key (Optional[str]): The key of the custom field.
        metadata (Optional[Dict[str, Any]]): The metadata of the custom field.
        name (str): The name of the custom field.
        type (str): The type of the custom field.
        updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
        uuid (Optional[str]): The UUID of the custom field.
    """

    def __init__(
        self,
        name: str,
        type: str,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "🎛️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the CustomField class.

        Args:
            created_at (Optional[datetime]): The timestamp when the custom field was created.
            description (Optional[str]): The description of the custom field.
            icon (Optional[str]): The icon of the custom field. Defaults to "🎛️".
            id (Optional[int]): The ID of the custom field.
            key (Optional[str]): The key of the custom field.
            metadata (Optional[Dict[str, Any]]): The metadata of the custom field.
            name (str): The name of the custom field.
            type (str): The type of the custom field.
            updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
            uuid (Optional[str]): The UUID of the custom field.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Gets the timestamp when the custom field was created.

        Returns:
            datetime: The timestamp when the custom field was created.
        """

        # Return the created_at attribute
        return self._created_at

    @property
    def description(self) -> str:
        """
        Gets the description of the custom field.

        Returns:
            str: The description of the custom field.
        """

        # Return the description attribute
        return self._description

    @property
    def icon(self) -> str:
        """
        Gets the icon of the custom field.

        Returns:
            str: The icon of the custom field.
        """

        # Return the icon attribute
        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the custom field.

        Returns:
            int: The ID of the custom field.
        """

        # Return the id attribute
        return self._id

    @property
    def key(self) -> str:
        """
        Gets the key of the custom field.

        Returns:
            str: The key of the custom field.
        """

        # Return the key attribute
        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the custom field.

        Returns:
            Dict[str, Any]: The metadata of the custom field.
        """

        # Return the metadata attribute
        return self._metadata

    @property
    def name(self) -> str:
        """
        Gets the name of the custom field.

        Returns:
            str: The name of the custom field.
        """

        # Return the name attribute
        return self._name

    @property
    def type(self) -> str:
        """
        Gets the type of the custom field.

        Returns:
            str: The type of the custom field.
        """

        # Return the type attribute
        return self._type

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the custom field was last updated.

        Returns:
            datetime: The timestamp when the custom field was last updated.
        """

        # Return the updated_at attribute
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the custom field.

        Returns:
            str: The UUID of the custom field.
        """

        # Return the uuid attribute
        return self._uuid

    def to_mutable(self) -> Optional["MutableCustomField"]:
        """
        Returns a mutable version of the immutable object.

        Returns:
            MutableCustomField: A mutable version of the immutable object.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableCustomField instance.
        """
        try:
            # Attempt to create and return a new instance of the MutableCustomField class from the dictionary representation of the ImmutableCustomField instance
            return MutableCustomField(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class MutableCustomField(MutableBaseObject):
    """
    A mutable class representing a custom field.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the custom field was created.
        description (Optional[str]): The description of the custom field.
        id (Optional[int]): The ID of the custom field.
        key (Optional[str]): The key of the custom field.
        metadata (Optional[Dict[str, Any]]): The metadata of the custom field.
        name (str): The name of the custom field.
        type (str): The type of the custom field.
        updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
        uuid (Optional[str]): The UUID of the custom field.
    """

    def __init__(
        self,
        name: str,
        type: str,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "🎛️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableCustomField class.

        Args:
            created_at (Optional[datetime]): The timestamp when the custom field was created.
            description (Optional[str]): The description of the custom field.
            icon (Optional[str]): The icon of the custom field. Defaults to "🎛️".
            id (Optional[int]): The ID of the custom field.
            key (Optional[str]): The key of the custom field.
            metadata (Optional[Dict[str, Any]]): The metadata of the custom field.
            name (str): The name of the custom field.
            type (str): The type of the custom field.
            updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
            uuid (Optional[str]): The UUID of the custom field.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Gets the timestamp when the custom field was created.

        Returns:
            datetime: The timestamp when the custom field was created.
        """

        # Return the created_at attribute
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the custom field was created.

        Args:
            value (datetime): The timestamp when the custom field was created.

        Returns:
            None
        """

        # Set the created_at attribute
        self._created_at = value

    @property
    def description(self) -> str:
        """
        Gets the description of the custom field.

        Returns:
            str: The description of the custom field.
        """

        # Return the description attribute
        return self._description

    @description.setter
    def description(
        self,
        value: str,
    ) -> None:
        """
        Sets the description of the custom field.

        Args:
            value (str): The description of the custom field.

        Returns:
            None
        """

        # Set the description attribute
        self._description = value

    @property
    def icon(self) -> str:
        """
        Gets the icon of the custom field.

        Returns:
            str: The icon of the custom field.
        """

        # Return the icon attribute
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the custom field.

        Args:
            value (str): The icon of the custom field.

        Returns:
            None
        """

        # Set the icon attribute
        self._icon = value

    @property
    def id(self) -> int:
        """
        Gets the ID of the custom field.

        Returns:
            int: The ID of the custom field.
        """

        # Return the id attribute
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the custom field.

        Args:
            value (int): The ID of the custom field.

        Returns:
            None
        """

        # Set the id attribute
        self._id = value

    @property
    def key(self) -> str:
        """
        Gets the key of the custom field.

        Returns:
            str: The key of the custom field.
        """

        # Return the key attribute
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the custom field.

        Args:
            value (str): The key of the custom field.

        Returns:
            None
        """

        # Set the key attribute
        self._key = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the custom field.

        Returns:
            Dict[str, Any]: The metadata of the custom field.
        """

        # Return the metadata attribute
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the metadata of the custom field.

        Args:
            **kwargs (Dict[str, Any]): The metadata of the custom field.

        Returns:
            None
        """

        # Check if the 'metadata' dictionary exists
        if not self.get(
            default=None,
            name="metadata",
        ):
            # Initialize the 'metadata' dictionary
            self.metadata = {}

        # Update the 'metadata' dictionary with the provided keyword arguments
        self.metadata.update(**kwargs)

    @property
    def name(self) -> str:
        """
        Gets the name of the custom field.

        Returns:
            str: The name of the custom field.
        """

        # Return the name attribute
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Sets the name of the custom field.

        Args:
            value (str): The name of the custom field.

        Returns:
            None
        """

        # Set the name attribute
        self._name = value

    @property
    def type(self) -> str:
        """
        Gets the type of the custom field.

        Returns:
            str: The type of the custom field.
        """

        # Return the type attribute
        return self._type

    @type.setter
    def type(
        self,
        value: str,
    ) -> None:
        """
        Sets the type of the custom field.

        Args:
            value (str): The type of the custom field.

        Returns:
            None
        """

        # Set the type attribute
        self._type = value

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the custom field was last updated.

        Returns:
            datetime: The timestamp when the custom field was last updated.
        """

        # Return the updated_at attribute
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the custom field was last updated.

        Args:
            value (datetime): The timestamp when the custom field was last updated.

        Returns:
            None
        """

        # Set the updated_at attribute
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the custom field.

        Returns:
            str: The UUID of the custom field.
        """

        # Return the uuid attribute
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the custom field.

        Args:
            value (str): The UUID of the custom field.

        Returns:
            None
        """

        # Set the uuid attribute
        self._uuid = value

    def to_immutable(self) -> Optional[ImmutableCustomField]:
        """
        Returns an immutable version of the mutable object.

        Returns:
            ImmutableCustomField: An immutable version of the mutable object.

        Raises:
            Exception: If an exception occurs while attempting to convert the MutableCustomField instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableCustomField class from the dictionary representation of the MutableCustomField instance
            return ImmutableCustomField(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class CustomFieldConverter:
    """
    A converter class for transforming between CustomFieldModel and CustomField instances.

    This class provides methods to convert a CustomFieldModel instance to an CustomField instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the CustomFieldConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="CustomFieldConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "CustomFieldModel",
    ) -> Optional[ImmutableCustomField]:
        """
        Converts a given CustomFieldModel instance to an CustomField instance.

        Args:
            model (CustomFieldModel): The CustomFieldModel instance to be converted.

        Returns:
            CustomField: The converted CustomField instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the CustomFieldModel instance.
        """
        try:
            # Attempt to create and return a new instance of the CustomField class from the dictionary representation of the CustomFieldModel instance
            return ImmutableCustomField(
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

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def object_to_model(
        cls,
        object: Union[ImmutableCustomField, MutableCustomField],
    ) -> Optional["CustomFieldModel"]:
        """
        Converts a given CustomField instance to a CustomFieldModel instance.

        Args:
            object (CustomField): The CustomField instance to be converted.

        Returns:
            CustomFieldModel: The converted CustomFieldModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the CustomField instance.
        """
        try:
            # Attempt to create and return a new instance of the CustomFieldModel class from the dictionary representation of the CustomField instance
            return CustomFieldModel(
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

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class CustomFieldFactory:
    """
    A factory class for creating instances of the CustomField class.

    Attributes:
        logger (Logger): The logger instance associated with the CustomFieldFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="CustomFieldFactory")

    @classmethod
    def create_custom_field(
        cls,
        name: str,
        type: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🎛️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableCustomField]:
        """
        Creates and returns a new instance of the CustomField class.

        Args:
            name (str): The name of the custom field.
            type (str): The type of the custom field.
            created_at (datetime): The timestamp when the custom field was created.
            icon (str): The icon of the custom field. Defaults to "🎛️".
            id (int): The ID of the custom field.
            key (str): The key of the custom field.
            updated_at (datetime): The timestamp when the custom field was last updated.
            uuid (str): The UUID of the custom field.

        Returns:
            Optional[ImmutableCustomField]: The newly created CustomField instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the CustomField instance.
        """
        try:
            # Attempt to create and return a new instance of the CustomField class
            return ImmutableCustomField(
                created_at=created_at,
                icon=icon,
                id=id,
                key=key,
                name=name,
                type=type,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_custom_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CustomFieldBuilder(BaseObjectBuilder):
    """ """

    def __init__(self) -> None:
        """
        Initializes a new instance of the CustomFieldBuilder class.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(
        self,
        as_mutable: bool = False,
    ) -> Optional[
        Union[
            ImmutableCustomField,
            MutableCustomField,
        ]
    ]:
        """
        Builds a new instance of the CustomField class.

        Args:
            as_mutable (bool): A flag indicating whether to return a mutable instance of the CustomField class. Defaults to False.

        Returns:
            Optional[Union[ImmutableCustomField, MutableCustomField]]: The newly created CustomField instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to build the CustomField instance.
        """
        try:
            # Attempt to create a new ImmutableCustomField instance
            custom_field: Optional[ImmutableCustomField] = (
                CustomFieldFactory.create_custom_field(**self.configuration)
            )

            # Check, if the custom field exists
            if not custom_field:
                # Log a warning message indicating an exception has occurred
                self.logger.warning(
                    message=f"Failed to build an instance of the ImmutableCustomField or MutableCustomField class from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Check, if the 'as_mutable' flag has been set to True
            if as_mutable:
                # Convert the custom field into a MutableCustomField instance and return it
                return custom_field.to_mutable()

            # Return the custom field
            return custom_field
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the created_at value.

        Args:
            value (datetime): The created_at value.

        Returns:
            Self: The builder instance.
        """

        # Set the created_at value
        self.configuration["created_at"] = value

        # Return the builder instance
        return self

    def name(
        self,
        value: str,
    ) -> Self:
        """
        Sets the name value.

        Args:
            value (str): The name value.

        Returns:
            Self: The builder instance.
        """

        # Set the name value
        self.configuration["name"] = value

        # Return the builder instance
        return self

    def type(
        self,
        value: str,
    ) -> Self:
        """
        Sets the type value.

        Args:
            value (str): The type value.

        Returns:
            Self: The builder instance.
        """

        # Set the type value
        self.configuration["type"] = value

        # Return the builder instance
        return self

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the updated_at value.

        Args:
            value (datetime): The updated_at value.

        Returns:
            Self: The builder instance.
        """

        # Set the updated_at value
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self


class CustomFieldManager(BaseObjectManager):
    """
    A manager class for managing custom fields in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for custom fields.

    Attributes:
        cache: (List[Any]): The cache for storing custom fields.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["CustomFieldManager"] = None

    def __new__(cls) -> "CustomFieldManager":
        """
        Creates and returns a new instance of the CustomFieldManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            CustomFieldManager: The created or existing instance of CustomFieldManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(CustomFieldManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the CustomFieldManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        custom_field: Union[
            ImmutableCustomField,
            MutableCustomField,
        ],
    ) -> MutableCustomField:
        """
        Runs pre-create tasks for the custom field.

        Args:
            custom_field (Union[ImmutableCustomField, MutableCustomField]): The custom field to run pre-create tasks for.

        Returns:
            MutableCustomField: The custom field with pre-create tasks run.
        """

        # Check, if the custom field is not mutable
        if not custom_field.is_mutable():
            # Convert the custom field into a mutable custom field
            custom_field: MutableCustomField = custom_field.to_mutable()

        # Set the created_at timestamp of the custom field
        custom_field.created_at = (
            custom_field.created_at or Miscellaneous.get_current_datetime()
        )

        # Set the key of the custom field
        custom_field.key = f"CUSTOM_FIELD_{self.count_custom_fields() + 1}"

        # Set the updated_at timestamp of the custom field
        custom_field.updated_at = (
            custom_field.updated_at or Miscellaneous.get_current_datetime()
        )

        # Set the uuid of the custom field
        custom_field.uuid = Miscellaneous.get_uuid()

        # Return the custom field
        return custom_field

    def count_custom_fields(self) -> int:
        """
        Returns the number of custom fields in the database.

        Returns:
            int: The number of custom fields in the database.
        """
        try:
            # Count and return the number of custom fields in the database
            return asyncio.run(CustomFieldModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return 0 indicating an exception has occurred
            return 0

    def create_custom_field(
        self,
        custom_field: Union[ImmutableCustomField, MutableCustomField],
    ) -> Optional[ImmutableCustomField]:
        """
        Creates a new custom field in the database.

        Args:
            custom field (Union[ImmutableCustomField, MutableCustomField]): The custom field to be created.

        Returns:
            Optional[ImmutableCustomField]: The newly created immutable custom field if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the custom field.
        """
        try:
            # Initialize the result (optional) ImmutableCustomField to none
            result: Optional[ImmutableCustomField] = None

            # Run pre-create tasks
            custom_field: MutableCustomField = self._run_pre_create_tasks(
                custom_field=custom_field
            )

            # Convert the custom field object to a CustomFieldModel object
            model: CustomFieldModel = CustomFieldConverter.object_to_model(
                object=custom_field
            )

            # Create a new custom field in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a custom field ({custom_field.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the custom field to a dictionary
            kwargs: Dict[str, Any] = custom_field.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the custom field
            kwargs["id"] = id

            # Create a new ImmutableCustomField object
            result = CustomFieldFactory.create_custom_field(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableCustomField from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the custom field to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableCustomField instance
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_custom_field' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def delete_custom_field(
        self,
        custom_field: Union[ImmutableCustomField, MutableCustomField],
    ) -> bool:
        """
        Deletes a custom field from the database.

        Args:
            custom field (Union[ImmutableCustomField, MutableCustomField]): The custom field to be deleted.

        Returns:
            bool: True if the custom field was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the custom field to an immutable custom field and delete the custom field from the database
            result: bool = asyncio.run(
                CustomFieldConverter.object_to_model(
                    object=CustomField(
                        **custom_field.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the custom field was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete_custom_field' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return False indicating an exception has occurred
            return False

    def get_all_custom_fields(self) -> Optional[List[ImmutableCustomField]]:
        """
        Returns a list of all custom fields in the database.

        Returns:
            Optional[List[ImmutableCustomField]]: A list of all custom fields in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_custom_fields():
                # Return the list of immutable custom fields from the cache
                return self.get_cache_values()

            # Get all custom fields from the database
            models: List[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of CustomFieldModel objects to a list of CustomField objects
            custom_fields: List[ImmutableCustomField] = [
                ImmutableCustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable custom fields
            for custom_field in custom_fields:
                if not self.is_key_in_cache(key=custom_field.key):
                    # Add the immutable custom field to the cache
                    self.add_to_cache(
                        key=custom_field.key,
                        value=custom_field,
                    )
                else:
                    # Update the immutable custom field in the cache
                    self.update_in_cache(
                        key=custom_field.key,
                        value=custom_field,
                    )

            # Return the list of immutable custom fields
            return custom_fields
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all_custom_fields' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def get_custom_field_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableCustomField]:
        """
        Retrieves a custom field by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableCustomField]: The custom field with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the custom field is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the custom field from the cache
                return self.get_value_from_cache(key=field)

            # Get the custom field with the given field and value from the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                return ImmutableCustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_by' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def get_custom_field_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableCustomField]:
        """
        Returns a custom field with the given ID.

        Args:
            id (int): The ID of the custom_field.

        Returns:
            Optional[ImmutableCustomField]: The custom field with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the custom field is already in the cache
            if self.is_key_in_cache(key=f"CUSTOM_FIELD_{id}"):
                # Return the custom field from the cache
                return self.get_value_from_cache(key=f"CUSTOM_FIELD_{id}")

            # Get the custom field with the given ID from the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                return ImmutableCustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def get_custom_field_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableCustomField]:
        """
        Returns a custom field with the given UUID.

        Args:
            uuid (str): The UUID of the custom_field.

        Returns:
            Optional[ImmutableCustomField]: The custom field with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the custom field is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the custom field from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the custom field with the given UUID from the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                return ImmutableCustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def search_custom_fields(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableCustomField]]]:
        """
        Searches for custom fields in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the CustomFieldModel class.

        Returns:
            Optional[Union[List[ImmutableCustomField]]]: The found custom fields if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableCustomField]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for custom fields in the database
            models: Optional[List[CustomFieldModel]] = asyncio.run(
                CustomFieldModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found custom fields if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableCustomField(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]
            else:
                # Return None indicating that no custom fields were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search_custom_fields' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def update_custom_field(
        self,
        custom_field: Union[ImmutableCustomField, MutableCustomField],
    ) -> Optional[ImmutableCustomField]:
        """
        Updates a custom field with the given ID.

        Args:
            custom field (Union[ImmutableCustomField, MutableCustomField]): The custom field to update.

        Returns:
            Optional[ImmutableCustomField]: The updated custom field if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the custom field to an immutable custom field and update the custom field in the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldConverter.object_to_model(
                    object=CustomField(
                        **custom_field.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **custom_field.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                custom_field = ImmutableCustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the custom field to the cache
                self.update_in_cache(
                    key=custom_field.key,
                    value=setting,
                )

                # Return the updated custom field
                return custom_field
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update_custom_field' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class CustomFieldModel(ImmutableBaseModel):
    """
    Represents the structure of a custom field model.

    Attributes:
        created_at (datetime): The timestamp when the custom field was created.
        description (Optional[str]): The description of the custom field.
        icon (str): The icon of the custom field. Defaults to "🎛️".
        id (int): The ID of the custom field.
        key (str): The key of the custom field.
        metadata (Dict[str, Any]): The metadata of the custom field.
        name (str): The name of the custom field.
        type (str): The type of the custom field.
        updated_at (datetime): The timestamp when the custom field was last updated.
        uuid (str): The UUID of the custom field.
    """

    table: Final[str] = Constants.CUSTOM_FIELDS

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

    description: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="description",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    icon: Field = Field(
        autoincrement=False,
        default="🎛️",
        description="",
        foreign_key=None,
        index=False,
        name="icon",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
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

    name: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="name",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="type",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
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
        description: Optional[str] = None,
        icon: Optional[str] = "🎛️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the CustomField class.

        Args:
            created_at (Optional[datetime]): The timestamp when the custom field was created.
            description (Optional[str]): The description of the custom field.
            icon (Optional[str]): The icon of the custom field. Defaults to "🎛️".
            id (Optional[int]): The ID of the custom field.
            key (Optional[str]): The key of the custom field.
            metadata (Optional[Dict[str, Any]]): The metadata of the custom field.
            name (Optional[str]): The name of the custom field.
            type (Optional[str]): The type of the custom field.
            updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
            uuid (Optional[str]): The UUID of the custom field.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            icon="🎛️",
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
        )
