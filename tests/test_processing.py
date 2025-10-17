import unittest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date

class TestBankingOperations(unittest.TestCase):
    # Создаем тестовые данные внутри класса
    test_data = [
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

    # Тесты для функции filter_by_state
    def test_filter_executed(self):
        result = filter_by_state(self.test_data, "EXECUTED")
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertEqual(item["state"], "EXECUTED")

    def test_filter_canceled(self):
        result = filter_by_state(self.test_data, "CANCELED")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["state"], "CANCELED")

    def test_filter_nonexistent_state(self):
        result = filter_by_state(self.test_data, "UNKNOWN")
        self.assertEqual(len(result), 0)

    def test_filter_default_state(self):
        result = filter_by_state(self.test_data)
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertEqual(item["state"], "EXECUTED")

    # Тесты для функции sort_by_date
    def test_sort_ascending(self):
        # Сортируем по возрастанию
        sorted_data = sort_by_date(self.test_data, reverse=False)

        # Создаем ожидаемый порядок сортировки
        expected_order = sorted(
            self.test_data,
            key=lambda x: datetime.fromisoformat(x["date"]),
            reverse=False
        )

        # Сравниваем результаты
        self.assertEqual(sorted_data, expected_order)

    def test_sort_descending(self):
        # Сортируем по убыванию
        sorted_data = sort_by_date(self.test_data)

        # Создаем ожидаемый порядок сортировки
        expected_order = sorted(
            self.test_data,
            key=lambda x: datetime.fromisoformat(x["date"]),
            reverse=True
        )

        # Сравниваем результаты
        self.assertEqual(sorted_data, expected_order)

    def test_sort_with_same_dates(self):
        data_with_same_dates = [
            {"id": "1", "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
            {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
        ]
        sorted_data = sort_by_date(data_with_same_dates)
        self.assertEqual(len(sorted_data), 2)

    def test_invalid_date_format(self):
        invalid_data = [
            {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
            {"id": "2", "state": "EXECUTED", "date": "01.01.2023T12:00:00"}
        ]
        with self.assertRaises(ValueError):
            sort_by_date(invalid_data)

    def test_missing_date_field(self):
        missing_date_data = [
            {"id": "1", "state": "EXECUTED"},
            {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
        ]
        with self.assertRaises(KeyError):
            sort_by_date(missing_date_data)


if __name__ == '__main__':
    unittest.main()
