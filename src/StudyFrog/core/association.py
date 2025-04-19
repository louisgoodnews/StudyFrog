"""
Author: lodego
Date: 2025-02-06
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
    "AImmutablessociation",
    "ImmutableAssociation",
    "AssociationConverter",
    "AssociationFactory",
    "AssociationManager",
    "AssociationModel",
]


class ImmutableAssociation(ImmutableBaseObject):
    """
    An immutable class representing an association between two entities.

    Attributes:
        association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
        answer (Optional[int]): The ID of the answer that is being associated with.
        change_history (Optional[int]): The ID of the change history that is being associated with.
        change_history_item (Optional[int]): The ID of the change history item that is being associated with.
        created_at (Optional[datetime]): The timestamp when the association was created.
        custom_field (Optional[int]): The ID of the custom field that is being associated with.
        default (Optional[int]): The ID of the default that is being associated with.
        difficulty (Optional[int]): The ID of the difficulty that is being associated with.
        flashcard (Optional[int]): The ID of the flashcard that is being associated with.
        icon (Optional[str]): The icon of the association..
        id (Optional[int]): The ID of the association.
        key (Optional[str]): The key of the association.
        learning_session (Optional[int]): The ID of the learning session that is being associated with.
        learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
        note (Optional[int]): The ID of the note that is being associated with.
        option (Optional[int]): The ID of the option that is being associated with.
        priority (Optional[int]): The ID of the priority that is being associated with.
        question (Optional[int]): The ID of the question that is being associated with.
        setting (Optional[int]): The ID of the setting that is being associated with.
        stack (Optional[int]): The ID of the stack that is being associated with.
        status (Optional[int]): The ID of the status that is being associated with.
        tag (Optional[int]): The ID of the tag that is being associated with.
        updated_at (Optional[datetime]): The timestamp when the association was last updated.
        user (Optional[int]): The ID of the user that is being associated with.
        uuid (Optional[str]): The UUID of the association.
    """

    def __init__(
        self,
        association_type: Literal[
            "ancestor",
            "dependant",
            "depends_on",
            "descendant",
            "tagged_with",
        ],
        answer: Optional[int] = None,
        change_history: Optional[int] = None,
        change_history_item: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field: Optional[int] = None,
        default: Optional[int] = None,
        difficulty: Optional[int] = None,
        flashcard: Optional[int] = None,
        icon: Optional[str] = "🔗",
        id: Optional[int] = None,
        key: Optional[str] = None,
        learning_session: Optional[int] = None,
        learning_session_item: Optional[int] = None,
        note: Optional[int] = None,
        option: Optional[int] = None,
        priority: Optional[int] = None,
        question: Optional[int] = None,
        setting: Optional[int] = None,
        stack: Optional[int] = None,
        status: Optional[int] = None,
        tag: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        user: Optional[int] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Association class.

        Args:
            association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
            answer (Optional[int]): The ID of the answer that is being associated with.
            change_history (Optional[int]): The ID of the change history that is being associated with.
            change_history_item (Optional[int]): The ID of the change history item that is being associated with.
            created_at (Optional[datetime]): The timestamp when the association was created.
            custom_field (Optional[int]): The ID of the custom field that is being associated with.
            default (Optional[int]): The ID of the default that is being associated with.
            difficulty (Optional[int]): The ID of the difficulty that is being associated with.
            flashcard (Optional[int]): The ID of the flashcard that is being associated with.
            icon (Optional[str]): The icon of the association. Defaults to "🔗".
            id (Optional[int]): The ID of the association.
            key (Optional[str]): The key of the association.
            learning_session (Optional[int]): The ID of the learning session that is being associated with.
            learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
            note (Optional[int]): The ID of the note that is being associated with.
            option (Optional[int]): The ID of the option that is being associated with.
            priority (Optional[int]): The ID of the priority that is being associated with.
            question (Optional[int]): The ID of the question that is being associated with.
            setting (Optional[int]): The ID of the setting that is being associated with.
            stack (Optional[int]): The ID of the stack that is being associated with.
            status (Optional[int]): The ID of the status that is being associated with.
            tag (Optional[int]): The ID of the tag that is being associated with.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            user (Optional[int]): The ID of the user that is being associated with.
            uuid (Optional[str]): The UUID of the association.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer=answer,
            association_type=association_type,
            change_history=change_history,
            change_history_item=change_history_item,
            created_at=created_at,
            custom_field=custom_field,
            default=default,
            difficulty=difficulty,
            flashcard=flashcard,
            icon=icon,
            id=id,
            key=key,
            learning_session=learning_session,
            learning_session_item=learning_session_item,
            note=note,
            option=option,
            priority=priority,
            question=question,
            setting=setting,
            stack=stack,
            status=status,
            tag=tag,
            updated_at=updated_at,
            user=user,
            uuid=uuid,
        )

    def to_mutable(self) -> Optional["MutableAssociation"]:
        """
        Converts the ImmutableAssociation instance to a MutableAssociation instance.

        Returns:
            Optional[MutableAssociation]: The converted MutableAssociation instance, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableAssociation instance.
        """
        try:
            # Create a MutableAssociation instance from the current ImmutableAssociation instance
            return MutableAssociation(
                **self.to_dict(
                    exclude=[
                        # Exclude the logger from the dictionary representation
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class MutableAssociation(MutableBaseObject):
    """
    A mutable class representing an association between two entities.

    Attributes:
        association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
        answer (Optional[int]): The ID of the answer that is being associated with.
        change_history (Optional[int]): The ID of the change history that is being associated with.
        change_history_item (Optional[int]): The ID of the change history item that is being associated with.
        created_at (Optional[datetime]): The timestamp when the association was created.
        custom_field (Optional[int]): The ID of the custom field that is being associated with.
        default (Optional[int]): The ID of the default that is being associated with.
        difficulty (Optional[int]): The ID of the difficulty that is being associated with.
        flashcard (Optional[int]): The ID of the flashcard that is being associated with.
        icon (Optional[str]): The icon of the association..
        id (Optional[int]): The ID of the association.
        key (Optional[str]): The key of the association.
        learning_session (Optional[int]): The ID of the learning session that is being associated with.
        learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
        note (Optional[int]): The ID of the note that is being associated with.
        option (Optional[int]): The ID of the option that is being associated with.
        priority (Optional[int]): The ID of the priority that is being associated with.
        question (Optional[int]): The ID of the question that is being associated with.
        setting (Optional[int]): The ID of the setting that is being associated with.
        stack (Optional[int]): The ID of the stack that is being associated with.
        status (Optional[int]): The ID of the status that is being associated with.
        tag (Optional[int]): The ID of the tag that is being associated with.
        updated_at (Optional[datetime]): The timestamp when the association was last updated.
        user (Optional[int]): The ID of the user that is being associated with.
        uuid (Optional[str]): The UUID of the association.
    """

    def __init__(
        self,
        association_type: Literal[
            "ancestor",
            "dependant",
            "depends_on",
            "descendant",
            "tagged_with",
        ],
        answer: Optional[int] = None,
        change_history: Optional[int] = None,
        change_history_item: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field: Optional[int] = None,
        default: Optional[int] = None,
        difficulty: Optional[int] = None,
        flashcard: Optional[int] = None,
        icon: Optional[str] = "🔗",
        id: Optional[int] = None,
        key: Optional[str] = None,
        learning_session: Optional[int] = None,
        learning_session_item: Optional[int] = None,
        note: Optional[int] = None,
        option: Optional[int] = None,
        priority: Optional[int] = None,
        question: Optional[int] = None,
        setting: Optional[int] = None,
        stack: Optional[int] = None,
        status: Optional[int] = None,
        tag: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        user: Optional[int] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableAssociation class.

        Args:
            association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
            answer (Optional[int]): The ID of the answer that is being associated with.
            change_history (Optional[int]): The ID of the change history that is being associated with.
            change_history_item (Optional[int]): The ID of the change history item that is being associated with.
            created_at (Optional[datetime]): The timestamp when the association was created.
            custom_field (Optional[int]): The ID of the custom field that is being associated with.
            default (Optional[int]): The ID of the default that is being associated with.
            difficulty (Optional[int]): The ID of the difficulty that is being associated with.
            flashcard (Optional[int]): The ID of the flashcard that is being associated with.
            icon (Optional[str]): The icon of the association. Defaults to "🔗".
            id (Optional[int]): The ID of the association.
            key (Optional[str]): The key of the association.
            learning_session (Optional[int]): The ID of the learning session that is being associated with.
            learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
            note (Optional[int]): The ID of the note that is being associated with.
            option (Optional[int]): The ID of the option that is being associated with.
            priority (Optional[int]): The ID of the priority that is being associated with.
            question (Optional[int]): The ID of the question that is being associated with.
            setting (Optional[int]): The ID of the setting that is being associated with.
            stack (Optional[int]): The ID of the stack that is being associated with.
            status (Optional[int]): The ID of the status that is being associated with.
            tag (Optional[int]): The ID of the tag that is being associated with.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            user (Optional[int]): The ID of the user that is being associated with.
            uuid (Optional[str]): The UUID of the association.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer=answer,
            association_type=association_type,
            change_history=change_history,
            change_history_item=change_history_item,
            created_at=created_at,
            custom_field=custom_field,
            default=default,
            difficulty=difficulty,
            flashcard=flashcard,
            icon=icon,
            id=id,
            key=key,
            learning_session=learning_session,
            learning_session_item=learning_session_item,
            note=note,
            option=option,
            priority=priority,
            question=question,
            setting=setting,
            stack=stack,
            status=status,
            tag=tag,
            updated_at=updated_at,
            user=user,
            uuid=uuid,
        )

    def to_immutable(self) -> Optional["ImmutableAssociation"]:
        """
        Converts the MutableAssociation instance to an ImmutableAssociation instance.

        Returns:
            Optional[ImmutableAssociation]: The converted ImmutableAssociation instance, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to convert the MutableAssociation instance.
        """
        try:
            # Create a ImmutableAssociation instance from the current MutableAssociation instance
            return ImmutableAssociation(
                **self.to_dict(
                    exclude=[
                        # Exclude the logger from the dictionary representation
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AssociationConverter:
    """
    A converter class for transforming between AssociationModel and Association instances.

    This class provides methods to convert a AssociationModel instance to an Association instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the AssociationConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="AssociationConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "AssociationModel",
    ) -> Optional[ImmutableAssociation]:
        """
        Converts a given AssociationModel instance to an ImmutableAssociation instance.

        Args:
            model (AssociationModel): The AssociationModel instance to be converted.

        Returns:
            ImmutableAssociation: The converted ImmutableAssociation instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the AssociationModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableAssociation class from the dictionary representation of the AssociationModel instance
            return ImmutableAssociation(
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
        object: ImmutableAssociation,
    ) -> Optional["AssociationModel"]:
        """
        Converts a given ImmutableAssociation instance to a AssociationModel instance.

        Args:
            object (ImmutableAssociation): The ImmutableAssociation instance to be converted.

        Returns:
            AssociationModel: The converted AssociationModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableAssociation instance.
        """
        try:
            # Attempt to create and return a new instance of the AssociationModel class from the dictionary representation of the ImmutableAssociation instance
            return AssociationModel(
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


class AssociationFactory:
    """
    A factory class used to create instances of Association class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Final[Logger] = Logger.get_logger(name="AssociationFactory")

    @classmethod
    def create_association(
        cls,
        association_type: Literal[
            "ancestor",
            "dependant",
            "depends_on",
            "descendant",
            "tagged_with",
        ],
        answer: Optional[int] = None,
        change_history: Optional[int] = None,
        change_history_item: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field: Optional[int] = None,
        default: Optional[int] = None,
        difficulty: Optional[int] = None,
        flashcard: Optional[int] = None,
        icon: Optional[str] = "🔗",
        id: Optional[int] = None,
        key: Optional[str] = None,
        learning_session: Optional[int] = None,
        learning_session_item: Optional[int] = None,
        note: Optional[int] = None,
        option: Optional[int] = None,
        priority: Optional[int] = None,
        question: Optional[int] = None,
        setting: Optional[int] = None,
        stack: Optional[int] = None,
        status: Optional[int] = None,
        tag: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        user: Optional[int] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableAssociation]:
        """
        Creates and returns a new instance of ImmutableAssociation class.

        Args:
            association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
            answer (Optional[int]): The ID of the answer that is being associated with.
            change_history (Optional[int]): The ID of the change history that is being associated with.
            change_history_item (Optional[int]): The ID of the change history item that is being associated with.
            created_at (Optional[datetime]): The timestamp when the association was created.
            custom_field (Optional[int]): The ID of the custom field that is being associated with.
            default (Optional[int]): The ID of the default that is being associated with.
            difficulty (Optional[int]): The ID of the difficulty that is being associated with.
            flashcard (Optional[int]): The ID of the flashcard that is being associated with.
            icon (Optional[str]): The icon of the association. Defaults to "🔗".
            id (Optional[int]): The ID of the association.
            key (Optional[str]): The key of the association.
            learning_session (Optional[int]): The ID of the learning session that is being associated with.
            learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
            note (Optional[int]): The ID of the note that is being associated with.
            option (Optional[int]): The ID of the option that is being associated with.
            priority (Optional[int]): The ID of the priority that is being associated with.
            question (Optional[int]): The ID of the question that is being associated with.
            setting (Optional[int]): The ID of the setting that is being associated with.
            stack (Optional[int]): The ID of the stack that is being associated with.
            status (Optional[int]): The ID of the status that is being associated with.
            tag (Optional[int]): The ID of the tag that is being associated with.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            user (Optional[int]): The ID of the user that is being associated with.
            uuid (Optional[str]): The UUID of the association.

        Returns:
            Optional[ImmutableAssociation]: The created association object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the association.
        """
        try:
            # Attempt to create an d return an ImmutableAssociation object
            return ImmutableAssociation(
                answer=answer,
                association_type=association_type,
                change_history=change_history,
                change_history_item=change_history_item,
                created_at=created_at,
                custom_field=custom_field,
                default=default,
                difficulty=difficulty,
                flashcard=flashcard,
                icon=icon,
                id=id,
                key=key,
                learning_session=learning_session,
                learning_session_item=learning_session_item,
                note=note,
                option=option,
                priority=priority,
                question=question,
                setting=setting,
                stack=stack,
                status=status,
                tag=tag,
                updated_at=updated_at,
                user=user,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_association' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AssociationBuilder(BaseObjectBuilder):
    def __init__(self) -> None:
        """
        Initializes a new instance of the AssociationBuilder class.

        This class is a builder for the Association class. It is used to create instances of the Association class from a configuration dictionary.

        Args:
            None: No arguments are required.

        Returns:
            None: No value is returned.
        """
        super().__init__()

    @override
    def build(self) -> ImmutableAssociation:
        """
        Builds and returns an instance of ImmutableAssociation class using the configuration dictionary.

        This method attempts to create an instance of the ImmutableAssociation class using the configuration dictionary passed to the constructor.
        If an exception occurs while creating the instance, this method will log an error message and return None.

        Returns:
            ImmutableAssociation: The created association object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run 'build' method from '{self.__name__}'
        """
        try:
            # Attempt to create an association object using the configuration dictionary
            association: Optional[ImmutableAssociation] = (
                AssociationFactory.create_association(**self.configuration)
            )

            # Check if the association was successfully created
            if not association:
                # Log a warning message indicating that something has gone wrong
                self.logger.warning(
                    message=f"Failed to create association from configuration: {self.configuration}"
                )

                # Return None indicating that the association could not be created
                return None

            # Return the created association object
            return association
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__name__}': {e}"
            )
            return None

    def answer(
        self,
        value: int,
    ) -> Self:
        """
        Sets the answer for the association.

        Args:
            value (int): The ID of the answer to be set.

        Returns:
            Self: The builder object with the answer set.
        """
        self.configuration["answer"] = value
        return self

    def change_history(
        self,
        value: int,
    ) -> Self:
        """
        Sets the change history for the association.

        Args:
            value (int): The ID of the change history to be set.

        Returns:
            Self: The builder object with the change history set.
        """
        self.configuration["change_history"] = value
        return self

    def change_history_item(
        self,
        value: int,
    ) -> Self:
        """
        Sets the change history item for the association.

        Args:
            value (int): The ID of the change history item to be set.

        Returns:
            Self: The builder object with the change history item set.
        """
        self.configuration["change_history_item"] = value
        return self

    def comment(
        self,
        value: int,
    ) -> Self:
        """
        Sets the comment for the association.

        Args:
            value (int): The ID of the comment to be set.

        Returns:
            Self: The builder object with the comment set.
        """
        self.configuration["comment"] = value
        return self

    def custom_field(
        self,
        value: int,
    ) -> Self:
        """
        Sets the custom field for the association.

        Args:
            value (int): The ID of the custom field to be set.

        Returns:
            Self: The builder object with the custom field set.
        """
        self.configuration["custom_field"] = value
        return self

    def default(
        self,
        value: int,
    ) -> Self:
        """
        Sets the default value for the association.

        Args:
            value (int): The ID of the default value to be set.

        Returns:
            Self: The builder object with the default value set.
        """
        self.configuration["default"] = value
        return self

    def difficulty(
        self,
        value: int,
    ) -> Self:
        """
        Sets the difficulty for the association.

        Args:
            value (int): The ID of the difficulty to be set.

        Returns:
            Self: The builder object with the difficulty set.
        """
        self.configuration["difficulty"] = value
        return self

    def flashcard(
        self,
        value: int,
    ) -> Self:
        """
        Sets the flashcard for the association.

        Args:
            value (int): The ID of the flashcard to be set.

        Returns:
            Self: The builder object with the flashcard set.
        """
        self.configuration["flashcard"] = value
        return self

    def note(
        self,
        value: int,
    ) -> Self:
        """
        Sets the note for the association.

        Args:
            value (int): The ID of the note to be set.

        Returns:
            Self: The builder object with the note set.
        """
        self.configuration["note"] = value
        return self

    def priority(
        self,
        value: int,
    ) -> Self:
        """
        Sets the priority for the association.

        Args:
            value (int): The ID of the priority to be set.

        Returns:
            Self: The builder object with the priority set.
        """
        self.configuration["priority"] = value
        return self

    def question(
        self,
        value: int,
    ) -> Self:
        """
        Sets the question for the association.

        Args:
            value (int): The ID of the question to be set.

        Returns:
            Self: The builder object with the question set.
        """
        self.configuration["question"] = value
        return self

    def setting(
        self,
        value: int,
    ) -> Self:
        """
        Sets the setting for the association.

        Args:
            value (int): The ID of the setting to be set.

        Returns:
            Self: The builder object with the setting set.
        """
        self.configuration["setting"] = value
        return self

    def stack(
        self,
        value: int,
    ) -> Self:
        """
        Sets the stack for the association.

        Args:
            value (int): The ID of the stack to be set.

        Returns:
            Self: The builder object with the stack set.
        """
        self.configuration["stack"] = value
        return self

    def tag(
        self,
        value: int,
    ) -> Self:
        """
        Sets the tag for the association.

        Args:
            value (int): The ID of the tag to be set.

        Returns:
            Self: The builder object with the tag set.
        """
        self.configuration["tag"] = value
        return self

    def user(
        self,
        value: int,
    ) -> Self:
        """
        Sets the user for the association.

        Args:
            value (int): The ID of the user to be set.

        Returns:
            Self: The builder object with the user set.
        """
        self.configuration["user"] = value
        return self


class AssociationManager(BaseObjectManager):
    """
    A manager class for managing associations in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for associations.

    Attributes:
        cache: (List[Any]): The cache for storing associations.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["AssociationManager"] = None

    def __new__(cls) -> "AssociationManager":
        """
        Creates and returns a new instance of the AssociationManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            AssociationManager: The created or existing instance of AssociationManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(AssociationManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the FlashcardManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def associate(
        self,
        association_type: Literal[
            "ancestor",
            "dependant",
            "depends_on",
            "descendant",
            "tagged_with",
        ],
        answer: Optional[int] = None,
        change_history: Optional[int] = None,
        change_history_item: Optional[int] = None,
        custom_field: Optional[int] = None,
        default: Optional[int] = None,
        difficulty: Optional[int] = None,
        flashcard: Optional[int] = None,
        learning_session: Optional[int] = None,
        learning_session_item: Optional[int] = None,
        note: Optional[int] = None,
        option: Optional[int] = None,
        priority: Optional[int] = None,
        question: Optional[int] = None,
        setting: Optional[int] = None,
        stack: Optional[int] = None,
        status: Optional[int] = None,
        tag: Optional[int] = None,
        user: Optional[int] = None,
    ) -> bool:
        """
        Associates two objects in the database by creating an Association.

        Args:
            association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
            answer (Optional[int]): The ID of the answer that is being associated with.
            change_history (Optional[int]): The ID of the change history that is being associated with.
            change_history_item (Optional[int]): The ID of the change history item that is being associated with.
            custom_field (Optional[int]): The ID of the custom field that is being associated with.
            default (Optional[int]): The ID of the default that is being associated with.
            difficulty (Optional[int]): The ID of the difficulty that is being associated with.
            flashcard (Optional[int]): The ID of the flashcard that is being associated with.
            learning_session (Optional[int]): The ID of the learning session that is being associated with.
            learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
            note (Optional[int]): The ID of the note that is being associated with.
            option (Optional[int]): The ID of the option that is being associated with.
            priority (Optional[int]): The ID of the priority that is being associated with.
            question (Optional[int]): The ID of the question that is being associated with.
            setting (Optional[int]): The ID of the setting that is being associated with.
            stack (Optional[int]): The ID of the stack that is being associated with.
            status (Optional[int]): The ID of the status that is being associated with.
            tag (Optional[int]): The ID of the tag that is being associated with.
            user (Optional[int]): The ID of the user that is being associated with.

        Returns:
            bool: True if the association was created successfully, False otherwise.

        Raises:
            Exception: If an exception occurs while attempting to associate the objects.
        """
        try:
            # Create an Association object
            association: ImmutableAssociation = AssociationFactory.create_association(
                answer=answer,
                association_type=association_type,
                change_history=change_history,
                change_history_item=change_history_item,
                created_at=created_at,
                custom_field=custom_field,
                default=default,
                difficulty=difficulty,
                flashcard=flashcard,
                learning_session=learning_session,
                learning_session_item=learning_session_item,
                note=note,
                option=option,
                priority=priority,
                question=question,
                setting=setting,
                stack=stack,
                status=status,
                tag=tag,
                user=user,
            )

            # Create the association in the database
            self.create_association(association=association)

            # Return True indicating the association was created successfully
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'associate' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def count_associations(self) -> int:
        """
        Returns the number of associations in the database.

        Returns:
            int: The number of associations in the database.
        """
        try:
            # Count the number of associations in the database
            result: Any = asyncio.run(
                AssociationModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.ASSOCIATIONS};",
                )
            )

            # Return the number of associations in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_association(
        self,
        association: Union[ImmutableAssociation, MutableAssociation],
    ) -> Optional[ImmutableAssociation]:
        """
        Creates a new association in the database.

        Args:
            association (Union[ImmutableAssociation, MutableAssociation]): The association to be created.

        Returns:
            Optional[ImmutableAssociation]: The newly created immutable association if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the association.
        """
        try:
            # Check if the association object is immutable
            if isinstance(
                association,
                ImmutableAssociation,
            ):
                # If it is, convert it to a mutable association
                association = association.to_mutable()

            # Set the created_at timestamp of the association
            association.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the association
            association.key = f"ASSOCIATION_{self.count_associations() + 1}"

            # Set the updated_at timestamp of the association
            association.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the association
            association.uuid = Miscellaneous.get_uuid()

            # Convert the association object to a AssociationModel object
            model: AssociationModel = AssociationConverter.object_to_model(
                object=association
            )

            # Create a new association in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the association
                association.id = id

                # Convert the association to an immutable association
                association = ImmutableAssociation(
                    **association.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the association to the cache
                self.add_to_cache(
                    key=association.key,
                    value=association,
                )

                # Return the newly created immutable association
                return association

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a association ({association}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_association' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_association(
        self,
        association: Union[ImmutableAssociation, MutableAssociation],
    ) -> bool:
        """
        Deletes a association from the database.

        Args:
            association (Union[ImmutableAssociation, MutableAssociation]): The association to be deleted.

        Returns:
            bool: True if the association was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the association to an immutable association and delete the association from the database
            result: bool = asyncio.run(
                AssociationConverter.object_to_model(
                    object=Association(
                        **association.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the association was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_associations(self) -> Optional[List[ImmutableAssociation]]:
        """
        Returns a list of all associations in the database.

        Returns:
            Optional[List[ImmutableAssociation]]: A list of all associations in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_associations():
                # Return the list of immutable associations from the cache
                return self.get_cache_values()

            # Get all associations from the database
            models: List[AssociationModel] = asyncio.run(
                AssociationModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of AssociationModel objects to a list of ImmutableAssociation objects
            associations: List[ImmutableAssociation] = [
                ImmutableAssociation(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable associations
            for association in associations:
                if not self.is_key_in_cache(key=association.key):
                    # Add the immutable association to the cache
                    self.add_to_cache(
                        key=association.key,
                        value=association,
                    )
                else:
                    # Update the immutable association in the cache
                    self.update_in_cache(
                        key=association.key,
                        value=association,
                    )

            # Return the list of immutable associations
            return associations
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_association_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableAssociation]:
        """
        Retrieves a association by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableAssociation]: The association with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the association is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the association from the cache
                return self.get_value_from_cache(key=field)

            # Get the association with the given field and value from the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the association if it exists
            if model is not None:
                # Convert the AssociationModel object to an ImmutableAssociation object
                return ImmutableAssociation(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_association_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableAssociation]:
        """
        Returns a association with the given ID.

        Args:
            id (int): The ID of the association.

        Returns:
            Optional[ImmutableAssociation]: The association with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the association is already in the cache
            if self.is_key_in_cache(key=f"ASSOCIATION_{id}"):
                # Return the association from the cache
                return self.get_value_from_cache(key=f"ASSOCIATION_{id}")

            # Get the association with the given ID from the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the association if it exists
            if model is not None:
                # Convert the AssociationModel object to an ImmutableAssociation object
                return ImmutableAssociation(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_association_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableAssociation]:
        """
        Returns a association with the given UUID.

        Args:
            uuid (str): The UUID of the association.

        Returns:
            Optional[ImmutableAssociation]: The association with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the association is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the association from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the association with the given UUID from the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the association if it exists
            if model is not None:
                # Convert the AssociationModel object to an ImmutableAssociation object
                return ImmutableAssociation(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_associations(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableAssociation]]]:
        """
        Searches for associations in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the AssociationModel class.

        Returns:
            Optional[Union[List[ImmutableAssociation]]]: The found associations if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableAssociation]] = self.search_cache(**kwargs)

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for associations in the database
            models: Optional[List[AssociationModel]] = asyncio.run(
                AssociationModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found associations if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableAssociation(
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
                # Return None indicating that no associations were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_association(
        self,
        association: ImmutableAssociation,
    ) -> Optional[ImmutableAssociation]:
        """
        Updates a association with the given ID.

        Args:
            association (ImmutableAssociation): The association to update.

        Returns:
            Optional[ImmutableAssociation]: The updated association if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the association to an immutable association and update the association in the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationConverter.object_to_model(
                    object=ImmutableAssociation(
                        **association.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **association.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated association if it exists
            if model is not None:
                # Convert the AssociationModel object to an ImmutableAssociation object
                association = ImmutableAssociation(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the association to the cache
                self.update_in_cache(
                    key=association.key,
                    value=association,
                )

                # Return the updated association
                return association
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AssociationModel(ImmutableBaseModel):
    """
    Represents the structure of a association model.

    Attributes:
        association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
        answer (Optional[int]): The ID of the answer that is being associated with.
        change_history (Optional[int]): The ID of the change history that is being associated with.
        change_history_item (Optional[int]): The ID of the change history item that is being associated with.
        created_at (Optional[datetime]): The timestamp when the association was created.
        custom_field (Optional[int]): The ID of the custom field that is being associated with.
        default (Optional[int]): The ID of the default that is being associated with.
        difficulty (Optional[int]): The ID of the difficulty that is being associated with.
        flashcard (Optional[int]): The ID of the flashcard that is being associated with.
        icon (Optional[str]): The icon of the association. Defaults to "🔗".
        id (Optional[int]): The ID of the association.
        key (Optional[str]): The key of the association.
        learning_session (Optional[int]): The ID of the learning session that is being associated with.
        learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
        note (Optional[int]): The ID of the note that is being associated with.
        option (Optional[int]): The ID of the option that is being associated with.
        priority (Optional[int]): The ID of the priority that is being associated with.
        question (Optional[int]): The ID of the question that is being associated with.
        setting (Optional[int]): The ID of the setting that is being associated with.
        stack (Optional[int]): The ID of the stack that is being associated with.
        status (Optional[int]): The ID of the status that is being associated with.
        tag (Optional[int]): The ID of the tag that is being associated with.
        updated_at (Optional[datetime]): The timestamp when the association was last updated.
        user (Optional[int]): The ID of the user that is being associated with.
        uuid (Optional[str]): The UUID of the association.
    """

    table: Final[str] = Constants.ASSOCIATIONS

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

    answer: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.ANSWERS}(id)",
        index=False,
        name="answer",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    association_type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="association_type",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    change_history: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.CHANGE_HISTORIES}(id)",
        index=False,
        name="change_history",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    change_history_item: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.CHANGE_HISTORY_ITEMS}(id)",
        index=False,
        name="change_history_item",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
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

    custom_field: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.CUSTOM_FIELDS}(id)",
        index=False,
        name="custom_field",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    default: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.DEFAULTS}(id)",
        index=False,
        name="default",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    difficulty: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.DIFFICULTIES}(id)",
        index=False,
        name="difficulty",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    flashcard: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.FLASHCARDS}(id)",
        index=False,
        name="flashcard",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    icon: Field = Field(
        autoincrement=False,
        default="🔗",
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

    learning_session: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.LEARNING_SESSIONS}(id)",
        index=False,
        name="learning_session",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    learning_session_item: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.LEARNING_SESSION_ITEMS}(id)",
        index=False,
        name="learning_session_item",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    note: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.NOTES}(id)",
        index=False,
        name="note",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    option: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.OPTIONS}(id)",
        index=False,
        name="option",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    priority: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.PRIORITIES}(id)",
        index=False,
        name="priority",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    question: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.QUESTIONS}(id)",
        index=False,
        name="question",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    setting: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.SETTINGS}(id)",
        index=False,
        name="setting",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    stack: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.STACKS}(id)",
        index=False,
        name="stack",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    status: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.STACKS}(id)",
        index=False,
        name="status",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    tag: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.TAGS}(id)",
        index=False,
        name="tag",
        nullable=False,
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
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    user: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.USERS}(id)",
        index=False,
        name="user",
        nullable=False,
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
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
        answer: Optional[int] = None,
        association_type: Optional[
            Literal[
                "ancestor",
                "dependant",
                "depends_on",
                "descendant",
                "tagged_with",
            ]
        ] = None,
        change_history: Optional[int] = None,
        change_history_item: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field: Optional[int] = None,
        default: Optional[int] = None,
        difficulty: Optional[int] = None,
        flashcard: Optional[int] = None,
        icon: Optional[str] = "🔗",
        id: Optional[int] = None,
        key: Optional[str] = None,
        learning_session: Optional[int] = None,
        learning_session_item: Optional[int] = None,
        note: Optional[int] = None,
        option: Optional[int] = None,
        priority: Optional[int] = None,
        question: Optional[int] = None,
        setting: Optional[int] = None,
        stack: Optional[int] = None,
        status: Optional[int] = None,
        tag: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        user: Optional[int] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the AssociationModel class.

        Args:
            association_type (Literal["ancestor", "dependant", "depends_on", "descendant", "tagged_with"]): The type of the association.
            answer (Optional[int]): The ID of the answer that is being associated with.
            change_history (Optional[int]): The ID of the change history that is being associated with.
            change_history_item (Optional[int]): The ID of the change history item that is being associated with.
            created_at (Optional[datetime]): The timestamp when the association was created.
            custom_field (Optional[int]): The ID of the custom field that is being associated with.
            default (Optional[int]): The ID of the default that is being associated with.
            difficulty (Optional[int]): The ID of the difficulty that is being associated with.
            flashcard (Optional[int]): The ID of the flashcard that is being associated with.
            icon (Optional[str]): The icon of the association. Defaults to "🔗".
            id (Optional[int]): The ID of the association.
            key (Optional[str]): The key of the association.
            learning_session (Optional[int]): The ID of the learning session that is being associated with.
            learning_session_item (Optional[int]): The ID of the learning session item that is being associated with.
            note (Optional[int]): The ID of the note that is being associated with.
            option (Optional[int]): The ID of the option that is being associated with.
            priority (Optional[int]): The ID of the priority that is being associated with.
            question (Optional[int]): The ID of the question that is being associated with.
            setting (Optional[int]): The ID of the setting that is being associated with.
            stack (Optional[int]): The ID of the stack that is being associated with.
            status (Optional[int]): The ID of the status that is being associated with.
            tag (Optional[int]): The ID of the tag that is being associated with.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            user (Optional[int]): The ID of the user that is being associated with.
            uuid (Optional[str]): The UUID of the association.
        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer=answer,
            association_type=association_type,
            change_history=change_history,
            change_history_item=change_history_item,
            created_at=created_at,
            custom_field=custom_field,
            default=default,
            difficulty=difficulty,
            flashcard=flashcard,
            icon="🔗",
            id=id,
            key=key,
            learning_session=learning_session,
            learning_session_item=learning_session_item,
            note=note,
            option=option,
            priority=priority,
            question=question,
            setting=setting,
            stack=stack,
            status=status,
            table=Constants.ASSOCIATIONS,
            tag=tag,
            updated_at=updated_at,
            user=user,
            uuid=uuid,
        )
