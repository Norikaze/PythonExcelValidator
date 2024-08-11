from datetime import datetime

import openpyxl
import json


def get_column_names():
    json_file = open("excel-definition.json", "r")
    data = json.load(json_file)
    json_file.close()
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

def print_excel_data():
    data_dict = get_excel_data()
    for value in data_dict.values():
        for data in value:
            print(data)


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


def compare_data_types():
    column_data_type_json = read_column_data_types()
    column_data_type_excel = get_excel_data()
    # print(column_data_type_excel.values())
    # print(column_data_type_json.values())

    types_correct = True
    for (column_name, column_data), expected_data_type in zip(column_data_type_excel.items(), column_data_type_json.values()):
        # print(f"printing data_excel")
        # print(column)
        # print(f"printing data_json")
        # print(expected_data_type)
        for cell_value in column_data:
            if type(cell_value) == expected_data_type:
                print("It's a match ✌")
            else:
                print(f"Not matching data type, expected {expected_data_type}, got value - {cell_value}, error in column - {column_name}")
                types_correct = False

    return types_correct

def read_column_data_types():
    json_file = open("excel-definition.json", "r")
    data = json.load(json_file)
    data_types = data["column_data_types"]
    json_file.close()
    rv = {}
    for k, v in data_types.items():
        # print(k, v)
        if v == "integer":
            rv[k] = int
        elif v == "string":
            rv[k] = str
        elif v == "boolean":
            rv[k] = bool
        elif v == "float":
            rv[k] = float
        elif v == "date":
            rv[k] = datetime

    return rv






if __name__ == "__main__":
    # print("Getting column names...")
    # print(get_column_names())
    # print("Getting excel data..")
    # print(get_excel_data())
    # print("Checking column number...")
    # print(check_column_number())
    # print("Checking column names..")
    # print(check_column_names())
    # print("Checking column order...")
    # print(check_column_order())
    print("comparing data types...")
    compare_data_types()
    # print("Reading column data types...")
    # print(read_column_data_types())
    #  print_excel_data()



