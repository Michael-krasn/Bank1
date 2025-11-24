import os
from loaders.transactions_loader import (
    load_transactions_from_csv,
    load_transactions_from_xlsx,
    load_transactions_from_json,
    load_transactions
)

DATA_DIR = "data"


def test_load_csv() -> None:
    path = os.path.join(DATA_DIR, "transactions.csv")
    data = load_transactions_from_csv(path)

    assert isinstance(data, list)
    assert len(data) > 0
    assert "amount" in data[0]


def test_load_xlsx() -> None:
    path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
    data = load_transactions_from_xlsx(path)

    assert isinstance(data, list)
    assert len(data) > 0
    assert "amount" in data[0]


def test_load_json() -> None:
    path = os.path.join(DATA_DIR, "transactions.json")
    data = load_transactions_from_json(path)

    assert isinstance(data, list)
    assert len(data) > 0


def test_universal_loader() -> None:
    csv_path = os.path.join(DATA_DIR, "transactions.csv")
    xlsx_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
    json_path = os.path.join(DATA_DIR, "transactions.json")

    assert len(load_transactions(csv_path)) > 0
    assert len(load_transactions(xlsx_path)) > 0
    assert len(load_transactions(json_path)) > 0
