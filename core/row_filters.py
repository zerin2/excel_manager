"""
Модуль фильтрации строк по заданным правилам.
"""

import re
from typing import Any


def filter_rows(rows: list[list[Any]], rules: dict[int, dict[str, Any]]) -> list[list[Any]]:
    """Фильтрация строк по правилам.

    rows: список строк
    rules: словарь вида:
        {
          col_idx: {
             "equals": ["A", "B"],   # исключить строки, где значение равно одному из списка
             "not_equals": ["X"],    # исключить, если значение = X
             "contains": ["ABC"],    # исключить, если значение содержит подстроку
             "regex": [r"..."],      # исключить, если значение совпадает по регулярке
             "empty": True,          # исключить пустые/нулевые значения
             "mode": "or",           # логика: or (по умолчанию) / and
          },
        }
    """
    result = []

    for r in rows:
        drop = False
        for col_idx, conds in rules.items():
            if len(r) <= col_idx:
                continue

            checks = []
            val = str(r[col_idx]).strip() if r[col_idx] not in (None, '') else ''

            equals = conds.get('equals', [])
            not_equals = conds.get('not_equals', [])
            contains = conds.get('contains', [])
            regex_list = conds.get('regex', [])

            if equals:
                checks.append(val in equals)
            if not_equals:
                checks.append(val in not_equals)
            if contains:
                checks.append(any(sub in val for sub in contains))
            if regex_list:
                checks.append(any(re.search(pat, val) for pat in regex_list))

            empty = conds.get('empty')
            if empty is True:
                checks.append(val in ('', '0'))
            elif empty is False:
                checks.append(val not in ('', '0'))

            mode = conds.get('mode', 'or').lower()
            if (mode == 'or' and any(checks)) or (mode == 'and' and all(checks)):
                drop = True
                break

        if not drop:
            result.append(r)

    return result
