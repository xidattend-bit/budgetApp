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


def get_balance(transactions: list[dict[str, Any]]) -> float:
    """Return the balance by summing all transaction amounts.

    Args:
        transactions: Transaction records to total.

    Returns:
        Total balance as a float. Empty input returns 0.0.
    """
    if not transactions:
        return 0.0

    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(transactions: list[dict[str, Any]], category: str) -> list[dict[str, Any]]:
    """Return transactions matching the given category, case-insensitively.

    Args:
        transactions: Transaction records to filter.
        category: Category name to match.

    Returns:
        A new list containing matching transactions.
    """
    normalized_category = category.lower()
    return [
        transaction
        for transaction in transactions
        if transaction["category"].lower() == normalized_category
    ]
