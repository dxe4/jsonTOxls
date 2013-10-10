from xlsxwriter.workbook import Workbook
from collections import OrderedDict
import common
import datetime


class XlsFactory:

    @staticmethod
    def create(input):
        filename = common.pop_dict(input, "filename")
        workbook = Workbook(filename)
        formats = InputFactory.init_formats(input, workbook)
        for sheet in input['sheets']:
            XlsFactory.process_sheet(workbook, sheet, formats)
        workbook.close()
        return filename

    @staticmethod
    def process_sheet(workbook, sheet, formats):
        for sheet_name, sheet_data in sheet.items():
            sorted_dict = OrderedDict(
                sorted(sheet_data.items(), key=lambda t: t[0])
            )
            worksheet = workbook.add_worksheet(sheet_name)
            XlsFactory.add_cells(worksheet, sorted_dict, formats)

    @staticmethod
    def add_cells(sheet, sorted_dict, formats):
        conditional_formats = common.pop_dict(sorted_dict, "conditional_formats")
        column_sizes = common.pop_dict(sorted_dict, "column_size")

        for cell_pos, cell_value in sorted_dict.items():
            new_value = InputFactory.get_args(cell_value, formats)
            new_key = InputFactory.parse_cell_position(cell_pos)
            args = new_key + new_value
            if isinstance(args[0], str) and ":" in args[0]:
                sheet.merge_range(*args)
            else:
                sheet.write(*args)

        XlsFactory.add_conditional_formats(conditional_formats, formats, sheet)
        XlsFactory.resize_columns(column_sizes, sheet)


    @staticmethod
    def add_conditional_formats(conditional_formats, formats, worksheet):
        for cells, criteria in conditional_formats.items():
            criteria["format"] = formats.get(criteria.get("format"))
            worksheet.conditional_format(cells, criteria)

    @staticmethod
    def resize_columns(column_sizes, worksheet):
        for k, v in column_sizes.items():
            worksheet.set_column(k, v)


class InputFactory:
    @staticmethod
    def init_formats(input, workbook):
        return_dict = {}
        for k, v in common.pop_dict(input, "formats").items():
            return_dict[k] = workbook.add_format(v)
        return return_dict

    @staticmethod
    def get_args(value, formats):
        def is_dict():
            key = "value" if "value" in value else "date"
            if "date" == key:
                nums = [int(n) for n in value[key].split("-")]
                date = datetime.date(nums[0], nums[1], nums[2])
                return date, formats[value['format']]
            else:
                return value['value'], formats[value['format']]

        def is_str():
            return (value,)

        functions = {dict: is_dict, str: is_str}
        return functions[value.__class__]()

    @staticmethod
    def parse_cell_position(k):
        if "," in k:
            return tuple(int(n) for n in k.split(","))
        else:
            return (k,)