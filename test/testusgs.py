import json
import requests

import requests
r = requests.get("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson")

event_id = r.json()['features'][0]['id']
depth = r.json()['features'][0]['geometry']['coordinates'][2]

title = r.json()['features'][0]['properties']['title']
quake_type = r.json()['features'][0]['properties']['type']
magnitude = r.json()['features'][0]['properties']['mag']
place = r.json()['features'][0]['properties']['place']
coordinates = r.json()['features'][0]['geometry']['coordinates']
latitute = r.json()['features'][0]['geometry']['coordinates'][0]
longitude = r.json()['features'][0]['geometry']['coordinates'][1]
time = r.json()['features'][0]['properties']['time']
url = r.json()['features'][0]['properties']['url']

print "Event ID:", event_id
print "Title:", title
print "Quake Type:", quake_type
print "Magnitude:", magnitude
print "Quake Depth", depth
print "Place:", place
print "Latitude:", latitute
print "Longitude:", longitude
print "Time:", time
print "URL:", url