"""Core business logic for the budget CLI app."""

from __future__ import annotations

import csv
from pathlib import Path
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


def load_transactions_from_csv(csv_path: str) -> list[dict[str, Any]]:
    """Load transactions from a CSV file.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        A list of transaction dictionaries with amount converted to int.
    """
    transactions: list[dict[str, Any]] = []
    with Path(csv_path).open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            transactions.append(
                {
                    "date": row["date"],
                    "type": row["type"],
                    "category": row["category"],
                    "description": row["description"],
                    "amount": int(row["amount"]),
                    "memo": row["memo"],
                }
            )

    return transactions
