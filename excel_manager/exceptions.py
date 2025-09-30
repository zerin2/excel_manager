"""Кастомные исключения проекта.

Содержит:
- `CustomBaseException` — базовый класс.
- `IncorrectSourceError` — ошибка неверного формата/структуры входного файла.
- `WrongColumnError` — ошибка при некорректной колонке.
- `MissingColumnsError` — ошибка при отсутствии нужных колонок.
"""


class CustomBaseException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __repr__(self):
        return f"({self.__class__.__name__}): {self.message}"

    def __str__(self):
        return self.__repr__()


class IncorrectSourceError(CustomBaseException):
    """Ошибка, возникающая при неверном формате или структуре входного файла."""

    def __init__(self, message="Неверный формат или структура входного файла"):
        super().__init__(message)


class WrongColumnError(CustomBaseException):
    """Ошибка, выбрасываемая при обнаружении некорректной колонки в данных."""

    def __init__(self, message="Обнаружена некорректная колонка в данных"):
        super().__init__(message)


class MissingColumnsError(CustomBaseException):
    """Ошибка, указывающая на отсутствие необходимых колонок в источнике данных."""

    def __init__(self, message="Отсутствуют необходимые колоноки в источнике данных"):
        super().__init__(message)
