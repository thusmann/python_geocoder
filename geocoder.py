from datetime import datetime, timedelta
import csv
import requests
import requests_cache

requests_cache.install_cache(cache_name = "orte")

# Import and export CSV
ifile = open("twitterAccounts.csv", "rb")
ofile = open("geocodedTwitterAccounts.csv", "wb")
reader = csv.reader(ifile, delimiter = ";")
writer = csv.writer(ofile, delimiter = ";")

url_mapquest = "http://open.mapquestapi.com/nominatim/v1/search.php"
url_osm = "http://nominatim.openstreetmap.org/search"

rownum = 0
for row in reader:
    # Save header row.
    newrow = []
    lat = ""
    lng = ""
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            if header[colnum] == "location":
                print "%-s: %s" % (header[colnum], col)
                try:
                    payload = {"q":col, "format":"json", "polygon":"1", "addressdetails":"1", "countrycodes":"ch", "limit":"1"}
                    r = requests.get(url_mapquest, params=payload)
                    json = r.json()
                    lat = json[0]["lat"]
                    lng = json[0]["lon"]
                    state = json[0]["address"]["state"]
                    city = json[0]["address"]["city"]
                    country = json[0]["address"]["country_code"]
                except:
                    lat = "na"
                    lng = "na"
                    state = "na"
                    city = "na"
                    country = "na"                    
                newrow.append(lat)
                newrow.append(lng)
                newrow.append(state.encode('utf-8'))
                newrow.append(city.encode('utf-8'))
                newrow.append(country)
            newrow.append(col)
            colnum += 1
    writer.writerow(newrow)
    rownum += 1

ifile.close()
ofile.close()
