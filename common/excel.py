a_to_z = range(ord("a"), ord("z"))


def number_to_cell(row, col):
    new_row = chr(a_to_z[col]).upper()
    return new_row.upper() + str(row)


def number_to_cell(col):
    return chr(a_to_z[col]).upper()


def number_to_cells(columns):
    return [chr(a_to_z[col]).upper() for col in columns]


