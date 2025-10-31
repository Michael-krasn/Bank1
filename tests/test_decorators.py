from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from decorators import log


def test_log_success(tmp_path: Path, capsys: Any) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(x: int, y: int) -> int:
        return x + y

    result = add(2, 3)
    assert result == 5

    content = log_file.read_text(encoding="utf-8").strip()
    assert content == "add ok"


def test_log_error(tmp_path: Path) -> None:
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    content = log_file.read_text(encoding="utf-8").strip()
    assert "divide error: ZeroDivisionError" in content
    assert "Inputs: (5, 0)" in content


def test_log_to_console(capsys: Any) -> None:
    @log()
    def mult(x: int, y: int) -> int:
        return x * y

    result = mult(3, 4)
    assert result == 12

    captured = capsys.readouterr()
    assert "mult ok" in captured.out


def test_log_error_console(capsys: Any) -> None:
    @log()
    def bad_div(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        bad_div(1, 0)

    captured = capsys.readouterr()
    assert "bad_div error: ZeroDivisionError" in captured.err
