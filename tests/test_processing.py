from datetime import datetime

import pytest

from src.processing import sort_by_date

# ----------------------------
# ФИКСТУРЫ
# ----------------------------


@pytest.fixture
def valid_data() -> list[dict[str, str]]:
    """Фикстура с корректными данными для сортировки."""
    return [
        {"id": "1", "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": "2", "state": "EXECUTED", "date": "2023-02-01T12:00:00"},
        {"id": "3", "state": "EXECUTED", "date": "2023-03-01T12:00:00"}
    ]


@pytest.fixture
def data_with_same_dates() -> list[dict[str, str]]:
    """Фикстура с одинаковыми датами."""
    return [
        {"id": "1", "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
    ]


@pytest.fixture
def invalid_cases() -> list[tuple[list[dict[str, str]], type[Exception]]]:
    """Фикстура с некорректными данными и ожидаемыми исключениями."""
    return [
        (
            [  # Неверный формат даты
                {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
                {"id": "2", "state": "EXECUTED", "date": "01.01.2023T12:00:00"}
            ],
            ValueError
        ),
        (
            [  # Отсутствует поле "date"
                {"id": "1", "state": "EXECUTED"},
                {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
            ],
            ValueError
        )
    ]


# ----------------------------
# ПАРАМЕТРИЗИРОВАННЫЕ ТЕСТЫ
# ----------------------------

@pytest.mark.parametrize("reverse", [False, True])
def test_sort_valid_data_parametrized(
        valid_data: list[dict[str, str]],
        reverse: bool
) -> None:
    """Тестируем корректную сортировку по возрастанию и убыванию."""
    sorted_data = sort_by_date(valid_data, reverse=reverse)
    dates_sorted = [datetime.fromisoformat(item["date"])
                    for item in sorted_data]
    expected = sorted([datetime.fromisoformat(item["date"])
                       for item in valid_data],
                      reverse=reverse)
    assert dates_sorted == expected
    assert isinstance(sorted_data, list)


def test_sort_with_same_dates(
        data_with_same_dates: list[dict[str, str]]
) -> None:
    """Проверяем сортировку при одинаковых датах."""
    sorted_data = sort_by_date(data_with_same_dates)
    assert len(sorted_data) == 2


@pytest.mark.parametrize("data, expected_error", [
    (
        [  # Неверный формат даты
            {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
            {"id": "2", "state": "EXECUTED", "date": "01.01.2023T12:00:00"}
        ],
        ValueError
    ),
    (
        [  # Отсутствует поле "date"
            {"id": "1", "state": "EXECUTED"},
            {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
        ],
        ValueError
    )
])
def test_sort_invalid_data(
    data: list[dict[str, str]],
    expected_error: type[Exception]
) -> None:
    """Проверяем обработку некорректных данных."""
    with pytest.raises(expected_error):
        sort_by_date(data)
