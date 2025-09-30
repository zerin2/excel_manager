"""Константы и справочные структуры проекта."""

from dataclasses import dataclass
from typing import Optional, Union

FILTER_RULES = {
    0: {  # A
        "equals": ['ОЕ Москва ООО "Миранда-медиа"', "ОЕ ОЦО"],
        "contains": ["Розничные системы"],
    },
    21: {"equals": ["Не завершена"]},  # V
    22: {"equals": ["Нет"]},  # W
    23: {"equals": ["Сторно"]},  # X
    2: {"contains": ["_НЕ КП"]},  # C
    43: {"equals": ["N"]},  # AR
    36: {"empty": True},  # AK
}

# @dataclass(frozen=True)
# class AppPaths:
#     """Ключевые пути.
#
#     `template_path` — путь к xlsx‑ шаблону результата.
#     `dicts_path` — опциональный путь к книге, из которой брать Эталон/Справочники.
#     """
#
#     template_path: str = UPLOAD_RESULT_TEMPLATE_FILE
#     dicts_path: Optional[str] = GUID_FILE

StrOrInt = Union[str, int]


@dataclass(frozen=True)
class AppConfig:
    """

    """

    scan_header_rows: int = 50


@dataclass(frozen=True)
class SheetNames:
    """Имена листов для работы."""

    name: tuple[str] = ('Name_1', 'Name_2')
