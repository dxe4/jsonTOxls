from xlsxwriter.workbook import Workbook
from collections import OrderedDict
from input_factory import InputHandler

filename = 'sample.xlsx'
def create(input):
    workbook = Workbook(filename)
    formats = InputHandler.init_formats(input,workbook)
    for sheet in input['sheets']:
        processSheet(workbook,sheet,formats)
    workbook.close()
    return filename


def processSheet(workbook,sheet,formats):
    for k,v in sheet.items():
        sorted_dict= OrderedDict(sorted(v.items(), key=lambda t: t[0]))
        sheet = workbook.add_worksheet(k)
        addCells(sheet,sorted_dict,formats)

def addCells(sheet,sorted_dict,formats):
    for k,v in sorted_dict.items():
        args = InputHandler.get_args(v,formats)
        def is_tuple():
            sheet.write(k,*args)
        def is_str():
            sheet.write(k,v)
        functions = {tuple:is_tuple,str:is_str}
        functions[args.__class__]()

