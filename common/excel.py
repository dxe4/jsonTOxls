a_to_z = range(ord("a"), ord("z"))


def number_to_cell(row, col):
    new_row = chr(a_to_z[row])
    return new_row.upper() + str(col)


