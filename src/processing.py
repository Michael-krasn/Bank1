from datetime import datetime
from typing import Any, Dict, List, Optional


def filter_by_state(
    data: List[Dict[str, str]],
    state: Optional[str] = None
) -> List[Dict[str, str]]:

    # Проверяем, если state None, устанавливаем значение по умолчанию
    if state is None:
        state = 'EXECUTED'

    # Добавляем отладку
    print(f"Фильтруем по состоянию: {state}")

    # Фильтрация с дополнительной проверкой
    return [
        item
        for item in data
        if item.get('state') is not None and item.get('state') == state
    ]


def sort_by_date(
    data: List[Dict[str, Any]],  # Список словарей с данными операций
    reverse: bool = False  # Флаг сортировки (по умолчанию - по возрастанию)
) -> List[Dict[str, Any]]:  # Возвращаем отсортированный список словарей
    try:
        return sorted(
            data,
            key=lambda x: datetime.fromisoformat(x["date"]),
            reverse=reverse
        )
    except KeyError:
        raise ValueError("В данных отсутствует поле 'date'")
    except ValueError as ve:
        raise ValueError(f"Ошибка формата даты: {str(ve)}")
