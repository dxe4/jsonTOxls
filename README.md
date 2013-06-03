jsonTOxls
=========

Create Excel files using json requests. A tornado server (http://www.tornadoweb.org/en/stable/) that accepts json requests to create xls,xlsx files using XlsxWriter (https://github.com/jmcnamara/XlsxWriter).
Both client and server build in python but the client can be written in any language.

___
It works as basic functionality (add values, sheets and formats)
___
Requires

    python3 (may work with 2 as well)
    and the libraries mentioned above
___
To run

    python3 server/server.py
    python3 client/client.py

Json and XLS examples in

    client/examples

