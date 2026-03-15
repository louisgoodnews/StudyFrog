from __future__ import annotations

import importlib

import pytest


@pytest.mark.parametrize(
    "module_name",
    [
        "studyfrog.constants.common",
        "studyfrog.constants.defaults",
        "studyfrog.models.factory",
        "studyfrog.models.models",
        "studyfrog.utils.common",
        "studyfrog.utils.directories",
        "studyfrog.utils.dispatcher",
        "studyfrog.utils.files",
        "studyfrog.utils.logging",
        "studyfrog.utils.storage",
    ],
)
def test_core_modules_import(module_name: str) -> None:
    module = importlib.import_module(module_name)

    assert module is not None
