from typing import Dict, List

import pytest


@pytest.fixture
def banking_data() -> List:
    return [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00"
        },
        {
            "id": "2",
            "state": "CANCELED",
            "date": "2023-02-01T12:00:00"
        },
        {
            "id": "3",
            "state": "EXECUTED",
            "date": "2023-03-01T12:00:00"
        },
        {
            "id": "4",
            "state": "PENDING",
            "date": "2023-04-01T12:00:00"
        }
    ]


@pytest.fixture
def invalid_date_data() -> List:
    return [
        {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
        {"id": "2", "state": "EXECUTED", "date": "01.01.2023T12:00:00"}
    ]


@pytest.fixture
def missing_date_data() -> List:
    return [
        {"id": "1", "state": "EXECUTED"},
        {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
    ]


@pytest.fixture
def valid_card_numbers() -> Dict:
    return {
        "base": {
            "input": "1234 5678 9012 3456",
            "expected": "1234 56** **** 3456"
        },
        "no_spaces": {
            "input": "1234567890123456",
            "expected": "1234 56** **** 3456"
        },
        "different_digits": {
            "input": "9876543210987654",
            "expected": "9876 54** **** 7654"
        }
    }


@pytest.fixture
def invalid_card_numbers() -> List[str]:
    return [
        "123456789012345",    # короче 16 цифр
        "12345678901234567",  # длиннее 16 цифр
        "",                   # пустая строка
        "1234abcd90123456",   # с буквами
        "1234!@#$90123456"    # со спецсимволами
    ]


@pytest.fixture
def valid_account_numbers() -> Dict:
    return {
        "base": {
            "input": "12049104570157075645",
            "expected": "**5645"
        },
        "different": {
            "input": "98765432109876543210",
            "expected": "**3210"
        }
    }


@pytest.fixture
def invalid_account_numbers() -> List[str]:
    return [
        "1234567890123456789",  # короче 20 цифр
        "123456789012345678901",  # длиннее 20 цифр
        "",                     # пустая строка
        "1234abcd901234567890",  # с буквами
        "1234!@#$901234567890",  # со спецсимволами
        "1234 5678 9012 3456 7890"  # с пробелами
    ]


@pytest.fixture
def invalid_inputs() -> List[str]:
    return [
        "1234567890123456",  # Отсутствует тип операции
        "Счет",              # Отсутствует номер счета
        "Карта",             # Отсутствует номер карты
        "Кошелек 1234567890123456"  # Неизвестный тип операции
    ]


@pytest.fixture
def valid_inputs() -> Dict[str, Dict[str, str]]:
    return {
        "account": {
            "input": "Счет 12345678901234567890",
            "expected": "Счет **7890"
        },
        "card": {
            "input": "Карта 1234567890123456",
            "expected": "Карта 1234 56** **** 3456"
        }
    }
