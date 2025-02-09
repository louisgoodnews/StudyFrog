"""
Author: lodego
Date: 2025-02-05
"""

import asyncio

from core.answer import AnswerModel
from core.association import AssociationModel
from core.change_history import ChangeHistoryModel, ChangeHistoryItemModel
from core.default import DefaultModel
from core.difficulty import DifficultyModel
from core.flashcard import FlashcardModel
from core.note import NoteModel
from core.priority import PriorityModel
from core.question import QuestionModel
from core.setting import SettingModel
from core.stack import StackModel
from core.tag import TagModel
from core.user import UserModel

from utils.constants import Constants
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


def debug() -> None:
    logger: Logger = Logger.get_logger(name="debug")

    # Iterate an drop and create the tables
    for model_class in [
        AnswerModel,
        AssociationModel,
        ChangeHistoryItemModel,
        ChangeHistoryModel,
        DefaultModel,
        DifficultyModel,
        FlashcardModel,
        NoteModel,
        PriorityModel,
        QuestionModel,
        SettingModel,
        StackModel,
        TagModel,
        UserModel,
    ]:
        # Drop the table
        asyncio.run(model_class.drop_table(database=Constants.DATABASE_PATH))

        # Create the table
        asyncio.run(model_class.create_table(database=Constants.DATABASE_PATH))


if __name__ == "__main__":
    debug()
