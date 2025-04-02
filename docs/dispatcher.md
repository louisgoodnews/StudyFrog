# StudyFrog Dispatcher Module Documentation 📣📡🐸

Welcome to the documentation for the `dispatcher` module in StudyFrog! This module implements a **publish-subscribe** system to dispatch events and manage subscriptions, allowing components to respond to dynamic behavior in a decoupled, traceable way.

---

## 📘 Overview
The Dispatcher module offers the ability to:
- Register functions to specific named events
- Dispatch events and notify all subscribers in a namespace
- Track notification results with duration and result mapping
- Remove or bulk-unregister subscriptions by event, namespace, or UUID

---

## 🧠 DispatcherEvent
An immutable object representing an event definition.

### Fields
- `id`: Numeric identifier
- `name`: Event name string
- `uuid`: Universally unique ID

### Method
- `compare_to(other: DispatcherEvent)` – Equality check by ID, name, and UUID

---

## 🏭 DispatcherEventFactory
Factory class to create `DispatcherEvent` instances.

- Uses `Constants.get_base_id()` for auto-increment
- Automatically assigns UUID via `Miscellaneous.get_uuid()`

### Method
- `create_event(name: str) → Optional[DispatcherEvent]`

---

## 📣 DispatcherNotification
Represents a single dispatched event and its results.

### Fields
- `event`: The related `DispatcherEvent`
- `namespace`: Where it was dispatched
- `start`, `end`, `duration`: Timestamps and timing
- `result`: Dict of results keyed by function name

### Methods
- `get_all_results()` → List[Any]
- `get_one_and_only_result()` → Optional[Any]
- `get_result_by_key(key: str)` → Optional[Any]
- `has(key: str)` / `is_empty()` → Boolean utilities

---

## 🏭 DispatcherNotificationFactory
Creates `DispatcherNotification` instances. Used internally by the builder and subscriptions.

---

## 🧱 DispatcherNotificationBuilder
Fluent builder class to construct notifications programmatically.

### Chainable Setters
- `.duration(value)`
- `.start(value)` / `.end(value)`
- `.namespace(value)` / `.event(value)`
- `.result(key, value)`

### Method
- `build() → DispatcherNotification`

---

## 🧩 DispatcherEventSubscription
Encapsulates subscriptions to a single `DispatcherEvent`. Manages functions organized by `namespace`.

### Methods
- `add_subscription(function, namespace, persistent)` → UUID
- `notify_subscriptions(namespace, *args, **kwargs)` → `DispatcherNotification`
- `remove_subscription(uuid)` → bool

Subscriptions can be **persistent** or auto-cleaned after one execution.

---

## 🏭 DispatcherEventSubscriptionFactory
Factory for `DispatcherEventSubscription` objects.

---

## 📡 Dispatcher (Singleton)
Global singleton for managing all dispatcher logic.

### Access
```python
dispatcher = Dispatcher()
```

### Key Methods
- `register(event, function, namespace, persistent)` → UUID
- `unregister(event=..., namespace=..., uuid=...)` – Supports flexible filters
- `dispatch(event, namespace, *args, **kwargs)` → `DispatcherNotification`

### Singleton Behavior
The dispatcher uses a shared `_shared_instance` and `__new__()` override to ensure only one instance exists.

---

## ✅ Best Practices
- Register your event handlers early in the app lifecycle
- Use consistent `namespace` values to group related listeners
- Mark subscriptions as non-persistent if they’re single-use
- Handle results from `DispatcherNotification` gracefully

---

## 💡 Future Extensions
- Async event dispatching
- Subscription priority ordering
- Global event logging and inspection
- Event schema validation and decorators

---

Decouple your logic, subscribe to change, and dispatch smarter 🚀📣🐸

