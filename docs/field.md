# StudyFrog Field Module Documentation 🧱📐🐸

Welcome to the documentation for the `field` module in StudyFrog! This module defines the structure of database table columns using the `Field` class, enabling robust schema generation and validation for ORM-based models.

---

## 📘 Overview
The `Field` class represents a column in a database table, encapsulating its type, constraints, and metadata. It is used by `ImmutableBaseModel` and other model components to dynamically generate SQL statements.

---

## 🧠 Class: `Field`

### Description
A data container for SQL column specifications. Inherits from `ImmutableBaseObject` and can be used directly in class-level definitions of ORM model schemas.

### Constructor Parameters
- `name: str`: Column name (required)
- `type: str`: SQL type — e.g., `INTEGER`, `TEXT`, `VARCHAR`, `BOOLEAN`, etc.
- `size: int`: Optional size constraint for variable types like `VARCHAR`
- `primary_key: bool`: Whether this field is a primary key
- `autoincrement: bool`: Whether to auto-increment the field (valid only on `INTEGER PRIMARY KEY` fields)
- `unique: bool`: Whether this field must be unique
- `nullable: bool`: If the field can contain NULL values
- `default: Any`: Default value
- `index: bool`: Whether to index the field
- `foreign_key: str`: Target table for foreign key constraint
- `on_delete: str`: Action to take when referenced record is deleted (`CASCADE`, `SET NULL`, etc.)
- `on_update: str`: Action to take on referenced record update
- `description: str`: Human-readable explanation
- `unique_together: List[str]`: For composite unique constraints

---

## 🎯 Supported SQL Types
You can assign any of the following SQL types to a field:
- `ARRAY`, `BLOB`, `BOOLEAN`, `DATE`, `DATETIME`, `FLOAT`, `INTEGER`, `JSON`, `NUMERIC`, `REAL`, `TEXT`, `TIME`, `VARCHAR`, `NULL`

---

## 🛠️ Method: `to_sql_string()`
Converts the field object into a SQL-compatible column definition string.

### Example
```python
Field(name="id", type="INTEGER", primary_key=True, autoincrement=True).to_sql_string()
# → '"id" INTEGER PRIMARY KEY AUTOINCREMENT'
```

### Internal Logic Includes:
- Appending `PRIMARY KEY`, `UNIQUE`, `DEFAULT`, `NULL/NOT NULL`
- Enforcing `AUTOINCREMENT` on valid primary key fields
- Handling foreign key constraints with `REFERENCES`, `ON DELETE`, and `ON UPDATE`

---

## ✅ Best Practices
- Always specify both `name` and `type`
- Use `autoincrement=True` only on `INTEGER PRIMARY KEY`
- Prefer `nullable=False` for mandatory fields
- Group related constraints (e.g., `unique_together`) in model class
- Use this class inside `ImmutableBaseModel` definitions only

---

## 💡 Future Features
- Validation of `default` values by type
- Automatic index/constraint generation from field sets
- Type hinting + metaclass integration for field inference

---

Define your schema clearly, and your data will follow 🧱💾🐸