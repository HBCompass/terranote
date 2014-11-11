from flask import Flask, request, render_template, redirect
from quake import get_quake

app = Flask(__name__)

@app.route("/")
def note():
	# get most recent quake record
	
	# pass dictionary k,v to jinja template
	return render_template("quake.html", quake=quake)


if (__name__)=="__main__":
	app.run(debug = True)