import unittest

from parameterized import parameterized  # type: ignore

from src.processing import filter_by_state, sort_by_date


class TestBankingOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data = [
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

    @parameterized.expand([
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("UNKNOWN", 0),
        ("", 2)  # Пустая строка как дефолт
    ])
    def test_filter_by_state(self, state, expected_count):
        # Проверяем оба варианта вызова функции
        if state:
            result = filter_by_state(self.test_data, state)
        else:
            result = filter_by_state(self.test_data)

        self.assertEqual(len(result), expected_count)
        if state:
            for item in result:
                self.assertEqual(item["state"], state)

    @parameterized.expand([
        (False, "2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01"),
        (True, "2023-04-01", "2023-03-01", "2023-02-01", "2023-01-01")
    ])
    def test_sort_by_date(self, reverse, *expected_dates):
        sorted_data = sort_by_date(self.test_data, reverse=reverse)
        actual_dates = [item["date"][:10] for item in sorted_data]
        self.assertEqual(actual_dates, list(expected_dates))

    def test_sort_with_same_dates(self):
        data_with_same_dates = [
            {"id": "1", "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
            {"id": "2", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
        ]
        sorted_data = sort_by_date(data_with_same_dates)
        self.assertEqual(len(sorted_data), 2)

    @parameterized.expand([
        ("2023-01-01", ValueError),
        ("01.01.2023T12:00:00", ValueError),
        ("2023-01-01 12:00:00", ValueError),
        ("12:00:00 2023-01-01", ValueError),
        (1234567890, ValueError),  # проверка на нестроковый тип
        (None, ValueError),  # проверка на None
        ("", ValueError),  # проверка на пустую строку
    ])
    def test_invalid_date_format(self, invalid_date, expected_exception):
        invalid_data = [
            {"id": "1", "state": "EXECUTED", "date": invalid_date}
        ]

        with self.assertRaises(expected_exception) as context:
            sort_by_date(invalid_data)

        self.assertIn("Неверный формат даты", str(context.exception))

    def test_valid_iso_format(self):
        valid_data = [
            {"id": "1", "state": "EXECUTED", "date": "2023-01-01T12:00:00"}
        ]

        result = sort_by_date(valid_data)
        self.assertEqual(len(result), 1)

    def test_non_string_date(self):
        invalid_data = [
            {"id": "1", "state": "EXECUTED", "date": 1234567890}
        ]

        with self.assertRaises(ValueError):
            sort_by_date(invalid_data)

    def test_none_date(self):
        invalid_data = [
            {"id": "1", "state": "EXECUTED", "date": None}
        ]

        with self.assertRaises(ValueError):
            sort_by_date(invalid_data)

    def test_empty_string_date(self):
        invalid_data = [
            {"id": "1", "state": "EXECUTED", "date": ""}
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
