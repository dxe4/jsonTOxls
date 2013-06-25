import os.path, sys
import pprint
sys.path.append(os.path.dirname(__file__))
import datetime
from multiprocessing.dummy import active_children
import random
import os.path
import sys
# from random import randrange
# from datetime import timedelta, time
# from report_iterator import ReportIterator
from example_data import Example4Data
from server.input_factory import InputHandler
from common import data_structures
from common import excel as excel_common
from collections import OrderedDict



def read_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    file = open(file_path, "r")
    file_lines = []
    for line in file:
        file_lines.append(line.replace("\n", ""))
    return file_lines


def example1_hello_world():
    sheet_data = {
        'A1': 'Item',
        'B1': 'Cost',
        #
        'A2': 'Rent',
        'A3': 'Gas',
        'A4': 'Food',
        'A5': 'Gym',
        'A6': 'Total',
        #
        'B2': '10.10',
        'B3': '100.1',
        'B4': '300.5',
        'B5': '50.0',
        'B6': '=SUM(B1:B4)'
    }

    sheet = {
        'sheets': [
            {"Test Sheet": sheet_data}
        ]
    }
    return sheet


def example2_formats_simple():
    sheet_data = {
        'A1': {'value': 'Item', 'format': 'bold'},
        'B1': {'value': 'Cost', 'format': 'bold'},
        #
        '1,0': 'Rent',
        '2,0': 'Gas',
        '3,0': 'Food',
        '4,0': 'Gym',
        '5,0': 'Total',
        #
        '1,1': {'value': '50.50', 'format': 'number_bold_red'},
        '2,1': {'value': '15.88', 'format': 'number_bold_red'},
        '3,1': {'value': '33.90', 'format': 'number_bold_red'},
        '4,1': {'value': '80.55', 'format': 'number_bold_red'},
        '5,1': {'value': '=SUM(B2:B5)', 'format': 'number_bold_red'}
    }

    sheet = {
        'sheets': [
            {"Test Sheet": sheet_data},
        ],
        "formats": {
            'bold': {'bold': True},
            'bold_red': {'bold': True, 'font_color': 'red'},
            #
            'number': {'num_format': '$#,##.##'},
            'number_bold_red': {'bold': True, 'font_color': 'red', 'num_format': '$#,##.##'},
            'number_bold_blue': {'bold': True, 'font_color': 'red', 'bg_color': '#99CCFF', 'num_format': '$#,##.##'},

        }
    }
    return sheet


def example3_formats_more():
    sheet_data = {
        'A1': {'value': 'Item', 'format': 'bold'},
        'B1': {'value': 'Cost', 'format': 'bold'},
        'C1': {'value': 'Date', 'format': 'bold'},
        #
        '1,0': 'Rent',
        '2,0': 'Gas',
        '3,0': 'Food',
        '4,0': 'Gym',
        '5,0': 'Total',
        #
        '1,1': {'value': '500.50', 'format': 'number_bold_red'},
        '2,1': {'value': '150.88', 'format': 'number_bold_red'},
        '3,1': {'value': '330.90', 'format': 'number_bold_red'},
        '4,1': {'value': '80.55', 'format': 'number_bold_red'},
        '5,1': {'value': '=SUM(B2:B5)', 'format': 'sum_format'},
        #
        '1,2': {'date': '2013-01-01', 'format': 'date_format'},
        '2,2': {'date': '2013-02-01', 'format': 'date_format'},
        '3,2': {'date': '2013-03-01', 'format': 'date_format2'},
        '4,2': {'date': '2013-04-01', 'format': 'date_format2'},
        #


        "conditional_formats": {
            'B2:B5': {
                'type': 'cell', 'criteria': '>=', 'value': 300, 'format': 'number_bold_blue'
            }
        },
        #
        "column_size": {
            'A:B': 15,
            'C:C': 25
        }
    }

    sheet = {
        'sheets': [
            {"Test Sheet": sheet_data},
        ],
        "formats": {
            'bold': {'bold': True},
            'bold_red': {'bold': True, 'font_color': 'red'},
            #
            'number': {'num_format': '$#,##.##'},
            'number_bold_red': {'bold': True, 'font_color': 'red', 'num_format': '$#,##.##'},
            'number_bold_blue': {'bold': True, 'font_color': 'red', 'bg_color': '#99CCFF', 'num_format': '$#,##.##'},
            #
            'sum_format': {'bold': True, 'bg_color': '#E9AA94'},
            'date_format': {'num_format': 'yyyy d mmmm'},
            'date_format2': {'num_format': 'yy dd mmm'}
        }
    }
    return sheet


class Example4:
    def __init__(self):
        self.locations = read_file("locations")
        self.example4Data = Example4Data(self.locations)
        self.data = self.example4Data.create_data()
        self.sheets = []
        self.json_data = OrderedDict()
        self.init_lambda()
        self.init_xls_writer_values()

    def init_xls_writer_values(self):
        self.formats = {
            'date_format': {'num_format': 'mmm d yyyy', 'font_size': 11},
            'number': {'num_format': '$#,##.##'},
            'header_description': {'bold': True, 'font_color': '#333300', 'bg_color': '#E0E0E0', 'font_size': 14},
            'header_arrival': {'bold': True, 'font_color': '#CC3300', 'bg_color': '#E0E0E0', 'font_size': 14},
            'header_departure': {'bold': True, 'font_color': '#CC0000', 'bg_color': '#E0E0E0', 'font_size': 14},
            'date_description': {'bg_color': '#CCFFFF', 'font_size': 12},
            'company': {'bg_color': '#CCFFFF', 'font_size': 12},
            'cond_format': { 'bg_color': '#FFFFCC', 'num_format': '$#,##.##'}
            #CCFFFF
        }
        self.column_size = {
            'A:H': 12
        }
        self.conditional_formats = {}

    def init_lambda(self):
        self.to_string = lambda row, col: str(row) + "," + str(col)
        self.header_lambda = lambda row, col, to_string: (
            #returns ['0,0', '0,1', '1,0', '1,1'],['24,0', '24,1', '25,0', '25,1'] etc
            [to_string(r, c) for r, c in
             [(row, col), (row, col + 1), (row + 1, col), (row + 1, col + 1), (row + 2, col + 1)]]
        )

    def add_headers(self, sheet, row, col, arrival, departure):

        """
            Add headers e.g.
                Arrival	'Teesside Airport'
                Departure	'Sandefjord Airport'
        :return: current row
        """
        header_data = self.header_lambda(row, col, self.to_string)

        def merge(cell_str):
            nums = [int(n) for n in cell_str.split(",")]
            col = nums[1]
            row = nums[0]
            columns = excel_common.number_to_cells([col, col + 3])
            return columns[0] + str(row + 1) + ":" + columns[1] + str(row + 1)

        sheet[header_data[0]] = {"value": "Arrival", "format": "header_description"}
        sheet[merge(header_data[1])] = {"value": arrival, "format": "header_arrival"}
        sheet[header_data[2]] = {"value": 'Departure', "format": "header_description"}
        sheet[merge(header_data[3])] = {"value": departure, "format": "header_departure"}
        row = int(header_data[4].split(",")[0]) #(int(x) for x in header_data[4].split(","))
        return row

    def add_companies(self, sheet, companies, row):
        """
            Add companies e.g. company 4	company 8	company 2
        """
        for count, company_name in enumerate(companies.keys()):
            sheet[self.to_string(row, count + 1)] = {"value": company_name, "format": "company"}
        return row + 1

    def add_prices(self, sheet, companies, row, date_to_match, description):
        col = 1
        min = -1
        for company, dates in companies.items():
            for date_in_company in dates[description]:
                price_for_date = data_structures.get_dict(date_in_company, date_to_match)
                if not price_for_date:
                    continue
                min = int(float(price_for_date)) if int(float(price_for_date)) < min or min == -1 else min
                sheet[self.to_string(row, col)] = {"value": price_for_date, "format": "number"}
            col += 1
        self.add_conditional_format(row, row, 1, col, min)

    def add_data(self, sheet, dates, companies, row):
        for description_count, description in enumerate(dates.keys()):
            description_row = description_count + row
            sheet[self.to_string(description_row, 0)] = {"value": description, "format": "date_description"}
            date_values = dates[description]
            for date_count, date in enumerate(date_values):
                self.add_dates(sheet, companies, description_row, description, date_count, date)
        return row + len(dates.keys()) + 1

    def add_dates(self, sheet, companies, description_row, description, date_count, date):
        date_row = description_row + date_count + 1
        sheet[self.to_string(date_row, 0)] = {'date': date.strftime('%Y-%m-%d'), 'format': 'date_format'}
        self.add_prices(sheet, companies, date_row, date, description)

    def add_conditional_format(self, start_row, end_row, start_col, end_col, min):
        cols = excel_common.number_to_cells([start_col, end_col - 1])
        self.conditional_formats[cols[0] + str(start_row + 1) + ":" + cols[1] + str(end_row + 1)] = {
            'type': 'cell', 'criteria': 'between', 'minimum': 1, 'maximum': min + 10, 'format': 'cond_format'
        }

    def post_create(self,sheet):
        sheet["column_size"] = self.column_size
        sheet["conditional_formats"] = self.conditional_formats
        self.sheets.append({"sheet": sheet})
        self.json_data["sheets"] = self.sheets
        self.json_data["formats"] = self.formats
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.json_data)

    def create(self):
        row, col = 0, 0
        sheet = OrderedDict()

        for k, v in self.data.items():
            departure, arrival, dates, companies = v["Departure"], v["Arrival"], v["dates"], v["companies"]
            row = self.add_headers(sheet, row, col, arrival, departure)
            row = self.add_companies(sheet, companies, row)
            row = self.add_data(sheet, dates, companies, row)

        self.post_create(sheet)
        return self.json_data


def example4_realistic():
    return Example4().create()


functions = {"1": example1_hello_world(),
             "2": example2_formats_simple(),
             "3": example3_formats_more(),
             "4": example4_realistic()
}