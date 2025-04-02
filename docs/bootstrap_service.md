# StudyFrog BootstrapService Module Documentation 🚀🛠️🐸

Welcome to the documentation for the `bootstrap_service` module in StudyFrog! This module contains the `BootstrapService` class, a central singleton responsible for initializing, registering, and managing all essential components of the StudyFrog application.

---

## 📘 Overview
The `BootstrapService` ensures that StudyFrog's UI, database, managers, event handlers, and default values are correctly set up at application startup — and safely shut down on exit.

---

## 🧠 Core Component: `BootstrapService`

### Description
A **singleton class** that:
- Initializes core services (Dispatcher, NotificationService, Unified Managers, etc.)
- Registers all object managers
- Creates database tables
- Fills in default values (difficulties, priorities, answers, statuses)
- Wires up all event handlers to the `Dispatcher`
- Registers all menus with the `UIRegistry`
- Cleans up on shutdown

---

## 🔄 Lifecycle Methods

### `__new__()`
Implements the singleton pattern. Creates a new instance only if one doesn't exist.

### `init()`
Initializes dispatcher, navigation service, setting service, unified object manager/service, and subscriptions.

### `run_startup_tasks()` → Tuple[...]
Runs all initialization logic in order:
- Creates tables
- Registers managers
- Registers event handlers
- Registers menus
- Populates default entries
- Logs duration

Returns initialized core services (Dispatcher, Navigation, Notification, etc.).

### `run_shutdown_tasks()`
Unregisters all event handlers and logs shutdown duration.

---

## 🧩 Core Component Setup

### `create_tables()`
Creates all model-related tables via `create_table()` on each `Model` class.

### `register_managers()`
Registers each manager (e.g. `FlashcardManager`) with the `UnifiedObjectManager`.

### `register_handlers()`
Connects hundreds of `on_request_*` events from `Events` to the `UnifiedObjectService` methods using the `Dispatcher`.

### `register_menus()`
Registers all UI views with the `UIRegistry`, enabling consistent access and launch.

---

## 🛠️ Default Initializers
These methods ensure the database contains expected startup entries.

### `create_default_answers()`
Registers `True` and `False` answer defaults.

### `create_default_difficulties()`
Registers "Easy", "Medium", and "Hard" difficulty defaults.

### `create_default_priorities()`
Registers priorities from "Lowest" to "Highest".

### `create_default_statuses()`
Registers statuses like "New", "Learning", "Review", "Completed".

---

## 🔧 Utility

### `unregister_handlers()`
Unsubscribes all previously registered event handlers (tracked via UUID).

---

## ✅ Best Practices
- Run `run_startup_tasks()` once during application startup
- Access the instance via `BootstrapService()` (singleton)
- Extend `register_handlers()` when new event-driven functionality is added
- Always use `create_default_*()` helpers for required DB defaults
- Clean up properly with `run_shutdown_tasks()`

---

## 💡 Future Enhancements
- Async startup/shutdown support
- Plugin bootstrap loader
- Versioned schema migration logic
- Environment-based configuration toggles

---

One frog to boot them all 🐸💡🚀 — Welcome to your StudyFrog launch center!