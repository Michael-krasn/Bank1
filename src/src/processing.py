import re
from datetime import datetime
from typing import Dict, List


def filter_by_state(banking_operation: List[Dict[str, str]], state="EXECUTED"):
    """функция принимает на вход списик словарей и параметр сортировки,
    возвращает новый отсортированный список по параметру. 'state'"""

    return [x for x in banking_operation if x["state"] == state]


def sort_by_date(
    data: List[Dict[str, str]],
    reverse: bool = False
) -> List[Dict[str, str]]:  # Добавляем аннотацию возвращаемого типа
    def parse_date(item):
        try:
            # Проверяем наличие поля date
            if "date" not in item:
                raise KeyError("Отсутствует поле даты")

            # Проверяем тип данных
            if not isinstance(item["date"], str):
                raise ValueError("Дата должна быть строкой")

            # Проверяем формат даты через регулярное выражение
            date_format = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
            if not re.match(date_format, item["date"]):
                raise ValueError("Неверный формат даты")

            datetime.fromisoformat(item["date"])
            return item["date"]

        except ValueError:
            raise ValueError("Неверный формат даты")
        except KeyError as e:
            raise KeyError(str(e))

    try:
        return sorted(
            data,
            key=parse_date,
            reverse=reverse
        )
    except (ValueError, KeyError) as e:
        raise e
