import json
import requests
from datetime import datetime
import time
import model

def get_quake():
	
	r = requests.get("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson")
	
	for feature in r.json()['features']:
		# print "************************"
		# print feature['geometry']['coordinates'][1]
		
		new_quake = model.Quake(
			quake_id = feature['id'], 
			quake_title = feature['properties']['title'],
			quake_type = feature['properties']['type'],
			magnitude = feature['properties']['mag'],
			place = feature['properties']['place'],
			latitude = feature['geometry']['coordinates'][0],
			longitude = feature['geometry']['coordinates'][1],
			# convert km to miles by * by 0.62 ??
			# depth = round((feature['geometry']['coordinates'][2]) * 0.62)
			depth = feature['geometry']['coordinates'][2],
			quake_datetime = datetime.fromtimestamp(feature['properties']['time']/1000),
			url = feature['properties']['url'],
			seismictype = feature['properties']['type'],
			status = feature['properties']['status'],
			felt = feature['properties']['felt'],
			tsunami = feature['properties']['tsunami'],
			recordtime = datetime.now())

		# print "**************************"
		# print new_quake

		model.session.merge(new_quake)
		model.session.commit()

if __name__ == '__main__':
	get_quake()

# Dictionary Version
	# quake = {}
	# r = requests.get("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson")
	# quake['event_id'] = r.json()['features'][0]['id']
	# quake['depth'] = r.json()['features'][0]['geometry']['coordinates'][2]
	# quake['title'] = r.json()['features'][0]['properties']['title']
	# quake['quake_type'] = r.json()['features'][0]['properties']['type']
	# quake['magnitude'] = r.json()['features'][0]['properties']['mag']
	# quake['place'] = r.json()['features'][0]['properties']['place']
	# quake['coordinates'] = r.json()['features'][0]['geometry']['coordinates']
	# quake['latitude'] = r.json()['features'][0]['geometry']['coordinates'][0]
	# quake['longitude'] = r.json()['features'][0]['geometry']['coordinates'][1]
	# quake['time'] = datetime.fromtimestamp(r.json()['features'][0]['properties']['time']/1000)
	# quake['url'] = r.json()['features'][0]['properties']['url']
	# quake['seismictype'] = r.json()['features'][0]['properties']['type']
	# quake['status'] = r.json()['features'][0]['properties']['status']
	# quake['felt'] = r.json()['features'][0]['properties']['felt']
	# quake['tsunami'] = r.json()['features'][0]['properties']['tsunami']
	# quake['recordtime'] = datetime.now()
	# return quake

# print get_quake()
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
