# A program for JSON data Parsing
#For that, Earthquakes data is taken from usgs.gov 
"""
Created by @Hrishikesh Salunkhe
"""
import urllib.request 
import json

def printResults(data):
    theJson= json.loads(data)
    if "title"  in theJson["metadata"]:
        print(theJson["metadata"]["title"])
    count=theJson ["metadata"]["count"]
    print(str(count)+"events recorded")
    for i in theJson["features"]:
        print(i["properties"]["place"])
    print("--------\n"  )   
    for i in theJson["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" %i["properties"]["mag"],i["properties"]["place"])  
    print("--------\n")      
    print("Theevent which are felt")
    for i in theJson["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" %i["properties"]["mag"],i["properties"]["place"])
            
webUrl= urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
print("Result code:", webUrl.getcode())
if (webUrl.getcode()==200):
    data=webUrl.read()
    printResults(data)
else:
    print("Error")