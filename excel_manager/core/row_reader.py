from typing import Any


def read_rows(ws, start_row: int = 1) -> list[list[Any]]:
    """Считываем строки листа начиная с start_row (по умолчанию 1),
    пропуская полностью пустые строки.
    """
    rows: list[list[Any]] = []
    for row in ws.iter_rows(min_row=start_row, values_only=True):
        if any(cell is not None and str(cell).strip() != "" for cell in row):
            rows.append(list(row))
    return rows
