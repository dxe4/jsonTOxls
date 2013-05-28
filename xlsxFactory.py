from xlsxwriter.workbook import Workbook
from collections import OrderedDict

filename = 'sample.xlsx'
def create(input):
    workbook = Workbook(filename)
    formats = init_formats(input,workbook)
    for sheet in input['sheets']:
        processSheet(workbook,sheet,formats)
    workbook.close()
    return filename

def init_formats(input,workbook):
    return_dict = {}
    if not input.__contains__('formats'):
        return return_dict
    for k,v in input.pop('formats').items():
        return_dict[k] = workbook.add_format(v)
    return return_dict

def processSheet(workbook,sheet,formats):
    for k,v in sheet.items():
        sorted_dict= OrderedDict(sorted(v.items(), key=lambda t: t[0]))
        sheet = workbook.add_worksheet(k)
        addCells(sheet,sorted_dict,formats)

def addCells(sheet,sorted_dict,formats):
    for k,v in sorted_dict.items():
        args = get_args(v,formats)
        def is_tuple():
            sheet.write(k,*args)
        def is_str():
            sheet.write(k,v)
        functions = {tuple:is_tuple,str:is_str}
        functions[args.__class__]()

def get_args(value,formats):
    def is_dict():
        return value['value'],formats[value['format']]
    def is_str():
        return value
    functions = {dict:is_dict,str:is_str}
    return functions[value.__class__]()