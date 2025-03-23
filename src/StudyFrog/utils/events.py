"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from utils.dispatcher import DispatcherEvent, DispatcherEventFactory


__all__: Final[List[str]] = ["Events"]


class Events:
    """
    A collection of application-level events.

    These events are dispatched using the Dispatcher class.
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

    # An event that indicates that the cancel button has been clicked
    CANCEL_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:cancel_button:clicked"
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

    # An event that indicates that a generic event has occurred
    GENERIC_EVENT: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:generic:event"
    )

    # An event that indicates that a label has been clicked
    LABEL_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:label:clicked"
    )

    # An event that indicates that a help button has been clicked
    HELP_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:help:button:clicked"
    )

    # An event that indicates that a menu button has been clicked
    MENU_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:menu:button:clicked"
    )

    # An event that indicates that a navigate event has occurred
    NAVIGATE: DispatcherEvent = DispatcherEventFactory.create_event(name="ui:navigate")

    # An event that indicates that a navigate validation has failed
    NAVIGATE_VALIDATE_FAILURE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:navigate:validate:failure"
    )

    # An event that indicates that a navigate validation has succeeded
    NAVIGATE_VALIDATE_SUCCESS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:navigate:validate:success"
    )

    # An event that indicates that a navigation has been completed
    NAVIGATION_COMPLETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:navigation:completed"
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

    # An event that indicates that an okay button has been clicked
    OKAY_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:button:okay:clicked"
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

    # An event that indicates that the user wants to create a new answer
    REQUEST_ANSWER_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:answer:create"
    )

    # An event that indicates that the user wants to delete an answer
    REQUEST_ANSWER_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:answer:delete"
    )

    # An event that indicates that the user wants to load an answer
    REQUEST_ANSWER_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:answer:load"
    )

    # An event that indicates that the user wants to lookup an answer
    REQUEST_ANSWER_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:answer:lookup"
    )

    # An event that indicates that the user wants to update an answer
    REQUEST_ANSWER_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:answer:update"
    )

    # An event that indicates that the application should be stopped
    REQUEST_APPLICATION_STOP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:application:stop"
    )

    # An event that indicates that the user wants to create a new association
    REQUEST_ASSOCIATION_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:association:create"
    )

    # An event that indicates that the user wants to delete an association
    REQUEST_ASSOCIATION_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:association:delete"
    )

    # An event that indicates that the user wants to load an association
    REQUEST_ASSOCIATION_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:association:load"
    )

    # An event that indicates that the user wants to lookup an association
    REQUEST_ASSOCIATION_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:association:lookup"
    )

    # An event that indicates that the user wants to update an association
    REQUEST_ASSOCIATION_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:association:update"
    )

    # An event that indicates that the user wants to go backward in the navigation stack
    REQUEST_BACKWARD_NAVIGATION: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:backward:navigation"
    )

    # An event that indicates that the user wants to create a new change history
    REQUEST_CHANGE_HISTORY_CREATE: DispatcherEvent = (
        DispatcherEventFactory.create_event(name="global:request:change_history:create")
    )

    # An event that indicates that the user wants to delete a change history
    REQUEST_CHANGE_HISTORY_DELETE: DispatcherEvent = (
        DispatcherEventFactory.create_event(name="global:request:change_history:delete")
    )

    # An event that indicates that the user wants to load a change history
    REQUEST_CHANGE_HISTORY_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:change_history:load"
    )

    # An event that indicates that the user wants to lookup a change history
    REQUEST_CHANGE_HISTORY_LOOKUP: DispatcherEvent = (
        DispatcherEventFactory.create_event(name="global:request:change_history:lookup")
    )

    # An event that indicates that the user wants to update a change history
    REQUEST_CHANGE_HISTORY_UPDATE: DispatcherEvent = (
        DispatcherEventFactory.create_event(name="global:request:change_history:update")
    )

    # An event that indicates that the user wants to create a new change history item
    REQUEST_CHANGE_HISTORY_ITEM_CREATE: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:create"
        )
    )

    # An event that indicates that the user wants to delete a change history item
    REQUEST_CHANGE_HISTORY_ITEM_DELETE: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:delete"
        )
    )

    # An event that indicates that the user wants to load a change history item
    REQUEST_CHANGE_HISTORY_ITEM_LOAD: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:load"
        )
    )

    # An event that indicates that the user wants to lookup a change history item
    REQUEST_CHANGE_HISTORY_ITEM_LOOKUP: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:lookup"
        )
    )

    # An event that indicates that the user wants to update a change history item
    REQUEST_CHANGE_HISTORY_ITEM_UPDATE: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:update"
        )
    )

    # An event that indicates that the user wants to create a new custom field
    REQUEST_CUSTOM_FIELD_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:custom_field:create"
    )

    # An event that indicates that the user wants to delete a custom field
    REQUEST_CUSTOM_FIELD_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:custom_field:delete"
    )

    # An event that indicates that the user wants to load a custom field
    REQUEST_CUSTOM_FIELD_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:custom_field:load"
    )

    # An event that indicates that the user wants to lookup a custom field
    REQUEST_CUSTOM_FIELD_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:custom_field:lookup"
    )

    # An event that indicates that the user wants to update a custom field
    REQUEST_CUSTOM_FIELD_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:custom_field:update"
    )

    # An event that indicates that the user wants to create a new difficulty
    REQUEST_DIFFICULTY_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:difficulty:create"
    )

    # An event that indicates that the user wants to delete a difficulty
    REQUEST_DIFFICULTY_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:difficulty:delete"
    )

    # An event that indicates that the user wants to load a difficulty
    REQUEST_DIFFICULTY_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:difficulty:load"
    )

    # An event that indicates that the user wants to lookup a difficulty
    REQUEST_DIFFICULTY_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:difficulty:lookup"
    )

    # An event that indicates that the user wants to update a difficulty
    REQUEST_DIFFICULTY_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:difficulty:update"
    )

    # An event that indicates that the user wants to exit the main UI loop
    REQUEST_EXIT_UI_MAINLOOP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:exit:mainloop"
    )

    # An event that indicates that the user wants to go forward in the navigation stack
    REQUEST_FORWARD_NAVIGATION: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:forward:navigation"
    )

    # An event that indicates that the user wants to create a new flashcard
    REQUEST_FLASHCARD_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:flashcard:create"
    )

    # An event that indicates that the user wants to delete a flashcard
    REQUEST_FLASHCARD_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:flashcard:delete"
    )

    # An event that indicates that the user wants to load a flashcard
    REQUEST_FLASHCARD_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:flashcard:load"
    )

    # An event that indicates that the user wants to lookup a flashcard
    REQUEST_FLASHCARD_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:flashcard:lookup"
    )

    # An event that indicates that the user wants to update a flashcard
    REQUEST_FLASHCARD_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:flashcard:update"
    )

    # An event that indicates that the user wants to get all answers
    REQUEST_GET_ALL_ANSWERS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:answers"
    )

    # An event that indicates that the user wants to get all associations
    REQUEST_GET_ALL_ASSOCIATIONS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:associations"
    )

    # An event that indicates that the user wants to get all change histories
    REQUEST_GET_ALL_CHANGE_HISTORIES: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:get:all:change:histories"
        )
    )

    # An event that indicates that the user wants to get all change history items
    REQUEST_GET_ALL_CHANGE_HISTORY_ITEMS: DispatcherEvent = (
        DispatcherEventFactory.create_event(
            name="global:request:get:all:change:history:items"
        )
    )

    # An event that indicates that the user wants to get all custom fields
    REQUEST_GET_ALL_CUSTOM_FIELDS: DispatcherEvent = (
        DispatcherEventFactory.create_event(name="global:request:get:all:custom:fields")
    )

    # An event that indicates that the user wants to get all defaults
    REQUEST_GET_ALL_DEFAULTS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:defaults"
    )

    # An event that indicates that the user wants to get all difficulties
    REQUEST_GET_ALL_DIFFICULTIES: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:difficulties"
    )

    # An event that indicates that the user wants to get all flashcards
    REQUEST_GET_ALL_FLASHCARDS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:flashcards"
    )

    # An event that indicates that the user wants to get all notes
    REQUEST_GET_ALL_NOTES: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:notes"
    )

    # An event that indicates that the user wants to get all options
    REQUEST_GET_ALL_OPTIONS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:options"
    )

    # An event that indicates that the user wants to get all priorities
    REQUEST_GET_ALL_PRIORITIES: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:priorities"
    )

    # An event that indicates that the user wants to get all questions
    REQUEST_GET_ALL_QUESTIONS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:questions"
    )

    # An event that indicates that the user wants to get all settings
    REQUEST_GET_ALL_SETTINGS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:settings"
    )

    # An event that indicates that the user wants to get all stacks
    REQUEST_GET_ALL_STACKS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:stacks"
    )

    # An event that indicates that the user wants to get all statuses
    REQUEST_GET_ALL_STATUSES: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:statuses"
    )

    # An event that indicates that the user wants to get all tags
    REQUEST_GET_ALL_TAGS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:tags"
    )

    # An event that indicates that the user wants to get all users
    REQUEST_GET_ALL_USERS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:all:users"
    )

    # An event that indicates that the user wants to get an object by its key
    REQUEST_GET_BY_KEY: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:by:key"
    )

    # An event that indicates that the user wants to get objects by their keys
    REQUEST_GET_BY_KEYS: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:get:by:keys"
    )

    # An event that indicates that the user wants to create a new note
    REQUEST_NOTE_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:note:create"
    )

    # An event that indicates that the user wants to delete a note
    REQUEST_NOTE_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:note:delete"
    )

    # An event that indicates that the user wants to load a note
    REQUEST_NOTE_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:note:load"
    )

    # An event that indicates that the user wants to lookup a note
    REQUEST_NOTE_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:note:lookup"
    )

    # An event that indicates that the user wants to update a note
    REQUEST_NOTE_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:note:update"
    )

    # An event that indicates that the user wants to create a new option
    REQUEST_OPTION_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:option:create"
    )

    # An event that indicates that the user wants to delete a option
    REQUEST_OPTION_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:option:delete"
    )

    # An event that indicates that the user wants to load a option
    REQUEST_OPTION_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:option:load"
    )

    # An event that indicates that the user wants to lookup an option
    REQUEST_OPTION_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:option:lookup"
    )

    # An event that indicates that the user wants to update a option
    REQUEST_OPTION_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:option:update"
    )

    # An event that indicates that the user wants to create a new priority
    REQUEST_PRIORITY_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:priority:create"
    )

    # An event that indicates that the user wants to delete a priority
    REQUEST_PRIORITY_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:priority:delete"
    )

    # An event that indicates that the user wants to load a priority
    REQUEST_PRIORITY_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:priority:load"
    )

    # An event that indicates that the user wants to lookup a priority
    REQUEST_PRIORITY_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:priority:lookup"
    )

    # An event that indicates that the user wants to update a priority
    REQUEST_PRIORITY_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:priority:update"
    )

    # An event that indicates that the user wants to create a new question
    REQUEST_QUESTION_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:question:create"
    )

    # An event that indicates that the user wants to delete a question
    REQUEST_QUESTION_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:question:delete"
    )

    # An event that indicates that the user wants to load a question
    REQUEST_QUESTION_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:question:load"
    )

    # An event that indicates that the user wants to lookup a question
    REQUEST_QUESTION_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:question:lookup"
    )

    # An event that indicates that the user wants to update a question
    REQUEST_QUESTION_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:question:update"
    )

    # An event that indicates that the user wants to create a new setting
    REQUEST_SETTING_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:setting:create"
    )

    # An event that indicates that the user wants to delete a setting
    REQUEST_SETTING_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:setting:delete"
    )

    # An event that indicates that the user wants to load a setting
    REQUEST_SETTING_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:setting:load"
    )

    # An event that indicates that the user wants to lookup a setting
    REQUEST_SETTING_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:setting:lookup"
    )

    # An event that indicates that the user wants to update a setting
    REQUEST_SETTING_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:setting:update"
    )

    # An event that indicates that the user wants to create a new stack
    REQUEST_STACK_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:stack:create"
    )

    # An event that indicates that the user wants to delete a stack
    REQUEST_STACK_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:stack:delete"
    )

    # An event that indicates that the user wants to load a stack
    REQUEST_STACK_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:stack:load"
    )

    # An event that indicates that the user wants to lookup a stack
    REQUEST_STACK_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:stack:lookup"
    )

    # An event that indicates that the user wants to update a stack
    REQUEST_STACK_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:stack:update"
    )

    # An event that indicates that the user wants to create a new status
    REQUEST_STATUS_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:status:create"
    )

    # An event that indicates that the user wants to delete a status
    REQUEST_STATUS_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:status:delete"
    )

    # An event that indicates that the user wants to load a status
    REQUEST_STATUS_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:status:load"
    )

    # An event that indicates that the user wants to lookup a status
    REQUEST_STATUS_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:status:lookup"
    )

    # An event that indicates that the user wants to update a status
    REQUEST_STATUS_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:status:update"
    )

    # An event that indicates that the user wants to create a new tag
    REQUEST_TAG_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:tag:create"
    )

    # An event that indicates that the user wants to delete a tag
    REQUEST_TAG_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:tag:delete"
    )

    # An event that indicates that the user wants to load a tag
    REQUEST_TAG_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:tag:load"
    )

    # An event that indicates that the user wants to lookup a tag
    REQUEST_TAG_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:tag:lookup"
    )

    # An event that indicates that the user wants to update a tag
    REQUEST_TAG_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:tag:update"
    )

    # An event that indicates that the user wants to pause a timer
    REQUEST_TIMER_PAUSE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:timer:pause"
    )

    # An event that indicates that the user wants to resume a timer
    REQUEST_TIMER_RESUME: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:timer:resume"
    )

    # An event that indicates that the user wants to start a timer
    REQUEST_TIMER_START: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:timer:start"
    )

    # An event that indicates that the user wants to stop a timer
    REQUEST_TIMER_STOP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:timer:stop"
    )

    # An event that indicates that the user wants to create a new user
    REQUEST_USER_CREATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:user:create"
    )

    # An event that indicates that the user wants to delete a user
    REQUEST_USER_DELETE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:user:delete"
    )

    # An event that indicates that the user wants to load a user
    REQUEST_USER_LOAD: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:user:load"
    )

    # An event that indicates that the user wants to lookup a user
    REQUEST_USER_LOOKUP: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:user:lookup"
    )

    # An event that indicates that the user wants to update a user
    REQUEST_USER_UPDATE: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:user:update"
    )

    # An event that indicates that the user wants to validate navigation
    REQUEST_VALIDATE_NAVIGATION: DispatcherEvent = DispatcherEventFactory.create_event(
        name="global:request:validate:navigation"
    )

    # An event that indicates that the settings button has been clicked
    SETTINGS_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:settings:button:clicked"
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

    # An event that indicates that a toast has been clicked
    TOAST_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:toast:clicked"
    )

    # An event that indicates that a toast has been destroyed
    TOAST_DESTROYED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:toast:destroyed"
    )

    # An event that indicates that the timer has been started
    TIMER_STARTED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:timer:started"
    )

    # An event that indicates that the timer has been stopped
    TIMER_STOPPED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:timer:stopped"
    )

    # An event that indicates that the user button has been clicked
    USER_BUTTON_CLICKED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="ui:button:user:clicked"
    )

    # An event that indicates that a user has been created in the backend
    USER_CREATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:user:created"
    )

    # An event that indicates that a user has been deleted in the backend
    USER_DELETED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:user:deleted"
    )

    # An event that indicates that a user has been loaed in the backend
    USER_LOADED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:user:loaded"
    )

    # An event that indicates that a user has been updated in the backend
    USER_UPDATED: DispatcherEvent = DispatcherEventFactory.create_event(
        name="backend:user:updated"
    )

    @classmethod
    def get_all_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all events in the Events class.
        """
        return list(cls.__dict__.values())

    @classmethod
    def get_event_by_name(
        cls,
        name: str,
    ) -> Optional[DispatcherEvent]:
        """
        Returns the event with the given name in the Events class.

        Args:
            name (str): The name of the event to retrieve.

        Returns:
            Optional[DispatcherEvent]: The event with the given name if found; None otherwise.
        """
        return next(
            (event for event in cls.get_all_events() if event.name == name),
            None,
        )

    @classmethod
    def get_event_names(cls) -> List[str]:
        """
        Returns a list of all event names in the Events class.

        Returns:
            List[str]: A list of all event names in the Events class.
        """
        return [event.name for event in cls.get_all_events()]

    @classmethod
    def get_answer_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all answer events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all answer events in the Events class.
        """
        return [
            cls.REQUEST_ANSWER_CREATE,
            cls.REQUEST_ANSWER_DELETE,
            cls.REQUEST_ANSWER_LOAD,
            cls.REQUEST_ANSWER_LOOKUP,
            cls.REQUEST_ANSWER_UPDATE,
        ]

    @classmethod
    def get_association_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all association events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all association events in the Events class.
        """
        return [
            cls.REQUEST_ASSOCIATION_CREATE,
            cls.REQUEST_ASSOCIATION_DELETE,
            cls.REQUEST_ASSOCIATION_LOAD,
            cls.REQUEST_ASSOCIATION_LOOKUP,
            cls.REQUEST_ASSOCIATION_UPDATE,
        ]

    @classmethod
    def get_change_history_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all change history events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all change history events in the Events class.
        """
        return [
            cls.REQUEST_CHANGE_HISTORY_CREATE,
            cls.REQUEST_CHANGE_HISTORY_DELETE,
            cls.REQUEST_CHANGE_HISTORY_LOAD,
            cls.REQUEST_CHANGE_HISTORY_LOOKUP,
            cls.REQUEST_CHANGE_HISTORY_UPDATE,
        ]

    @classmethod
    def get_change_history_item_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all change history item events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all change history item events in the Events class.
        """
        return [
            cls.REQUEST_CHANGE_HISTORY_ITEM_CREATE,
            cls.REQUEST_CHANGE_HISTORY_ITEM_DELETE,
            cls.REQUEST_CHANGE_HISTORY_ITEM_LOAD,
            cls.REQUEST_CHANGE_HISTORY_ITEM_LOOKUP,
            cls.REQUEST_CHANGE_HISTORY_ITEM_UPDATE,
        ]

    @classmethod
    def get_custom_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all custom field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all custom field events in the Events class.
        """
        return [
            cls.REQUEST_CUSTOM_FIELD_CREATE,
            cls.REQUEST_CUSTOM_FIELD_DELETE,
            cls.REQUEST_CUSTOM_FIELD_LOAD,
            cls.REQUEST_CUSTOM_FIELD_LOOKUP,
            cls.REQUEST_CUSTOM_FIELD_UPDATE,
        ]

    @classmethod
    def get_difficulty_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all difficulty events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all difficulty events in the Events class.
        """
        return [
            cls.REQUEST_DIFFICULTY_CREATE,
            cls.REQUEST_DIFFICULTY_DELETE,
            cls.REQUEST_DIFFICULTY_LOAD,
            cls.REQUEST_DIFFICULTY_LOOKUP,
            cls.REQUEST_DIFFICULTY_UPDATE,
        ]

    @classmethod
    def get_flashcard_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all flashcard events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all flashcard events in the Events class.
        """
        return [
            cls.REQUEST_FLASHCARD_CREATE,
            cls.REQUEST_FLASHCARD_DELETE,
            cls.REQUEST_FLASHCARD_LOAD,
            cls.REQUEST_FLASHCARD_LOOKUP,
            cls.REQUEST_FLASHCARD_UPDATE,
        ]

    @classmethod
    def get_navigation_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all navigation events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all navigation events in the Events class.
        """
        return [
            cls.REQUEST_BACKWARD_NAVIGATION,
            cls.REQUEST_FORWARD_NAVIGATION,
        ]

    @classmethod
    def get_note_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all note events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all note events in the Events class.
        """
        return [
            cls.REQUEST_NOTE_CREATE,
            cls.REQUEST_NOTE_DELETE,
            cls.REQUEST_NOTE_LOAD,
            cls.REQUEST_NOTE_LOOKUP,
            cls.REQUEST_NOTE_UPDATE,
        ]

    @classmethod
    def get_option_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all option events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all option events in the Events class.
        """
        return [
            cls.REQUEST_OPTION_CREATE,
            cls.REQUEST_OPTION_DELETE,
            cls.REQUEST_OPTION_LOAD,
            cls.REQUEST_OPTION_LOOKUP,
            cls.REQUEST_OPTION_UPDATE,
        ]

    @classmethod
    def get_priority_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all priority events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all priority events in the Events class.
        """
        return [
            cls.REQUEST_PRIORITY_CREATE,
            cls.REQUEST_PRIORITY_DELETE,
            cls.REQUEST_PRIORITY_LOAD,
            cls.REQUEST_PRIORITY_LOOKUP,
            cls.REQUEST_PRIORITY_UPDATE,
        ]

    @classmethod
    def get_question_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all question events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all question events in the Events class.
        """
        return [
            cls.REQUEST_QUESTION_CREATE,
            cls.REQUEST_QUESTION_DELETE,
            cls.REQUEST_QUESTION_LOAD,
            cls.REQUEST_QUESTION_LOOKUP,
            cls.REQUEST_QUESTION_UPDATE,
        ]

    @classmethod
    def get_setting_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all setting events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all setting events in the Events class.
        """
        return [
            cls.REQUEST_SETTING_CREATE,
            cls.REQUEST_SETTING_DELETE,
            cls.REQUEST_SETTING_LOAD,
            cls.REQUEST_SETTING_LOOKUP,
            cls.REQUEST_SETTING_UPDATE,
        ]

    @classmethod
    def get_stack_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all stack events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all stack events in the Events class.
        """
        return [
            cls.REQUEST_STACK_CREATE,
            cls.REQUEST_STACK_DELETE,
            cls.REQUEST_GET_ALL_STACKS,
            cls.REQUEST_STACK_LOAD,
            cls.REQUEST_STACK_LOOKUP,
            cls.REQUEST_STACK_UPDATE,
        ]

    @classmethod
    def get_status_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all status events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all status events in the Events class.
        """
        return [
            cls.REQUEST_STATUS_CREATE,
            cls.REQUEST_STATUS_DELETE,
            cls.REQUEST_STATUS_LOAD,
            cls.REQUEST_STATUS_LOOKUP,
            cls.REQUEST_STATUS_UPDATE,
        ]

    @classmethod
    def get_tag_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all tag events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all tag events in the Events class.
        """
        return [
            cls.REQUEST_TAG_CREATE,
            cls.REQUEST_TAG_DELETE,
            cls.REQUEST_TAG_LOAD,
            cls.REQUEST_TAG_LOOKUP,
            cls.REQUEST_TAG_UPDATE,
        ]

    @classmethod
    def get_timer_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all timer events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all timer events in the Events class.
        """
        return [
            cls.REQUEST_TIMER_PAUSE,
            cls.REQUEST_TIMER_RESUME,
            cls.REQUEST_TIMER_START,
            cls.REQUEST_TIMER_STOP,
        ]

    @classmethod
    def get_user_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all user events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all user events in the Events class.
        """
        return [
            cls.REQUEST_USER_CREATE,
            cls.REQUEST_USER_DELETE,
            cls.REQUEST_USER_LOAD,
            cls.REQUEST_USER_LOOKUP,
            cls.REQUEST_USER_UPDATE,
        ]
