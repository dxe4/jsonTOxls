def example1():
    sheet_data = {
        'A1': 'Item',#{'value':'Item'},
        'B1':'Cost',
         #
        'A2':'Rent',
        'A3':'Gas',
        'A4':'Food',
        'A5':'Gym',
        'A6':'Total',
         #
        'B2':'1000',
        'B3':'100',
        'B4':'300',
        'B5':'50',
        'B6':'=SUM(B1:B4)'
    }

    sheet = [{"Test Sheet" :  sheet_data}]
    return sheet