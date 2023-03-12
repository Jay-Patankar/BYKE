
import requests
srcres=requests.get("https://api.tomtom.com/search/2/geocode/"+"Suvidha angan society ,tulajabhavaninagar , narhe , pune-41 , India ."+".json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
srcgeo=srcres.json()["results"][0]["position"]
print(srcgeo)