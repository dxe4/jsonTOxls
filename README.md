=========
jsonTOxls
=========

Create Excel files using json requests. A tornado server (http://www.tornadoweb.org/en/stable/) that accepts json requests to create xls,xlsx files using XlsxWriter (https://github.com/jmcnamara/XlsxWriter).
Both client and server build in python but the client can be written in any language.

___
It works as basic functionality (add values, sheets, formats, conditional formatting)
___
Requires
------------

    python3 (may work with 2 as well)
    and the libraries mentioned above
___
To run
------------

    python3 server/server.py
    python3 client/client.py  (change the example variable to run different example)

Json and XLS examples in
------------

    client/examples

Documentation
------------

    I am planning for documentation in http://www.readthedocs.org but for now
    you can see the examples in client/examples/exmaple_functions.py and exmaple1-4.xls‎

    For input documentation used to create files you can check xlsxwritter documentation at:
    https://xlsxwriter.readthedocs.org/en/latest/

