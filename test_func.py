from excel_manager.config import BASEDIR_PROJECT
from excel_manager.core.base import ExcelManager

p = path=BASEDIR_PROJECT / 'test_data' / 'test_data.xlsx'

exl_manager = ExcelManager(path=p)

# print(exl_manager.filter({'Столбец3': {'contains': ['Виктор2']}}))
exl_manager.copy_columns(
    dest_path=p,
    dest_sheet='Лист_2',
    columns=[0,1,2]
)