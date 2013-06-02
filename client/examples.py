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
        'B5':'50.0',#'format':{'num_format': '$#,##.##'}
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
        '0,0':{'value':'Item','format':'bold'},
        'B1':{'value':'Cost','format':'bold'},
         #
        'A2':'Rent',
        'A3':'Gas',
        'A4':'Food',
        'A5':'Gym',
        'A6':'Total',
         #
        'B2':'100',
        'B3':{'value':'200','format':'number_bold_red'},
        'B4':{'value':'300','format':'number_bold_red'},
        'B5':{'value':'600','format':'number_bold_red'}  ,#'format':{'num_format': '$#,##.##'}
        'B6':'=SUM(B2:B5)',

        "conditional_formats" : {
            'B2:B5': {
                    'type':'cell','criteria': '>=','value':    300, 'format':   'number_bold_blue'
            }
        }
    }

    sheet = {
        'sheets':[
            {"Test Sheet" :  sheet_data},
        ],
        "formats" : {
            'number' : {'num_format':'$#,##.##'} ,
            'bold' : {'bold':True},
            'bold_red' : {'bold': True, 'font_color': 'red'},
            'number_bold_red' : {'bold': True, 'font_color': 'red','num_format':'$#,##.##'},
            'number_bold_blue' : {'bold': True, 'font_color': 'blue','num_format':'$#,##.##'}
        }
    }
    return sheet