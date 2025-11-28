from typing import List, Dict
from src.utils import load_operations
from src.processing import filter_by_state, sort_by_date
from src.external_api import get_rub_amount
from src.search import process_bank_search
from src.masks import get_mask_account, get_mask_card_number

def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Пользователь: ").strip()

    if file_choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        data = load_operations("data/operations.json")
    elif file_choice == "2":
        from src.file_readers import read_transactions_from_csv
        data = read_transactions_from_csv("data/transactions.csv")
    elif file_choice == "3":
        from src.file_readers import read_transactions_from_excel
        data = read_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Некорректный выбор файла")
        return

    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_input = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                             "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n"
                             "Пользователь: ").upper()
        if status_input in valid_states:
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    filtered_data: List[Dict] = filter_by_state(data, status_input)

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice in ["да", "yes"]:
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        reverse = order == "по убыванию"
        filtered_data = sort_by_date(filtered_data, reverse=reverse)

    rub_only = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if rub_only in ["да", "yes"]:
        filtered_data = [t for t in filtered_data if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if search_choice in ["да", "yes"]:
        search_word = input("Введите строку для поиска: ")
        filtered_data = process_bank_search(filtered_data, search_word)

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
    for t in filtered_data:
        date = t.get("date", "дата неизвестна")
        description = t.get("description", "")
        amount = t.get("operationAmount", {}).get("amount", "")
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "")
        from_acc = t.get("from", "")
        to_acc = t.get("to", "")

        if from_acc and to_acc:
            from_acc_masked = get_mask_card_number(from_acc) if "Карта" in from_acc else get_mask_account(from_acc)
            to_acc_masked = get_mask_card_number(to_acc) if "Карта" in to_acc else get_mask_account(to_acc)
            print(f"{date} {description}\n{from_acc_masked} -> {to_acc_masked}\nСумма: {amount} {currency}\n")
        else:
            account_masked = get_mask_account(to_acc) if to_acc else ""
            print(f"{date} {description}\n{account_masked}\nСумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()
