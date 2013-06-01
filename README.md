jsonTOxls
=========

create xls files using json requests

The goal is to create a tornado (http://www.tornadoweb.org/en/stable/) server which takes json requests and creates .xls/.xlsx files (https://github.com/jmcnamara/XlsxWriter)

It works as basic functionality (add values, sheets and formats)
Requires:
    python3 (may work with 2 as well)
    and the libraries mentioned above

To run:
    python3 server/server.py
    python3 client/client.py

Json examples in client/examples.py