"""Tests for budget.core."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-01",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 1
    assert len(transactions) == 0


def test_add_transaction_preserves_negative_amount() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == -12000
    assert result[-1]["type"] == "지출"


def test_add_transaction_preserves_positive_amount() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == 3500000
    assert result[-1]["type"] == "수입"


def test_add_transaction_allows_empty_description() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["description"] == ""
