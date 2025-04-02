# StudyFrog Priority Module Documentation 🔥⏳

Welcome to the documentation for the `priority` module in the StudyFrog API. This module handles **prioritization** of flashcards, notes, and questions. Priorities help determine what content needs more immediate attention.

---

## 📘 Overview
Priorities are defined by a name, value (0–1), and a visual emoji/icon. This module provides:

- Immutable and mutable priority representations
- Conversion between DB model and object
- Factory pattern for instantiation
- Manager for full database lifecycle
- ORM mapping for storage

---

## 📦 ImmutablePriority

### Description
Immutable version of a priority. Safe for read-only operations.

### Attributes
- `name`: e.g., *highest*, *medium*, *low*
- `emoji`: Visual level indicator (🔴, 🟡, 🟢...)
- `value`: Float from 0.0 to 1.0
- `icon`: Defaults to "🔥"
- `id`, `key`, `uuid`
- `created_at`, `updated_at`

### Method
- `to_mutable() → MutablePriority`

---

## ✍️ MutablePriority

### Description
Writable version of a priority object.

### Method
- `to_immutable() → ImmutablePriority`

---

## 🔁 PriorityConverter

### Description
Converts between `PriorityModel` (DB) and `ImmutablePriority` (domain object).

### Methods
- `model_to_object(model: PriorityModel)`
- `object_to_model(object: ImmutablePriority)`

All conversions are safely wrapped in error-logging.

---

## 🏭 PriorityFactory

### Description
Creates new `ImmutablePriority` instances with all required metadata.

### Method
- `create_priority(...) → Optional[ImmutablePriority]`

Supports emoji, custom values, timestamps, and UUID generation.

---

## 🧠 PriorityManager

### Description
The `PriorityManager` handles storage, retrieval, updates, and deletion of priority objects.

### Key Methods
- `create_priority(priority)`
- `count_priorities()`
- `delete_priority(priority)`
- `get_all_priorities()`
- `get_priority_by(field, value)` / `get_priority_by_id(id)` / `get_priority_by_uuid(uuid)`
- `search_priorities(**kwargs)`
- `update_priority(priority)`
- `get_default_priorities()` – loads default priorities (HIGHEST to LOWEST) from database or creates them on the fly

---

## 🧬 PriorityModel

### Description
The ORM model for the priority table. Defines database schema.

### Table
- Table name: `Constants.PRIORITIES`

### Fields
- `id`, `name`, `value`, `emoji`, `icon`, `key`, `uuid`, `created_at`, `updated_at`

---

## ✅ Contributor Best Practices
- Use `PriorityFactory.create_priority()` to create new priorities
- Always use `PriorityManager.create_priority()` to store them
- Retrieve defaults with `get_default_priorities()`
- Use cache-aware `get_priority_by_*` methods to avoid redundant DB hits
- Extend the emoji system to add more levels if needed

---

## 🚀 Example Usage
```python
manager = PriorityManager()
new_priority = PriorityFactory.create_priority(
    name="Critical",
    emoji="🚨",
    value=1.0
)
manager.create_priority(new_priority)
```

---

## 💡 Future Improvements
- Weight-based scheduling that incorporates both difficulty and priority
- Per-user priority presets
- Visual analytics showing user focus over time

---

Focus on what truly matters – powered by 🔥 priorities and 🐸 StudyFrog!