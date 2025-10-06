from typing import Optional

from core.excel_manager import ExcelManager, StrOrInt


class ExcelReview(ExcelManager):
    """«Служебный» класс:

    - вывести заголовки
    - вывести значения из столбца
    - посчитать строки
    - показать листы
    """

    def print_headers(self) -> None:
        print('Заголовки:')
        for i, name in enumerate(self.headers(), start=1):
            print(f'[{i:>2}] {name}')

    def print_sheets(self) -> None:
        print('Листы книги:')
        for i, name in enumerate(self.list_sheets(), start=1):
            print(f'[{i:>2}] {name}')

    def print_column(self, col: StrOrInt, limit: Optional[int] = 20,
                     include_header: bool = False) -> None:
        vals = self.get_column_values(col, include_header=include_header)
        if limit is not None:
            vals = vals[:limit]
        title = f'Столбец: {col!r}'
        print(title)
        print('-' * len(title))
        for i, v in enumerate(vals, start=1):
            print(f'{i:>5}: {v!r}')
