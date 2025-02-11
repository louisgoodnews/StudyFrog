"""
Author: lodego
Date: 2025-02-09
"""

from typing import *

from core.answer import ImmutableAnswer
from core.association import Association
from core.change_history import ChangeHistory, ChangeHistoryItem
from core.custom_field import CustomField
from core.difficulty import Difficulty
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.option import ImmutableOption
from core.priority import Priority
from core.question import ImmutableQuestion
from core.stack import ImmutableStack
from core.tag import ImmutableTag
from core.user import ImmutableUser

from utils.logger import Logger


class UnifiedObjectManager:
    """
    A singleton manager class for registering and managing multiple manager instances.

    This class provides methods to create a single shared instance of the UnifiedObjectManager,
    initialize it with a logger and a dictionary for storing registered managers, and
    register manager instances using their class names as keys.

    Attributes:
        _shared_instance (Optional[UnifiedObjectManager]): The shared singleton instance of the class.
        logger (Logger): The logger instance associated with the UnifiedObjectManager.
        managers (Dict[str, Any]): The dictionary storing registered managers.
    """

    _shared_instance: Optional["UnifiedObjectManager"] = None

    def __new__(cls) -> "UnifiedObjectManager":
        """
        Creates and returns a new instance of the UnifiedObjectManager class.

        If the instance does not exist, creates a new one by calling the parent class constructor.
        If the instance already exists, returns the existing instance.

        Returns:
            UnifiedObjectManager: The created or existing instance of UnifiedObjectManager class.
        """

        # Check if a shared instance already exists
        if cls._shared_instance is None:
            # Create a new instance
            cls._shared_instance = super().__new__(cls)

            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the UnifiedObjectManager instance by creating a logger and an empty dictionary for storing registered managers.

        Returns:
            None
        """
        # Create a logger instance for the UnifiedObjectManager class
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize an empty dictionary for storing registered managers
        self.managers: Dict[str, Any] = {}

    def __getattr__(
        self,
        name: str,
    ) -> Any:
        """
        Automatically routes method calls to the appropriate manager.

        If `unified_manager.get_flashcard_by_id(1234)` is called,
        this method automatically forwards it to `FlashcardManager.get_flashcard_by_id(1234)`.
        """

        # Check if the method is available on the UnifiedObjectManager instance
        if not hasattr(
            self,
            name,
        ):
            # Iterate over the registered managers and check if the method is available
            for (
                manager_name,
                manager_instance,
            ) in self.managers.items():
                if hasattr(
                    manager_instance,
                    name,
                ):
                    return getattr(
                        manager_instance,
                        name,
                    )

        # If the method is available, return the result of calling it
        return getattr(
            self,
            name,
        )

    def register_manager(
        self,
        name: str,
        manager: Type[Any],
    ) -> None:
        """
        Registers a manager instance with the UnifiedObjectManager.

        Args:
            name (str): The name of the manager to be registered.
            manager (Type[Any]): The manager instance to be registered.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during registration.
        """
        try:
            # Add the manager to the managers dictionary using its class name as the key
            self.managers[name] = manager()

            # Log a success message indicating the manager has been registered
            self.logger.info(
                message=f"Registered manager '{name}' with class '{manager.__name__}'"
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register_manager' from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def run(
        self,
        manager: str,
        method: str,
        **kwargs,
    ) -> Any:
        """
        Dynamically calls a method on a specified manager.

        Args:
            manager (str): The name of the manager (e.g., 'flashcard').
            method (str): The name of the method to call (e.g., 'get_by_id').
            **kwargs: Additional parameters to pass to the method.

        Returns:
            Any: The result of the method execution.

        Raises:
            AttributeError: If the manager or method does not exist.
        """

        # Check if the specified manager exists
        if manager not in self.managers:
            raise AttributeError(
                f"Manager '{manager}' not found in UnifiedObjectManager."
            )

        # Get the manager instance from the dictionary
        manager_instance: Any = self.managers[manager]

        # Check if the specified method exists in the manager
        if not hasattr(
            manager_instance,
            method,
        ):
            raise AttributeError(f"Method '{method}' not found in manager '{manager}'.")

        # Dynamically call the method on the manager instance
        try:
            return getattr(
                manager_instance,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run '{manager}.{method}' from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e


class UnifiedObjectService:
    """
    A singleton service class for managing unified objects.

    This class provides a shared instance that listens to events and dispatches
    events to registered handlers.

    Attributes:
        logger (Logger): The logger instance for logging information and errors.
    """

    _shared_instance: Optional["UnifiedObjectService"] = None

    def __new__(
        cls,
        unified_manager: UnifiedObjectManager,
    ) -> "UnifiedObjectService":
        """
        Creates and returns a new instance of UnifiedObjectService.

        If the instance does not exist, it creates a new one by calling the parent class constructor
        and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            unified_manager (UnifiedObjectManager): The manager instance to be used by the service.

        Returns:
            UnifiedObjectService: The created or existing instance of UnifiedObjectService class.
        """

        # Check if a shared instance already exists
        if cls._shared_instance is None:
            # Create a new instance
            cls._shared_instance = super().__new__(cls)

            # Initialize the instance
            cls._shared_instance.init(unified_manager=unified_manager)

        # Return the shared instance
        return cls._shared_instance

    def init(self, unified_manager: UnifiedObjectManager) -> None:
        """
        Initializes the shared instance of UnifiedObjectService.

        Args:
            unified_manager (UnifiedObjectManager): The manager instance to be used by the service.

        Returns:
            None
        """

        # Get an instance of the Logger class and store it in an instance variable
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed unified_manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

    def on_request_answer_create(
        self,
        answer: ImmutableAnswer,
    ) -> Optional[ImmutableAnswer]:
        return self.unified_manager.create_answer(answer=answer)

    def on_request_answer_delete(
        self,
        answer: ImmutableAnswer,
    ) -> Optional[ImmutableAnswer]:
        return self.unified_manager.delete_answer(answer=answer)

    def on_request_answer_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableAnswer]]:
        return self.unified_manager.get_answer_by(**kwargs)

    def on_request_answer_update(
        self,
        answer: ImmutableAnswer,
    ) -> Optional[ImmutableAnswer]:
        return self.unified_manager.update_answer(answer=answer)

    def on_request_association_create(
        self,
        association: Association,
    ) -> Optional[Association]:
        return self.unified_manager.create_association(association=association)

    def on_request_association_delete(
        self,
        association: Association,
    ) -> Optional[Association]:
        return self.unified_manager.delete_association(association=association)

    def on_request_association_load(
        self,
        **kwargs,
    ) -> Optional[List[Association]]:
        return self.unified_manager.get_association_by(**kwargs)

    def on_request_association_update(
        self,
        association: Association,
    ) -> Optional[Association]:
        return self.unified_manager.update_association(association=association)

    def on_request_change_history_create(
        self,
        change_history: ChangeHistory,
    ) -> Optional[ChangeHistory]:
        return self.unified_manager.create_change_history(change_history=change_history)

    def on_request_change_history_delete(
        self,
        change_history: ChangeHistory,
    ) -> Optional[ChangeHistory]:
        return self.unified_manager.delete_change_history(change_history=change_history)

    def on_request_change_history_load(
        self,
        **kwargs,
    ) -> Optional[List[ChangeHistory]]:
        return self.unified_manager.get_change_history_by(**kwargs)

    def on_request_change_history_update(
        self,
        change_history: ChangeHistory,
    ) -> Optional[ChangeHistory]:
        return self.unified_manager.update_change_history(change_history=change_history)

    def on_request_change_history_item_create(
        self,
        change_history_item: ChangeHistoryItem,
    ) -> Optional[ChangeHistoryItem]:
        return self.unified_manager.create_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_change_history_item_delete(
        self,
        change_history_item: ChangeHistoryItem,
    ) -> Optional[ChangeHistoryItem]:
        return self.unified_manager.delete_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_change_history_item_load(
        self,
        **kwargs,
    ) -> Optional[List[ChangeHistoryItem]]:
        return self.unified_manager.get_change_history_item_by(**kwargs)

    def on_request_change_history_item_update(
        self,
        change_history_item: ChangeHistoryItem,
    ) -> Optional[ChangeHistoryItem]:
        return self.unified_manager.update_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_custom_field_create(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        return self.unified_manager.create_custom_field(custom_field=custom_field)

    def on_request_custom_field_delete(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        return self.unified_manager.delete_custom_field(custom_field=custom_field)

    def on_request_custom_field_load(
        self,
        **kwargs,
    ) -> Optional[List[CustomField]]:
        return self.unified_manager.get_custom_field_by(**kwargs)

    def on_request_custom_field_update(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        return self.unified_manager.update_custom_field(custom_field=custom_field)

    def on_request_difficulty_create(
        self,
        difficulty: Difficulty,
    ) -> Optional[Difficulty]:
        return self.unified_manager.create_difficulty(difficulty=difficulty)

    def on_request_difficulty_delete(
        self,
        difficulty: Difficulty,
    ) -> Optional[Difficulty]:
        return self.unified_manager.delete_difficulty(difficulty=difficulty)

    def on_request_difficulty_load(
        self,
        **kwargs,
    ) -> Optional[List[Difficulty]]:
        return self.unified_manager.get_difficulty_by(**kwargs)

    def on_request_difficulty_update(
        self,
        difficulty: Difficulty,
    ) -> Optional[Difficulty]:
        return self.unified_manager.update_difficulty(difficulty=difficulty)

    def on_request_flashcard_create(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        return self.unified_manager.create_flashcard(flashcard=flashcard)

    def on_request_flashcard_delete(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        return self.unified_manager.delete_flashcard(flashcard=flashcard)

    def on_request_flashcard_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableFlashcard]]:
        return self.unified_manager.get_flashcard_by(**kwargs)

    def on_request_flashcard_update(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        return self.unified_manager.update_flashcard(flashcard=flashcard)

    def on_request_option_create(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        return self.unified_manager.create_immutable_option(option=option)

    def on_request_option_delete(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        return self.unified_manager.delete_immutable_option(option=option)

    def on_request_option_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableOption]]:
        return self.unified_manager.get_immutable_option_by(**kwargs)

    def on_request_option_update(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        return self.unified_manager.update_immutable_option(option=option)

    def on_request_note_create(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        return self.unified_manager.create_immutable_note(note=note)

    def on_request_note_delete(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        return self.unified_manager.delete_immutable_note(note=note)

    def on_request_note_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableNote]]:
        return self.unified_manager.get_immutable_note_by(**kwargs)

    def on_request_note_update(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        return self.unified_manager.update_immutable_note(note=note)

    def on_request_priority_create(
        self,
        priority: Priority,
    ) -> Optional[Priority]:
        return self.unified_manager.create_priority(priority=priority)

    def on_request_priority_delete(
        self,
        priority: Priority,
    ) -> Optional[Priority]:
        return self.unified_manager.delete_priority(priority=priority)

    def on_request_priority_load(
        self,
        **kwargs,
    ) -> Optional[List[Priority]]:
        return self.unified_manager.get_priority_by(**kwargs)

    def on_request_priority_update(
        self,
        priority: Priority,
    ) -> Optional[Priority]:
        return self.unified_manager.update_priority(priority=priority)

    def on_request_question_create(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        return self.unified_manager.create_immutable_question(question=question)

    def on_request_question_delete(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        return self.unified_manager.delete_immutable_question(question=question)

    def on_request_question_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableQuestion]]:
        return self.unified_manager.get_immutable_question_by(**kwargs)

    def on_request_question_update(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        return self.unified_manager.update_immutable_question(question=question)

    def on_request_stack_create(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        return self.unified_manager.create_immutable_stack(stack=stack)

    def on_request_stack_delete(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        return self.unified_manager.delete_immutable_stack(stack=stack)

    def on_request_stack_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableStack]]:
        return self.unified_manager.get_immutable_stack_by(**kwargs)

    def on_request_stack_update(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        return self.unified_manager.update_immutable_stack(stack=stack)

    def on_request_tag_create(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        return self.unified_manager.create_immutable_tag(tag=tag)

    def on_request_tag_delete(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        return self.unified_manager.delete_immutable_tag(tag=tag)

    def on_request_tag_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableTag]]:
        return self.unified_manager.get_immutable_tag_by(**kwargs)

    def on_request_tag_update(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        return self.unified_manager.update_immutable_tag(tag=tag)

    def on_request_user_create(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        return self.unified_manager.create_immutable_user(user=user)

    def on_request_user_delete(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        return self.unified_manager.delete_immutable_user(user=user)

    def on_request_user_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableUser]]:
        return self.unified_manager.get_immutable_user_by(**kwargs)

    def on_request_user_update(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        return self.unified_manager.update_immutable_user(user=user)
