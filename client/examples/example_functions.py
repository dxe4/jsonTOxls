import os.path, sys

sys.path.append(os.path.dirname(__file__))
import datetime
from multiprocessing.dummy import active_children
import random
import os.path
import sys
from random import randrange
from datetime import timedelta, time
from report_iterator import ReportIterator
from example_data import Example4


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


def example4_realistic():
    locations = read_file("locations")
    example4 = Example4(locations)
    data = example4.create_data()

    sheets, sheet, json_data = [], {}, {}
    row, col = 0, 0

    for k, v in data.items():

        departure, arrival, dates, companies = v["Departure"], v["Arrival"], v["dates"], v["companies"]
        to_string = lambda row, col: str(row) + "," + str(col)
        header_lambda = lambda row, col, to_string: (
            #returns ['0,0', '0,1', '1,0', '1,1'],['24,0', '24,1', '25,0', '25,1'] etc
            [to_string(r, c) for r, c in
             [(row, col), (row, col + 1), (row + 1, col), (row + 1, col + 1), (row + 2, col + 1)]]
        )
        header_data = header_lambda(row, col, to_string)
        sheet[header_data[0]] = "Arrival"
        sheet[header_data[1]] = arrival
        sheet[header_data[2]] = "Departure"
        sheet[header_data[3]] = departure

        row, col = (int(x) for x in header_data[4].split(","))

        column_iterator = ReportIterator(end=len(companies))
        row_iterator = ReportIterator(end=len(dates), child_iterator=column_iterator)

        for k, v in companies.items():
            sheet[str(row) + "," + str(col)] = k
            col += 1

        col = 0
        row += 1
        for k, v in dates.items():
            sheet[to_string(row, col)] = k
            row += 1
            for date in v:
                sheet[to_string(row, col)] = date.strftime('%m/%d/%Y')
                row += 1
        row += 1

    print(sheet)

    # for row in report_iterator:
    #     for col in report_iterator.child_iterator:
    #         print("row " + str(row),"col " + str(col))
    sheets.append({"sheet": sheet})
    json_data["sheets"] = sheets
    return json_data


example4_realistic()

functions = {"1": example1_hello_world(),
             "2": example2_formats_simple(),
             "3": example3_formats_more(),
             "4": example4_realistic()
}