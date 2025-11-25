import csv
import os
from typing import Any, Dict, List

from openpyxl import load_workbook

# Пути к файлам
DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "transactions.csv")
XLSX_FILE = os.path.join(DATA_DIR, "transactions_excel.xlsx")


def read_transactions_from_csv() -> List[Dict[str, Any]]:
    """
    Чтение финансовых операций из CSV-файла (data/transactions.csv)
    список словарей с транзакциями
    """
    transactions: List[Dict[str, Any]] = []

    # DictReader сам использует запятую как разделитель по умолчанию
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(dict(row))

    return transactions


def read_transactions_from_excel() -> List[Dict[str, Any]]:
    """
    Чтение финансовых операций из Excel-файла (data/transactions_excel.xlsx)
    список словарей с транзакциями
    """
    workbook = load_workbook(filename=XLSX_FILE)
    sheet = workbook.active

    # Заголовки из первой строки
    headers: List[str] = [cell.value for cell in next(sheet.iter_rows(min_row=1, max_row=1))]  # type: ignore

    transactions: List[Dict[str, Any]] = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        entry: Dict[str, Any] = {headers[i]: row[i] for i in range(len(headers))}
        transactions.append(entry)

    return transactions
