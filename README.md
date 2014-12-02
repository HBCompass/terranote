#TerraNote#
=========

TerraNote meets the need for real-time information during natural disasters and extreme weather events. When a disaster strikes there is a lag between when it happens and when news sources can update their audiences with information. TerraNote connects users to a human readable summary of information directly from monitoring agencies. The app generates a summary for each event, maps the event’s location and allows users to share the information with their preferred social network.

![homepage screenshot](https://raw.githubusercontent.com/HBCompass/terranote/master/screenshots/TerraNote_home.PNG)

##Technology Stack##

TerraNote is a flask app connected to a sqlite database and uses SQLAlchemy as the ORM. Pages are controlled by Jinja2 Templates with a Bootstrap framework. The current version uses the [geoJSON](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) api from the United States Geological Survery and the Google Maps Javascript API V3. 

