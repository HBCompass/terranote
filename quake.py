import json
import requests
from datetime import datetime
import time

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
	quake['time'] = datetime.fromtimestamp(r.json()['features'][0]['properties']['time']/1000)
	quake['url'] = r.json()['features'][0]['properties']['url']
	quake['type'] = r.json()['features'][0]['properties']['type']
	quake['status'] = r.json()['features'][0]['properties']['status']
	quake['tsunami'] = r.json()['features'][0]['properties']['tsunami']
	# get the datetime for when the summary is written
	quake['recordtime'] = datetime.now()
	return quake

#print get_quake()
# Original pull in format for testing:

# r = requests.get("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
# event_id = r.json()['features'][0]['id']
# depth = r.json()['features'][0]['geometry']['coordinates'][2]
# title = r.json()['features'][0]['properties']['title']
# quake_type = r.json()['features'][0]['properties']['type']
# magnitude = r.json()['features'][0]['properties']['mag']
# place = r.json()['features'][0]['properties']['place']
# coordinates = r.json()['features'][0]['geometry']['coordinates']
# latitute = r.json()['features'][0]['geometry']['coordinates'][0]
# longitude = r.json()['features'][0]['geometry']['coordinates'][1]
# time = r.json()['features'][0]['properties']['time']
# url = r.json()['features'][0]['properties']['url']
# recordtime = datetime.now()

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
# print "RecordTime:", recordtime
