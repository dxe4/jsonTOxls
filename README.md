=========
jsonTOxls
=========

Create Excel files using json requests. Send json to create xls,xlsx files using XlsxWriter (https://github.com/jmcnamara/XlsxWriter).
You can optionally run a tornado server to accept the requests.

___
It works as basic functionality (add values, sheets, formats, conditional formatting, merging)
___
Requires
------------

    python3 (may work with 2 as well)
    and the libraries mentioned above
___
To run
------------

    server (optional) : python3 jsonTOxls_server.py
    python3 jsonTOxls.py (will run example 4)

    if you want to run different examples run :
        python3 jsonTOxls.py 1
        python3 jsonTOxls.py 2
        python3 jsonTOxls.py 3
        python3 jsonTOxls.py 4

Json and XLS examples in
------------

    client/examples

Documentation
------------

    I am planning for documentation in http://www.readthedocs.org but for now
    you can see the examples in examples/exmaple_functions.py and exmaple1-4.xls‎

    For input documentation used to create files you can check xlsxwritter documentation at:
    https://xlsxwriter.readthedocs.org/en/latest/

    Note: See exmaples/example4.xls and examples/example4.json for a realistic example,
    It contains lot of data, conditional formatting, fonts, colors, mergin etc

