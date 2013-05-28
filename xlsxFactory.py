from xlsxwriter.workbook import Workbook
from collections import OrderedDict

filename = 'sample.xlsx'
def create(sheet_list):
    print(sheet_list)
    workbook = Workbook(filename)
    for sheet in sheet_list:
        for k,v in sheet.items():
            sorted_dict= OrderedDict(sorted(v.items(), key=lambda t: t[0]))
            sheet = workbook.add_worksheet(k)
            processSheet(sheet,sorted_dict)
    workbook.close()
    return filename

def processSheet(sheet,dict):
    for k,v in dict.items():
        sheet.write(k,v)
