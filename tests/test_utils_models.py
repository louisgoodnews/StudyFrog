from __future__ import annotations

from studyfrog.models.factory import get_stack_model
from studyfrog.utils.models import (
    add_flashcard,
    count_flashcards,
    count_models,
    create_model,
    delete_model,
    get_flashcard,
    read_all_models,
    read_model,
    update_model,
)


def test_utils_models_crud_round_trip(tmp_path, monkeypatch) -> None:
    from studyfrog.utils import storage

    monkeypatch.setattr(storage, "DATA_DIR", tmp_path / "data")

    stack = get_stack_model(name="Physics")

    created_id = create_model(
        model=stack,
        force=True,
    )

    assert created_id == 0
    assert count_models(model_type="stack") == 1

    created_model = read_model(
        id_=created_id,
        model_type="stack",
    )

    assert created_model is not None
    assert created_model.name == "Physics"

    created_model.name = "Advanced Physics"
    updated_model = update_model(model=created_model)

    assert updated_model is not None
    assert updated_model.name == "Advanced Physics"

    all_models = read_all_models(model_type="stack")

    assert all_models is not None
    assert len(all_models) == 1
    assert all_models[0].name == "Advanced Physics"

    deleted_model = delete_model(
        id_=created_id,
        model_type="stack",
    )

    assert deleted_model is not None
    assert count_models(model_type="stack") == 0


def test_typed_shortcuts_delegate_to_generic_crud(tmp_path, monkeypatch) -> None:
    from studyfrog.models.factory import get_flashcard_model
    from studyfrog.utils import storage

    monkeypatch.setattr(storage, "DATA_DIR", tmp_path / "data")

    created_id = add_flashcard(
        model=get_flashcard_model(
            front="Question",
            back="Answer",
        ),
        force=True,
    )

    assert created_id == 0
    assert count_flashcards() == 1

    flashcard = get_flashcard(id_=created_id)

    assert flashcard is not None
    assert flashcard.front == "Question"
    assert flashcard.back == "Answer"
