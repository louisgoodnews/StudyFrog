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

__all__: List[str] = [
    "UnifiedObjectManager",
    "UnifiedObjectService",
]


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

    def init(
        self,
        unified_manager: UnifiedObjectManager,
    ) -> None:
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
        """
        Handles the 'request_answer_create' event and creates a new answer in the database.

        Args:
            answer (ImmutableAnswer): The answer to be created.

        Returns:
            Optional[ImmutableAnswer]: The created answer object if no exception occurs. Otherwise, None.
        """

        # Create and return the answer
        return self.unified_manager.create_answer(answer=answer)

    def on_request_answer_delete(
        self,
        answer: ImmutableAnswer,
    ) -> bool:
        """
        Handles the 'request_answer_delete' event and deletes an answer from the database.

        Args:
            answer (ImmutableAnswer): The answer to be deleted.

        Returns:
            bool: True if the answer was deleted successfully. False otherwise.
        """

        # Delete the answer and return a boolean indicating success or failure
        return self.unified_manager.delete_answer(answer=answer)

    def on_request_answer_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableAnswer]]:
        """
        Handles the 'request_answer_load' event and loads answers from the database.

        Args:
            **kwargs: The keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableAnswer]]: The loaded answers if no exception occurs. Otherwise, None.
        """

        # Load the answer and return it
        return self.unified_manager.get_answer_by(**kwargs)

    def on_request_answer_update(
        self,
        answer: ImmutableAnswer,
    ) -> Optional[ImmutableAnswer]:
        """
        Handles the 'request_answer_update' event and updates an answer in the database.

        Args:
            answer (ImmutableAnswer): The answer to be updated.

        Returns:
            Optional[ImmutableAnswer]: The updated immutable answer if no exception occurs. Otherwise, None.
        """

        # Update the answer and return it
        return self.unified_manager.update_answer(answer=answer)

    def on_request_association_create(
        self,
        association: Association,
    ) -> Optional[Association]:
        """
        Handles the 'request_association_create' event and creates a new association in the database.

        Args:
            association (Association): The association to be created.

        Returns:
            Optional[Association]: The created association object if no exception occurs. Otherwise, None.
        """

        # Create and return the association
        return self.unified_manager.create_association(association=association)

    def on_request_association_delete(
        self,
        association: Association,
    ) -> bool:
        """
        Handles the 'request_association_delete' event and deletes an association from the database.

        Args:
            association (Association): The association to be deleted.

        Returns:
            bool: True if the association was deleted successfully. False otherwise.
        """

        # Delete the association and return a boolean indicating success or failure
        return self.unified_manager.delete_association(association=association)

    def on_request_association_load(
        self,
        **kwargs,
    ) -> Optional[List[Association]]:
        """
        Handles the 'request_association_load' event and loads associations from the database.

        Args:
            **kwargs: Keyword arguments to be used for querying associations.

        Returns:
            Optional[List[Association]]: A list of loaded associations if no exception occurs. Otherwise, None.
        """

        # Retrieve associations using the provided keyword arguments
        return self.unified_manager.get_association_by(**kwargs)

    def on_request_association_update(
        self,
        association: Association,
    ) -> Optional[Association]:
        """
        Handles the 'request_association_update' event and updates an association in the database.

        Args:
            association (Association): The association to be updated.

        Returns:
            Optional[Association]: The updated association object if no exception occurs. Otherwise, None.
        """

        # Update and return the association
        return self.unified_manager.update_association(association=association)

    def on_request_change_history_create(
        self,
        change_history: ChangeHistory,
    ) -> Optional[ChangeHistory]:
        """
        Handles the 'request_change_history_create' event and creates a new change history in the database.

        Args:
            change_history (ChangeHistory): The change history to be created.

        Returns:
            Optional[ChangeHistory]: The created change history object if no exception occurs. Otherwise, None.
        """

        # Create and return the change history
        return self.unified_manager.create_change_history(change_history=change_history)

    def on_request_change_history_delete(
        self,
        change_history: ChangeHistory,
    ) -> bool:
        """
        Handles the 'request_change_history_delete' event and deletes a change history from the database.

        Args:
            change_history (ChangeHistory): The change history to be deleted.

        Returns:
            bool: True if the change history was deleted successfully. False otherwise.
        """

        # Delete the change history and return a boolean indicating success or failure
        return self.unified_manager.delete_change_history(change_history=change_history)

    def on_request_change_history_load(
        self,
        **kwargs,
    ) -> Optional[List[ChangeHistory]]:
        """
        Handles the 'request_change_history_load' event and loads change histories from the database.

        Args:
            **kwargs: Keyword arguments to be used for querying change histories.

        Returns:
            Optional[List[ChangeHistory]]: A list of loaded change histories if no exception occurs. Otherwise, None.
        """

        # Retrieve change histories using the provided keyword arguments
        return self.unified_manager.get_change_history_by(**kwargs)

    def on_request_change_history_update(
        self,
        change_history: ChangeHistory,
    ) -> Optional[ChangeHistory]:
        """
        Handles the 'request_change_history_update' event and updates a change history in the database.

        Args:
            change_history (ChangeHistory): The change history to be updated.

        Returns:
            Optional[ChangeHistory]: The updated change history object if no exception occurs. Otherwise, None.
        """

        # Update and return the change history
        return self.unified_manager.update_change_history(change_history=change_history)

    def on_request_change_history_item_create(
        self,
        change_history_item: ChangeHistoryItem,
    ) -> Optional[ChangeHistoryItem]:
        """
        Handles the 'request_change_history_item_create' event and creates a new change history item in the database.

        Args:
            change_history_item (ChangeHistoryItem): The change history item to be created.

        Returns:
            Optional[ChangeHistoryItem]: The created change history item object if no exception occurs. Otherwise, None.
        """

        # Create and return the change history item
        return self.unified_manager.create_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_change_history_item_delete(
        self,
        change_history_item: ChangeHistoryItem,
    ) -> bool:
        """
        Handles the 'request_change_history_item_delete' event and deletes a change history item from the database.

        Args:
            change_history_item (ChangeHistoryItem): The change history item to be deleted.

        Returns:
            bool: True if the change history item was deleted successfully. False otherwise.
        """

        # Delete the change history item and return a boolean indicating success or failure
        return self.unified_manager.delete_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_change_history_item_load(
        self,
        **kwargs,
    ) -> Optional[List[ChangeHistoryItem]]:
        """
        Handles the 'request_change_history_item_load' event and retrieves a list of change history items from the database.

        Args:
            **kwargs: The keyword arguments to be used for retrieving the change history items.

        Returns:
            Optional[List[ChangeHistoryItem]]: A list of loaded change history items if no exception occurs. Otherwise, None.
        """

        # Retrieve change history items using the provided keyword arguments
        return self.unified_manager.get_change_history_item_by(**kwargs)

    def on_request_change_history_item_update(
        self,
        change_history_item: ChangeHistoryItem,
    ) -> Optional[ChangeHistoryItem]:
        """
        Handles the 'request_change_history_item_update' event and updates a change history item in the database.

        Args:
            change_history_item (ChangeHistoryItem): The change history item to be updated.

        Returns:
            Optional[ChangeHistoryItem]: The updated change history item object if no exception occurs. Otherwise, None.
        """

        # Update and return the change history item
        return self.unified_manager.update_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_custom_field_create(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        """
        Handles the 'request_custom_field_create' event and creates a new custom field in the database.

        Args:
            custom_field (CustomField): The custom field to be created.

        Returns:
            Optional[CustomField]: The newly created custom field if no exception occurs. Otherwise, None.
        """

        # Create and return the custom field
        return self.unified_manager.create_custom_field(custom_field=custom_field)

    def on_request_custom_field_delete(
        self,
        custom_field: CustomField,
    ) -> bool:
        """
        Handles the 'request_custom_field_delete' event and deletes a custom field from the database.

        Args:
            custom_field (CustomField): The custom field to be deleted.

        Returns:
            bool: True if the custom field was deleted successfully. False otherwise.
        """

        # Delete and return the result of the deletion
        return self.unified_manager.delete_custom_field(custom_field=custom_field)

    def on_request_custom_field_load(
        self,
        **kwargs,
    ) -> Optional[List[CustomField]]:
        """
        Handles the 'request_custom_field_load' event and retrieves a list of custom fields from the database.

        Args:
            **kwargs: The keyword arguments to be used for retrieving the custom fields.

        Returns:
            Optional[List[CustomField]]: A list of loaded custom fields if no exception occurs. Otherwise, None.
        """

        # Retrieve custom fields using the provided keyword arguments
        return self.unified_manager.get_custom_field_by(**kwargs)

    def on_request_custom_field_update(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        """
        Handles the 'request_custom_field_update' event and updates a custom field in the database.

        Args:
            custom_field (CustomField): The custom field to be updated.

        Returns:
            Optional[CustomField]: The updated custom field object if no exception occurs. Otherwise, None.
        """

        # Update and return the custom field
        return self.unified_manager.update_custom_field(custom_field=custom_field)

    def on_request_difficulty_create(
        self,
        difficulty: Difficulty,
    ) -> Optional[Difficulty]:
        """
        Handles the 'request_difficulty_create' event and creates a new difficulty in the database.

        Args:
            difficulty (Difficulty): The difficulty to be created.

        Returns:
            Optional[Difficulty]: The newly created difficulty if no exception occurs. Otherwise, None.
        """

        # Create and return the difficulty
        return self.unified_manager.create_difficulty(difficulty=difficulty)

    def on_request_difficulty_delete(
        self,
        difficulty: Difficulty,
    ) -> bool:
        """
        Handles the 'request_difficulty_delete' event and deletes a difficulty from the database.

        Args:
            difficulty (Difficulty): The difficulty to be deleted.

        Returns:
            bool: True if the difficulty was deleted successfully. False otherwise.
        """

        # Delete and return the result of the deletion
        return self.unified_manager.delete_difficulty(difficulty=difficulty)

    def on_request_difficulty_load(
        self,
        **kwargs,
    ) -> Optional[List[Difficulty]]:
        """
        Handles the 'request_difficulty_load' event and loads difficulties from the database.

        Args:
            **kwargs: Keyword arguments to be passed to the database query.

        Returns:
            Optional[List[Difficulty]]: The loaded difficulties if no exception occurs. Otherwise, None.
        """

        # Load the difficulties from the database
        return self.unified_manager.get_difficulty_by(**kwargs)

    def on_request_difficulty_update(
        self,
        difficulty: Difficulty,
    ) -> Optional[Difficulty]:
        """
        Handles the 'request_difficulty_update' event and updates a difficulty in the database.

        Args:
            difficulty (Difficulty): The difficulty to be updated.

        Returns:
            Optional[Difficulty]: The updated difficulty if no exception occurs. Otherwise, None.
        """

        # Update and return the difficulty
        return self.unified_manager.update_difficulty(difficulty=difficulty)

    def on_request_flashcard_create(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        """
        Handles the 'request_flashcard_create' event and creates a new flashcard in the database.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be created.

        Returns:
            Optional[ImmutableFlashcard]: The newly created flashcard if no exception occurs. Otherwise, None.
        """

        # Create and return the flashcard
        return self.unified_manager.create_flashcard(flashcard=flashcard)

    def on_request_flashcard_delete(
        self,
        flashcard: ImmutableFlashcard,
    ) -> bool:
        """
        Handles the 'request_flashcard_delete' event and deletes a flashcard from the database.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be deleted.

        Returns:
            bool: True if the flashcard was deleted successfully. False otherwise.
        """

        # Delete the flashcard from the database and return the result of the deletion
        return self.unified_manager.delete_flashcard(flashcard=flashcard)

    def on_request_flashcard_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableFlashcard]]:
        """
        Handles the 'request_flashcard_load' event and retrieves a list of flashcards from the database.

        Args:
            **kwargs: The keyword arguments to be passed to the unified manager's get_flashcard_by method.

        Returns:
            Optional[List[ImmutableFlashcard]]: A list of flashcards retrieved from the database if no exception occurs. Otherwise, None.
        """

        # Load the flashcards from the database and return them
        return self.unified_manager.get_flashcard_by(**kwargs)

    def on_request_flashcard_update(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        """
        Handles the 'request_flashcard_update' event and updates a flashcard in the database.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be updated.

        Returns:
            Optional[ImmutableFlashcard]: The updated flashcard if no exception occurs. Otherwise, None.
        """

        # Update and return the flashcard
        return self.unified_manager.update_flashcard(flashcard=flashcard)

    def on_request_option_create(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        """
        Handles the 'request_option_create' event and creates a new option in the database.

        Args:
            option (ImmutableOption): The option to be created.

        Returns:
            Optional[ImmutableOption]: The newly created option if no exception occurs. Otherwise, None.
        """

        # Create and return the option
        return self.unified_manager.create_option(option=option)

    def on_request_option_delete(
        self,
        option: ImmutableOption,
    ) -> bool:
        """
        Handles the 'request_option_delete' event and deletes an option from the database.

        Args:
            option (ImmutableOption): The option to be deleted.

        Returns:
            bool: True if the option was deleted successfully. False otherwise.
        """

        # Delete the option from the database and return the result of the deletion
        return self.unified_manager.delete_option(option=option)

    def on_request_option_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableOption]]:
        """
        Handles the 'request_option_load' event and loads options from the database.

        Args:
            **kwargs: Keyword arguments for filtering the options.

        Returns:
            Optional[List[ImmutableOption]]: A list of immutable options if found. None otherwise.
        """
        return self.unified_manager.get_option_by(**kwargs)

    def on_request_option_update(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        """
        Handles the 'request_option_update' event and updates an option in the database.

        Args:
            option (ImmutableOption): The option to be updated.

        Returns:
            Optional[ImmutableOption]: The updated immutable option if no exception occurs. Otherwise, None.
        """

        # Update the option in the database and return the updated option
        return self.unified_manager.update_option(option=option)

    def on_request_note_create(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_create' event and creates a new note in the database.

        Args:
            note (ImmutableNote): The note to be created.

        Returns:
            Optional[ImmutableNote]: The created immutable note if no exception occurs. Otherwise, None.
        """

        # Create a new note in the database and return the created immutable note
        return self.unified_manager.create_note(note=note)

    def on_request_note_delete(
        self,
        note: ImmutableNote,
    ) -> bool:
        """
        Handles the 'request_note_delete' event and deletes a note from the database.

        Args:
            note (ImmutableNote): The note to be deleted.

        Returns:
            bool: True if the note was deleted successfully. False otherwise.
        """

        # Delete the note from the database and return the result of the deletion
        return self.unified_manager.delete_note(note=note)

    def on_request_note_load(
        self,
        **kwargs,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_load' event and loads a note from the database.

        Args:
            **kwargs: The keyword arguments to be used for querying the note.

        Returns:
            Optional[ImmutableNote]: The loaded immutable note if no exception occurs. Otherwise, None.
        """

        # Load the note from the database and return the loaded immutable note
        return self.unified_manager.get_note_by(**kwargs)

    def on_request_note_update(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_update' event and updates a note in the database.

        Args:
            note (ImmutableNote): The note to be updated.

        Returns:
            Optional[ImmutableNote]: The updated immutable note if no exception occurs. Otherwise, None.
        """

        # Update the note in the database and return the updated note
        return self.unified_manager.update_note(note=note)

    def on_request_priority_create(
        self,
        priority: Priority,
    ) -> Optional[Priority]:
        """
        Handles the 'request_priority_create' event and creates a new priority in the database.

        Args:
            priority (Priority): The priority to be created.

        Returns:
            Optional[Priority]: The created priority object if no exception occurs. Otherwise, None.
        """

        # Create and return the priority
        return self.unified_manager.create_priority(priority=priority)

    def on_request_priority_delete(
        self,
        priority: Priority,
    ) -> bool:
        """
        Handles the 'request_priority_delete' event and deletes a priority from the database.

        Args:
            priority (Priority): The priority to be deleted.

        Returns:
            bool: True if no exception occurs. Otherwise, False.
        """

        # Delete the priority from the database and return the result
        return self.unified_manager.delete_priority(priority=priority)

    def on_request_priority_load(
        self,
        **kwargs,
    ) -> Optional[List[Priority]]:
        """
        Handles the 'request_priority_load' event and loads a priority from the database.

        Args:
            **kwargs: The keyword arguments to be used for querying the priority.

        Returns:
            Optional[List[Priority]]: The loaded immutable priority if no exception occurs. Otherwise, None.
        """

        # Load the priority from the database and return the loaded immutable priority
        return self.unified_manager.get_priority_by(**kwargs)

    def on_request_priority_update(
        self,
        priority: Priority,
    ) -> Optional[Priority]:
        """
        Handles the 'request_priority_update' event and updates a priority in the database.

        Args:
            priority (Priority): The priority to be updated.

        Returns:
            Optional[Priority]: The updated priority object if no exception occurs. Otherwise, None.
        """

        # Update the priority in the database and return the updated priority
        return self.unified_manager.update_priority(priority=priority)

    def on_request_question_create(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        """
        Handles the 'request_question_create' event and creates a new question in the database.

        Args:
            question (ImmutableQuestion): The question to be created.

        Returns:
            Optional[ImmutableQuestion]: The created immutable question if no exception occurs. Otherwise, None.
        """

        # Create and return the question
        return self.unified_manager.create_question(question=question)

    def on_request_question_delete(
        self,
        question: ImmutableQuestion,
    ) -> bool:
        """
        Handles the 'request_question_delete' event and deletes a question from the database.

        Args:
            question (ImmutableQuestion): The question to be deleted.

        Returns:
            bool: True if the question was deleted successfully. False otherwise.
        """

        # Delete the question from the database and return the result of the deletion
        return self.unified_manager.delete_question(question=question)

    def on_request_question_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableQuestion]]:
        """
        Handles the 'request_question_load' event and loads questions from the database.

        Args:
            **kwargs: The keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableQuestion]]: A list of loaded questions if no exception occurs. Otherwise, None.
        """

        # Load the questions from the database using the provided keyword arguments
        return self.unified_manager.get_question_by(**kwargs)

    def on_request_question_update(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        """
        Handles the 'request_question_update' event and updates a question in the database.

        Args:
            question (ImmutableQuestion): The question to be updated.

        Returns:
            Optional[ImmutableQuestion]: The updated immutable question if no exception occurs. Otherwise, None.
        """

        # Update the question in the database and return the result of the update
        return self.unified_manager.update_question(question=question)

    def on_request_stack_create(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        """
        Handles the 'request_stack_create' event and creates a new stack in the database.

        Args:
            stack (ImmutableStack): The stack to be created.

        Returns:
            Optional[ImmutableStack]: The created immutable stack if no exception occurs. Otherwise, None.
        """

        # Create a new stack in the database and return the created stack
        return self.unified_manager.create_stack(stack=stack)

    def on_request_stack_delete(
        self,
        stack: ImmutableStack,
    ) -> bool:
        """
        Handles the 'request_stack_delete' event and deletes a stack from the database.

        Args:
            stack (ImmutableStack): The stack to be deleted.

        Returns:
            bool: True if the stack is deleted successfully, False otherwise.
        """

        # Delete the stack from the database and return the result of the deletion
        return self.unified_manager.delete_stack(stack=stack)

    def on_request_stack_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableStack]]:
        """
        Handles the 'request_stack_load' event and loads stacks from the database.

        Args:
            **kwargs: The keyword arguments to be used for querying stacks.

        Returns:
            Optional[List[ImmutableStack]]: A list of loaded stacks if no exception occurs. Otherwise, None.
        """

        # Load stacks using the provided keyword arguments and return them
        return self.unified_manager.get_stack_by(**kwargs)

    def on_request_stack_update(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        """
        Handles the 'request_stack_update' event and updates a stack in the database.

        Args:
            stack (ImmutableStack): The stack to be updated.

        Returns:
            Optional[ImmutableStack]: The updated immutable stack if no exception occurs. Otherwise, None.
        """

        # Update the stack in the database and return the result of the update
        return self.unified_manager.update_stack(stack=stack)

    def on_request_tag_create(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        """
        Handles the 'request_tag_create' event and creates a new tag in the database.

        Args:
            tag (ImmutableTag): The tag to be created.

        Returns:
            Optional[ImmutableTag]: The created immutable tag if no exception occurs. Otherwise, None.
        """

        # Create the tag in the database and return the result of the creation
        return self.unified_manager.create_tag(tag=tag)

    def on_request_tag_delete(
        self,
        tag: ImmutableTag,
    ) -> bool:
        """
        Handles the 'request_tag_delete' event and deletes a tag from the database.

        Args:
            tag (ImmutableTag): The tag to be deleted.

        Returns:
            bool: True if the tag was deleted successfully. False otherwise.
        """

        # Delete the tag in the database and return the result of the deletion
        return self.unified_manager.delete_tag(tag=tag)

    def on_request_tag_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableTag]]:
        """
        Handles the 'request_tag_load' event and loads tags from the database.

        Args:
            **kwargs: The keyword arguments to be used for querying tags.

        Returns:
            Optional[List[ImmutableTag]]: A list of loaded tags if no exception occurs. Otherwise, None.
        """

        # Retrieve tags using the provided keyword arguments
        return self.unified_manager.get_tag_by(**kwargs)

    def on_request_tag_update(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        """
        Handles the 'request_tag_update' event and updates a tag in the database.

        Args:
            tag (ImmutableTag): The tag to be updated.

        Returns:
            Optional[ImmutableTag]: The updated immutable tag if no exception occurs. Otherwise, None.
        """

        # Update the tag in the database and return the result of the update
        return self.unified_manager.update_tag(tag=tag)

    def on_request_user_create(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        """
        Handles the 'request_user_create' event and creates a new user in the database.

        Args:
            user (ImmutableUser): The user to be created.

        Returns:
            Optional[ImmutableUser]: The newly created immutable user if no exception occurs. Otherwise, None.
        """

        # Create the user in the database and return the result of the creation
        return self.unified_manager.create_user(user=user)

    def on_request_user_delete(
        self,
        user: ImmutableUser,
    ) -> bool:
        """
        Handles the 'request_user_delete' event and deletes a user from the database.

        Args:
            user (ImmutableUser): The user to be deleted.

        Returns:
            bool: True if the user was deleted successfully. False otherwise.
        """

        # Delete the user in the database and return the result of the deletion
        return self.unified_manager.delete_user(user=user)

    def on_request_user_load(
        self,
        **kwargs,
    ) -> Optional[List[ImmutableUser]]:
        """
        Handles the 'request_user_load' event and loads users from the database.

        Args:
            **kwargs: The keyword arguments to be used for querying users.

        Returns:
            Optional[List[ImmutableUser]]: A list of loaded users if no exception occurs. Otherwise, None.
        """

        # Retrieve users using the provided keyword arguments
        return self.unified_manager.get_user_by(**kwargs)

    def on_request_user_update(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        """
        Handles the 'request_user_update' event and updates a user in the database.

        Args:
            user (ImmutableUser): The user to be updated.

        Returns:
            Optional[ImmutableUser]: The updated immutable user if no exception occurs. Otherwise, None.
        """

        # Update the user in the database and return the result of the update
        return self.unified_manager.update_user(user=user)
