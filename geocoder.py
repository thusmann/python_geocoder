import requests
import csv
#from time import sleep

inputfile = open("placelist.txt")
outputfile = csv.writer(open("geocoded-placelist.txt", "w"))

for row in inputfile:
        row = row.rstrip()
        url_mapquest = "http://open.mapquestapi.com/nominatim/v1/search.php"
        url_osm = "http://nominatim.openstreetmap.org/search"
        payload = {"q":row, "format":"json", "polygon":"1", "addressdetails":"0", "countrycodes":"ch", "limit":"1"}
        try:
                r = requests.get(url_mapquest, params=payload)
                #print r.url
                #print r.text
                json = r.json()
                lat = json[0]["lat"]
                lng = json[0]["lon"]
        except:
                lat = "n/a"
                lng = "n/a"
        
        newrow = [row, lat, lng]
        outputfile.writerow(newrow)
        
        print lat,lng
        #sleep(1)
