from flask import Flask, request, render_template, redirect
from flask import session as user_session
from model import Quake, session as db_session
from quake import get_quake
import json
from flask import jsonify
import os


app = Flask(__name__)

#-------------------------------
# Home page
#-------------------------------

@app.route("/")
def home_map():
	topten = db_session.query(Quake).order_by(Quake.quake_datetime.desc()).limit(10)
	cols = Quake.__table__.columns
	json_compiled = {} 
	for quake in topten:
		json_compiled[quake.quake_id] = {}
		json_compiled[quake.quake_id]['lat'] = quake.latitude
		json_compiled[quake.quake_id]['lng'] = quake.longitude
		json_compiled[quake.quake_id]['title'] = quake.quake_title
		json_compiled[quake.quake_id]['id'] = quake.quake_id
	print json_compiled
	recent_quakes = db_session.query(Quake).order_by(Quake.quake_datetime.desc()).limit(10)
	return render_template("home.html", recent_quakes=recent_quakes, top_ten=json_compiled)

#-------------------------------
# Earthquake routes
#-------------------------------

@app.route("/quakes")
def quake_notes():
	data = Quake.query.order_by(Quake.quake_datetime.desc()).limit(25)
	cols = Quake.__table__.columns
	#print cols
	json_compiled = {} 
	for quake in data:
		json_compiled[quake.quake_id] = {}
		json_compiled[quake.quake_id]['lat'] = quake.latitude
		json_compiled[quake.quake_id]['lng'] = quake.longitude
		json_compiled[quake.quake_id]['title'] = quake.quake_title
		json_compiled[quake.quake_id]['id'] = quake.quake_id
	#print json_compiled
	quakes = Quake.query.order_by(Quake.quake_datetime.desc()).all()
	return render_template("quakes.html", quakes=quakes, quake_points=json_compiled)


@app.route("/quakes/<quake_id>")
def quake_note(quake_id):
	quake = Quake.query.get(quake_id)
	return render_template("quake.html", quake=quake)

#-------------------------------
# Aurora route
#-------------------------------

@app.route("/aurora")
def aurora():
	return render_template("aurora.html")

#-------------------------------
# Fire route
#-------------------------------

@app.route("/fires")
def fires():
	return render_template("fire.html")

@app.route("/fires/<fire_id>")
def fire():
	return render_template("fire.html")
	pass

#-------------------------------
# Volcano route
#-------------------------------

@app.route("/volcanoes")
def volcanoes():
	return render_template("volcano.html")

@app.route("/volcanoes/<volcano_id>")
def volcano():
	return render_template("volcano.html")
	pass

#-------------------------------
# Flood route
#-------------------------------

@app.route("/floods")
def floods():
	return render_template("flood.html")

@app.route("/floods/<flood_id>")
def flood():
	return render_template("flood.html")
	pass

#-------------------------------
# Winterstorm route
#-------------------------------

@app.route("/winterstorms")
def winter():
	return render_template("winterstorm.html")

@app.route("/winterstorms/<winterstorm_id>")
def winter():
	return render_template("winterstorm.html")
	pass	

#-------------------------------
# Testing and in-progress pages
#-------------------------------

@app.route("/location")
def user_location():
	user_latlong = request.args.get("latlon")
	# print user_latlong
	return "hi"

@app.route("/note_example")
def note():
	# get most recent quake record
	quake = db_session.query(Quake).order_by(Quake.quake_datetime.desc()).first()
	# pass dictionary k,v to jinja template
	return render_template("quake.html", quake=quake)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404



app.secret_key = "testing"

if __name__=="__main__":
	app.run(debug=True,
			host="0.0.0.0", 
		    port=int(os.environ.get('PORT', 5000)))