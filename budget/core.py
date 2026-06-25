"""Core business logic for the budget CLI app."""

from __future__ import annotations

from typing import Any


def add_transaction(transactions: list[dict[str, Any]], transaction: dict[str, Any]) -> list[dict[str, Any]]:
    """Add a transaction to the given transaction list.

    Args:
        transactions: Existing transaction records.
        transaction: A single transaction record to append.

    Returns:
        A new list containing the added transaction.
    """
    return [*transactions, transaction]
