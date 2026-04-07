from __future__ import annotations

# Import all exported functions from individual GUI modules

# GUI framework functions
from studyfrog.gui.gui import (
    get_bottom_frame,
    get_center_frame,
    get_root,
    get_top_frame,
)

# Widget functions
from studyfrog.gui.widgets import (
    get_error_toast,
    get_info_toast,
    get_success_toast,
    get_warning_toast,
)

# Import all form functions
from studyfrog.gui.forms import (
    get_answer_choice_create_form,
    get_answer_open_ended_create_form,
    get_answer_true_false_create_form,
    get_flashcard_create_form,
    get_flashcard_edit_form,
    get_note_create_form,
    get_question_create_form,
    get_stack_create_form,
)

# Import all logic functions
from studyfrog.gui.logic import (
    on_cancel_button_click,
    on_create_button_click,
    on_stack_combobox_select,
    on_type_combobox_select,
    on_delete_button_click,
    on_edit_button_click,
    on_okay_button_click,
    on_save_button_click,
    on_start_button_click,
    end_rehearsal_run,
    on_easy_button_click,
    on_end_button_click,
    on_hard_button_click,
    on_medium_button_click,
    on_next_button_click,
    on_previous_button_click,
    start_rehearsal_run,
)

# Import all view functions
from studyfrog.gui.views import (
    get_answer_rehearsal_view,
    get_create_view,
    get_dashboard_view,
    get_delete_confirmation_view,
    get_edit_view,
    get_flashcard_rehearsal_view,
    set_flip_side,
    get_note_rehearsal_view,
    get_question_rehearsal_view,
    get_rehearsal_run_setup_view,
    get_rehearsal_run_view,
)

# Export all GUI functions
__all__: list[str] = [
    # GUI framework functions
    "get_bottom_frame",
    "get_center_frame",
    "get_root",
    "get_top_frame",
    # Widget functions
    "get_error_toast",
    "get_info_toast",
    "get_success_toast",
    "get_warning_toast",
    # Form functions
    "get_answer_choice_create_form",
    "get_answer_open_ended_create_form",
    "get_answer_true_false_create_form",
    "get_flashcard_create_form",
    "get_flashcard_edit_form",
    "get_note_create_form",
    "get_question_create_form",
    "get_stack_create_form",
    # Logic functions
    "on_cancel_button_click",
    "on_create_button_click",
    "on_stack_combobox_select",
    "on_type_combobox_select",
    "on_delete_button_click",
    "on_edit_button_click",
    "on_okay_button_click",
    "on_save_button_click",
    "on_start_button_click",
    "end_rehearsal_run",
    "on_easy_button_click",
    "on_end_button_click",
    "on_hard_button_click",
    "on_medium_button_click",
    "on_next_button_click",
    "on_previous_button_click",
    "start_rehearsal_run",
    # View functions
    "get_answer_rehearsal_view",
    "get_create_view",
    "get_dashboard_view",
    "get_delete_confirmation_view",
    "get_edit_view",
    "get_flashcard_rehearsal_view",
    "set_flip_side",
    "get_note_rehearsal_view",
    "get_question_rehearsal_view",
    "get_rehearsal_run_setup_view",
    "get_rehearsal_run_view",
]
