"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from typing import Any, Callable, Final, Optional

from constants.common import GLOBAL
from utils.common import get_now, generate_uuid4_str
from utils.logging import log_error, log_info, log_warning


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "bulk_dispatch",
    "bulk_subscribe",
    "bulk_unsubscribe",
    "dispatch",
    "subscribe",
    "unsubscribe",
]


# ---------- Constants ---------- #

SUBSCRIBERS: Final[dict[str, dict[str, dict[str, Any]]]] = {}

UUIDS: Final[dict[str, dict[str, str]]] = {}


# ---------- Functions ---------- #


def bulk_dispatch(
    *args: tuple[Any],
    events: list[str],
    namespaces: list[str],
    **kwargs: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Dispatches the given events in the given namespaces.

    Args:
        *args (tuple[Any]): The arguments to pass to the events.
        events (list[str]): The list of events to dispatch.
        namespaces (list[str]): The list of namespaces to dispatch to.
        **kwargs (dict[str, Any]): The keyword arguments to pass to the events.

    Returns:
        list[dict[str, Any]]: The results of the dispatch.
    """

    results: list[dict[str, Any]] = []

    for (
        event,
        namespace,
    ) in zip(
        events,
        namespaces,
        strict=True,
    ):
        results.append(
            dispatch(
                event=event,
                namespace=namespace,
                *args,
                **kwargs,
            )
        )

    return results


def bulk_subscribe(
    events: list[str],
    functions: list[Callable[[..., Any], Any]],
    namespaces: list[str],
    priorities: list[int],
    persistents: list[bool],
) -> list[str]:
    """
    Subscribes functions to events based on namespaces.

    Args:
        events (list[str]): The list of events to subscribe to.
        functions (list[Callable[[..., Any], Any]]): The list of functions to subscribe.
        namespaces (list[str]): The list of namespaces to subscribe to.
        priorities (list[int]): The list of priorities to subscribe to.
        persistents (list[bool]): The list of persistents to subscribe to.

    Returns:
        list[str]

    Raises:
        ValueError: If the lists are not of the same length.
    """

    result: list[str] = []

    for (
        event,
        function,
        namespace,
        priority,
        persistent,
    ) in zip(
        events,
        functions,
        namespaces,
        priorities,
        persistents,
        strict=True,
    ):
        result.append(
            subscribe(
                event=event,
                function=function,
                namespace=namespace,
                priority=priority,
                persistent=persistent,
            )
        )

    return result


def bulk_unsubscribe(uuids: list[str]) -> bool:
    """
    Unscubscribes subscriptions in bulk.

    Args:
        uuids (list[str]): The IDs (UUIDs) of the subscriptions to unsubscribe.

    Returns:
        bool: Whether all subscriptions were successfully unsubscribed.
    """

    result: list[bool] = []

    for uuid in uuids:
        result.append(unsubscribe(uuid=uuid))

    return all(result)


def dispatch(
    *args: tuple[Any],
    event: str,
    namespace: str = GLOBAL,
    **kwargs: dict[str, Any],
) -> dict[str, Any]:
    """
    Dispatches an event in the given namespace. (Defaults to 'GLOBAL')

    Additional parameters such as args and kwargs are optional.

    Args:
        event (str): The event to dispatch.
        namespace (str): The namespace in which to dispatch the event.
        *args: tuple[Any]: Additional positional arguments to pass along with the event.
        **kwargs: dict[str, Any]: Additional keyword arguments to pass along with the event.

    Returns:
        dict[str, Any]: The result of the dispatch.

    Raises:
        ValueError: If any error occurs during the dispatch.
    """

    event = event.upper()
    namespace = namespace.upper()

    result: dict[str, Any] = {}

    report: Optional[dict[str, Any]] = None

    if event not in SUBSCRIBERS:
        report = {
            "message": f"Event '{event}' not found. Aborting...",
            "status": "WARNING",
        }

        log_warning(
            message=report,
            name="DISPATCHER",
        )

        return report

    if namespace not in SUBSCRIBERS[event]:
        report = {
            "message": f"Namespace '{namespace}' not found. Aborting...",
            "status": "WARNING",
        }

        log_warning(
            message=report,
            name="DISPATCHER",
        )

        return report

    result["args"] = args
    result["kwargs"] = kwargs
    result["event"] = event
    result["namespace"] = namespace
    result["start"] = get_now()

    subscriptions: list[dict[str, Any]] = list(
        sorted(
            list(SUBSCRIBERS[event][namespace].values()),
            key=lambda x: x["priority"],
            reverse=True,
        )
    )

    non_persistents: list[str] = []

    for subscription in subscriptions:
        if subscription["function"]["name"] not in result:
            result[subscription["function"]["name"]] = []

        try:
            result[subscription["function"]["name"]].append(
                {
                    "result": subscription["function"]["function"](
                        *args,
                        **kwargs,
                    ),
                    "uuid": subscription["uuid"],
                }
            )
        except Exception as e:
            report = {
                "exception": e,
                "message": f"Function '{subscription["function"]["name"]}' failed. Aborting...",
                "status": "ERROR",
            }

            log_error(
                message=report,
                name="DISPATCHER",
            )

        if not subscription["persistent"]:
            non_persistents.append(subscription["uuid"])

    result["end"] = get_now()
    result["duration"] = (result["end"] - result["start"]).total_seconds()

    result["start"] = result["start"].isoformat()
    result["end"] = result["end"].isoformat()

    bulk_unsubscribe(uuids=non_persistents)

    return result


def subscribe(
    event: str,
    function: Callable[[..., Any], Any],
    namespace: str = GLOBAL,
    persistent: bool = False,
    priority: int = 0,
) -> str:
    """
    Subscribes a function to an event based on a namespace. (Defaults to the 'GLOBAL' namespace)

    Additional parameters such as persistent and priority are optional.

    Args:
        event (str): The event to subscribe to.
        function (Callable[[..., Any], Any]): The function to subscribe.
        namespace (str, optional): The namespace to subscribe to. Defaults to GLOBAL.
        persistent (bool, optional): Whether the subscription should persist. Defaults to False.
        priority (int, optional): The priority of the subscription. Defaults to 0.

    Returns:
        str: The ID (UUID) of the subscription.
    """

    event = event.upper()
    namespace = namespace.upper()

    if event not in SUBSCRIBERS:
        SUBSCRIBERS[event] = {}

    if namespace not in SUBSCRIBERS[event]:
        SUBSCRIBERS[event][namespace] = {}

    subscription: dict[str, Any] = {
        "event": event,
        "namespace": namespace,
        "function": {
            "function": function,
            "name": function.__name__,
        },
        "persistent": persistent,
        "priority": priority,
        "uuid": generate_uuid4_str(),
    }

    SUBSCRIBERS[event][namespace][subscription["uuid"]] = subscription

    UUIDS[subscription["uuid"]] = {
        "event": event,
        "namespace": namespace,
    }

    log_info(
        message=f"Subscribed to event '{event}' in namespace '{namespace}' with UUID '{subscription['uuid']}'.",
        name="DISPATCHER",
    )

    return subscription["uuid"]


def unsubscribe(uuid: str) -> bool:
    """
    Unscubribes a subscription with the passed ID (UUID).

    Args:
        uuid (str): The ID (UUID) of the subscription to unsubscribe.

    Returns:
        bool: Whether the subscription was successfully unsubscribed.
    """

    if uuid not in UUIDS:
        return False

    event: str = UUIDS[uuid]["event"]
    namespace: str = UUIDS[uuid]["namespace"]

    SUBSCRIBERS[event][namespace].pop(uuid)

    del UUIDS[uuid]

    if not SUBSCRIBERS[event][namespace]:
        del SUBSCRIBERS[event][namespace]

    if not SUBSCRIBERS[event]:
        del SUBSCRIBERS[event]

    log_info(
        message=f"Unsubscribed from event '{event}' in namespace '{namespace}' with UUID '{uuid}'.",
        name="DISPATCHER",
    )

    return True
