"""
Author: lodego
Date: 2025-02-05
"""

import asyncio

from typing import *

from core.learning.learning_session import (
    LearningSessionModel,
    LearningSessionItemModel,
)

from core.answer import AnswerModel
from core.association import AssociationModel
from core.change_history import ChangeHistoryModel, ChangeHistoryItemModel
from core.comment import CommentModel
from core.custom_field import CustomFieldModel
from core.default import DefaultModel
from core.difficulty import DifficultyModel
from core.flashcard import FlashcardModel
from core.note import NoteModel
from core.option import OptionModel
from core.priority import PriorityModel
from core.question import QuestionModel
from core.setting import SettingModel
from core.stack import StackModel
from core.status import StatusModel
from core.tag import TagModel
from core.user import UserModel

from utils.constants import Constants
from utils.logger import Logger
from utils.model import ImmutableBaseModel


def debug() -> None:
    """
    Debugging function.

    This function clears the database tables by iterating the set of model classes
    and dropping and creating the tables.
    """

    # Get the logger
    logger: Logger = Logger.get_logger(name="debug")

    # Log a debug message
    logger.debug(message="Debugging...")

    def clear_database() -> bool:
        """
        Clears the database tables by iterating the set of model classes and
        dropping and creating the tables.

        Returns:
            bool: True if the tables were successfully cleared, False otherwise.
        """

        # Set of model classes to clear
        model_classes: Set[Type[ImmutableBaseModel]] = {
            AnswerModel,
            AssociationModel,
            ChangeHistoryItemModel,
            ChangeHistoryModel,
            CommentModel,
            CustomFieldModel,
            DefaultModel,
            DifficultyModel,
            FlashcardModel,
            LearningSessionModel,
            LearningSessionItemModel,
            NoteModel,
            OptionModel,
            PriorityModel,
            QuestionModel,
            SettingModel,
            StackModel,
            StatusModel,
            TagModel,
            UserModel,
        }

        # Iterate an drop and create the tables
        for model_class in model_classes:
            try:
                # Drop the table
                asyncio.run(model_class.drop_table(database=Constants.DATABASE_PATH))
            except Exception as e:
                # Log an error message indicating an exception has occurred
                logger.error(
                    message=f"Failed to drop table '{model_class.__name__}': {str(e)}"
                )

                # Return False indicating an exception has occurred
                return False

            try:
                # Create the table
                asyncio.run(model_class.create_table(database=Constants.DATABASE_PATH))
            except Exception as e:
                # Log an error message indicating an exception has occurred
                logger.error(
                    message=f"Failed to create table '{model_class.__name__}': {str(e)}"
                )

                # Return False indicating an exception has occurred
                return False

        return True

    # Clear the database
    clear_database()

    # Log a debug message
    logger.debug(message="Debugging completed.")


if __name__ == "__main__":
    debug()
