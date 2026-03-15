from __future__ import annotations

from datetime import date, datetime

from studyfrog.models.factory import get_flashcard_model, get_model, get_stack_model
from studyfrog.models.models import FlashcardModel, StackModel


def test_get_stack_model_creates_typed_model() -> None:
    model = get_stack_model(name="Biology")

    assert isinstance(model, StackModel)
    assert model.name == "Biology"
    assert model.type_ == "STACK"
    assert model.id is None
    assert model.key is None


def test_get_model_converts_string_dates_and_uuid_capable_fields() -> None:
    created_at = "2026-01-01T10:00:00"
    created_on = "2026-01-01"

    model = get_model(
        type_="flashcard",
        back="Answer",
        front="Question",
        created_at=created_at,
        created_on=created_on,
    )

    assert isinstance(model, FlashcardModel)
    assert isinstance(model.created_at, datetime)
    assert isinstance(model.created_on, date)
    assert model.front == "Question"
    assert model.back == "Answer"


def test_invalid_model_type_returns_none() -> None:
    assert get_model(type_="not_a_model") is None
