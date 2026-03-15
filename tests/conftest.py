from __future__ import annotations

import sys

from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


@pytest.fixture(autouse=True)
def reset_dispatcher_state():
    from studyfrog.utils import dispatcher

    dispatcher.SUBSCRIBERS.clear()
    dispatcher.UUIDS.clear()

    yield

    dispatcher.SUBSCRIBERS.clear()
    dispatcher.UUIDS.clear()
