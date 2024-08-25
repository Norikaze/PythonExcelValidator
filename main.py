from datetime import datetime

import openpyxl
import json
from data_checkers import check_column_number, check_column_names, check_column_order
from file_access import get_column_names, get_excel_data

def print_excel_data(excel_file_name):
    data_dict = get_excel_data(excel_file_name)
    for value in data_dict.values():
        for data in value:
            print(data)



def compare_data_types(excel_file_name):
    column_data_type_json = read_column_data_types()
    column_data_type_excel = get_excel_data(excel_file_name)
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
    excel_file_name = r"C:\Users\admin\PycharmProjects\ExcelStart\15isInRange.xlsx"
    print("Getting column names...")
    print(get_column_names())
    print("Getting excel data..")
    print(get_excel_data(excel_file_name))
    print("Checking column number...")
    print(check_column_number(excel_file_name))
    print("Checking column names..")
    print(check_column_names(excel_file_name))
    print("Checking column order...")
    print(check_column_order(excel_file_name))
    print("comparing data types...")
    compare_data_types("15isInRange.xlsx")
    print("Reading column data types...")
    print(read_column_data_types())
    print_excel_data(excel_file_name)



