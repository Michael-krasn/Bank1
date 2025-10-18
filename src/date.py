from datetime import datetime


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формате
    '2024-03-11T02:26:18.671407' в формат 'ДД.ММ.ГГГГ'.
    """
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


#  Пример использования:
date_string = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_string)
print(formatted_date)  # Выведет: 11.03.2024
