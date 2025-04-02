# StudyFrog Events Module Documentation 📅📡🐸

Welcome to the documentation for the `events` module in StudyFrog! This module defines a centralized registry of **application-wide events**, represented as `DispatcherEvent` objects. These events serve as signals within the app's pub-sub system, powered by the `dispatcher` module.

---

## 📘 Overview
The `Events` class provides:
- A single static definition point for **all dispatcher events**
- Categorized events for **backend**, **UI**, and **global** interactions
- Utility methods for retrieving and grouping events dynamically

---

## 🧠 Core Component: `Events` Class

### Description
A static registry that defines all known `DispatcherEvent` instances in the application. It also provides accessors to retrieve events by type, name, or category.

### Examples of Registered Events
- `ANSWER_CREATED`, `FLASHCARD_UPDATED`, `APPLICATION_STARTED`
- `REQUEST_NOTE_CREATE`, `UI:BUTTON:CLICKED`, etc.
- Naming convention: `domain:object:action` (e.g. `backend:note:updated`)

---

## 🔑 Key Attributes
Each attribute is a `Final[DispatcherEvent]` defined via:
```python
DispatcherEventFactory.create_event(name="...")
```

These attributes include hundreds of specific actions like:
- Backend: `backend:flashcard:created`
- UI: `ui:button:clicked`
- Global: `global:request:note:update`

Events are **grouped semantically** for maintainability.

---

## 🔍 Event Access Methods

### `get_all_events(as_dict=False)` → List or Dict
Returns all declared events as a list or dictionary, depending on `as_dict`.

### `get_event_by_name(name: str)` → Optional[DispatcherEvent]
Searches for an event with a given name. Logs a warning if not found.

### `get_event_names()` → List[str]
Returns the names of all registered events.

### Specialized Accessors
These return grouped events, e.g.:
- `get_flashcard_events()`
- `get_note_events()`
- `get_tag_events()`
- `get_stack_events()`

All return `List[DispatcherEvent]`.

---

## 🧩 Use Cases
- **Event dispatching** via `Dispatcher.dispatch(event, ...)`
- **Subscription registration** using `Dispatcher.register(event, func, namespace)`
- **UI communication**, e.g. tracking user actions
- **Backend orchestration**, e.g. DB changes or sync triggers

---

## ✅ Best Practices
- Use namespaced event names to ensure clarity (`domain:scope:action`)
- Retrieve events via accessors (`get_event_by_name`, `get_*_events`) for clarity and maintainability
- Don't instantiate events directly; always use the static ones defined in `Events`
- Combine with the `Dispatcher` module to decouple complex workflows

---

## 💡 Potential Extensions
- Auto-registration or discovery of event handlers
- Schema validation for event payloads
- Event metadata such as severity or UI relevance
- Categorization by severity, timing, or permissions

---

Stay eventful and responsive — let your app talk through events 🧠📡🐸

