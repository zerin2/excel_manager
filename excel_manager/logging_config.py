"""Модуль настройки логирования.

Содержит:
- `setup_logging(log_dir, level)` — настройка loguru: вывод в консоль и файлы.
- `log_timed(message)` — декоратор для логирования времени выполнения функций.
"""

import sys
from functools import wraps
from pathlib import Path
from time import perf_counter
from typing import Optional

from loguru import logger


def setup_logging(log_dir: Optional[Path] = None, level: str = "INFO") -> None:
    logger.remove()

    fmt = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
        "| <level>{level: <8}</level> "
        "| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> "
        "- <level>{message}</level>"
    )

    logger.add(sys.stderr, level=level, format=fmt, enqueue=True, backtrace=True, diagnose=True)

    if log_dir:
        Path(log_dir).mkdir(parents=True, exist_ok=True)

        logger.add(
            Path(log_dir) / "info.log",
            rotation="20 MB",
            retention=10,
            level="INFO",
            format=fmt,
            enqueue=True,
        )

        logger.add(
            Path(log_dir) / "error.log",
            rotation="10 MB",
            retention=10,
            level="ERROR",
            format=fmt,
            enqueue=True,
        )

        logger.add(
            Path(log_dir) / "traceback.log",
            rotation="10 MB",
            retention=5,
            level="ERROR",
            backtrace=True,
            diagnose=True,
            format=fmt,
            enqueue=True,
        )


def log_timed(message: str = ""):
    """Декоратор для логирования времени исполнения через perf_counter()."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"{message} — старт")
            t0 = perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.exception(f"Ошибка в {func.__name__}: {e}")
                raise
            finally:
                dt = perf_counter() - t0
                logger.info(f"{message} — завершено за {dt / 60:.2f} мин.")

        return wrapper

    return decorator
