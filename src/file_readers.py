import csv
from typing import List, Dict, Any
import openpyxl
import os

DATA_DIR = os.path.join(os.getcwd(), "data")
CSV_FILE = os.path.join(DATA_DIR, "transactions.csv")
XLSX_FILE = os.path.join(DATA_DIR, "transactions_excel.xlsx")


def read_transactions_from_csv(path: str) -> List[Dict[str, str]]:
    """
    Читает CSV-файл и возвращает список словарей транзакций.
    CSV использует разделитель ';'
    """
    transactions: List[Dict[str, str]] = []

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            transactions.append(dict(row))

    return transactions


def read_transactions_from_excel(path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл (xlsx) и возвращает список словарей транзакций.
    """
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    rows = list(ws.values)
    headers = rows[0]
    transactions: List[Dict[str, Any]] = []

    for row in rows[1:]:
        transactions.append(dict(zip(headers, row)))

    return transactions
