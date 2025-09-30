"""
Модуль фильтрации строк по заданным правилам.

"""

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
             "regex": [r"..."],  # исключить, если значение совпадает по регулярке
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
            val = str(r[col_idx]).strip() if r[col_idx] not in (None, '') else ''

            checks = []

            if 'equals' in conds:
                checks.append(val in conds['equals'])
            if 'not_equals' in conds:
                checks.append(val in conds['not_equals'])
            if 'contains' in conds:
                checks.append(any(sub in val for sub in conds['contains']))
            if 'regex' in conds:
                import re
                checks.append(any(re.search(pat, val) for pat in conds['regex']))
            if 'empty' in conds:
                if conds['empty'] is True:
                    checks.append(val in ('', '0'))
                elif conds['empty'] is False:
                    checks.append(val not in ('', '0'))

            mode = conds.get('mode', 'or').lower()
            if (mode == 'or' and any(checks)) or (mode == 'and' and all(checks)):
                drop = True
                break

        if not drop:
            result.append(r)
    return result
