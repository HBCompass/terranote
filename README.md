#TerraNote#
=========

TerraNote meets the need for real-time information during natural disasters and extreme weather events. When a disaster strikes there is a lag between when it happens and when news sources can update their audiences with information. TerraNote connects users to a human readable summary of information directly from monitoring agencies. The app generates a summary for each event, maps the event’s location and allows users to share the information with their preferred social network.

![homepage screenshot](https://raw.githubusercontent.com/HBCompass/terranote/master/screenshots/TerraNote_home.PNG)

##Technology Stack##

TerraNote is a flask app connected to a sqlite database and uses SQLAlchemy as the ORM. Pages are controlled by Jinja2 templates with a Bootstrap framework. The current version uses the [geoJSON](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) api from the United States Geological Survery and the Google Maps Javascript API v3. 

###File Guide###

-model.py : Creates the database
-quake.py : Gets the feed from the USGS
-note.py : Controls the flask app

*There are additional files in the repo for features in progress, but this list covers the ones you need to recreate the project as depicted in the screenshots.*

###Installation###

- Clone the repo
- Set up a virtual environment
- Pip install -r requirements.txt
- At the command line: 

```xml
python -i model.py
```
Then:

```xml
engine = create_engine("sqlite:///terranote.db", echo=True)
```
Then: 

```xml
Base.metadata.create_all(engine)
```
- In a new shell use ls command in project folder and verify *terranote.db* exists
- To see the structure of the database go to the command line:
```xml
sqlite3 terranote.db
sqlite> .tables
sqlite> .schema
```
- To add quakes to the database, quit SQLlite and run quake.py
```xml
python quake.py
```
-Run the app by starting the flask server:
```xml
python note.py
```