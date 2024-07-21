import openpyxl
import json


def get_column_names():
    json_file = open("excel-definition.json", "r")
    data = json.load(json_file)
    return data["column_names"]


def get_excel_data():
    workbook = openpyxl.load_workbook("15isInRange.xlsx")
    sheet = workbook.active
    values = []
    tabela = {}
    for cell in sheet[1]:
        tabela[cell.value] = []
    keys = list(tabela.keys())
    for row in sheet.iter_rows(min_row=2):
        for i, cell in enumerate(row):
            tabela[keys[i]].append(cell.value)
    return tabela


def check_column_number():
    column_number_json = len(get_column_names())
    column_number_excel = len(get_excel_data())

    if column_number_json == column_number_excel:
        print("it's even")
        return True
    else:
        print("it's not even")
        return False


def check_column_names():
    column_names_json = set(get_column_names())
    column_names_excel = set(get_excel_data())

    if column_names_json == column_names_excel:
        return True
    else:
        return False


def check_column_order():
    column_order_json = list(get_column_names())
    column_order_excel = list(get_excel_data())

    if column_order_json == column_order_excel:
        return True
    else:
        return False

if __name__ == "__main__":
    print(get_column_names())
    print(get_excel_data())
    print(check_column_number())
    print(check_column_names())
    print(check_column_order())


