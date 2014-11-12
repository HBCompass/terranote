from flask import Flask, request, render_template, redirect
from flask import session as user_session
from model import Quake, session as db_session
from quake import get_quake

app = Flask(__name__)

@app.route("/")
def note():
	# get most recent quake record
	quake = db_session.query(Quake).first()
	# pass dictionary k,v to jinja template
	return render_template("quake.html", quake=quake)


if __name__=="__main__":
	app.run(debug = True)