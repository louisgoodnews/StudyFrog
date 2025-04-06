"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from utils.dispatcher import DispatcherEvent, DispatcherEventFactory
from utils.logger import Logger


__all__: Final[List[str]] = ["Events"]


class Events:
    """
    A collection of application-level events as DispatcherEvent objects.

    These events are dispatched using the Dispatcher class.

    Attributes:
        logger (Logger): The logger instance used by the class.
    """

    # The logger instance used by the class
    logger: Final[Logger] = Logger.get_logger(name="Events")

    # An event that indicates that an answer has been created in the backend
    ANSWER_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:answer:created"
    )

    # An event that indicates that an answer has been deleted in the backend
    ANSWER_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:answer:deleted"
    )

    # An event that indicates that an answer has been loaed in the backend
    ANSWER_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:answer:loaded"
    )

    # An event that indicates that an answer has been updated in the backend
    ANSWER_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:answer:updated"
    )

    # An event that indicates that the application has started
    APPLICATION_STARTED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:application:started"
    )

    # An event that indicates that the application has stopped
    APPLICATION_STOPPED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:application:stopped"
    )

    # An event that indicates that an association has been created in the backend
    ASSOCIATION_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:association:created"
    )

    # An event that indicates that an association has been deleted in the backend
    ASSOCIATION_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:association:deleted"
    )

    # An event that indicates that an association has been loaed in the backend
    ASSOCIATION_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:association:loaded"
    )

    # An event that indicates that an association has been updated in the backend
    ASSOCIATION_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:association:updated"
    )

    # An event that indicates that a button has been clicked
    BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:button:clicked"
    )

    # An event that indicates that the cancel button has been clicked
    CANCEL_BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:cancel_button:clicked"
    )

    # An event that indicates that a change history has been created in the backend
    CHANGE_HISTORY_CREATED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history:created")
    )

    # An event that indicates that a change history has been deleted in the backend
    CHANGE_HISTORY_DELETED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history:deleted")
    )

    # An event that indicates that a change history has been loaed in the backend
    CHANGE_HISTORY_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:change_history:loaded"
    )

    # An event that indicates that a change history has been updated in the backend
    CHANGE_HISTORY_UPDATED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history:updated")
    )

    # An event that indicates that a change history item has been created in the backend
    CHANGE_HISTORY_ITEM_CREATED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history_item:created")
    )

    # An event that indicates that a change history item has been deleted in the backend
    CHANGE_HISTORY_ITEM_DELETED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history_item:deleted")
    )

    # An event that indicates that a change history item has been loaed in the backend
    CHANGE_HISTORY_ITEM_LOADED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history_item:loaded")
    )

    # An event that indicates that a change history item has been updated in the backend
    CHANGE_HISTORY_ITEM_UPDATED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="backend:change_history_item:updated")
    )

    # An event that indicates that a checkbox field has changed
    CHECKBUTTON_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:checkbox:field:changed")
    )

    # An event that indicates that a checkbox field has been cleared
    CHECKBUTTON_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:checkbox:field:cleared")
    )

    # An event that indicates that a checkbox field's value has been retrieved
    CHECKBUTTON_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:checkbox:field:get"
    )

    # An event that indicates that a checkbox field has been set
    CHECKBUTTON_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:checkbox:field:set"
    )

    # An event that indicates that a combobox field has changed
    COMBOBOX_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:combobox_:field:changed")
    )

    # An event that indicates that a combobox field has been cleared
    COMBOBOX_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:combobox_:field:cleared")
    )

    # An event that indicates that a combobox field's value has been retrieved
    COMBOBOX_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:combobox_:field:get"
    )

    # An event that indicates that a combobox field has been set
    COMBOBOX_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:combobox_:field:set"
    )

    # An event that indicates that a combobox field has changed
    COMBOBOX_SELECT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:combobox_select:field:changed")
    )

    # An event that indicates that a combobox field has been cleared
    COMBOBOX_SELECT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:combobox_select:field:cleared")
    )

    # An event that indicates that a combobox field's value has been retrieved
    COMBOBOX_SELECT_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:combobox_select:field:get"
    )

    # An event that indicates that a combobox field has been set
    COMBOBOX_SELECT_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:combobox_select:field:set"
    )

    # An event that indicates that a create button has been clicked
    CREATE_BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:create:button:clicked"
    )

    # An event that indicates that a date select field has changed
    DATE_SELECT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:combobox_select:field:changed")
    )

    # An event that indicates that a date select field has been cleared
    DATE_SELECT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:combobox_select:field:cleared")
    )

    # An event that indicates that a date select field's value has been retrieved
    DATE_SELECT_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:combobox_select:field:get"
    )

    # An event that indicates that a date select field has been set
    DATE_SELECT_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:combobox_select:field:set"
    )

    # An event that indicates that a difficulty has been created in the backend
    DIFFICULTY_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:difficulty:created"
    )

    # An event that indicates that a difficulty has been deleted in the backend
    DIFFICULTY_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:difficulty:deleted"
    )

    # An event that indicates that a difficulty has been loaed in the backend
    DIFFICULTY_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:difficulty:loaded"
    )

    # An event that indicates that a difficulty has been updated in the backend
    DIFFICULTY_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:difficulty:updated"
    )

    # An event that indicates that a flashcard has been created in the backend
    FLASHCARD_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:flashcard:created"
    )

    # An event that indicates that a flashcard has been deleted in the backend
    FLASHCARD_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:flashcard:deleted"
    )

    # An event that indicates that a flashcard has been flipped in the flashcard learning view
    FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED: DispatcherEventFactory.create_event(
        name="flashcardlearningview:flashcard:flipped"
    )

    # An event that indicates that a flashcard has been loaed in the backend
    FLASHCARD_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:flashcard:loaded"
    )

    # An event that indicates that a flashcard has been updated in the backend
    FLASHCARD_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:flashcard:updated"
    )

    # An event that indicates that a float spinbox field has been changed
    FLOAT_SPINBOX_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:float_spinbox:field:changed")
    )
    # An event that indicates that a float spinbox field has been cleared
    FLOAT_SPINBOX_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:float_spinbox:field:cleared")
    )

    # An event that indicates that a float spinbox field has been retrieved
    FLOAT_SPINBOX_FIELD_GET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:float_spinbox:field:get")
    )

    # An event that indicates that a float spinbox field has been set
    FLOAT_SPINBOX_FIELD_SET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:float_spinbox:field:set")
    )

    # An event that indicates that a generic event has occurred
    GENERIC_EVENT: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:generic:event"
    )

    # An event that indicates that a help button has been clicked
    HELP_BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:help:button:clicked"
    )

    # An event that indicates that an int spinbox field has been changed
    INT_SPINBOX_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:int_spinbox:field:changed")
    )
    # An event that indicates that an int spinbox field has been cleared
    INT_SPINBOX_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:int_spinbox:field:cleared")
    )

    # An event that indicates that an int spinbox field has been retrieved
    INT_SPINBOX_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:int_spinbox:field:get"
    )

    # An event that indicates that an int spinbox field has been set
    INT_SPINBOX_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:int_spinbox:field:set"
    )

    # An event that indicates that a label has been clicked
    LABEL_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:label:clicked"
    )

    # An event that indicates that a menu button has been clicked
    MENU_BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:menu:button:clicked"
    )

    # An event that indicates that a multi line text field has changed
    MULTI_LINE_TEXT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_line_text:field:changed")
    )

    # An event that indicates that a multi line text field has been cleared
    MULTI_LINE_TEXT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_line_text:field:cleared")
    )

    # An event that indicates that a multi line text field has been retrieved
    MULTI_LINE_TEXT_FIELD_GET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_line_text:field:get")
    )

    # An event that indicates that a multi line text field has been set
    MULTI_LINE_TEXT_FIELD_SET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_line_text:field:set")
    )

    # An event that indicates that a multi select field has changed
    MULTI_SELECT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_select:field:changed")
    )

    # An event that indicates that a multi select field has been cleared
    MULTI_SELECT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_select:field:cleared")
    )

    # An event that indicates that a multi select field has been retrieved
    MULTI_SELECT_FIELD_GET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_select:field:get")
    )

    # An event that indicates that a multi select field has been set
    MULTI_SELECT_FIELD_SET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:multi_select:field:set")
    )

    # An event that indicates that a navigate event has occurred
    NAVIGATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:navigate"
    )

    # An event that indicates that a navigate validation has failed
    NAVIGATE_VALIDATE_FAILURE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:navigate:validate:failure")
    )

    # An event that indicates that a navigate validation has succeeded
    NAVIGATE_VALIDATE_SUCCESS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:navigate:validate:success")
    )

    # An event that indicates that a navigation has been completed
    NAVIGATION_COMPLETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:navigation:completed"
    )

    # An event that indicates that a note has been created in the backend
    NOTE_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:note:created"
    )

    # An event that indicates that a note has been deleted in the backend
    NOTE_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:note:deleted"
    )

    # An event that indicates that a note has been loaed in the backend
    NOTE_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:note:loaded"
    )

    # An event that indicates that a note has been updated in the backend
    NOTE_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:note:updated"
    )

    # An event that indicates that a notifications button has been clicked
    NOTIFICATIONS_BUTTON_CLICKED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:notifications:button:clicked")
    )

    # An event that indicates that a learning session difficulty button has been clicked
    NOTIFY_LEARNING_SESSION_DIFFICULTY_BUTTON_CLICKED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="ui:notify:state:learning_session:difficulty:button:clicked"
        )
    )

    # An event that indicates that a flashcard has been flipped in the flashcard learning view
    NOTIFY_FLASHCARD_LEARNING_VIEW_FLASHCARD_FLIPPED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:notify:state:flashcard_learning_view:flashcard:flipped"
        )
    )

    # An event that indicates that a learning session runner has been loaded in the backend
    NOTIFY_LEARNING_SESSION_RUNNER_LOADED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:notify:state:learning_session_runner:loaded"
        )
    )

    # An event that indicates that a UI countdown has ended
    NOTIFY_UI_COUNTDOWN_ENDED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:notify:state:ui:countdown:ended"
        )
    )

    # An event that indicates that a UI countdown has started
    NOTIFY_UI_COUNTDOWN_STARTED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:notify:state:ui:countdown:started"
        )
    )

    # An event that indicates that a UI countup has started
    NOTIFY_UI_COUNTUP_STARTED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:notify:state:ui:countup:started"
        )
    )

    # An event that indicates that an okay button has been clicked
    OKAY_BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:button:okay:clicked"
    )

    # An event that indicates that a password text field has changed
    PASSWORD_TEXT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:password_text_field:changed")
    )

    # An event that indicates that a password text field has been retrieved
    PASSWORD_TEXT_FIELD_GET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:password_text_field:get")
    )

    # An event that indicates that a password text field has been set
    PASSWORD_TEXT_FIELD_SET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:password_text_field:set")
    )

    # An event that indicates that a priority has been created in the backend
    PRIORITY_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:priority:created"
    )

    # An event that indicates that a priority has been deleted in the backend
    PRIORITY_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:priority:deleted"
    )

    # An event that indicates that a priority has been loaed in the backend
    PRIORITY_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:priority:loaded"
    )

    # An event that indicates that a priority has been updated in the backend
    PRIORITY_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:priority:updated"
    )

    # An event that indicates that a question has been created in the backend
    QUESTION_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:question:created"
    )

    # An event that indicates that a question has been deleted in the backend
    QUESTION_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:question:deleted"
    )

    # An event that indicates that a question has been loaed in the backend
    QUESTION_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:question:loaded"
    )

    # An event that indicates that a question has been updated in the backend
    QUESTION_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:question:updated"
    )

    # An event that indicates that a radiobutton field has been changed
    RADIOBUTTON_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:radiobutton_field:changed")
    )

    # An event that indicates that a radiobutton field has been cleared
    RADIOBUTTON_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:radiobutton_field:cleared")
    )

    # An event that indicates that a radiobutton field has been retrieved
    RADIOBUTTON_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:radiobutton_field:get"
    )

    # An event that indicates that a radiobutton field has been set
    RADIOBUTTON_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:radiobutton_field:set"
    )

    # An event that indicates that a radiobutton select field has been changed
    RADIOBUTTON_SELECT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:radiobutton_select_field:changed")
    )

    # An event that indicates that a radiobutton select field has been cleared
    RADIOBUTTON_SELECT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:radiobutton_select_field:cleared")
    )

    # An event that indicates that a radiobutton select field has been retrieved
    RADIOBUTTON_SELECT_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:radiobutton_select_field:get"
    )

    # An event that indicates that a radiobutton select field has been set
    RADIOBUTTON_SELECT_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:radiobutton_select_field:set"
    )

    # An event that indicates that a read-only field has been changed
    READONLY_MULTI_LINE_TEXT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:readonly:multi_line_text_field:changed")
    )

    # An event that indicates that a read-only field has been cleared
    READONLY_MULTI_LINE_TEXT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:readonly:multi_line_text_field:cleared")
    )

    # An event that indicates that a read-only field has been retrieved
    READONLY_MULTI_LINE_TEXT_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:readonly:multi_line_text_field:get"
    )

    # An event that indicates that a read-only field has been set
    READONLY_MULTI_LINE_TEXT_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:readonly:multi_line_text_field:set"
    )

    # An event that indicates that a read-only field has been changed
    READONLY_SINGLE_LINE_TEXT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:readonly:single_line_text_field:changed")
    )

    # An event that indicates that a read-only field has been cleared
    READONLY_SINGLE_LINE_TEXT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:readonly:single_line_text_field:cleared")
    )

    # An event that indicates that a read-only field has been retrieved
    READONLY_SINGLE_LINE_TEXT_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:readonly:single_line_text_field:get"
    )

    # An event that indicates that a read-only field has been set
    READONLY_SINGLE_LINE_TEXT_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:readonly:single_line_text_field:set"
    )

    # An event that indicates that the user wants to create a new answer
    REQUEST_ANSWER_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:answer:create"
    )

    # An event that indicates that the user wants to delete an answer
    REQUEST_ANSWER_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:answer:delete"
    )

    # An event that indicates that the user wants to load an answer
    REQUEST_ANSWER_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:answer:load"
    )

    # An event that indicates that the user wants to lookup an answer
    REQUEST_ANSWER_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:answer:lookup"
    )

    # An event that indicates that the user wants to update an answer
    REQUEST_ANSWER_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:answer:update"
    )

    # An event that indicates that the application should be stopped
    REQUEST_APPLICATION_STOP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:application:stop")
    )

    # An event that indicates that the user wants to create a new association
    REQUEST_ASSOCIATION_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:association:create")
    )

    # An event that indicates that the user wants to delete an association
    REQUEST_ASSOCIATION_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:association:delete")
    )

    # An event that indicates that the user wants to load an association
    REQUEST_ASSOCIATION_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:association:load")
    )

    # An event that indicates that the user wants to lookup an association
    REQUEST_ASSOCIATION_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:association:lookup")
    )

    # An event that indicates that the user wants to update an association
    REQUEST_ASSOCIATION_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:association:update")
    )

    # An event that indicates that the user wants to go backward in the navigation stack
    REQUEST_BACKWARD_NAVIGATION: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:backward:navigation")
    )

    # An event that indicates that the user wants to create a new change history
    REQUEST_CHANGE_HISTORY_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:change_history:create")
    )

    # An event that indicates that the user wants to delete a change history
    REQUEST_CHANGE_HISTORY_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:change_history:delete")
    )

    # An event that indicates that the user wants to load a change history
    REQUEST_CHANGE_HISTORY_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:change_history:load")
    )

    # An event that indicates that the user wants to lookup a change history
    REQUEST_CHANGE_HISTORY_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:change_history:lookup")
    )

    # An event that indicates that the user wants to update a change history
    REQUEST_CHANGE_HISTORY_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:change_history:update")
    )

    # An event that indicates that the user wants to create a new change history item
    REQUEST_CHANGE_HISTORY_ITEM_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:create"
        )
    )

    # An event that indicates that the user wants to delete a change history item
    REQUEST_CHANGE_HISTORY_ITEM_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:delete"
        )
    )

    # An event that indicates that the user wants to load a change history item
    REQUEST_CHANGE_HISTORY_ITEM_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:load"
        )
    )

    # An event that indicates that the user wants to lookup a change history item
    REQUEST_CHANGE_HISTORY_ITEM_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:lookup"
        )
    )

    # An event that indicates that the user wants to update a change history item
    REQUEST_CHANGE_HISTORY_ITEM_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:change_history_item:update"
        )
    )

    # An event that indicates that the user wants to create a new custom field
    REQUEST_CUSTOM_FIELD_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:custom_field:create")
    )

    # An event that indicates that the user wants to delete a custom field
    REQUEST_CUSTOM_FIELD_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:custom_field:delete")
    )

    # An event that indicates that the user wants to load a custom field
    REQUEST_CUSTOM_FIELD_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:custom_field:load")
    )

    # An event that indicates that the user wants to lookup a custom field
    REQUEST_CUSTOM_FIELD_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:custom_field:lookup")
    )

    # An event that indicates that the user wants to update a custom field
    REQUEST_CUSTOM_FIELD_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:custom_field:update")
    )

    # An event that indicates that the user wants to create a new difficulty
    REQUEST_DIFFICULTY_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:difficulty:create")
    )

    # An event that indicates that the user wants to delete a difficulty
    REQUEST_DIFFICULTY_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:difficulty:delete")
    )

    # An event that indicates that the user wants to load a difficulty
    REQUEST_DIFFICULTY_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:difficulty:load")
    )

    # An event that indicates that the user wants to lookup a difficulty
    REQUEST_DIFFICULTY_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:difficulty:lookup")
    )

    # An event that indicates that the user wants to update a difficulty
    REQUEST_DIFFICULTY_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:difficulty:update")
    )

    # An event that indicates that the user wants to exit the main UI loop
    REQUEST_EXIT_UI_MAINLOOP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:exit:mainloop")
    )

    # An event that indicates that the user wants to go forward in the navigation stack
    REQUEST_FORWARD_NAVIGATION: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:forward:navigation")
    )

    # An event that indicates that the user wants to create a new flashcard
    REQUEST_FLASHCARD_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:flashcard:create")
    )

    # An event that indicates that the user wants to delete a flashcard
    REQUEST_FLASHCARD_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:flashcard:delete")
    )

    # An event that indicates that the user wants to flip the flashcard in the flashcard learning view
    REQUEST_FLASHCARD_LEARNING_VIEW_FLIP_FLASHCARD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="learningsessionui:request:flashcard_learning_view:flip_flashcard"
        )
    )

    # An event that indicates that the user wants to load a flashcard in the flashcard learning view
    REQUEST_FLASHCARD_LEARNING_VIEW_LOAD_FLASHCARD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="learningsessionui:request:flashcard_learning_view:load_flashcard"
        )
    )

    # An event that indicates that the user wants to load a flashcard
    REQUEST_FLASHCARD_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:flashcard:load")
    )

    # An event that indicates that the user wants to lookup a flashcard
    REQUEST_FLASHCARD_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:flashcard:lookup")
    )

    # An event that indicates that the user wants to update a flashcard
    REQUEST_FLASHCARD_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:flashcard:update")
    )

    # An event that indicates that the user wants to get all answers
    REQUEST_GET_ALL_ANSWERS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:answers")
    )

    # An event that indicates that the user wants to get all associations
    REQUEST_GET_ALL_ASSOCIATIONS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:associations")
    )

    # An event that indicates that the user wants to get all change histories
    REQUEST_GET_ALL_CHANGE_HISTORIES: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:get:all:change:histories"
        )
    )

    # An event that indicates that the user wants to get all change history items
    REQUEST_GET_ALL_CHANGE_HISTORY_ITEMS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:get:all:change:history:items"
        )
    )

    # An event that indicates that the user wants to get all custom fields
    REQUEST_GET_ALL_CUSTOM_FIELDS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:custom:fields")
    )

    # An event that indicates that the user wants to get all defaults
    REQUEST_GET_ALL_DEFAULTS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:defaults")
    )

    # An event that indicates that the user wants to get all difficulties
    REQUEST_GET_ALL_DIFFICULTIES: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:difficulties")
    )

    # An event that indicates that the user wants to get all flashcards
    REQUEST_GET_ALL_FLASHCARDS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:flashcards")
    )

    # An event that indicates that the user wants to get all notes
    REQUEST_GET_ALL_NOTES: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:get:all:notes"
    )

    # An event that indicates that the user wants to get all options
    REQUEST_GET_ALL_OPTIONS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:options")
    )

    # An event that indicates that the user wants to get all priorities
    REQUEST_GET_ALL_PRIORITIES: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:priorities")
    )

    # An event that indicates that the user wants to get all questions
    REQUEST_GET_ALL_QUESTIONS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:questions")
    )

    # An event that indicates that the user wants to get all settings
    REQUEST_GET_ALL_SETTINGS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:settings")
    )

    # An event that indicates that the user wants to get all stacks
    REQUEST_GET_ALL_STACKS: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:stacks")
    )

    # An event that indicates that the user wants to get all statuses
    REQUEST_GET_ALL_STATUSES: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:get:all:statuses")
    )

    # An event that indicates that the user wants to get all tags
    REQUEST_GET_ALL_TAGS: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:get:all:tags"
    )

    # An event that indicates that the user wants to get all users
    REQUEST_GET_ALL_USERS: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:get:all:users"
    )

    # An event that indicates that the user wants to get an object by its key
    REQUEST_GET_BY_KEY: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:get:by:key"
    )

    # An event that indicates that the user wants to get objects by their keys
    REQUEST_GET_BY_KEYS: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:get:by:keys"
    )

    # An event that indicates that the user wants to create a new learning session
    REQUEST_LEARNING_SESSION_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session:create"
        )
    )

    # An event that indicates that the user wants to delete a learning session
    REQUEST_LEARNING_SESSION_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session:delete"
        )
    )

    # An event that indicates that the user wants to load a learning session
    REQUEST_LEARNING_SESSION_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:learning_session:load")
    )

    # An event that indicates that the user wants to lookup a learning session
    REQUEST_LEARNING_SESSION_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session:lookup"
        )
    )

    # An event that indicates that the user wants to update a learning session
    REQUEST_LEARNING_SESSION_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session:update"
        )
    )

    # An event that indicates that the user wants to create a new learning session action
    REQUEST_LEARNING_SESSION_ACTION_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_action:create"
        )
    )

    # An event that indicates that the user wants to delete a learning session action
    REQUEST_LEARNING_SESSION_ACTION_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_action:delete"
        )
    )

    # An event that indicates that the user wants to load a learning session action
    REQUEST_LEARNING_SESSION_ACTION_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_action:load"
        )
    )

    # An event that indicates that the user wants to lookup a learning session action
    REQUEST_LEARNING_SESSION_ACTION_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_action:lookup"
        )
    )

    # An event that indicates that the user wants to update a learning session action
    REQUEST_LEARNING_SESSION_ACTION_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_action:update"
        )
    )

    # An event that indicates that the user wants to create a new learning session item
    REQUEST_LEARNING_SESSION_ITEM_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_item:create"
        )
    )

    # An event that indicates that the user wants to delete a learning session item
    REQUEST_LEARNING_SESSION_ITEM_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_item:delete"
        )
    )

    # An event that indicates that the user wants to load a learning session item
    REQUEST_LEARNING_SESSION_ITEM_LOAD: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_item:load"
        )
    )

    # An event that indicates that the user wants to lookup a learning session item
    REQUEST_LEARNING_SESSION_ITEM_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_item:lookup"
        )
    )

    # An event that indicates that the user wants to update a learning session item
    REQUEST_LEARNING_SESSION_ITEM_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="global:request:learning_session_item:update"
        )
    )

    # An event that indicates that the user wants to get the index and limit of the learning session runner
    REQUEST_LEARNING_SESSION_RUNNER_GET_INDEX_AND_LIMIT: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="ui:request:learning_session_runner:get_index_and_limit"
        )
    )

    # An event that indicates that the user wants to log a user action in the learning session runner
    REQUEST_LEARNING_SESSION_RUNNER_LOG_USER_ACTION: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="ui:request:learning_session_runner:log_user_action"
        )
    )

    # An event that indicates that the user wants to load the next item in the learning session runner
    REQUEST_LEARNING_SESSION_RUNNER_LOAD_NEXT_ITEM: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="ui:request:learning_session_runner:load_next_item"
        )
    )

    # An event that indicates that the user wants to load the previous item in the learning session runner
    REQUEST_LEARNING_SESSION_RUNNER_LOAD_PREVIOUS_ITEM: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="ui:request:learning_session_runner:load_previous_item"
        )
    )

    # An event that indicates that the user wants to create a new note
    REQUEST_NOTE_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:note:create"
    )

    # An event that indicates that the user wants to delete a note
    REQUEST_NOTE_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:note:delete"
    )

    # An event that indicates that the user wants to hide the note in the note learning view
    REQUEST_NOTE_LEARNING_VIEW_HIDE_NOTE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="learningsessionui:request:note_learning_view:hide_note"
        )
    )

    # An event that indicates that the user wants to load a note in the note learning view
    REQUEST_NOTE_LEARNING_VIEW_LOAD_NOTE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="learningsessionui:request:note_learning_view:load_note"
        )
    )

    # An event that indicates that the user wants to show the note in the note learning view
    REQUEST_NOTE_LEARNING_VIEW_SHOW_NOTE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="learningsessionui:request:note_learning_view:show_note"
        )
    )

    # An event that indicates that the user wants to load a note
    REQUEST_NOTE_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:note:load"
    )

    # An event that indicates that the user wants to lookup a note
    REQUEST_NOTE_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:note:lookup"
    )

    # An event that indicates that the user wants to update a note
    REQUEST_NOTE_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:note:update"
    )

    # An event that indicates that the user wants to create a new option
    REQUEST_OPTION_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:option:create"
    )

    # An event that indicates that the user wants to delete a option
    REQUEST_OPTION_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:option:delete"
    )

    # An event that indicates that the user wants to load a option
    REQUEST_OPTION_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:option:load"
    )

    # An event that indicates that the user wants to lookup an option
    REQUEST_OPTION_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:option:lookup"
    )

    # An event that indicates that the user wants to update a option
    REQUEST_OPTION_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:option:update"
    )

    # An event that indicates that the user wants to create a new priority
    REQUEST_PRIORITY_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:priority:create")
    )

    # An event that indicates that the user wants to delete a priority
    REQUEST_PRIORITY_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:priority:delete")
    )

    # An event that indicates that the user wants to load a priority
    REQUEST_PRIORITY_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:priority:load"
    )

    # An event that indicates that the user wants to lookup a priority
    REQUEST_PRIORITY_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:priority:lookup")
    )

    # An event that indicates that the user wants to update a priority
    REQUEST_PRIORITY_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:priority:update")
    )

    # An event that indicates that the user wants to create a new question
    REQUEST_QUESTION_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:question:create")
    )

    # An event that indicates that the user wants to delete a question
    REQUEST_QUESTION_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:question:delete")
    )

    # An event that indicates that the user wants to load a question in the question learning view
    REQUEST_QUESTION_LEARNING_VIEW_LOAD_QUESTION: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(
            name="learningsessionui:request:question_learning_view:load_question"
        )
    )

    # An event that indicates that the user wants to load a question
    REQUEST_QUESTION_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:question:load"
    )

    # An event that indicates that the user wants to lookup a question
    REQUEST_QUESTION_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:question:lookup")
    )

    # An event that indicates that the user wants to update a question
    REQUEST_QUESTION_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:question:update")
    )

    # An event that indicates that the user wants to create a new setting
    REQUEST_SETTING_CREATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:setting:create")
    )

    # An event that indicates that the user wants to delete a setting
    REQUEST_SETTING_DELETE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:setting:delete")
    )

    # An event that indicates that the user wants to load a setting
    REQUEST_SETTING_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:setting:load"
    )

    # An event that indicates that the user wants to lookup a setting
    REQUEST_SETTING_LOOKUP: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:setting:lookup")
    )

    # An event that indicates that the user wants to update a setting
    REQUEST_SETTING_UPDATE: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:setting:update")
    )

    # An event that indicates that the user wants to create a new stack
    REQUEST_STACK_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:stack:create"
    )

    # An event that indicates that the user wants to delete a stack
    REQUEST_STACK_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:stack:delete"
    )

    # An event that indicates that the user wants to load a stack
    REQUEST_STACK_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:stack:load"
    )

    # An event that indicates that the user wants to lookup a stack
    REQUEST_STACK_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:stack:lookup"
    )

    # An event that indicates that the user wants to update a stack
    REQUEST_STACK_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:stack:update"
    )

    # An event that indicates that the user wants to create a new status
    REQUEST_STATUS_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:status:create"
    )

    # An event that indicates that the user wants to delete a status
    REQUEST_STATUS_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:status:delete"
    )

    # An event that indicates that the user wants to load a status
    REQUEST_STATUS_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:status:load"
    )

    # An event that indicates that the user wants to lookup a status
    REQUEST_STATUS_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:status:lookup"
    )

    # An event that indicates that the user wants to update a status
    REQUEST_STATUS_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:status:update"
    )

    # An event that indicates that the user wants to create a new tag
    REQUEST_TAG_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:tag:create"
    )

    # An event that indicates that the user wants to delete a tag
    REQUEST_TAG_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:tag:delete"
    )

    # An event that indicates that the user wants to load a tag
    REQUEST_TAG_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:tag:load"
    )

    # An event that indicates that the user wants to lookup a tag
    REQUEST_TAG_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:tag:lookup"
    )

    # An event that indicates that the user wants to update a tag
    REQUEST_TAG_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:tag:update"
    )

    # An event that indicates that the user wants to pause a timer
    REQUEST_TIMER_PAUSE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:timer:pause"
    )

    # An event that indicates that the user wants to resume a timer
    REQUEST_TIMER_RESUME: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:timer:resume"
    )

    # An event that indicates that the user wants to start a timer
    REQUEST_TIMER_START: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:timer:start"
    )

    # An event that indicates that the user wants to stop a timer
    REQUEST_TIMER_STOP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:timer:stop"
    )

    # An event that indicates that the navigator requests the ui to validate navigation
    REQUEST_UI_VALIDATE_NAVIGATION: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:request:validate:navigation")
    )

    # An event that indicates that the user wants to update an object
    REQUEST_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:update"
    )

    # An event that indicates that the user wants to update objects in bulk
    REQUEST_UPDATE_IN_BULK: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:update_in_bulk")
    )

    # An event that indicates that the user wants to create a new user
    REQUEST_USER_CREATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:user:create"
    )

    # An event that indicates that the user wants to delete a user
    REQUEST_USER_DELETE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:user:delete"
    )

    # An event that indicates that the user wants to load a user
    REQUEST_USER_LOAD: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:user:load"
    )

    # An event that indicates that the user wants to lookup a user
    REQUEST_USER_LOOKUP: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:user:lookup"
    )

    # An event that indicates that the user wants to update a user
    REQUEST_USER_UPDATE: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="global:request:user:update"
    )

    # An event that indicates that the user wants to validate navigation
    REQUEST_VALIDATE_NAVIGATION: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="global:request:validate:navigation")
    )

    # An event that indicates that a scale field has been changed
    SCALE_FIELD_CHANGED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:scale:field:changed"
    )

    # An event that indicates that a scale field has been cleared
    SCALE_FIELD_CLEARED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:scale:field:cleared"
    )

    # An event that indicates that a scale field has been retrieved
    SCALE_FIELD_GET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:scale:field:get"
    )

    # An event that indicates that a scale field has been set
    SCALE_FIELD_SET: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:scale:field:set"
    )

    # An event that indicates that the settings button has been clicked
    SETTINGS_BUTTON_CLICKED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:settings:button:clicked")
    )

    # An event that indicates that the search query has been changed
    SEARCH_QUERY_CHANGED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:search:query:changed"
    )

    # An event that indicates that a single line text field has been changed
    SINGLE_LINE_TEXT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_line_text:field:changed")
    )

    # An event that indicates that a single line text field has been cleared
    SINGLE_LINE_TEXT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_line_text:field:cleared")
    )

    # An event that indicates that a single line text field has been retrieved
    SINGLE_LINE_TEXT_FIELD_GET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_line_text:field:get")
    )

    # An event that indicates that a single line text field has been set
    SINGLE_LINE_TEXT_FIELD_SET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_line_text:field:set")
    )

    # An event that indicates that a single select field has been changed
    SINGLE_SELECT_FIELD_CHANGED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_select:field:changed")
    )

    # An event that indicates that a single select field has been cleared
    SINGLE_SELECT_FIELD_CLEARED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_select:field:cleared")
    )

    # An event that indicates that a single select field has been retrieved
    SINGLE_SELECT_FIELD_GET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_select:field:get")
    )

    # An event that indicates that a single select field has been set
    SINGLE_SELECT_FIELD_SET: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="ui:single_select:field:set")
    )

    # An event that indicates that a stack has been created in the backend
    STACK_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:stack:created"
    )

    # An event that indicates that a stack has been deleted in the backend
    STACK_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:stack:deleted"
    )

    # An event that indicates that a stack has been loaed in the backend
    STACK_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:stack:loaded"
    )

    # An event that indicates that a stack has been updated in the backend
    STACK_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:stack:updated"
    )

    # An event that indicates that a tag has been created in the backend
    TAG_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:tag:created"
    )

    # An event that indicates that a tag has been deleted in the backend
    TAG_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:tag:deleted"
    )

    # An event that indicates that a tag has been loaed in the backend
    TAG_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:tag:loaded"
    )

    # An event that indicates that a tag has been updated in the backend
    TAG_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:tag:updated"
    )

    # An event that indicates that a text analysis has been completed
    TEXT_ANALYZER_ANALYSIS_COMPLETED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="text_analyzer:analysis:completed")
    )

    # An event that indicates that a text analysis has been started
    TEXT_ANALYZER_ANALYSIS_STARTED: Final[DispatcherEvent] = (
        DispatcherEventFactory.create_event(name="text_analyzer:analysis:started")
    )

    # An event that indicates that a toast has been clicked
    TOAST_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:toast:clicked"
    )

    # An event that indicates that a toast has been destroyed
    TOAST_DESTROYED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:toast:destroyed"
    )

    # An event that indicates that the timer has been started
    TIMER_STARTED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:timer:started"
    )

    # An event that indicates that the timer has been stopped
    TIMER_STOPPED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:timer:stopped"
    )

    # An event that indicates that the user button has been clicked
    USER_BUTTON_CLICKED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="ui:button:user:clicked"
    )

    # An event that indicates that a user has been created in the backend
    USER_CREATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:user:created"
    )

    # An event that indicates that a user has been deleted in the backend
    USER_DELETED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:user:deleted"
    )

    # An event that indicates that a user has been loaed in the backend
    USER_LOADED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:user:loaded"
    )

    # An event that indicates that a user has been updated in the backend
    USER_UPDATED: Final[DispatcherEvent] = DispatcherEventFactory.create_event(
        name="backend:user:updated"
    )

    @classmethod
    def get_all_events(
        cls,
        as_dict: bool = False,
    ) -> Union[List[DispatcherEvent], Dict[str, DispatcherEvent]]:
        """
        Returns a list or dictionary of all events in the Events class.

        Args:
            as_dict (bool, optional): If True, returns a dictionary of events; otherwise, returns a list of events. Defaults to False.

        Returns:
            Union[List[DispatcherEvent], Dict[str, DispatcherEvent]]: A list or dictionary of all events in the Events class.
        """
        if as_dict:
            return {
                value.name: value
                for value in cls.__dict__.values()
                if isinstance(
                    value,
                    DispatcherEvent,
                )
            }

        return [
            value
            for value in cls.__dict__.values()
            if isinstance(
                value,
                DispatcherEvent,
            )
        ]

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
        event: Optional[DispatcherEvent] = next(
            (event for event in cls.get_all_events() if event.name == name),
            None,
        )

        if not event:
            # Log a warning message
            cls.logger.warning(f"Event with name '{name}' not found.")

        return event

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
    def get_checkbutton_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all checkbutton field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all checkbutton field events in the Events class.
        """
        return [
            cls.CHECKBUTTON_FIELD_CHANGED,
            cls.CHECKBUTTON_FIELD_CLEARED,
            cls.CHECKBUTTON_FIELD_GET,
            cls.CHECKBUTTON_FIELD_SET,
        ]

    @classmethod
    def get_combobox_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all combobox field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all combobox field events in the Events class.
        """
        return [
            cls.COMBOBOX_FIELD_CHANGED,
            cls.COMBOBOX_FIELD_CLEARED,
            cls.COMBOBOX_FIELD_GET,
            cls.COMBOBOX_FIELD_SET,
        ]

    @classmethod
    def get_combobox_select_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all combobox select field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all combobox select field events in the Events class.
        """
        return [
            cls.COMBOBOX_SELECT_FIELD_CHANGED,
            cls.COMBOBOX_SELECT_FIELD_CLEARED,
            cls.COMBOBOX_SELECT_FIELD_GET,
            cls.COMBOBOX_SELECT_FIELD_SET,
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
    def get_date_select_fiel_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all date select field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all date select field events in the Events class.
        """
        return [
            cls.DATE_SELECT_FIELD_CHANGED,
            cls.DATE_SELECT_FIELD_CLEARED,
            cls.DATE_SELECT_FIELD_GET,
            cls.DATE_SELECT_FIELD_SET,
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
    def get_float_spinbox_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all float spinbox field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all float spinbox field events in the Events class.
        """
        return [
            cls.FLOAT_SPINBOX_FIELD_CHANGED,
            cls.FLOAT_SPINBOX_FIELD_CLEARED,
            cls.FLOAT_SPINBOX_FIELD_GET,
            cls.FLOAT_SPINBOX_FIELD_SET,
        ]

    @classmethod
    def get_int_spinbox_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all int spinbox field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all int spinbox field events in the Events class.
        """
        return [
            cls.INT_SPINBOX_FIELD_CHANGED,
            cls.INT_SPINBOX_FIELD_CLEARED,
            cls.INT_SPINBOX_FIELD_GET,
            cls.INT_SPINBOX_FIELD_SET,
        ]

    @classmethod
    def get_learning_session_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all learning session events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all learning session events in the Events class.
        """
        return [
            cls.REQUEST_LEARNING_SESSION_CREATE,
            cls.REQUEST_LEARNING_SESSION_DELETE,
            cls.REQUEST_LEARNING_SESSION_LOAD,
            cls.REQUEST_LEARNING_SESSION_LOOKUP,
            cls.REQUEST_LEARNING_SESSION_UPDATE,
        ]

    @classmethod
    def get_learning_session_action_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all learning session action events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all learning session action events in the Events class.
        """
        return [
            cls.REQUEST_LEARNING_SESSION_ACTION_CREATE,
            cls.REQUEST_LEARNING_SESSION_ACTION_DELETE,
            cls.REQUEST_LEARNING_SESSION_ACTION_LOAD,
            cls.REQUEST_LEARNING_SESSION_ACTION_LOOKUP,
            cls.REQUEST_LEARNING_SESSION_ACTION_UPDATE,
        ]

    @classmethod
    def get_learning_session_item_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all learning session item events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all learning session item events in the Events class.
        """
        return [
            cls.REQUEST_LEARNING_SESSION_ITEM_CREATE,
            cls.REQUEST_LEARNING_SESSION_ITEM_DELETE,
            cls.REQUEST_LEARNING_SESSION_ITEM_LOAD,
            cls.REQUEST_LEARNING_SESSION_ITEM_LOOKUP,
            cls.REQUEST_LEARNING_SESSION_ITEM_UPDATE,
        ]

    @classmethod
    def get_multi_line_text_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all multi line text field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all multi line text field events in the Events class.
        """
        return [
            cls.MULTI_LINE_TEXT_FIELD_CHANGED,
            cls.MULTI_LINE_TEXT_FIELD_CLEARED,
            cls.MULTI_LINE_TEXT_FIELD_GET,
            cls.MULTI_LINE_TEXT_FIELD_SET,
        ]

    @classmethod
    def get_multi_select_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all multi select field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all multi select field events in the Events class.
        """
        return [
            cls.MULTI_SELECT_FIELD_CHANGED,
            cls.MULTI_SELECT_FIELD_CLEARED,
            cls.MULTI_SELECT_FIELD_GET,
            cls.MULTI_SELECT_FIELD_SET,
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
    def get_password_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all password field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all password field events in the Events class.
        """
        return [
            cls.PASSWORD_TEXT_FIELD_CHANGED,
            cls.PASSWORD_TEXT_FIELD_GET,
            cls.PASSWORD_TEXT_FIELD_SET,
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
    def get_radiobutton_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all radiobutton field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all radiobutton field events in the Events class.
        """
        return [
            cls.RADIOBUTTON_FIELD_CHANGED,
            cls.RADIOBUTTON_FIELD_CLEARED,
            cls.RADIOBUTTON_FIELD_GET,
            cls.RADIOBUTTON_FIELD_SET,
        ]

    @classmethod
    def get_radiobutton_select_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all radiobutton select field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all radiobutton select field events in the Events class.
        """
        return [
            cls.RADIOBUTTON_SELECT_FIELD_CHANGED,
            cls.RADIOBUTTON_SELECT_FIELD_CLEARED,
            cls.RADIOBUTTON_SELECT_FIELD_GET,
            cls.RADIOBUTTON_SELECT_FIELD_SET,
        ]
    
    @classmethod
    def get_readonly_multi_line_text_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all readonly multi line text field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all readonly multi line text field events in the Events class.
        """
        return [
            cls.READONLY_MULTI_LINE_TEXT_FIELD_CHANGED,
            cls.READONLY_MULTI_LINE_TEXT_FIELD_CLEARED,
            cls.READONLY_MULTI_LINE_TEXT_FIELD_GET,
            cls.READONLY_MULTI_LINE_TEXT_FIELD_SET,
        ]

    @classmethod
    def get_readonly_single_line_text_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all readonly single line text field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all readonly single line text field events in the Events class.
        """
        return [
            cls.READONLY_SINGLE_LINE_TEXT_FIELD_CHANGED,
            cls.READONLY_SINGLE_LINE_TEXT_FIELD_CLEARED,
            cls.READONLY_SINGLE_LINE_TEXT_FIELD_GET,
            cls.READONLY_SINGLE_LINE_TEXT_FIELD_SET,
        ]

    @classmethod
    def get_scale_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all scale field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all scale field events in the Events class.
        """
        return [
            cls.SCALE_FIELD_CHANGED,
            cls.SCALE_FIELD_CLEARED,
            cls.SCALE_FIELD_GET,
            cls.SCALE_FIELD_SET,
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
    def get_single_line_text_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all single line text field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all single line text field events in the Events class.
        """
        return [
            cls.SINGLE_LINE_TEXT_FIELD_CHANGED,
            cls.SINGLE_LINE_TEXT_FIELD_CLEARED,
            cls.SINGLE_LINE_TEXT_FIELD_GET,
            cls.SINGLE_LINE_TEXT_FIELD_SET,
        ]

    @classmethod
    def get_single_select_field_events(cls) -> List[DispatcherEvent]:
        """
        Returns a list of all single select field events in the Events class.

        Returns:
            List[DispatcherEvent]: A list of all single select field events in the Events class.
        """
        return [
            cls.SINGLE_SELECT_FIELD_CHANGED,
            cls.SINGLE_SELECT_FIELD_CLEARED,
            cls.SINGLE_SELECT_FIELD_GET,
            cls.SINGLE_SELECT_FIELD_SET,
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
