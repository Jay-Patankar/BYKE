import requests
import json
import pprint
'''
query={
  "origins": [
    {
      "point": { "latitude": 45.458545, "longitude": 9.15049 }
    },
    {
      "point": { "latitude": 45.403337, "longitude": 11.050541 }
    }
  ],
  "destinations": [
    {
      "point": { "latitude": 48.149853, "longitude": 11.499931 }
    },
    {
      "point": { "latitude": 50.033688, "longitude": 14.538226 }
    }
  ]
  
  }


"options": {
    "departAt": "1996-12-19T16:39:57",
    "traffic": "historical",
    "travelMode": "truck",
    "vehicleMaxSpeed": 90,
    "vehicleWeight": 12000,
    "vehicleAxleWeight": 4000,
    "vehicleLength": 13.6,
    "vehicleWidth": 2.42,
    "vehicleHeight": 2.4,
    "vehicleCommercial": True,
    "vehicleLoadType": ["otherHazmatExplosive", "otherHazmatGeneral"],
    "vehicleAdrTunnelRestrictionCode": "C",
    "avoid": ["unpavedRoads"]
p={"baseURL":"api.tomtom.com","versionNumber":2,"key":"lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv"}
h={"Content-Type":"application/json"}
response = requests.post('https://api.tomtom.com/routing/matrix/2?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv',json=query,headers=h)
print(type(response))
print(response.status_code)
print(response.reason)
ans=response.json()
print(ans["data"][0][ "routeSummary"]["lengthInMeters"])
print(ans["data"][1][ "routeSummary"]["lengthInMeters"])
print(ans["data"][2][ "routeSummary"]["lengthInMeters"])
print(ans["data"][3][ "routeSummary"]["lengthInMeters"])


response = requests.get("https://api.open-notify.org/astros.json")
print(response.status_code)
'''
res=requests.get("https://api.tomtom.com/search/2/geocode/Suvidha Aangan  Narhe  pune India.json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
src=res.json()["results"][0]["position"]
res=requests.get("https://api.tomtom.com/search/2/geocode/Shaniwarwada Shaniwar peth  pune India.json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
dest=res.json()["results"][0]["position"]
query={
  "origins": [
    {
      "point": { "latitude": src["lat"], "longitude": src["lon"] }
    }
  ],
  "destinations": [
    {
      "point": { "latitude": dest["lat"], "longitude": dest["lon"] }
    }
  ]
  
  }
h={"Content-Type":"application/json"}
response = requests.post('https://api.tomtom.com/routing/matrix/2?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv',json=query,headers=h)
print(response.json()["data"][0][ "routeSummary"]["lengthInMeters"]/1000)