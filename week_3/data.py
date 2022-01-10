import json
import csv
import urllib.request


link = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
request = urllib.request.urlopen(link)
data = json.load(request)

All_location = []

for i in range(0,58):    
    location = data["result"]["results"][i]["stitle"]
    address = data["result"]["results"][i]["address"][5:8]
    longitude = data["result"]["results"][i]["longitude"]
    latitude = data["result"]["results"][i]["latitude"]
    img_url = data["result"]["results"][0]["file"]
    img = img_url.split('jpg')[0]+"jpg"
    detail_data = {"location" : location,
                 "address" : address,
                 "longitude" : longitude,
                 'latitude' : latitude ,
                 "img" : img
                 }  
    All_location.append(detail_data)



fields = ['location', 'address', 'longitude', 'latitude',"img"] 
# name of csv file 
filename = "student.csv"
    
# writing to csv file 
with open(filename, 'w',encoding="utf-8") as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields)       
    # writing headers (field names) 
    writer.writeheader()        
    # writing data rows 
    writer.writerows(All_location) 