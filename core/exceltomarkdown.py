


def get_longest_values_by_column(rows):
    result = {}

    for row in rows:
        for index, cell in enumerate(row):
            result[index] = get_longest_value_in_column(rows, index)

    return result


def get_longest_value_in_column(rows, index):
    longest_value = ''

    for row in rows:
        try:
            value = row[index]
        except IndexError:
            break
        if len(str(value)) > len(str(longest_value)):
            longest_value = value

    return longest_value


def just_values(row, longest_values_by_column):
    a = []
    for i, value in enumerate(row):
        a.append(str(value).ljust(longest_values_by_column[i]))
    return a


def headers_values(longest_values_by_column):
    a = []
    for k, v in longest_values_by_column.items():
        a.append('-' * v)
    return a

def write_table(rows: list):
    lines = []
    longest_values_by_column = {k: len(str(v)) for k, v in get_longest_values_by_column(rows).items()}
    headers_done = False
    for row in rows:
        lines.append('| ' + ' | '.join(just_values(row, longest_values_by_column)) + ' |')

        if not headers_done:
            headers_done = True
            lines.append('| ' + ' | '.join(headers_values(longest_values_by_column)) + ' |')

    return '\n'.join(lines)


def generate_tables_from_workbook(file_path, handler):
    data = handler(file_path)

    contents = []

    for sheet, values in data.items():
        contents.append(sheet + '\n')
        contents.append(write_table(values))

    return '\n'.join(contents)


def generate_tables_from_excel_file(file_path: str):
    from pyexcel_xlsx import get_data
    return generate_tables_from_workbook(file_path, get_data)


def generate_tables_from_ods_file(file_path: str):
    from pyexcel_ods import get_data
    return generate_tables_from_workbook(file_path, get_data)
