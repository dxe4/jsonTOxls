=========
jsonTOxls
=========

Create Excel files using json requests. Send json to create xls,xlsx files using XlsxWriter (https://github.com/jmcnamara/XlsxWriter).
You can optionally run a tornado server to accept the requests.

It works as basic functionality (add values, sheets, formats, conditional formatting, merging)
___
#Requires

    python3 (may work with 2 as well)
    and the libraries mentioned above

#To run

    server (optional) : python3 jsonTOxls_server.py
    python3 jsonTOxls.py (will run example 4)

    if you want to run different examples run :
        python3 jsonTOxls.py 1
        python3 jsonTOxls.py 2
        python3 jsonTOxls.py 3
        python3 jsonTOxls.py 4

#Documentation

For input documentation used to create files you can check xlsxwritter documentation at:https://xlsxwriter.readthedocs.org/en/latest/ 


Example 1:
---
Just a "Hello World example".

     -The json contains a list of sheets.
     -Each sheet is a dictionary sheet name to data
___
```python
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
```
Example 1 Output:
---
![alt text](https://raw.github.com/papaloizouc/jsonTOxls/master/examples/images/example1.png "Example 1")
___
Example 2:
---
Formats 
      
    -Json structure: {'sheets' : list of sheets, 'formats': dict of formats}
    -You can use either A1 or 0,0 it gives the same result
    -You can also use either '0,0':'Foo' or '0,0':{'value':'Foo','format':'the_format'}
    -For more about formats check the xlsxWritter doc
___
```python
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
```
Example 2 Output:
---
![alt text](https://raw.github.com/papaloizouc/jsonTOxls/master/examples/images/example2.png "Example 2")
___

Example 3:
---
     -Resize is inside the sheet data because different sheets may have different column sizes, same for conditional formatting.
___
```python
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
```
Example 3 Output:
---
![alt text](https://raw.github.com/papaloizouc/jsonTOxls/master/examples/images/example3.png "Example 3")
___


Example 4:
--- 
This example is very big but the generated json and xls file is in the project examples folder.

Merge
---
To merge use this:
     
     A1-D1:'merged region'

Progress
---
You can check PROGRESS.txt for implemented functionality, coming functionality and known issues.

Motivation: Why do we need this anyway?
---
1) Unified approach, It's not specific to your programming language (if you run tornado).

2) Abstraction: Chunking Up from excel specific code as shown in 3 to json dicts lists

3) Personally i dislike report code, hence this pseudo code example*:
```python
     rowIndex, colIndex = 1,0
     row = sheet.createRow(rowIndex)
     cell = row.createCell(colIndex)
     cell.setValue(values[(rowIndex,colIndex)])
     cell.setStyle(styles[(rowIndex,colIndex)])
```
Changes to:
```python
     row,col = 1,0
     sheet[str(row) + "," + str(col)] = {
               "value":values[(row,col)],
               "format":formats[(row,col)]
     }
```
And with some imagination:
```python
     row,col = 1,0
     key = lambda row,col: str(row) + "," + str(col)
     val = lambda row,col:(
              {
                 "value":values[(row,col)],
                  "format":formats[(row,col)]
              }
     )
     sheet[key(row,col)] = val(row,col)
```
*Note i didn't run this code, I just wrote it in the readme file to demonstrate an example.

4) And you end up applying divide and conquer technique for the problem which is now split in 4 steps: 
     
     - Fetch data
     - Process data (decide which cells hold which values - create values and formats dictionaries)
      -Create json as shown above
      -Send json to create xls without writing code

I will try to demonstrate this in the up-coming Exmaple 5 because theory is easier than practice (sometimes).
     
Feedback
---
If you disagree with anything or want to request a feature feel free: ANY feedback is much appreciated as well as criticism. 
