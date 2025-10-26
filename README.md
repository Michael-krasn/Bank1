                                             # Новые банковские операции #
## Цель проекта ##
Разширить функционал банковских операций.
## Установка ##
1.Клонируйте [проект](https://github.com/Michael-krasn/Bank1/tree/main/src)
2.Клонируйте проект:

bash
git clone https://github.com/Michael-krasn/Bank1/tree/main/src
Установите Poetry (если еще не установлен):

bash
curl -sSL https://install.python-poetry.org | python3 -
Перейдите в директорию проекта:

bash
cd путь/к/проекту
Активируйте виртуальное окружение:

bash
poetry shell
Установите зависимости проекта:

bash
poetry install

Обновить все зависимости:

bash
poetry update

## Использование ##
В проекте есть несколько функции, реализующих разные фичи
* filter_by_state, функция сортирует операции по статусу
Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
* функция sort_by_date сортирует данные операций по дате
Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
* функция mask_account_card скрывает счёт или номер карты
 Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции

# Модуль generators

Модуль generators содержит функции-генераторы для работы с транзакциями и генерации номеров карт.

## Функции

### 1. filter_by_currency(transactions, currency)
Фильтрует список транзакций по коду валюты и возвращает итератор.

Пример:
```python
from generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}},
]

usd_tx = filter_by_currency(transactions, "USD")
for tx in usd_tx:
    print(tx)
```
## Обновление ##

Была добавлена функция generators


## Автор ##
Красноперов Михаил Андреевич

