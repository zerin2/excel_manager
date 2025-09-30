from excel_manager.config import BASEDIR_PROJECT
from excel_manager.core.base import ExcelManager

exl_manager = ExcelManager(path=BASEDIR_PROJECT / 'test_data' / 'test_data.xlsx')
header = exl_manager.build_header()
print(header.row_idx)
print(header.name_to_idx)
print(header.names)
print(exl_manager.list_sheets())