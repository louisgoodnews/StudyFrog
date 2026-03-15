from __future__ import annotations

from pathlib import Path

from studyfrog.models.factory import get_stack_model
from studyfrog.utils.files import read_file_json
from studyfrog.utils.storage import add_entry, get_entry


def test_add_entry_and_get_entry_round_trip(tmp_path, monkeypatch) -> None:
    from studyfrog.utils import storage

    data_dir = tmp_path / "data"
    monkeypatch.setattr(storage, "DATA_DIR", data_dir)

    stack = get_stack_model(name="Chemistry")

    entry_id = add_entry(
        model=stack,
        table_name="stacks",
    )

    saved_model = get_entry(
        id_=entry_id,
        table_name="stacks",
    )

    assert entry_id == 0
    assert saved_model is not None
    assert saved_model.name == "Chemistry"
    assert saved_model.type_ == "STACK"

    table_file = data_dir / "stacks.json"
    table_data = read_file_json(table_file)

    assert table_file.exists()
    assert table_data is not None
    assert table_data["entries"]["total"] == 1
    assert "0" in table_data["entries"]["entries"]
    assert table_data["entries"]["entries"]["0"]["identifiable"]["id"] == 0
    assert table_data["entries"]["entries"]["0"]["identifiable"]["key"] == "STACK_0"


def test_get_entry_returns_none_for_missing_id(tmp_path, monkeypatch) -> None:
    from studyfrog.utils import storage

    data_dir = tmp_path / "data"
    monkeypatch.setattr(storage, "DATA_DIR", data_dir)

    missing = get_entry(
        id_=999,
        table_name="stacks",
    )

    assert missing is None
