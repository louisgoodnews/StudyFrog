# StudyFrog Stack Module Documentation 📚🐸

Welcome to the detailed documentation for the `stack` module in the StudyFrog API. This module is central to the application, representing and managing collections of flashcards, notes, and questions, referred to as **Stacks**.

## Overview 💡
The stack module provides both **immutable** and **mutable** representations of stack objects. It also includes factory, converter, and manager classes for creating, transforming, and managing stacks across the system.

---

## 📦 ImmutableStack

### Description
Represents a read-only version of a stack with various helper methods for accessing stack metadata.

### Key Attributes
- `name`, `description`, `icon`, `difficulty`, `priority`, `status`
- `contents`: List of references to flashcards, notes, or questions.
- `ancestor` / `descendants`: Hierarchical relationships between stacks.
- `custom_field_values`: Custom metadata.
- `created_at`, `updated_at`, `last_viewed_at`, `due_by`
- `id`, `uuid`, `key`, `tags`

### Key Methods
- `has_ancestor()`, `has_contents()`, `has_descendants()`
- `is_ancestor_of(key)` / `is_descendant_of(key)`
- `is_content_of(key)`
- `get_content_grouped_by(type_key)`
- `to_mutable() → MutableStack`

---

## ✍️ MutableStack

### Description
A writable version of a stack that extends `MutableBaseObject`. Supports editing stack content and structure.

### Additional Methods
- `add_to_contents(content)` / `remove_from_contents(content)`
- `add_to_descendants(descendant)` / `remove_from_descendants(obj)`
- `to_immutable() → ImmutableStack`

---

## 🔁 StackConverter

### Description
A utility class that converts between `StackModel` and `ImmutableStack`.

### Methods
- `model_to_object(model: StackModel) → ImmutableStack`
- `object_to_model(object: ImmutableStack) → StackModel`

Handles exceptions and logs errors via the internal `Logger` instance.

---

## 🏭 StackFactory

### Description
Factory class for instantiating `ImmutableStack` objects using provided arguments.

### Method
- `create_stack(...) → ImmutableStack`

Includes full support for optional parameters and provides fallbacks where needed.

---

## 🧠 StackManager

### Description
Singleton manager for interacting with stack data in the database. Extends `BaseObjectManager` and includes CRUD methods.

### Highlights
- `get_all_stacks()`: Retrieve all stacks (cached if possible)
- `create_stack(stack)`: Add a new stack
- `update_stack(stack)`: Update an existing stack
- `delete_stack(stack)`: Remove a stack
- `count_stacks()`: Total number of stacks
- `get_stack_by(field, value)`, `get_stack_by_id(id)`, `get_stack_by_uuid(uuid)`
- `search_stacks(**kwargs)`: Filter stacks by search params
- `get_from_stacks(condition, limit)`: Filter stacks with a callback

---

## 🧬 StackModel

### Description
ORM-based class defining the schema and database structure for stacks.

### Core Fields
- Fields match exactly with the attributes of the `ImmutableStack` class.
- Uses custom `Field` descriptors to describe type, constraints, relationships, etc.

### Table Name
- Stored under `Constants.STACKS`

---

## 📌 Notes for Developers
- Always use `StackFactory.create_stack()` to create stack objects.
- When writing data to the DB, convert mutable stacks to `StackModel` using `StackConverter`.
- Prefer `StackManager.get_all_stacks()` and related methods for accessing stack data.
- Each stack is uniquely identified by `uuid` and internally referenced with a `key` like `STACK_1`, `STACK_2`, ...
- Be cautious with the cache mechanism – keep it in sync when adding/removing stacks manually.

---

## ✅ Example Usage
```python
# Create a new stack
manager = StackManager()
new_stack = StackFactory.create_stack(name="Biology Basics")
manager.create_stack(new_stack)

# Retrieve by ID
retrieved = manager.get_stack_by_id(1)
print(retrieved.name)  # → Biology Basics
```

---

## 🚧 To Do / Future Extensions
- Enforce stronger typing in contents (`Union[Flashcard, Note, Question]`)
- Add filtering/sorting by `due_by`, `priority`, etc.
- Connect with user profiles for personalized stack suggestions

---

Made with 💚 for contributors of StudyFrog 🐸

