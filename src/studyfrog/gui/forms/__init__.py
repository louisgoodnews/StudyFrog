from __future__ import annotations

# Import all exported functions from individual form modules

# Answer create form functions
from studyfrog.gui.forms.answer_create_form import (
    get_answer_choice_create_form,
    get_answer_open_ended_create_form,
    get_answer_true_false_create_form,
)

# Flashcard create form functions
from studyfrog.gui.forms.flashcard_create_form import (
    get_flashcard_create_form,
)

# Flashcard edit form functions
from studyfrog.gui.forms.flashcard_edit_form import (
    get_flashcard_edit_form,
)

# Note create form functions
from studyfrog.gui.forms.note_create_form import (
    get_note_create_form,
)

# Question create form functions
from studyfrog.gui.forms.question_create_form import (
    get_question_create_form,
)

# Stack create form functions
from studyfrog.gui.forms.stack_create_form import (
    get_stack_create_form,
)

# Export all form functions
__all__: list[str] = [
    # Answer create form functions
    "get_answer_choice_create_form",
    "get_answer_open_ended_create_form",
    "get_answer_true_false_create_form",
    # Flashcard create form functions
    "get_flashcard_create_form",
    # Flashcard edit form functions
    "get_flashcard_edit_form",
    # Note create form functions
    "get_note_create_form",
    # Question create form functions
    "get_question_create_form",
    # Stack create form functions
    "get_stack_create_form",
]
