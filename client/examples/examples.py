import datetime
from tree import Tree,Node
import random
import os.path
import sys
from random import randrange
from datetime import timedelta


def read_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__),file_name)
    file = open(file_path,"r")
    file_lines = []
    for line in file:
        file_lines.append(line.replace("\n",""))
    return file_lines


def random_list_item(list):
    index = random.randrange(0,list.__len__())
    return list[index]


def example1_hello_world():
    sheet_data = {
        'A1':'Item',
        'B1':'Cost',
         #
        'A2':'Rent',
        'A3':'Gas',
        'A4':'Food',
        'A5':'Gym',
        'A6':'Total',
         #
        'B2':'10.10',
        'B3':'100.1',
        'B4':'300.5',
        'B5':'50.0',
        'B6':'=SUM(B1:B4)'
    }

    sheet = {
        'sheets':[
            {"Test Sheet" :  sheet_data}
        ]
    }
    return sheet


def example2_formats_simple():
    sheet_data = {
        'A1':{'value':'Item','format':'bold'},
        'B1':{'value':'Cost','format':'bold'},
         #
        '1,0':'Rent',
        '2,0':'Gas',
        '3,0':'Food',
        '4,0':'Gym',
        '5,0':'Total',
         #
        '1,1':{'value':'50.50','format':'number_bold_red'},
        '2,1':{'value':'15.88','format':'number_bold_red'},
        '3,1':{'value':'33.90','format':'number_bold_red'},
        '4,1':{'value':'80.55','format':'number_bold_red'},
        '5,1':{'value':'=SUM(B2:B5)','format':'number_bold_red'}
    }

    sheet = {
        'sheets':[
            {"Test Sheet" :  sheet_data},
        ],
        "formats" : {
            'bold' : {'bold':True},
            'bold_red' : {'bold': True, 'font_color': 'red'},
            #
            'number' : {'num_format':'$#,##.##'} ,
            'number_bold_red' : {'bold': True, 'font_color': 'red','num_format':'$#,##.##'},
            'number_bold_blue' : {'bold': True, 'font_color': 'red','bg_color': '#99CCFF','num_format':'$#,##.##'},

        }
    }
    return sheet


def example3_formats_more():
    sheet_data = {
        'A1':{'value':'Item','format':'bold'},
        'B1':{'value':'Cost','format':'bold'},
        'C1':{'value':'Date','format':'bold'},
         #
        '1,0':'Rent',
        '2,0':'Gas',
        '3,0':'Food',
        '4,0':'Gym',
        '5,0':'Total',
         #
        '1,1':{'value':'500.50','format':'number_bold_red'},
        '2,1':{'value':'150.88','format':'number_bold_red'},
        '3,1':{'value':'330.90','format':'number_bold_red'},
        '4,1':{'value':'80.55','format':'number_bold_red'},
        '5,1':{'value':'=SUM(B2:B5)','format':'sum_format'},
        #
        '1,2':{'date':'2013-01-01','format':'date_format'},
        '2,2':{'date':'2013-02-01','format':'date_format'},
        '3,2':{'date':'2013-03-01','format':'date_format2'},
        '4,2':{'date':'2013-04-01','format':'date_format2'},
        #
        "conditional_formats" : {
            'B2:B5': {
                    'type':'cell','criteria': '>=','value':    300, 'format':   'number_bold_blue'
            }
        },
        #
        "column_size":{
             'A:B': 15,
             'C:C':25
        }
    }

    sheet = {
        'sheets':[
            {"Test Sheet" :  sheet_data},
        ],
        "formats" : {
            'bold' : {'bold':True},
            'bold_red' : {'bold': True, 'font_color': 'red'},
            #
            'number' : {'num_format':'$#,##.##'} ,
            'number_bold_red' : {'bold': True, 'font_color': 'red','num_format':'$#,##.##'},
            'number_bold_blue' : {'bold': True, 'font_color': 'red','bg_color': '#99CCFF','num_format':'$#,##.##'},
            #
            'sum_format' : {'bold':True,'bg_color':'#E9AA94'},
            'date_format':{'num_format': 'yyyy d mmmm'},
            'date_format2':{'num_format': 'yy dd mmm'}
        }
    }
    return sheet


def example4_realistic():
    locations = read_file("locations")
    location_1 = random_list_item(locations)
    location_2 = random_list_item(locations)

    def random_dates():
        date_1 = datetime.date(2003, random.randrange(1,12), random.randrange(1,28))
        date_2 = datetime.date(2003, random.randrange(1,12), random.randrange(1,28))
        if date_1 if date_1 < date_2 else date_2:
            return date_1,date_2
        else:
            return date_2,date_1

    def random_companies():
        companies = []
        for i in range(1,7):
            companies.append(random.randrange(1,10))

    companies = random_dates()
    depart_date,arrive_date = random_dates()
    tree = Tree()

example4_realistic()



functions = {"1":example1_hello_world(),"2":example2_formats_simple(),"3":example3_formats_more()}