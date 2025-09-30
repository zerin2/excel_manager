"""Модуль фильтрации строк по заданным правилам.

Содержит:
- `filter_rows(rows, rules)` — исключает строки, если значения в колонках
  удовлетворяют условиям (`equals`, `not_equals`, `contains`, `empty`).
"""

from typing import Any


def filter_rows(rows: list[list[Any]], rules: dict[int, dict[str, Any]]) -> list[list[Any]]:
    """Фильтрация строк по правилам.

    rows: список строк
    rules: словарь вида:
        {
          col_idx: {
             "equals": ["A", "B"], # исключить строки, где значение равно одному из списка
             "contains": ["ABC"], # исключить, если значение содержит подстроку
             "not_equals": ["X"], # исключить, если значение = X
             "empty": True,   # исключить пустые/нулевые значения
          },
        }
    """
    result = []
    for r in rows:
        drop = False
        for col_idx, conds in rules.items():
            if len(r) <= col_idx:
                continue
            val = str(r[col_idx]).strip() if r[col_idx] not in (None, "") else ""

            if "equals" in conds and val in conds["equals"]:
                drop = True
                break
            if "not_equals" in conds and val not in conds["not_equals"]:
                drop = True
                break
            if "contains" in conds and any(sub in val for sub in conds["contains"]):
                drop = True
                break
            if conds.get("empty") and val in ("", "0"):
                drop = True
                break

        if not drop:
            result.append(r)
    return result
