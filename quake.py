import json
import requests

def get_quake():
	quake = {}
	r = requests.get("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
	quake['event_id'] = r.json()['features'][0]['id']
	quake['depth'] = r.json()['features'][0]['geometry']['coordinates'][2]
	quake['title'] = r.json()['features'][0]['properties']['title']
	quake['quake_type'] = r.json()['features'][0]['properties']['type']
	quake['magnitude'] = r.json()['features'][0]['properties']['mag']
	quake['place'] = r.json()['features'][0]['properties']['place']
	quake['coordinates'] = r.json()['features'][0]['geometry']['coordinates']
	quake['latitute'] = r.json()['features'][0]['geometry']['coordinates'][0]
	quake['longitude'] = r.json()['features'][0]['geometry']['coordinates'][1]
	quake['time'] = r.json()['features'][0]['properties']['time']
	quake['url'] = r.json()['features'][0]['properties']['url']
	return quake

print get_quake()

# print "Event ID:", event_id
# print "Title:", title
# print "Quake Type:", quake_type
# print "Magnitude:", magnitude
# print "Quake Depth", depth
# print "Place:", place
# print "Latitude:", latitute
# print "Longitude:", longitude
# print "Time:", time
# print "URL:", url