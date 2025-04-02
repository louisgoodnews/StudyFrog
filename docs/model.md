# StudyFrog Model Module Documentation 🧬📦🐸

Welcome to the documentation for the `model` module in StudyFrog. This module provides the foundation for interacting with SQLite databases via immutable model classes.

---

## 📘 Overview
This module introduces the `ImmutableBaseModel`, which extends `ImmutableBaseObject` and acts as the common base class for all ORM-backed objects. It defines reusable database logic including:

- Creating, updating, deleting, and querying entries
- Automatically generating or adjusting tables from field definitions
- Centralized logging and SQL safety

All functionality integrates with StudyFrog’s `DatabaseService`, `Field`, and `Miscellaneous` utilities.

---

## 🧱 ImmutableBaseModel

### Description
A universal, reusable base class for ORM-style database models. All StudyFrog models inherit from this.

### Inherits from
- `ImmutableBaseObject`

### Key Class Attributes
- `logger`: Logger instance for consistent structured logging

---

## 🛠️ Core Methods

### `create(database: str) → Optional[int]`
Insert a new entry into the DB. Returns the new row ID or `None` on error.

### `update(database: str, **kwargs) → bool`
Update the current model instance with new values.

### `delete(database: str) → bool`
Delete the current model instance by ID.

---

## 📊 Table Management

### `create_table(database: str) → bool`
Creates the model's table in the DB based on defined `Field`s.

### `drop_table(database: str) → bool`
Drops the table from the database.

### `upsert_table(database: str) → None`
Creates or modifies the table to match the current schema definition (adds/removes columns).

---

## 🔎 Queries

### `count(database: str) → Optional[int]`
Returns the number of entries in the model’s table.

### `get_all(database: str) → List[Model]`
Returns a list of all entries in the table.

### `get_by(database: str, column: str, value: Any) → Optional[Union[Model, List[Model]]]`
Returns one or more entries matching a specific column value.

### `search(database: str, **kwargs) → Optional[List[Model]]`
Flexible multi-field search using keyword arguments. Field type–aware.

---

## 🧪 Custom Execution

### `execute(database: str, sql: str, parameters: Optional[Tuple[Any, ...]] = []) → Any`
Low-level access to execute custom SQL queries directly via `DatabaseService`.

---

## 🧠 Utility

### `to_sql_string() → str`
Returns the `CREATE TABLE` SQL statement segment for all declared fields.

---

## ✅ Best Practices
- Define fields using `Field` class at the class level
- Call `create_table()` or `upsert_table()` before creating entries
- Use `Miscellaneous.convert_to_db_format()` for data safety
- Always use `await` with async DB operations
- Catch and log exceptions for traceability

---

## 💡 Future Features
- Type-hint-based automatic field declaration
- Index creation support
- Versioned schema migration utilities
- Field-level access control or validation hooks

---

Your data layer, simplified and safe. 📦🛡️🐸

