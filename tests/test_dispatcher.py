from __future__ import annotations

from studyfrog.utils.dispatcher import dispatch, subscribe, unsubscribe


def test_dispatch_calls_subscribers_in_priority_order() -> None:
    calls: list[str] = []

    def low_priority_handler() -> str:
        calls.append("low")
        return "low"

    def high_priority_handler() -> str:
        calls.append("high")
        return "high"

    subscribe(
        event="test_event",
        function=low_priority_handler,
        namespace="test",
        priority=10,
    )
    subscribe(
        event="test_event",
        function=high_priority_handler,
        namespace="test",
        priority=100,
    )

    result = dispatch(event="test_event", namespace="test")

    assert calls == ["high", "low"]
    assert result["event"] == "TEST_EVENT"
    assert result["namespace"] == "TEST"
    assert result["high_priority_handler"][0]["result"] == "high"
    assert result["low_priority_handler"][0]["result"] == "low"


def test_non_persistent_subscribers_are_removed_after_dispatch() -> None:
    def handler() -> str:
        return "done"

    subscription_id = subscribe(
        event="ephemeral",
        function=handler,
        namespace="test",
        persistent=False,
    )

    dispatch(event="ephemeral", namespace="test")

    assert unsubscribe(subscription_id) is False


def test_dispatch_returns_warning_for_unknown_event() -> None:
    result = dispatch(event="missing", namespace="test")

    assert result["status"] == "WARNING"
    assert "not found" in result["message"]
