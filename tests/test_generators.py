import builtins as blt
from typing import Any, Dict, List
import pytest

# Явный импорт из пакета src
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions
)


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с примером транзакций"""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2022-01-01T10:00:00.000000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "Доллар США", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2022-01-02T10:00:00.000000",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "Евро", "code": "EUR"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "state": "CANCELED",
            "date": "2022-01-03T10:00:00.000000",
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "Доллар США", "code": "USD"},
            },
            "description": "Оплата услуг",
        },
    ]


# ---------- Тесты для filter_by_currency ----------

def test_filter_by_currency_usd(
        sample_transactions: List[Dict[str, Any]])\
        -> None:
    result_list: List[Dict[str, Any]] = blt.list(
        filter_by_currency(sample_transactions, "USD"))
    assert len(result_list) == 2
    assert all(
        tx["operationAmount"]["currency"]["code"] == "USD"
        for tx in result_list)


def test_filter_by_currency_no_match(
        sample_transactions:
        List[Dict[str, Any]]) -> None:
    result_list: List[Dict[str, Any]] = blt.list(
        filter_by_currency(sample_transactions, "GBP"))
    assert result_list == []


def test_filter_by_currency_empty_list() -> None:
    result_list: List[Dict[str, Any]] = blt.list(filter_by_currency([], "USD"))
    assert result_list == []


def test_filter_by_currency_missing_keys() -> None:
    transactions: List[Dict[str, Any]] = [{"id": 1}, {"operationAmount": {}}]
    result_list: List[Dict[str, Any]] = blt.list(
        filter_by_currency(transactions, "USD"))
    assert result_list == []


# ---------- Тесты для transaction_descriptions ----------

def test_transaction_descriptions(
        sample_transactions:
        List[Dict[str, Any]]) -> None:
    descriptions_list: List[str] = list(
        transaction_descriptions(sample_transactions))
    assert descriptions_list == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Оплата услуг",
    ]


def test_transaction_descriptions_empty_list() -> None:
    descriptions_list: List[str] = list(
        transaction_descriptions([]))
    assert descriptions_list == []


def test_transaction_descriptions_missing_field() -> None:
    tx: List[Dict[str, Any]] = [{"id": 1}, {"description": "Тест"}]
    descriptions_list: List[str] = list(
        transaction_descriptions(tx))
    assert descriptions_list == ["Тест"]


# ---------- Тесты для card_number_generator ----------

@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003"]),
        (
            9999999999999997,
            9999999999999999,
            [
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator_valid(
        start: int, end: int, expected: List[str])\
        -> None:
    result_list: List[str] = blt.list(card_number_generator(start, end))
    assert result_list == expected


@pytest.mark.parametrize("start, end", [(0, 10), (5, 1), (1, 10**20)])
def test_card_number_generator_invalid_range(start: int, end: int) -> None:
    with pytest.raises(ValueError):
        _ = blt.list(card_number_generator(start, end))
