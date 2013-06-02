from xlsxwriter.workbook import Workbook
from collections import OrderedDict
from input_factory import InputHandler


def create(input):
    """
    Creates the xls file.
    :param input: the json given after its decoded
    :return: return the file name of the file created.
    """
    filename = InputHandler.pop_dict(input,"filename")
    workbook = Workbook(filename)
    formats = InputHandler.init_formats(input,workbook)
    for sheet in input['sheets']:
        process_sheet(workbook,sheet,formats)
    workbook.close()
    return filename


def process_sheet(workbook,sheet,formats):
    """
    Create sheet and add the data given.
    :param workbook: The workbook created for this request.
    :param sheet: The sheetName as given in the json.
    :param formats: Dictionary of string:cell_format as processed by input factory.
    """

    for k,v in sheet.items():
        sorted_dict= OrderedDict(sorted(v.items(), key=lambda t: t[0]))#sort may be important when adding formulas,rely on correct input
        worksheet = workbook.add_worksheet(k)
        add_cells(worksheet,sorted_dict,formats)


def add_cells(sheet,sorted_dict,formats):
    """
    Add cell data to the sheet.
    :param sheet: The current sheet.
    :param sorted_dict: The cell values as given by user.
    :param formats: Dictionary of string:cell_format as processed by input factory.
    """
    conditional_formats = InputHandler.pop_dict(sorted_dict,"conditional_formats")
    column_sizes = InputHandler.pop_dict(sorted_dict,"column_size")

    for k,v in sorted_dict.items():
        new_value = InputHandler.get_args(v,formats)
        new_key = InputHandler.parse_cell_position(k)
        args = new_key+new_value
        sheet.write(*args)#'B2':'1000.10'

    add_conditional_formats(conditional_formats,formats,sheet)
    resize_columns(column_sizes,sheet)


def add_conditional_formats(conditional_formats,formats,worksheet):
    """
     Adds conditional formats on the spreadsheet
    :param conditional_formats: The map of conditional formats as given by json.
    :param formats: The map of formats as given by json.
    :param worksheet: The current worksheet.
    """
    if not conditional_formats:
        return
    for k,v in conditional_formats.items():
        v["format"] = formats.get(v.get("format"))#replace format value with actual format - see json.
        worksheet.conditional_format(k,v)

def resize_columns(column_sizes,worksheet):
    """
    Sets the column size in the given range. Examples 'A:B': 15,'C:C':25.
    :param column_sizes: Map from range (A:B) to value (15).
    :param worksheet: The current worksheet.
    """
    if not column_sizes:
        return
    for k,v in column_sizes.items():
        worksheet.set_column(k,v)