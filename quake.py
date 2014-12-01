import json
import requests
from datetime import datetime
import time
import model

def get_quake():


	# Gets earthquake feed from USGS	
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