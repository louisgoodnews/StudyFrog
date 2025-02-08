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
        ANSWER_CREATED (DispatcherEvent): An event that indicates that an answer has been created in the backend.
        ANSWER_DELETED (DispatcherEvent): An event that indicates that an answer has been deleted in the backend.
        ANSWER_LOADED (DispatcherEvent): An event that indicates that an answer has been loaed in the backend.
        ANSWER_UPDATED (DispatcherEvent): An event that indicates that an answer has been updated in the backend.
        APPLICATION_STARTED (DispatcherEvent): An event that indicates that the application has started.
        APPLICATION_STOPPED (DispatcherEvent): An event that indicates that the application has stopped.
        ASSOCIATION_CREATED (DispatcherEvent): An event that indicates that an association has been created in the backend.
        ASSOCIATION_DELETED (DispatcherEvent): An event that indicates that an association has been deleted in the backend.
        ASSOCIATION_LOADED (DispatcherEvent): An event that indicates that an association has been loaed in the backend.
        ASSOCIATION_UPDATED (DispatcherEvent): An event that indicates that an association has been updated in the backend.
        BUTTON_CLICKED (DispatcherEvent): An event that indicates that a button has been clicked.
        CHANGE_HISTORY_CREATED (DispatcherEvent): An event that indicates that a change history has been created in the backend.
        CHANGE_HISTORY_DELETED (DispatcherEvent): An event that indicates that a change history has been deleted in the backend.
        CHANGE_HISTORY_LOADED (DispatcherEvent): An event that indicates that a change history has been loaed in the backend.
        CHANGE_HISTORY_UPDATED (DispatcherEvent): An event that indicates that a change history has been updated in the backend.
        CHANGE_HISTORY_ITEM_CREATED (DispatcherEvent): An event that indicates that a change history item has been created in the backend.
        CHANGE_HISTORY_ITEM_DELETED (DispatcherEvent): An event that indicates that a change history item has been deleted in the backend.
        CHANGE_HISTORY_ITEM_LOADED (DispatcherEvent): An event that indicates that a change history item has been loaed in the backend.
        CHANGE_HISTORY_ITEM_UPDATED (DispatcherEvent): An event that indicates that a change history item has been updated in the backend.
        CREATE_BUTTON_CLICKED (DispatcherEvent): An event that indicates that a create button has been clicked.
        DIFFICULTY_CREATED (DispatcherEvent): An event that indicates that a difficulty has been created in the backend.
        DIFFICULTY_DELETED (DispatcherEvent): An event that indicates that a difficulty has been deleted in the backend.
        DIFFICULTY_LOADED (DispatcherEvent): An event that indicates that a difficulty has been loaed in the backend.
        DIFFICULTY_UPDATED (DispatcherEvent): An event that indicates that a difficulty has been updated in the backend.
        FLASHCARD_CREATED (DispatcherEvent): An event that indicates that a flashcard has been created in the backend.
        FLASHCARD_DELETED (DispatcherEvent): An event that indicates that a flashcard has been deleted in the backend.
        FLASHCARD_LOADED (DispatcherEvent): An event that indicates that a flashcard has been loaed in the backend.
        FLASHCARD_UPDATED (DispatcherEvent): An event that indicates that a flashcard has been updated in the backend.
        HELP_BUTTON_CLICKED (DispatcherEvent): An event that indicates that a help button has been clicked.
        MENU_BUTTON_CLICKED (DispatcherEvent): An event that indicates that a menu button has been clicked.
        NOTE_CREATED (DispatcherEvent): An event that indicates that a note has been created in the backend.
        NOTE_DELETED (DispatcherEvent): An event that indicates that a note has been deleted in the backend.
        NOTE_LOADED (DispatcherEvent): An event that indicates that a note has been loaed in the backend.
        NOTE_UPDATED (DispatcherEvent): An event that indicates that a note has been updated in the backend.
        NOTIFICATIONS_BUTTON_CLICKED (DispatcherEvent): An event that indicates that a notifications button has been clicked.
        PRIORITY_CREATED (DispatcherEvent): An event that indicates that a priority has been created in the backend.
        PRIORITY_DELETED (DispatcherEvent): An event that indicates that a priority has been deleted in the backend.
        PRIORITY_LOADED (DispatcherEvent): An event that indicates that a priority has been loaed in the backend.
        PRIORITY_UPDATED (DispatcherEvent): An event that indicates that a priority has been updated in the backend.
        QUESTION_CREATED (DispatcherEvent): An event that indicates that a question has been created in the backend.
        QUESTION_DELETED (DispatcherEvent): An event that indicates that a question has been deleted in the backend.
        QUESTION_LOADED (DispatcherEvent): An event that indicates that a question has been loaed in the backend.
        QUESTION_UPDATED (DispatcherEvent): An event that indicates that a question has been updated in the backend.
        SEARCH_QUERY_CHANGED (DispatcherEvent): An event that indicates that the search query has been changed.
        STACK_CREATED (DispatcherEvent): An event that indicates that a stack has been created in the backend.
        STACK_DELETED (DispatcherEvent): An event that indicates that a stack has been deleted in the backend.
        STACK_LOADED (DispatcherEvent): An event that indicates that a stack has been loaed in the backend.
        STACK_UPDATED (DispatcherEvent): An event that indicates that a stack has been updated in the backend.
        TAG_CREATED (DispatcherEvent): An event that indicates that a tag has been created in the backend.
        TAG_DELETED (DispatcherEvent): An event that indicates that a tag has been deleted in the backend.
        TAG_LOADED (DispatcherEvent): An event that indicates that a tag has been loaed in the backend.
        TAG_UPDATED (DispatcherEvent): An event that indicates that a tag has been updated in the backend.
        REQUEST_APPLICATION_STOP (DispatcherEvent): An event that indicates that the application should be stopped.
        REQUEST_FORWARD_NAVIGATION (DispatcherEvent): An event that indicates that the user wants to go forward in the navigation stack.
        REQUEST_BACKWARD_NAVIGATION (DispatcherEvent): An event that indicates that the user wants to go backward in the navigation stack.
        SETTINGS_BUTTON_CLICKED (DispatcherEvent): An event that indicates that the settings button has been clicked.
        USER_BUTTON_CLICKED (DispatcherEvent): An event that indicates that the user button has been clicked.
    """

    # An event that indicates that an answer has been created in the backend
    ANSWER_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:answer:created"
    )

    # An event that indicates that an answer has been deleted in the backend
    ANSWER_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:answer:deleted"
    )

    # An event that indicates that an answer has been loaed in the backend
    ANSWER_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:answer:loaded"
    )

    # An event that indicates that an answer has been updated in the backend
    ANSWER_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:answer:updated"
    )

    # An event that indicates that the application has started
    APPLICATION_STARTED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:application:started"
    )

    # An event that indicates that the application has stopped
    APPLICATION_STOPPED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:application:stopped"
    )

    # An event that indicates that an association has been created in the backend
    ASSOCIATION_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:association:created"
    )

    # An event that indicates that an association has been deleted in the backend
    ASSOCIATION_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:association:deleted"
    )

    # An event that indicates that an association has been loaed in the backend
    ASSOCIATION_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:association:loaded"
    )

    # An event that indicates that an association has been updated in the backend
    ASSOCIATION_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:association:updated"
    )

    # An event that indicates that a button has been clicked
    BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:button:clicked"
    )

    # An event that indicates that a change history has been created in the backend
    CHANGE_HISTORY_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history:created"
    )

    # An event that indicates that a change history has been deleted in the backend
    CHANGE_HISTORY_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history:deleted"
    )

    # An event that indicates that a change history has been loaed in the backend
    CHANGE_HISTORY_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history:loaded"
    )

    # An event that indicates that a change history has been updated in the backend
    CHANGE_HISTORY_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history:updated"
    )

    # An event that indicates that a change history item has been created in the backend
    CHANGE_HISTORY_ITEM_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history_item:created"
    )

    # An event that indicates that a change history item has been deleted in the backend
    CHANGE_HISTORY_ITEM_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history_item:deleted"
    )

    # An event that indicates that a change history item has been loaed in the backend
    CHANGE_HISTORY_ITEM_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history_item:loaded"
    )

    # An event that indicates that a change history item has been updated in the backend
    CHANGE_HISTORY_ITEM_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:change_history_item:updated"
    )

    # An event that indicates that a create button has been clicked
    CREATE_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:create:button:clicked"
    )

    # An event that indicates that a difficulty has been created in the backend
    DIFFICULTY_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:difficulty:created"
    )

    # An event that indicates that a difficulty has been deleted in the backend
    DIFFICULTY_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:difficulty:deleted"
    )

    # An event that indicates that a difficulty has been loaed in the backend
    DIFFICULTY_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:difficulty:loaded"
    )

    # An event that indicates that a difficulty has been updated in the backend
    DIFFICULTY_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:difficulty:updated"
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

    # An event that indicates that a help button has been clicked
    HELP_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:help:button:clicked"
    )

    # An event that indicates that a menu button has been clicked
    MENU_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:menu:button:clicked"
    )

    # An event that indicates that a note has been created in the backend
    NOTE_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:note:created"
    )

    # An event that indicates that a note has been deleted in the backend
    NOTE_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:note:deleted"
    )

    # An event that indicates that a note has been loaed in the backend
    NOTE_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:note:loaded"
    )

    # An event that indicates that a note has been updated in the backend
    NOTE_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:note:updated"
    )

    # An event that indicates that a notifications button has been clicked
    NOTIFICATIONS_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:notifications:button:clicked"
    )

    # An event that indicates that a priority has been created in the backend
    PRIORITY_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:priority:created"
    )

    # An event that indicates that a priority has been deleted in the backend
    PRIORITY_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:priority:deleted"
    )

    # An event that indicates that a priority has been loaed in the backend
    PRIORITY_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:priority:loaded"
    )

    # An event that indicates that a priority has been updated in the backend
    PRIORITY_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:priority:updated"
    )

    # An event that indicates that a question has been created in the backend
    QUESTION_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:question:created"
    )

    # An event that indicates that a question has been deleted in the backend
    QUESTION_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:question:deleted"
    )

    # An event that indicates that a question has been loaed in the backend
    QUESTION_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:question:loaded"
    )

    # An event that indicates that a question has been updated in the backend
    QUESTION_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:question:updated"
    )

    # An event that indicates that the search query has been changed
    SEARCH_QUERY_CHANGED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:search:query:changed"
    )

    # An event that indicates that a stack has been created in the backend
    STACK_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:stack:created"
    )

    # An event that indicates that a stack has been deleted in the backend
    STACK_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:stack:deleted"
    )

    # An event that indicates that a stack has been loaed in the backend
    STACK_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:stack:loaded"
    )

    # An event that indicates that a stack has been updated in the backend
    STACK_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:stack:updated"
    )

    # An event that indicates that a tag has been created in the backend
    TAG_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:tag:created"
    )

    # An event that indicates that a tag has been deleted in the backend
    TAG_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:tag:deleted"
    )

    # An event that indicates that a tag has been loaed in the backend
    TAG_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:tag:loaded"
    )

    # An event that indicates that a tag has been updated in the backend
    TAG_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:tag:updated"
    )

    # An event that indicates that the application should be stopped
    REQUEST_APPLICATION_STOP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:application:stop"
    )

    # An event that indicates that the user wants to go backward in the navigation stack
    REQUEST_BACKWARD_NAVIGATION: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:backward:navigation"
    )

    # An event that indicates that the user wants to go forward in the navigation stack
    REQUEST_FORWARD_NAVIGATION: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:forward:navigation"
    )

    # An event that indicates that the settings button has been clicked
    SETTINGS_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:settings:button:clicked"
    )

    # An event that indicates that the user button has been clicked
    USER_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:user:button:clicked"
    )
