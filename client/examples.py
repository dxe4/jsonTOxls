import datetime

def hello_world():
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
        'B2':'1000.10',
        'B3':'100.11',
        'B4':'300.50',
        'B5':'50.0',
        'B6':'=SUM(B1:B4)'
    }

    sheet = {
        'sheets':[
            {"Test Sheet" :  sheet_data}
        ]
    }
    return sheet

def formats():
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
