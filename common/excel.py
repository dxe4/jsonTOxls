a_to_z = range(ord("a"), ord("z"))


def number_to_cell(row, col):
    new_row = chr(a_to_z[col])
    return new_row.upper() + str(row)


def number_to_cell(col):
    return chr(a_to_z[col])


def number_to_cells(columns):
    return [chr(a_to_z[col]) for col in columns]


