from file_access import get_column_names, get_excel_data
def check_column_number(excel_file_name):
    column_number_json = len(get_column_names())
    column_number_excel = len(get_excel_data(excel_file_name))

    if column_number_json == column_number_excel:
        print("it's even")
        return True
    else:
        print("it's not even")
        return False


def check_column_names(excel_file_name):
    column_names_json = set(get_column_names())
    column_names_excel = set(get_excel_data(excel_file_name))

    if column_names_json == column_names_excel:
        return True
    else:
        return False


def check_column_order(excel_file_name):
    column_order_json = list(get_column_names())
    column_order_excel = list(get_excel_data(excel_file_name))

    if column_order_json == column_order_excel:
        return True
    else:
        return False