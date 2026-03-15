from __future__ import annotations

from studyfrog.utils.directories import ensure_directory, is_directory_empty, remove_directory
from studyfrog.utils.files import (
    does_file_exist,
    does_file_have_content,
    ensure_file,
    read_file_json,
    read_file_text,
    write_file_json,
    write_file_text,
)


def test_directory_helpers_round_trip(tmp_path) -> None:
    directory = tmp_path / "nested" / "folder"

    assert ensure_directory(directory) is True
    assert directory.exists()
    assert is_directory_empty(directory) is True

    (directory / "child.txt").write_text("content", encoding="utf-8")

    assert is_directory_empty(directory) is False
    assert remove_directory(directory) is True
    assert directory.exists() is False


def test_file_helpers_round_trip(tmp_path) -> None:
    text_file = tmp_path / "notes" / "sample.txt"
    json_file = tmp_path / "notes" / "sample.json"

    assert ensure_file(text_file) is True
    assert does_file_exist(text_file) is True
    assert does_file_have_content(text_file) is False

    assert write_file_text("hello", text_file) is True
    assert read_file_text(text_file) == "hello"
    assert does_file_have_content(text_file) is True

    payload = {"name": "StudyFrog", "kind": "test"}
    assert write_file_json(payload, json_file) is True
    assert read_file_json(json_file) == payload
