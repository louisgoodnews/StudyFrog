from __future__ import annotations

# Import all exported functions from individual view modules

# Answer rehearsal view functions
from studyfrog.gui.views.answer_rehearsal_view import (
    get_answer_rehearsal_view,
)

# Create view functions
from studyfrog.gui.views.create_view import (
    get_create_view,
)

# Dashboard view functions
from studyfrog.gui.views.dashboard_view import (
    get_dashboard_view,
)

# Delete confirmation view functions
from studyfrog.gui.views.delete_confirmation_view import (
    get_delete_confirmation_view,
)

# Edit view functions
from studyfrog.gui.views.edit_view import (
    get_edit_view,
)

# Flashcard rehearsal view functions
from studyfrog.gui.views.flashcard_rehearsal_view import (
    get_flashcard_rehearsal_view,
    set_flip_side,
)

# Note rehearsal view functions
from studyfrog.gui.views.note_rehearsal_view import (
    get_note_rehearsal_view,
)

# Question rehearsal view functions
from studyfrog.gui.views.question_rehearsal_view import (
    get_question_rehearsal_view,
)

# Rehearsal run result view functions (empty, included for completeness)
from studyfrog.gui.views.rehearsal_run_result_view import *

# Rehearsal run setup view functions
from studyfrog.gui.views.rehearsal_run_setup_view import (
    get_rehearsal_run_setup_view,
)

# Rehearsal run view functions
from studyfrog.gui.views.rehearsal_run_view import (
    get_rehearsal_run_view,
)

# Export all view functions
__all__: list[str] = [
    # Answer rehearsal view functions
    "get_answer_rehearsal_view",
    # Create view functions
    "get_create_view",
    # Dashboard view functions
    "get_dashboard_view",
    # Delete confirmation view functions
    "get_delete_confirmation_view",
    # Edit view functions
    "get_edit_view",
    # Flashcard rehearsal view functions
    "get_flashcard_rehearsal_view",
    "set_flip_side",
    # Note rehearsal view functions
    "get_note_rehearsal_view",
    # Question rehearsal view functions
    "get_question_rehearsal_view",
    # Rehearsal run setup view functions
    "get_rehearsal_run_setup_view",
    # Rehearsal run view functions
    "get_rehearsal_run_view",
]
