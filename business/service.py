"""
Programmer: Varshil Patel
File: service.py
Description: Business logic for managing in-memory dataset.
"""

from typing import List
from model.record import Record
from persistence.repository import load_records

_records: List[Record] = []


def reload_data() -> None:
    """Reloads the dataset from file into the in-memory list."""
    global _records
    _records = load_records()


def get_all_records() -> List[Record]:
    """Returns a copy of all records."""
    return list(_records)


def get_record(index: int) -> Record | None:
    """Returns one record by index, or None if index is invalid."""
    if 0 <= index < len(_records):
        return _records[index]
    return None


def add_record(record: Record) -> None:
    """Adds a new record to the in-memory list."""
    _records.append(record)


def update_record(index: int, new_record: Record) -> bool:
    """
    Replaces a record at a given index.
    Returns True if successful, False if index is invalid.
    """
    if 0 <= index < len(_records):
        _records[index] = new_record
        return True
    return False


def delete_record(index: int) -> bool:
    """
    Deletes a record at the given index.
    Returns True if successful, False if index is invalid.
    """
    if 0 <= index < len(_records):
        del _records[index]
        return True
    return False
