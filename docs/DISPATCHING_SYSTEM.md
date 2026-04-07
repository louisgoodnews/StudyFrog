# StudyFrog Dispatching System Documentation

## Overview

The dispatching system is the **central nervous system** of StudyFrog, implementing a publish-subscribe pattern that enables loose coupling between components. It's the primary way information travels through the application, allowing different modules to communicate without direct dependencies.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Core Components](#core-components)
3. [Event Types and Namespaces](#event-types-and-namespaces)
4. [Subscription Management](#subscription-management)
5. [Event Dispatching](#event-dispatching)
6. [Advanced Features](#advanced-features)
7. [Usage Patterns](#usage-patterns)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Architecture Overview

### Publish-Subscribe Pattern

The dispatching system implements the classic publish-subscribe pattern:

```
Publisher (Component A) → Event → Dispatcher → Subscribers (Components B, C, D)
                                      ↘ Component E
                                      ↘ Component F
```

**Key Benefits:**
- **Loose Coupling**: Components don't need to know about each other
- **Flexibility**: Easy to add new subscribers without changing publishers
- **Scalability**: One event can have multiple subscribers
- **Testability**: Components can be tested in isolation

### Data Flow

```
1. Event occurs in Component A
2. Component A calls dispatch(event, data)
3. Dispatcher finds all subscribers to event
4. Dispatcher calls each subscriber with event data
5. Subscribers process the event independently
```

### System Architecture

```python
# Core data structures
SUBSCRIBERS = {
    "EVENT_NAME": {
        "NAMESPACE": {
            "UUID_1": {
                "event": "EVENT_NAME",
                "namespace": "NAMESPACE", 
                "function": {...},
                "persistent": False,
                "priority": 0,
                "uuid": "UUID_1"
            },
            "UUID_2": {...}
        }
    }
}

UUIDS = {
    "UUID_1": {
        "event": "EVENT_NAME",
        "namespace": "NAMESPACE"
    }
}
```

---

## Core Components

### 1. Dispatcher Functions

The dispatcher provides several core functions in `src/studyfrog/utils/dispatcher.py`:

#### `dispatch()` - Main Event Dispatcher

```python
def dispatch(
    *args: tuple[Any],
    event: str,
    namespace: str = GLOBAL,
    **kwargs: dict[str, Any],
) -> dict[str, Any]:
```

**Purpose**: Dispatches an event to all subscribers in a specific namespace.

**Parameters**:
- `event`: The event name (case-insensitive)
- `namespace`: The namespace (defaults to 'GLOBAL')
- `*args`: Positional arguments passed to subscribers
- `**kwargs`: Keyword arguments passed to subscribers

**Returns**: Dictionary with dispatch results and metadata

**Example**:
```python
# Dispatch a flashcard creation event
dispatch(
    FLASHCARD_CREATED,
    flashcard=new_flashcard,
    source="create_view",
    timestamp=datetime.now()
)
```

#### `subscribe()` - Event Subscription

```python
def subscribe(
    event: str,
    function: Callable[[..., Any], Any],
    namespace: str = GLOBAL,
    persistent: bool = False,
    priority: int = 0,
) -> str:
```

**Purpose**: Subscribes a function to receive events.

**Parameters**:
- `event`: Event name to subscribe to
- `function`: Callback function to execute
- `namespace`: Namespace (defaults to 'GLOBAL')
- `persistent`: Whether subscription persists after one-time use
- `priority`: Priority (higher = called first)

**Returns**: UUID string for the subscription

**Example**:
```python
def handle_flashcard_created(flashcard, **kwargs):
    print(f"New flashcard: {flashcard.front}")

subscription_id = subscribe(
    FLASHCARD_CREATED,
    handle_flashcard_created,
    priority=10  # High priority
)
```

#### `unsubscribe()` - Remove Subscription

```python
def unsubscribe(uuid: str) -> bool:
```

**Purpose**: Removes a subscription using its UUID.

**Parameters**:
- `uuid`: The subscription UUID returned by `subscribe()`

**Returns**: True if successful, False if not found

**Example**:
```python
# Unsubscribe from event
success = unsubscribe(subscription_id)
```

### 2. Bulk Operations

#### `bulk_dispatch()` - Multiple Events

```python
def bulk_dispatch(
    *args: tuple[Any],
    events: list[str],
    namespaces: list[str],
    **kwargs: dict[str, Any],
) -> list[dict[str, Any]]:
```

**Purpose**: Dispatches multiple events to multiple namespaces efficiently.

**Example**:
```python
results = bulk_dispatch(
    data,
    events=[FLASHCARD_CREATED, STACK_UPDATED],
    namespaces=['GLOBAL', 'STORAGE'],
    source="bulk_operation"
)
```

#### `bulk_subscribe()` - Multiple Subscriptions

```python
def bulk_subscribe(
    events: list[str],
    functions: list[Callable[[..., Any], Any]],
    namespaces: list[str],
    priorities: list[int],
    persistents: list[bool],
) -> list[str]:
```

**Purpose**: Subscribe multiple functions to multiple events efficiently.

**Example**:
```python
subscription_ids = bulk_subscribe(
    events=[FLASHCARD_CREATED, FLASHCARD_UPDATED, FLASHCARD_DELETED],
    functions=[handle_created, handle_updated, handle_deleted],
    namespaces=['GLOBAL'] * 3,
    priorities=[10, 10, 10],
    persistents=[False, False, False]
)
```

---

## Event Types and Namespaces

### Event Categories

The system defines over 100 events organized into logical categories:

#### Application Lifecycle Events

```python
APPLICATION_STARTING = "APPLICATION_STARTING"
APPLICATION_STARTED = "APPLICATION_STARTED"
APPLICATION_STOPPING = "APPLICATION_STOPPING"
APPLICATION_STOPPED = "APPLICATION_STOPPED"
```

#### CRUD Events

```python
# Flashcard events
FLASHCARD_CREATED = "FLASHCARD_CREATED"
FLASHCARD_UPDATED = "FLASHCARD_UPDATED"
FLASHCARD_DELETED = "FLASHCARD_DELETED"
ADD_FLASHCARD_TO_DB = "ADD_FLASHCARD_TO_DB"
ALL_FLASHCARDS_RETRIEVED = "ALL_FLASHCARDS_RETRIEVED"

# Stack events
STACK_CREATED = "STACK_CREATED"
STACK_UPDATED = "STACK_UPDATED"
STACK_DELETED = "STACK_DELETED"
ADD_STACK_TO_DB = "ADD_STACK_TO_DB"

# Question/Answer events
QUESTION_CREATED = "QUESTION_CREATED"
ANSWER_CREATED = "ANSWER_CREATED"
ADD_QUESTION_TO_DB = "ADD_QUESTION_TO_DB"
ADD_ANSWER_TO_DB = "ADD_ANSWER_TO_DB"
```

#### GUI Events

```python
# Navigation events
GET_DASHBOARD_VIEW = "GET_DASHBOARD_VIEW"
GET_CREATE_VIEW = "GET_CREATE_VIEW"
GET_EDIT_VIEW = "GET_EDIT_VIEW"
GET_REHEARSAL_RUN_SETUP_VIEW = "GET_REHEARSAL_RUN_SETUP_VIEW"

# Interaction events
CLICKED_CANCEL_BUTTON = "CLICKED_CANCEL_BUTTON"
CLICKED_EASY_BUTTON = "CLICKED_EASY_BUTTON"
CLICKED_SAVE_BUTTON = "CLICKED_SAVE_BUTTON"
```

#### Rehearsal Events

```python
REHEARSAL_RUN_STARTED = "REHEARSAL_RUN_STARTED"
REHEARSAL_RUN_COMPLETED = "REHEARSAL_RUN_COMPLETED"
ADD_REHEARSAL_RUN_TO_DB = "ADD_REHEARSAL_RUN_TO_DB"
ADD_REHEARSAL_RUN_ITEM_TO_DB = "ADD_REHEARSAL_RUN_ITEM_TO_DB"
```

### Namespaces

Namespaces provide logical grouping and isolation:

```python
# Global namespace (default)
GLOBAL = "GLOBAL"

# Component-specific namespaces
STORAGE = "STORAGE"
GUI = "GUI"
REHEARSAL = "REHEARSAL"
BOOTSTRAP = "BOOTSTRAP"
```

**Namespace Benefits**:
- **Isolation**: Events in one namespace don't affect others
- **Organization**: Logical grouping of related events
- **Debugging**: Easy to trace event flow in specific areas
- **Testing**: Can test specific namespaces independently

---

## Subscription Management

### Subscription Structure

Each subscription contains:

```python
subscription = {
    "event": "FLASHCARD_CREATED",           # Event name
    "namespace": "GLOBAL",                  # Namespace
    "function": {                           # Function details
        "function": callback_function,
        "name": "handle_flashcard_created"
    },
    "persistent": False,                     # One-time or persistent
    "priority": 10,                         # Execution priority
    "uuid": "550e8400-e29b-41d4-a716-446655440000"  # Unique identifier
}
```

### Priority System

Subscriptions are executed in priority order (highest first):

```python
# Priority levels
H_PRIORITY = 100      # Highest priority
MEDIUM_PRIORITY = 50   # Medium priority
LOW_PRIORITY = 10      # Low priority
DEFAULT_PRIORITY = 0    # Default priority
```

**Execution Order**:
1. Sort subscriptions by priority (descending)
2. Execute subscriptions with same priority in subscription order
3. Return results from all subscriptions

### Persistent vs Non-Persistent

```python
# Non-persistent (default) - removed after first execution
subscribe(FLASHCARD_CREATED, handle_one_time, persistent=False)

# Persistent - remains active until explicitly unsubscribed
subscribe(FLASHCARD_CREATED, handle_all, persistent=True)
```

### Subscription Lifecycle

1. **Creation**: `subscribe()` returns UUID
2. **Storage**: Subscription stored in `SUBSCRIBERS` and `UUIDS`
3. **Execution**: Called when matching event is dispatched
4. **Cleanup**: Non-persistent subscriptions auto-removed
5. **Removal**: `unsubscribe()` removes manually

---

## Event Dispatching

### Dispatch Process Flow

```python
def dispatch(event, namespace=GLOBAL, *args, **kwargs):
    # 1. Normalize inputs
    event = event.upper()
    namespace = namespace.upper()
    
    # 2. Validate event and namespace exist
    if event not in SUBSCRIBERS:
        return warning_result("Event not found")
    
    if namespace not in SUBSCRIBERS[event]:
        return warning_result("Namespace not found")
    
    # 3. Get subscriptions sorted by priority
    subscriptions = sorted(
        SUBSCRIBERS[event][namespace].values(),
        key=lambda x: x["priority"],
        reverse=True
    )
    
    # 4. Execute subscriptions
    results = {}
    non_persistent = []
    
    for subscription in subscriptions:
        try:
            # Execute callback
            result = subscription["function"]["function"](*args, **kwargs)
            results[subscription["function"]["name"]] = {
                "result": result,
                "uuid": subscription["uuid"]
            }
            
            # Track non-persistent for cleanup
            if not subscription["persistent"]:
                non_persistent.append(subscription["uuid"])
                
        except Exception as e:
            # Log error but continue with other subscriptions
            log_error(f"Subscription failed: {e}")
    
    # 5. Cleanup non-persistent subscriptions
    bulk_unsubscribe(non_persistent)
    
    # 6. Return results with metadata
    return {
        "event": event,
        "namespace": namespace,
        "args": args,
        "kwargs": kwargs,
        "start": timestamp,
        "end": timestamp,
        "duration": duration,
        "results": results
    }
```

### Event Data Format

#### Standard Event Data

```python
event_data = {
    "model": flashcard_instance,        # Primary model/data
    "action": "created",              # Action type
    "source": "create_view",          # Origin component
    "timestamp": datetime.now(),        # When event occurred
    "user_id": current_user_id,        # User context
    "metadata": {...}                  # Additional context
}
```

#### Common Event Patterns

```python
# Creation events
dispatch(FLASHCARD_CREATED, {
    "model": flashcard,
    "action": "created",
    "source": "create_view"
})

# Update events
dispatch(FLASHCARD_UPDATED, {
    "model": flashcard,
    "action": "updated", 
    "old_values": old_data,
    "new_values": new_data,
    "source": "edit_view"
})

# Deletion events
dispatch(FLASHCARD_DELETED, {
    "model_key": flashcard.key,
    "action": "deleted",
    "source": "edit_view"
})
```

---

## Advanced Features

### Bulk Operations

#### Bulk Dispatch

```python
# Dispatch multiple events efficiently
results = bulk_dispatch(
    flashcards,  # Common data
    events=[FLASHCARD_CREATED, STACK_UPDATED],
    namespaces=['GLOBAL', 'STORAGE'],
    source="bulk_import"
)
```

#### Bulk Subscribe

```python
# Subscribe multiple handlers efficiently
subscription_ids = bulk_subscribe(
    events=[FLASHCARD_CREATED, FLASHCARD_UPDATED, FLASHCARD_DELETED],
    functions=[handle_create, handle_update, handle_delete],
    namespaces=['GLOBAL', 'GLOBAL', 'GLOBAL'],
    priorities=[10, 10, 10],
    persistents=[True, True, True]
)
```

### Cross-Namespace Communication

```python
# Dispatch to specific namespace
dispatch(STORAGE_EVENT, data, namespace='STORAGE')

# Subscribe to specific namespace
subscribe(GUI_EVENT, handler, namespace='GUI')
```

### Event Chaining

```python
def handle_flashcard_created(flashcard, **kwargs):
    # Chain another event
    dispatch(STACK_ITEM_COUNT_CHANGED, {
        "stack_key": flashcard.stack_key,
        "change": "+1"
    })

subscribe(FLASHCARD_CREATED, handle_flashcard_created)
```

---

## Usage Patterns

### 1. Component Communication

#### GUI to Storage

```python
# In GUI component
def on_save_button_click():
    flashcard = get_form_data()
    
    # Dispatch event to trigger storage
    dispatch(ADD_FLASHCARD_TO_DB, {
        "model": flashcard,
        "source": "create_view"
    })

# In storage component
def handle_add_flashcard(model, **kwargs):
    success = add_entry(FLASHCARDS_DB_JSON, model)
    
    if success:
        # Dispatch success event
        dispatch(FLASHCARD_CREATED, {
            "model": model,
            "source": "storage"
        })

subscribe(ADD_FLASHCARD_TO_DB, handle_add_flashcard, namespace='STORAGE')
```

#### Model Updates

```python
# When model changes, notify interested components
def update_flashcard(flashcard, new_data):
    old_data = flashcard.to_dict()
    flashcard.update(new_data)
    
    # Dispatch update event
    dispatch(FLASHCARD_UPDATED, {
        "model": flashcard,
        "old_values": old_data,
        "new_values": new_data,
        "source": "edit_view"
    })

# GUI components listen for updates
subscribe(FLASHCARD_UPDATED, refresh_flashcard_display)
```

### 2. Workflow Orchestration

#### Multi-Step Workflows

```python
def create_flashcard_workflow(flashcard_data):
    # Step 1: Validate
    dispatch(FLASHCARD_VALIDATION_STARTED, flashcard_data)
    
    # Step 2: Create model
    flashcard = get_flashcard_model(**flashcard_data)
    dispatch(FLASHCARD_MODEL_CREATED, flashcard)
    
    # Step 3: Save to storage
    dispatch(ADD_FLASHCARD_TO_DB, {"model": flashcard})
    
    # Step 4: Update GUI
    dispatch(FLASHCARD_CREATED, {"model": flashcard})

# Each step has its own handler
subscribe(FLASHCARD_VALIDATION_STARTED, validate_flashcard_data)
subscribe(FLASHCARD_MODEL_CREATED, log_model_creation)
subscribe(ADD_FLASHCARD_TO_DB, storage_handler)
subscribe(FLASHCARD_CREATED, gui_refresh_handler)
```

### 3. Error Handling and Recovery

#### Error Event Pattern

```python
def safe_operation(data):
    try:
        result = risky_operation(data)
        dispatch(OPERATION_SUCCESS, {"result": result})
        return result
    except Exception as e:
        dispatch(OPERATION_ERROR, {
            "error": e,
            "data": data,
            "source": "safe_operation"
        })
        return None

def handle_operation_error(error, data, **kwargs):
    log_error(f"Operation failed: {error}")
    show_error_dialog(f"Error: {error}")
    
    # Optionally retry
    if should_retry(error):
        dispatch(OPERATION_RETRY, {"data": data})

subscribe(OPERATION_ERROR, handle_operation_error)
```

---

## Best Practices

### 1. Event Naming

```python
# Good - descriptive, consistent
FLASHCARD_CREATED
STACK_UPDATED
REHEARSAL_RUN_STARTED

# Avoid - unclear, inconsistent
FC_CREATED
STK_UPD
RRS_START
```

### 2. Namespace Usage

```python
# Good - logical grouping
dispatch(STORAGE_EVENT, data, namespace='STORAGE')
dispatch(GUI_EVENT, data, namespace='GUI')

# Avoid - everything in global
dispatch(EVERYTHING, data)  # Hard to debug and maintain
```

### 3. Data Structure

```python
# Good - structured, self-documenting
dispatch(FLASHCARD_CREATED, {
    "model": flashcard,
    "action": "created",
    "source": "create_view",
    "timestamp": datetime.now()
})

# Avoid - unstructured data
dispatch(FLASHCARD_CREATED, flashcard)  # What is this data?
```

### 4. Error Handling

```python
# Good - handle exceptions in subscriptions
def robust_handler(event_data):
    try:
        process_event(event_data)
    except Exception as e:
        log_error(f"Handler failed: {e}")
        # Don't let one failure break the whole system

subscribe(EVENT, robust_handler)
```

### 5. Memory Management

```python
# Good - cleanup non-persistent subscriptions
def temporary_handler(event_data):
    process_once(event_data)

# Use non-persistent for one-time handlers
subscribe(EVENT, temporary_handler, persistent=False)

# Good - unsubscribe when component destroyed
def cleanup_component():
    for subscription_id in component_subscriptions:
        unsubscribe(subscription_id)
```

### 6. Priority Usage

```python
# Good - use priorities for important handlers
subscribe(CRITICAL_EVENT, critical_handler, priority=100)
subscribe(NORMAL_EVENT, normal_handler, priority=50)
subscribe(LOG_EVENT, logging_handler, priority=10)

# Critical handlers execute first
```

---

## Troubleshooting

### Common Issues

#### 1. Events Not Being Received

**Problem**: Subscriber not getting events

**Causes**:
- Wrong event name (case sensitivity)
- Wrong namespace
- Subscription not properly registered

**Debugging**:
```python
# Check if event exists
print("Available events:", list(SUBSCRIBERS.keys()))

# Check if namespace exists
print("Available namespaces:", list(SUBSCRIBERS[event].keys()))

# Check subscription
print("Subscriptions:", SUBSCRIBERS[event][namespace])
```

#### 2. Subscription Not Working

**Problem**: `subscribe()` not working

**Causes**:
- Function signature mismatch
- Invalid parameters
- Event not defined

**Debugging**:
```python
def debug_handler(*args, **kwargs):
    print(f"Handler called with args: {args}, kwargs: {kwargs}")

try:
    subscription_id = subscribe(EVENT, debug_handler)
    print(f"Subscription successful: {subscription_id}")
except Exception as e:
    print(f"Subscription failed: {e}")
```

#### 3. Performance Issues

**Problem**: Slow event dispatching

**Causes**:
- Too many high-priority subscriptions
- Complex handler functions
- Inefficient bulk operations

**Solutions**:
```python
# Use appropriate priorities
subscribe(EVENT, simple_handler, priority=10)  # Only for critical handlers

# Optimize handler functions
def optimized_handler(event_data):
    # Fast processing, minimal work
    pass

# Use bulk operations
bulk_dispatch(events, namespaces, data)  # More efficient than multiple dispatch()
```

### Debug Tools

#### Event Logging

```python
def debug_dispatch(event, namespace, *args, **kwargs):
    print(f"DISPATCH: {event} in {namespace}")
    print(f"ARGS: {args}")
    print(f"KWARGS: {kwargs}")
    print(f"SUBSCRIBERS: {len(SUBSCRIBERS.get(event, {}).get(namespace, {}))}")
    
    # Call real dispatch
    return original_dispatch(event, namespace, *args, **kwargs)

# Monkey patch for debugging
original_dispatch = dispatch
dispatch = debug_dispatch
```

#### Subscription Tracking

```python
def list_all_subscriptions():
    """List all active subscriptions for debugging."""
    for event_name, namespaces in SUBSCRIBERS.items():
        print(f"\nEvent: {event_name}")
        for namespace, subscriptions in namespaces.items():
            print(f"  Namespace: {namespace}")
            for uuid, subscription in subscriptions.items():
                print(f"    {uuid}: {subscription['function']['name']} (priority: {subscription['priority']})")

# Call during debugging
list_all_subscriptions()
```

### Performance Monitoring

```python
def monitored_dispatch(*args, **kwargs):
    start_time = time.time()
    result = original_dispatch(*args, **kwargs)
    end_time = time.time()
    
    duration = end_time - start_time
    if duration > 0.1:  # Log if > 100ms
        log_warning(f"Slow dispatch: {duration:.3f}s for {kwargs.get('event', 'unknown')}")
    
    return result
```

---

## Integration Examples

### Complete Example: Flashcard Creation Flow

```python
# 1. GUI Component - User clicks save
def on_save_flashcard():
    form_data = get_form_data()
    
    # Dispatch validation request
    dispatch(FLASHCARD_VALIDATION_REQUEST, {
        "data": form_data,
        "source": "create_view"
    })

# 2. Validation Component
def validate_flashcard(data, **kwargs):
    errors = validate_flashcard_data(data)
    
    if errors:
        dispatch(FLASHCARD_VALIDATION_FAILED, {
            "errors": errors,
            "data": data
        })
    else:
        dispatch(FLASHCARD_VALIDATION_PASSED, {
            "data": data
        })

subscribe(FLASHCARD_VALIDATION_REQUEST, validate_flashcard, namespace='VALIDATION')

# 3. Model Component
def create_flashcard_model(data, **kwargs):
    flashcard = get_flashcard_model(**data)
    
    dispatch(FLASHCARD_MODEL_CREATED, {
        "model": flashcard,
        "source": "factory"
    })
    
    return flashcard

subscribe(FLASHCARD_VALIDATION_PASSED, create_flashcard_model, namespace='FACTORY')

# 4. Storage Component
def save_flashcard(model, **kwargs):
    success = add_entry(FLASHCARDS_DB_JSON, model)
    
    if success:
        dispatch(FLASHCARD_SAVED, {
            "model": model,
            "source": "storage"
        })
    else:
        dispatch(FLASHCARD_SAVE_FAILED, {
            "model": model,
            "source": "storage"
        })

subscribe(ADD_FLASHCARD_TO_DB, save_flashcard, namespace='STORAGE')

# 5. GUI Update Component
def refresh_flashcard_list(model, **kwargs):
    update_flashcard_display()
    show_success_message("Flashcard created successfully!")

subscribe(FLASHCARD_SAVED, refresh_flashcard_list, namespace='GUI')
```

This example shows how the dispatching system enables loose coupling between GUI, validation, model creation, storage, and display components.

---

## Summary

The StudyFrog dispatching system provides:

- **Decoupled Architecture**: Components communicate without direct dependencies
- **Flexible Event Handling**: Support for priorities, namespaces, and persistence
- **Bulk Operations**: Efficient handling of multiple events/subscriptions
- **Robust Error Handling**: Isolated failures don't crash the system
- **Debugging Support**: Comprehensive logging and tracking capabilities
- **Performance Optimization**: Priority-based execution and efficient bulk operations

This system is the backbone of StudyFrog's architecture, enabling maintainable, testable, and extensible code through event-driven communication patterns.
