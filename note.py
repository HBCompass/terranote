from flask import Flask, request, render_template, redirect
from flask import session as user_session
from model import Quake, session as db_session
from quake import get_quake
import json


app = Flask(__name__)

@app.route("/")
def home_map():
	# get user location from session data
	# user_location = request.args.get("userpoint")
	# pass user location to home.html as userlat, userlng
	recent_quakes = db_session.query(Quake).order_by(Quake.quake_datetime.desc()).limit(10)
	return render_template("home.html", recent_quakes=recent_quakes)


@app.route("/location", methods=['POST'])
def user_location():
	user_latlong = request.form.get(data)
	pass



@app.route("/quakes")
def quake_notes():
	# data = Quake.query.order_by(Quake.quake_datetime.desc()).limit(25)
	# mapdata = json.dumps(json_list = data.all())
	quakes = Quake.query.order_by(Quake.quake_datetime.desc()).all()
	return render_template("quakes.html", quakes=quakes)


@app.route("/quakes/<quake_id>")
def quake_note(quake_id):
	# quake = db_session.query(Quake).first()
	# quake = db_session.query(Quake).filter_by(Quake.quake_id == quake_id)
	quake = Quake.query.get(quake_id)
	return render_template("quake.html", quake=quake)

@app.route("/note_example")
def note():
	# get most recent quake record
	quake = db_session.query(Quake).order_by(Quake.quake_datetime.desc()).first()
	# pass dictionary k,v to jinja template
	return render_template("quake.html", quake=quake)

app.secret_key = "testing"

if __name__=="__main__":
	app.run(debug = True)