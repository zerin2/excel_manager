from src.core.main import ExcelManager

p = path = 'test_data.xlsx'

em = ExcelManager(path=p)
rows = em.data_rows()
em.filter_and_transfer(
    dest_path=p,
    dest_sheet="Лист_555",
    columns=["Столбец2", "Столбец3", "Столбец10", "Столбец13", "Столбец14"],
    rules={
        "Столбец3": {"equals": ["Виктор2"], "empty": True},
        "Столбец2": {"equals": ["Надя", "М"], 'mode': 'and'},

    },
    rows=rows,
)
