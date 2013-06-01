from xlsxwriter.workbook import Workbook
from collections import OrderedDict
from input_factory import InputHandler

filename = 'sample.xlsx'
def create(input):
    """
    Creates the xls file
    :param input: the json given after its decoded
    :return: return the file name of the file created.
    """
    workbook = Workbook(filename)
    formats = InputHandler.init_formats(input,workbook)
    for sheet in input['sheets']:
        processSheet(workbook,sheet,formats)
    workbook.close()
    return filename


def processSheet(workbook,sheetName,formats):
    """
    Create sheet and add the data given
    :param workbook: The workbook created for this request
    :param sheetName: The sheetName as given in the json
    :param formats: Dictionary of string:cell_format as processed by input factory
    """
    for k,v in sheetName.items():
        sorted_dict= OrderedDict(sorted(v.items(), key=lambda t: t[0]))#sort may be important when adding formulas,rely on correct input
        sheet = workbook.add_worksheet(k)
        addCells(sheet,sorted_dict,formats)

def addCells(sheet,sorted_dict,formats):
    """
    Add cell data to the sheet
    :param sheet: The current sheet
    :param sorted_dict: The cell values as given by user
    :param formats: Dictionary of string:cell_format as processed by input factory
    """
    for k,v in sorted_dict.items():
        args = InputHandler.get_args(v,formats)
        def is_tuple():
            sheet.write(k,*args)#'B3':{'value':'123.52','format':'number_bold_red'},
        def is_str():
            sheet.write(k,v)#'B2':'1000.10',
        functions = {tuple:is_tuple,str:is_str}
        functions[args.__class__]()


