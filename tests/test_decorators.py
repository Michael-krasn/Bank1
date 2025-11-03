from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from src.decorators import log


def test_log_success(tmp_path: Path, capsys: Any) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(x: int, y: int) -> int:
        return x + y

    result = add(2, 3)
    assert result == 5

    content = log_file.read_text(encoding="utf-8").strip()
    # Проверяем части строки, а не точное совпадение
    assert "Функция: add" in content
    assert "Результат: 5" in content
    assert "Время:" in content


def test_log_error(tmp_path: Path) -> None:
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    content = log_file.read_text(encoding="utf-8").strip()

    # Проверяем ключевые части сообщения
    assert "Ошибка в функции: divide" in content
    assert "ZeroDivisionError: division by zero" in content
    assert "Аргументы: args=(5, 0)" in content
    assert "Время:" in content


def test_log_to_console(capsys: Any) -> None:
    @log()
    def mult(x: int, y: int) -> int:
        return x * y

    result = mult(3, 4)
    assert result == 12

    captured = capsys.readouterr()

    # Проверяем фрагменты реального лога
    assert "Функция: mult" in captured.out
    assert "Результат: 12" in captured.out
    assert "Время:" in captured.out


def test_log_error_console(capsys: Any) -> None:
    @log()
    def bad_div(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        bad_div(1, 0)

    captured = capsys.readouterr()

    # Проверяем ключевые части реального лога
    assert "Ошибка в функции: bad_div" in captured.out
    assert "ZeroDivisionError: division by zero" in captured.out
    assert "Аргументы: args=(1, 0)" in captured.out
    assert "Время:" in captured.out
