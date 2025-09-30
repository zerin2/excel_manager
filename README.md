# Excel Manager

Инструменты для чтения, фильтрации и переноса данных из Excel (XLSX) файлов с использованием [openpyxl](https://openpyxl.readthedocs.io/).

## Установка

```bash
pip install openpyxl
```

---

## Основные классы и функции

### `BaseExcelManager` (core/base.py)

Базовый класс для работы с Excel.

**Методы:**

- `list_sheets() -> list[str]`  
  Возвращает имена листов книги.
  ```python
  mgr = BaseExcelManager("data.xlsx")
  print(mgr.list_sheets())  # ["Лист1", "Sheet2"]
  ```

- `headers(as_indexed: bool = False)`  
  Возвращает список заголовков.
  ```python
  mgr.headers()          # ["Имя", "Фамилия"]
  mgr.headers(True)      # [(0, "Имя"), (1, "Фамилия")]
  ```

- `data_rows() -> list[list[Any]]`  
  Строки данных после заголовка (без пустых).
  ```python
  rows = mgr.data_rows()
  print(len(rows))
  ```

- `count_rows() -> int`  
  Количество строк данных.
  ```python
  print(mgr.count_rows())
  ```

- `col_to_idx(col: str|int) -> int`  
  Преобразует имя/индекс столбца в 0-based индекс.

- `get_value(row_number: int, col: str|int, absolute: bool=False)`  
  Получить значение из строки/столбца.
  ```python
  mgr.get_value(1, "Имя")          # значение из первой строки данных
  mgr.get_value(5, 2, absolute=True)  # абсолютная ссылка на Excel-ряд
  ```

- `get_column_values(col, include_header=False)`  
  Все значения столбца.
  ```python
  mgr.get_column_values("Фамилия")
  ```

- `filter(rules)`  
  Фильтрация строк по правилам.  
  Пример правил:
  ```python
  rules = {
      "статус": {"equals": ["Отменено", "Черновик"]},
      5: {"contains": ["VIP"]},
  }
  filtered = mgr.filter(rules)
  ```

- `copy_columns(dest_path, dest_sheet, columns, ...)`  
  Копирование выбранных столбцов в другой файл/лист.
  ```python
  mgr.copy_columns("out.xlsx", "Результат", ["Имя", "Фамилия"])
  ```

- `write_rows(dest_path, dest_sheet, rows, start_cell="A1")`  
  Запись произвольных строк.
  ```python
  mgr.write_rows("out.xlsx", "Sheet1", [["A", "B"], [1, 2]])
  ```

- `transfer_by_headers(dest_path, dest_sheet, headers)`  
  Перенос по названиям столбцов.
  ```python
  mgr.transfer_by_headers("out.xlsx", "Sheet1", ["Имя", "Фамилия"])
  ```

- `filter_and_transfer(dest_path, dest_sheet, columns, rules)`  
  Фильтрация и перенос выбранных колонок.
  ```python
  mgr.filter_and_transfer("out.xlsx", "Sheet1", ["Имя"], {"статус": {"equals": ["OK"]}})
  ```

- `transfer_styles(dest_path, dest_sheet, columns, ...)`  
  Перенос стилей (⚠ работает только если `read_only=False`).

---

### `ExcelReview` (review.py)

Наследник `BaseExcelManager` для быстрого анализа данных.

- `print_headers()`  
  Выводит заголовки с индексами.
- `print_sheets()`  
  Показывает список листов.
- `print_column(col, limit=20, include_header=False)`  
  Выводит значения указанного столбца.

```python
from core.review import ExcelReview

r = ExcelReview("data.xlsx")
r.print_headers()
r.print_sheets()
r.print_column("Имя", limit=5)
```

---

### `filter_rows` (row_filters.py)

Фильтрация строк по правилам.

**Сигнатура:**
```python
filter_rows(rows, rules) -> list[list[Any]]
```

**Пример:**
```python
rows = [
    ["A", "VIP"],
    ["B", "Черновик"],
    ["C", ""],
]
rules = {
    1: {"contains": ["VIP"]},
    0: {"equals": ["B"]},
}
filtered = filter_rows(rows, rules)
```

Поддерживаемые условия:
- `equals`
- `not_equals`
- `contains`
- `regex`
- `empty` (True/False)
- `mode` ("or" / "and")

---

### `read_rows` (row_reader.py)

Считывает строки с листа Excel, начиная с заданного ряда.

```python
from core.row_reader import read_rows
rows = read_rows(ws, start_row=2)
```

---

### `utils.py`

- `_norm_header(s)` — нормализация заголовка (нижний регистр + trim).
- `get_sheet_name(wb, names)` — ищет лист по имени (без учёта регистра).
- `make_output_path(src_wb_path)` — формирует путь для результирующего файла.
- `ensure_ws(wb, sheet_name)` — возвращает лист (создаёт при отсутствии).

```python
from core.utils import get_sheet_name, ensure_ws

ws = get_sheet_name(wb, "Данные")
ws2 = ensure_ws(wb, "Результат")
```

---

## Пример сценария

```python
from core.base import BaseExcelManager

mgr = BaseExcelManager("data.xlsx", sheet="Лист1")

# Заголовки
print(mgr.headers())

# Фильтрация
rules = {"Статус": {"equals": ["OK"]}}
rows = mgr.filter(rules)

# Перенос в новый файл
mgr.copy_columns("out.xlsx", "Sheet1", ["Имя", "Фамилия"], rows)
```

---

## Требования

- Python 3.9+
- `openpyxl`
