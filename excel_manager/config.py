"""Конфигурация проекта.

Содержит:
- Пути к рабочим, служебным и справочным файлам.
- Инициализацию логирования через `setup_logging`.
"""

from pathlib import Path

from excel_manager.logging_config import setup_logging

BASEDIR_PROJECT = Path(__file__).resolve().parents[1]
LOG_DIR = BASEDIR_PROJECT / 'logs'

setup_logging(log_dir=Path(LOG_DIR), level='INFO')
