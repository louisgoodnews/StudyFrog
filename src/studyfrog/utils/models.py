"""
Functional CRUD helpers for StudyFrog models.
"""

from __future__ import annotations

from typing import Any, Final, Optional, Union

from studyfrog.constants.common import PATTERNS
from studyfrog.models.models import Model
from studyfrog.utils.common import exists, pluralize_word, search_string
from studyfrog.utils.logging import log_error, log_info
from studyfrog.utils.storage import (
    add_entries,
    add_entries_if_not_exist,
    add_entry,
    add_entry_if_not_exist,
    count_entries,
    delete_entries,
    delete_entry,
    filter_entries,
    get_all_entries,
    get_entries,
    get_entries_by_keys,
    get_entry,
    get_entry_by_key,
    update_entries,
    update_entry,
)


MODEL_SHORTCUT_TYPES: Final[tuple[str, ...]] = (
    "answer",
    "association",
    "customfield",
    "difficulty",
    "flashcard",
    "image",
    "note",
    "option",
    "priority",
    "question",
    "rehearsal_action",
    "rehearsal_run",
    "rehearsal_run_item",
    "stack",
    "subject",
    "tag",
    "teacher",
    "user",
)


__all__: list[str] = [
    "count_models",
    "create_model",
    "create_models",
    "delete_model",
    "delete_models",
    "filter_models",
    "read_all_models",
    "read_model",
    "read_model_by_key",
    "read_models",
    "read_models_by_keys",
    "update_model",
    "update_models",
]


def _ensure_model_storage_id(model: Model) -> Model:
    """
    Normalizes the storage-facing ID attribute expected by utils.storage.
    """

    if hasattr(model, "id_") and exists(value=getattr(model, "id_", None)):
        return model

    model_id: Optional[Union[int, str]] = getattr(model, "id", None)

    if not exists(value=model_id) and exists(value=getattr(model, "key", None)):
        model_id = search_string(
            pattern=PATTERNS["MODEL_ID"],
            string=model.key,
        )

    setattr(model, "id_", model_id)

    return model


def _get_table_name(
    model: Optional[Model] = None,
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> str:
    """
    Resolves the storage table name for a model operation.

    Args:
        model (Optional[Model]): The model instance whose type should determine the table.
        model_type (Optional[str]): The model type to resolve into a plural table name.
        table_name (Optional[str]): The explicit table name to use.

    Returns:
        str: The resolved table name.

    Raises:
        ValueError: If no table name can be derived from the provided arguments.
    """

    if exists(value=table_name):
        return str(table_name)

    if exists(value=model):
        return pluralize_word(word=model.type_.lower())

    if exists(value=model_type):
        return pluralize_word(word=str(model_type).lower())

    raise ValueError("Unable to resolve table name. Pass 'table_name', 'model', or 'model_type'.")


def count_models(
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> int:
    """
    Counts the number of stored models in a resolved table.

    Args:
        model_type (Optional[str]): The model type to count.
        table_name (Optional[str]): The explicit table name to count.

    Returns:
        int: The number of entries stored in the table.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Counting models in '{resolved_table_name}' table.")

    return count_entries(table_name=resolved_table_name)


def create_model(
    model: Model,
    force: bool = False,
    table_name: Optional[str] = None,
) -> Optional[Union[int, Model]]:
    """
    Creates a single model in storage.

    Args:
        model (Model): The model to persist.
        force (bool): Whether to bypass duplicate checks and force insertion.
        table_name (Optional[str]): The explicit table name to write to.

    Returns:
        Optional[Union[int, Model]]: The created model ID for forced inserts, or the
            storage layer's result for duplicate-aware inserts.
    """

    resolved_table_name: str = _get_table_name(
        model=model,
        table_name=table_name,
    )

    log_info(message=f"Creating model '{model.type_}' in '{resolved_table_name}' table.")

    try:
        if force:
            return add_entry(
                model=model,
                table_name=resolved_table_name,
            )

        return add_entry_if_not_exist(
            model=model,
            table_name=resolved_table_name,
        )
    except Exception as e:
        log_error(message=f"Failed to create model '{model.type_}': {e}")
        raise e


def create_models(
    models: list[Model],
    force: bool = False,
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[Union[list[int], list[Model]]]:
    """
    Creates multiple models in storage.

    Args:
        models (list[Model]): The models to persist.
        force (bool): Whether to bypass duplicate checks and force insertion.
        model_type (Optional[str]): The model type to use when the models list is empty.
        table_name (Optional[str]): The explicit table name to write to.

    Returns:
        Optional[Union[list[int], list[Model]]]: The IDs of created models for forced
            inserts, or the storage layer's duplicate-aware result.
    """

    resolved_table_name: str = _get_table_name(
        model=models[0] if exists(value=models) else None,
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Creating {len(models)} models in '{resolved_table_name}' table.")

    try:
        if force:
            return add_entries(
                models=models,
                table_name=resolved_table_name,
            )

        return add_entries_if_not_exist(
            models=models,
            table_name=resolved_table_name,
        )
    except Exception as e:
        log_error(message=f"Failed to create models in '{resolved_table_name}' table: {e}")
        raise e


def delete_model(
    id_: Union[int, str],
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[Model]:
    """
    Deletes a single model from storage.

    Args:
        id_ (Union[int, str]): The ID of the model to delete.
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to delete from.

    Returns:
        Optional[Model]: The deleted model if one was found and removed.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Deleting model '{id_}' from '{resolved_table_name}' table.")

    return delete_entry(
        id_=id_,
        table_name=resolved_table_name,
    )


def delete_models(
    ids: list[Union[int, str]],
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[list[Model]]:
    """
    Deletes multiple models from storage.

    Args:
        ids (list[Union[int, str]]): The IDs of the models to delete.
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to delete from.

    Returns:
        Optional[list[Model]]: The models that were deleted.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Deleting {len(ids)} models from '{resolved_table_name}' table.")

    return delete_entries(
        ids=ids,
        table_name=resolved_table_name,
    )


def filter_models(
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
    **kwargs: Any,
) -> Optional[list[Model]]:
    """
    Filters models from storage by arbitrary criteria.

    Args:
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to query.
        **kwargs: The filter criteria passed through to the storage layer.

    Returns:
        Optional[list[Model]]: The list of matching models.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Filtering models in '{resolved_table_name}' table with criteria {kwargs}.")

    return filter_entries(
        table_name=resolved_table_name,
        **kwargs,
    )


def read_all_models(
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[list[Model]]:
    """
    Reads all models from a resolved storage table.

    Args:
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to query.

    Returns:
        Optional[list[Model]]: All models found in the table.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Reading all models from '{resolved_table_name}' table.")

    return get_all_entries(table_name=resolved_table_name)


def read_model(
    id_: Union[int, str],
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[Model]:
    """
    Reads a single model by ID from storage.

    Args:
        id_ (Union[int, str]): The ID of the model to retrieve.
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to query.

    Returns:
        Optional[Model]: The retrieved model, if found.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Reading model '{id_}' from '{resolved_table_name}' table.")

    return get_entry(
        id_=id_,
        table_name=resolved_table_name,
    )


def read_model_by_key(
    key: str,
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[Model]:
    """
    Reads a single model by key from storage.

    Args:
        key (str): The model key to retrieve.
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to query.

    Returns:
        Optional[Model]: The retrieved model, if found.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Reading model '{key}' from '{resolved_table_name}' table by key.")

    return get_entry_by_key(
        key=key,
        table_name=resolved_table_name,
    )


def read_models(
    ids: list[Union[int, str]],
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[list[Model]]:
    """
    Reads multiple models by ID from storage.

    Args:
        ids (list[Union[int, str]]): The IDs of the models to retrieve.
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to query.

    Returns:
        Optional[list[Model]]: The retrieved models.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Reading {len(ids)} models from '{resolved_table_name}' table.")

    return get_entries(
        ids=ids,
        table_name=resolved_table_name,
    )


def read_models_by_keys(
    keys: list[str],
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[list[Model]]:
    """
    Reads multiple models by key from storage.

    Args:
        keys (list[str]): The keys of the models to retrieve.
        model_type (Optional[str]): The model type to resolve the table from.
        table_name (Optional[str]): The explicit table name to query.

    Returns:
        Optional[list[Model]]: The retrieved models.
    """

    resolved_table_name: str = _get_table_name(
        model_type=model_type,
        table_name=table_name,
    )

    log_info(message=f"Reading {len(keys)} models from '{resolved_table_name}' table by key.")

    return get_entries_by_keys(
        keys=keys,
        table_name=resolved_table_name,
    )


def update_model(
    model: Model,
    table_name: Optional[str] = None,
) -> Optional[Model]:
    """
    Updates a single model in storage.

    Args:
        model (Model): The model to update.
        table_name (Optional[str]): The explicit table name to update in.

    Returns:
        Optional[Model]: The updated model returned by the storage layer.
    """

    resolved_table_name: str = _get_table_name(
        model=model,
        table_name=table_name,
    )

    normalized_model: Model = _ensure_model_storage_id(model=model)

    log_info(message=f"Updating model '{normalized_model.type_}' in '{resolved_table_name}' table.")

    return update_entry(
        model=normalized_model,
        table_name=resolved_table_name,
    )


def update_models(
    models: list[Model],
    model_type: Optional[str] = None,
    table_name: Optional[str] = None,
) -> Optional[list[Model]]:
    """
    Updates multiple models in storage.

    Args:
        models (list[Model]): The models to update.
        model_type (Optional[str]): The model type to use when the models list is empty.
        table_name (Optional[str]): The explicit table name to update in.

    Returns:
        Optional[list[Model]]: The updated models returned by the storage layer.
    """

    resolved_table_name: str = _get_table_name(
        model=models[0] if exists(value=models) else None,
        model_type=model_type,
        table_name=table_name,
    )

    normalized_models: list[Model] = [_ensure_model_storage_id(model=model) for model in models]

    log_info(message=f"Updating {len(normalized_models)} models in '{resolved_table_name}' table.")

    return update_entries(
        models=normalized_models,
        table_name=resolved_table_name,
    )


def _register_model_shortcuts(model_type: str) -> None:
    """
    Registers shorthand CRUD callables for a specific model type.

    Args:
        model_type (str): The singular model type to register shortcuts for.

    Returns:
        None
    """

    plural_model_type: str = pluralize_word(word=model_type)

    def add_single(
        model: Model,
        force: bool = False,
    ) -> Optional[Union[int, Model]]:
        """
        Creates a single typed model in storage.

        Args:
            model (Model): The typed model instance to persist.
            force (bool): Whether to bypass duplicate checks.

        Returns:
            Optional[Union[int, Model]]: The storage result for the add operation.
        """

        return create_model(
            model=model,
            force=force,
            table_name=plural_model_type,
        )

    def add_multiple(
        models: list[Model],
        force: bool = False,
    ) -> Optional[Union[list[int], list[Model]]]:
        """
        Creates multiple typed models in storage.

        Args:
            models (list[Model]): The typed models to persist.
            force (bool): Whether to bypass duplicate checks.

        Returns:
            Optional[Union[list[int], list[Model]]]: The storage result for the add operation.
        """

        return create_models(
            models=models,
            force=force,
            table_name=plural_model_type,
        )

    def count_typed() -> int:
        """
        Counts all typed models in storage.

        Returns:
            int: The number of stored typed models.
        """

        return count_models(table_name=plural_model_type)

    def delete_single(id_: Union[int, str]) -> Optional[Model]:
        """
        Deletes a single typed model by ID.

        Args:
            id_ (Union[int, str]): The model ID to delete.

        Returns:
            Optional[Model]: The deleted typed model, if found.
        """

        return delete_model(
            id_=id_,
            table_name=plural_model_type,
        )

    def delete_multiple(ids: list[Union[int, str]]) -> Optional[list[Model]]:
        """
        Deletes multiple typed models by ID.

        Args:
            ids (list[Union[int, str]]): The model IDs to delete.

        Returns:
            Optional[list[Model]]: The deleted typed models.
        """

        return delete_models(
            ids=ids,
            table_name=plural_model_type,
        )

    def filter_typed(**kwargs: Any) -> Optional[list[Model]]:
        """
        Filters typed models by arbitrary criteria.

        Args:
            **kwargs: The filter criteria.

        Returns:
            Optional[list[Model]]: The matching typed models.
        """

        return filter_models(
            table_name=plural_model_type,
            **kwargs,
        )

    def get_all_typed() -> Optional[list[Model]]:
        """
        Reads all typed models from storage.

        Returns:
            Optional[list[Model]]: All stored typed models.
        """

        return read_all_models(table_name=plural_model_type)

    def get_single(id_: Union[int, str]) -> Optional[Model]:
        """
        Reads a single typed model by ID.

        Args:
            id_ (Union[int, str]): The model ID to retrieve.

        Returns:
            Optional[Model]: The retrieved typed model, if found.
        """

        return read_model(
            id_=id_,
            table_name=plural_model_type,
        )

    def get_single_by_key(key: str) -> Optional[Model]:
        """
        Reads a single typed model by key.

        Args:
            key (str): The model key to retrieve.

        Returns:
            Optional[Model]: The retrieved typed model, if found.
        """

        return read_model_by_key(
            key=key,
            table_name=plural_model_type,
        )

    def get_multiple(ids: list[Union[int, str]]) -> Optional[list[Model]]:
        """
        Reads multiple typed models by ID.

        Args:
            ids (list[Union[int, str]]): The model IDs to retrieve.

        Returns:
            Optional[list[Model]]: The retrieved typed models.
        """

        return read_models(
            ids=ids,
            table_name=plural_model_type,
        )

    def get_multiple_by_keys(keys: list[str]) -> Optional[list[Model]]:
        """
        Reads multiple typed models by key.

        Args:
            keys (list[str]): The model keys to retrieve.

        Returns:
            Optional[list[Model]]: The retrieved typed models.
        """

        return read_models_by_keys(
            keys=keys,
            table_name=plural_model_type,
        )

    def update_single(model: Model) -> Optional[Model]:
        """
        Updates a single typed model in storage.

        Args:
            model (Model): The typed model to update.

        Returns:
            Optional[Model]: The updated typed model.
        """

        return update_model(
            model=model,
            table_name=plural_model_type,
        )

    def update_multiple(models: list[Model]) -> Optional[list[Model]]:
        """
        Updates multiple typed models in storage.

        Args:
            models (list[Model]): The typed models to update.

        Returns:
            Optional[list[Model]]: The updated typed models.
        """

        return update_models(
            models=models,
            table_name=plural_model_type,
        )

    shortcut_map: dict[str, Any] = {
        f"add_{model_type}": add_single,
        f"add_{plural_model_type}": add_multiple,
        f"count_{plural_model_type}": count_typed,
        f"delete_{model_type}": delete_single,
        f"delete_{plural_model_type}": delete_multiple,
        f"filter_{plural_model_type}": filter_typed,
        f"get_all_{plural_model_type}": get_all_typed,
        f"get_{model_type}": get_single,
        f"get_{model_type}_by_key": get_single_by_key,
        f"get_{plural_model_type}": get_multiple,
        f"get_{plural_model_type}_by_keys": get_multiple_by_keys,
        f"update_{model_type}": update_single,
        f"update_{plural_model_type}": update_multiple,
    }

    for (
        name,
        function,
    ) in shortcut_map.items():
        function.__name__ = name
        function.__qualname__ = name
        globals()[name] = function
        __all__.append(name)


for _model_type in MODEL_SHORTCUT_TYPES:
    _register_model_shortcuts(model_type=_model_type)
