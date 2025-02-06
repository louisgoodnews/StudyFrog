"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from utils.dispatcher import DispatcherEvent, DispatcherEventFactory


__all__: List[str] = ["Events"]


class Events:
    """
    A collection of application-level events.

    Attributes:
        APPLICATION_STARTED (DispatcherEvent): An event that indicates that the application has started.
        APPLICATION_STOPPED (DispatcherEvent): An event that indicates that the application has stopped.
        BUTTON_CLICKED (DispatcherEvent): An event that indicates that a button has been clicked.
        FLASHCARD_CREATED (DispatcherEvent): An event that indicates that a flashcard has been created in the backend.
        FLASHCARD_DELETED (DispatcherEvent): An event that indicates that a flashcard has been deleted in the backend.
        FLASHCARD_LOADED (DispatcherEvent): An event that indicates that a flashcard has been loaed in the backend.
        FLASHCARD_UPDATED (DispatcherEvent): An event that indicates that a flashcard has been updated in the backend.
    """

    # An event that indicates that the application has started
    APPLICATION_STARTED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:application:started"
    )

    # An event that indicates that the application has stopped
    APPLICATION_STOPPED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:application:stopped"
    )

    # An event that indicates that a button has been clicked
    BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:button:clicked"
    )

    # An event that indicates that a flashcard has been created in the backend
    FLASHCARD_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:flashcard:created"
    )

    # An event that indicates that a flashcard has been deleted in the backend
    FLASHCARD_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:flashcard:deleted"
    )

    # An event that indicates that a flashcard has been loaed in the backend
    FLASHCARD_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:flashcard:loaded"
    )

    # An event that indicates that a flashcard has been updated in the backend
    FLASHCARD_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:flashcard:updated"
    )
