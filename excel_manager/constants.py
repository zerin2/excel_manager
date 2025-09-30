"""Константы и справочные структуры проекта.

Содержит:
- `FILTER_RULES` — словарь правил фильтрации строк.
- `AppPaths` — ключевые пути (шаблон, справочники).
- `StageName` — названия этапов.
- `SheetNames` — имена листов.
- `ColumnMap` — индексы колонок (с комментариями по Excel).
"""

from dataclasses import dataclass
from typing import Optional


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


@dataclass(frozen=True)
class AppPaths:
    """Ключевые пути.

    `template_path` — путь к xlsx‑ шаблону результата.
    `dicts_path` — опциональный путь к книге, из которой брать Эталон/Справочники.
    """

    template_path: str = UPLOAD_RESULT_TEMPLATE_FILE
    dicts_path: Optional[str] = GUID_FILE


@dataclass(frozen=True)
class StageName:
    """Имена этапов работы скрипта."""

    attachments_report: str = "Этап 1. Отчёт по вложениям."
    sf_only_report: str = "Этап 2. Проверка СФ без вложений."
    tax_none_with_sf_report: str = "Этап 3. Нет налога, но есть СФ."
    tax_yes_without_sf_report: str = "Этап 4. Отчёт: есть налог, но нет СФ."
    full_file_processing = "Полная обработка файла"


@dataclass(frozen=True)
class SheetNames:
    """Имена листов в исходнике и шаблоне."""

    spec: tuple[str] = ("Спец.выгрузка", "Export Worksheet")
    etalon: tuple[str] = ("Эталон",)
    sprav: tuple[str] = ("Справочник", "Справочники")

    # Листы результата в шаблоне:
    stage1: str = "1_набор-вложения"
    stage2: str = "2_набор-вложения"
    stage3: str = "3_код налога-вложение"
    stage4: str = "4_код налога-уведомление"


@dataclass(frozen=True)
class ColumnMap:
    """Карта индексов (0-based) для колонок листа «Спец.выгрузка».

    Назначение:
    - каждый атрибут соответствует определённой колонке Excel;
    - используется при выборках и проверках на всех этапах;
    - индексы заданы в Python-стиле (0 = первая колонка в Excel).
    """

    # Ключ документа (Номер транзакции)
    vkey_idx: int = 4  # excel 5

    # Тип / словарь
    tip_idx: int = 36  # excel 37

    # Примечание для сверки со справочником:
    note_idx: int = 26  # excel 27

    # Флаг "формирует сч.ф." (Да/Нет)
    tax_flag_idx: int = 16  # excel 17

    # Код налога
    tax_code_idx: int = 15  # excel 16

    # Вложения типа СФ ищутся по "Категории влож.документа"
    doc_category_idx: int = 26  # excel 27

    # Куда пишем в Этапе 1:
    comment_col_idx: int = 42  # (43 столбец) ->  AP
    notes_col_idx: int = 43  # (44 столбец) ->  AQ

    # Запись в шаблоне
    output_start_row: int = 3  # начинаем запись с A3
