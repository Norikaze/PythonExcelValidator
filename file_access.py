import json

import openpyxl

def get_column_names():
    json_file = open("excel-definition.json", "r")
    data = json.load(json_file)
    json_file.close()
    return data["column_names"]

def get_excel_data(excel_file_name):
    workbook = openpyxl.load_workbook(excel_file_name)
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