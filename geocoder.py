import requests
import csv

inputfile = open("placelist.txt")
outputfile = csv.writer(open("geocoded-placelist.txt", "w"))

for row in inputfile:
        row = row.rstrip()
        url = "http://nominatim.openstreetmap.org/search"
        payload = {"q":row, "format":"json", "polygon":"1", "addressdetails":"1",  "email":"thusmann@gmail.com"}
        try:
                r = requests.get(url, params=payload)
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

