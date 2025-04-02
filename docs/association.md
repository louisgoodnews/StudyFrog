# StudyFrog Association Module Documentation 🔗🧩🐸

Welcome to the documentation for the `association` module in StudyFrog. This module enables flexible, type-safe relationships between different object types in the StudyFrog ecosystem.

---

## 📘 Overview
Associations describe **typed links** between entities like flashcards, notes, questions, stacks, and more. They're essential for representing relationships such as:

- A flashcard being tagged
- A note depending on a question
- A stack being marked as a descendant of another

This module provides:
- Mutable and immutable association objects
- A factory and builder for creation
- A converter for ORM ↔ object mapping
- A singleton manager for full database lifecycle
- A model class to define persistent structure

---

## 🧊 ImmutableAssociation / ✍️ MutableAssociation

### Description
Both classes represent the same core structure of an association, differing only in mutability. The immutable form is used after creation, while the mutable form is used for edits.

### Shared Fields
- `association_type`: Type of link ("ancestor", "dependant", etc.)
- `answer`, `flashcard`, `note`, `stack`, `question`, `tag`, etc. – IDs of linked items
- `created_at`, `updated_at`, `uuid`, `key`, `icon`

### Conversions
- `ImmutableAssociation.to_mutable()`
- `MutableAssociation.to_immutable()`

---

## 🏗️ AssociationBuilder

Fluent-style builder for composing associations dynamically.
```python
builder = AssociationBuilder()
assoc = builder.flashcard(1).tag(5).build()
```

Supports most object types via dedicated setter methods.

---

## 🧪 AssociationFactory

Creates new validated `ImmutableAssociation` instances from keyword args. Useful when structure is known.

---

## 🔁 AssociationConverter

### Purpose
Handles bidirectional transformation:
- `model_to_object(model)` → ImmutableAssociation
- `object_to_model(object)` → AssociationModel

Includes error logging on failure.

---

## 🧠 AssociationManager (Singleton)

### Description
Manages caching and CRUD operations for all associations. Inherits from `BaseObjectManager` and implemented as a **Singleton**.

### Key Methods
- `associate(...)` – quickly link two entities
- `create_association(...)`
- `delete_association(...)`
- `update_association(...)`
- `get_all_associations()`
- `get_association_by(field, value)` / `by_id()` / `by_uuid()`
- `search_associations(**kwargs)`
- `count_associations()`

Associations are automatically cached to improve performance.

---

## 🧬 AssociationModel

### Description
ORM model defining the structure of the `ASSOCIATIONS` table. All foreign key references are represented as integers.

### Fields
- Every major object type has a foreign key field: `flashcard`, `note`, `tag`, etc.
- `association_type`, `created_at`, `updated_at`, `uuid`, `key`, `icon`

---

## ✅ Best Practices
- Use `AssociationManager().associate(...)` to link two objects instead of manually creating associations
- Implement all association managers as **Singletons** (already done)
- Avoid hardcoding IDs; retrieve objects via managers
- Use builder when building programmatically, factory when values are known

---

## 🚀 Example
```python
manager = AssociationManager()
manager.associate(
    association_type="tagged_with",
    flashcard=1,
    tag=7,
)
```

---

## 💡 Future Ideas
- Inverse query resolution (e.g., find all notes "depending on" this question)
- Graph visualization of associations
- Rule-based constraint engine for invalid links
- Association expiration / deactivation

---

Connect the dots – make your study universe relational 🔗🧠🐸

