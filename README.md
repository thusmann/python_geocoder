python_geocoder
===============

A Python based geocoder that uses Open Street Maps Nominatim on the Mapquest API.

It takes a CSV (actually semicolon separated list) as input and outputs the same list with lat/long added. Needs UTF-8 input, otherwise the Nominatim API has some problems mit Umlauts (ä, ö, ü, ...). 

## ToDo
* add header row
* solve encoding problems (ANSI, etc.)