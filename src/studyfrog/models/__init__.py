from __future__ import annotations

# Import all exported variables and functions from individual modules

# Model classes
from studyfrog.models.models import (
    AnswerModel,
    AssociationModel,
    CustomfieldModel,
    DifficultyModel,
    FlashcardModel,
    ImageModel,
    Model,
    NoteModel,
    OptionModel,
    PriorityModel,
    QuestionModel,
    RehearsalRunItemModel,
    RehearsalRunModel,
    StackModel,
    SubjectModel,
    TagModel,
    TeacherModel,
    UserModel,
)

# Factory functions
from studyfrog.models.factory import (
    get_answer_model,
    get_association_model,
    get_customfield_model,
    get_difficulty_model,
    get_flashcard_model,
    get_image_model,
    get_model,
    get_note_model,
    get_option_model,
    get_priority_model,
    get_question_model,
    get_rehearsal_action_model,
    get_rehearsal_run_model,
    get_rehearsal_run_item_model,
    get_stack_model,
    get_subject_model,
    get_tag_model,
    get_teacher_model,
    get_user_model,
)

# Observable model classes
from studyfrog.models.observables import (
    AnswerObservableModel,
    DifficultyObservableModel,
    FlashcardObservableModel,
    NoteObservableModel,
    PriorityObservableModel,
    QuestionObservableModel,
    StackObservableModel,
    SubjectObservableModel,
    TagObservableModel,
    TeacherObservableModel,
    ObservableModel,  # TypeAlias
)

# Export all models, functions, and type aliases
__all__: list[str] = [
    # Model classes
    "AnswerModel",
    "AssociationModel",
    "CustomfieldModel",
    "DifficultyModel",
    "FlashcardModel",
    "ImageModel",
    "Model",
    "NoteModel",
    "OptionModel",
    "PriorityModel",
    "QuestionModel",
    "RehearsalRunItemModel",
    "RehearsalRunModel",
    "StackModel",
    "SubjectModel",
    "TagModel",
    "TeacherModel",
    "UserModel",
    # Factory functions
    "get_answer_model",
    "get_association_model",
    "get_customfield_model",
    "get_difficulty_model",
    "get_flashcard_model",
    "get_image_model",
    "get_model",
    "get_note_model",
    "get_option_model",
    "get_priority_model",
    "get_question_model",
    "get_rehearsal_action_model",
    "get_rehearsal_run_model",
    "get_rehearsal_run_item_model",
    "get_stack_model",
    "get_subject_model",
    "get_tag_model",
    "get_teacher_model",
    "get_user_model",
    # Observable model classes
    "AnswerObservableModel",
    "DifficultyObservableModel",
    "FlashcardObservableModel",
    "NoteObservableModel",
    "PriorityObservableModel",
    "QuestionObservableModel",
    "StackObservableModel",
    "SubjectObservableModel",
    "TagObservableModel",
    "TeacherObservableModel",
    "ObservableModel",  # TypeAlias
]
