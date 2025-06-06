"""
Author: lodego
Date: 2025-04-29
"""

import asyncio

from typing import *

from core.learning.learning_session import (
    LearningSessionModel,
    LearningSessionActionModel,
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
from core.subject import SubjectModel
from core.tag import TagModel
from core.teacher import TeacherModel
from core.user import UserModel

from utils.constants import Constants
from utils.logger import Logger
from utils.model import ImmutableBaseModel


__all__: Final[List[str]] = ["upsert_database"]


def upsert_database() -> bool:
    """
    Upserts the database tables by iterating the set of model classes and
    upserting the tables.

    Returns:
        bool: True if the tables were successfully upserted, False otherwise.
    """

    # Get the logger
    logger: Logger = Logger.get_logger(name="upsert_database")

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
        LearningSessionActionModel,
        LearningSessionItemModel,
        NoteModel,
        OptionModel,
        PriorityModel,
        QuestionModel,
        SettingModel,
        StackModel,
        StatusModel,
        SubjectModel,
        TagModel,
        TeacherModel,
        UserModel,
    }

    # Iterate and upsert the tables
    for model_class in model_classes:

        try:
            # Upsert the table
            asyncio.run(model_class.upsert_table(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            logger.error(
                message=f"Failed to upsert table '{model_class.__name__}': {str(e)}"
            )

            # Return False indicating an exception has occurred
            return False

    # Return True indicating the tables were successfully upserted
    return True


if __name__ == "__main__":
    upsert_database()
