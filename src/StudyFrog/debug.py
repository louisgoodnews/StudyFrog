"""
Author: lodego
Date: 2025-02-05
"""

import asyncio
import tkinter

from tkinter.constants import *
from typing import *

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

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.logger import Logger
from utils.model import ImmutableBaseModel


def debug() -> None:
    logger: Logger = Logger.get_logger(name="debug")

    logger.debug(message="Debugging...")

    def clear_database(logger: Logger) -> bool:
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

                # Log an info message
                logger.info(f"Dropped table '{model_class.__name__}'.")
            except Exception as e:
                # Log an error message indicating an exception has occurred
                logger.error(f"Failed to drop table '{model_class.__name__}': {str(e)}")

                return False

            try:
                # Create the table
                asyncio.run(model_class.create_table(database=Constants.DATABASE_PATH))

                # Log an info message
                logger.info(f"Created table '{model_class.__name__}'.")
            except Exception as e:
                # Log an error message indicating an exception has occurred
                logger.error(
                    f"Failed to create table '{model_class.__name__}': {str(e)}"
                )

                return False

        return True

    clear_database(logger=logger)

    root: tkinter.Tk = UIBuilder.get_tk()

    root.grid_columnconfigure(
        index=0,
        weight=1,
    )

    root.grid_rowconfigure(
        index=0,
        weight=1,
    )

    single_select: Dict[str, Any] = UIBuilder.get_single_select_field(
        label="Single Select: ",
        master=root,
        values=[
            "Option 1",
            "Option 2",
            "Option 3",
        ]
    )

    single_select["root"].grid(
        column=0,
        row=0,
        sticky=NSEW,
    )

    root.mainloop()


if __name__ == "__main__":
    debug()
