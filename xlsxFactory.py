from xlsxwriter.workbook import Workbook
from collections import OrderedDict

filename = 'sample.xlsx'
def create(sorted_dict):
    workbook = Workbook(filename)
    worksheet = workbook.add_worksheet()
    for k,v in sorted_dict.items():
        worksheet.write(k,v)
    workbook.close()
    return filename