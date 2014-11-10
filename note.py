from flask import Flask, request, render_template, redirect
from quake import get_quake

app = Flask(__name__)

@app.route("/")
def note():
	# call get_quake
	quake = get_quake()
	# pass dictionary k,v to jinja template
	return render_template("quake.html", quake=quake)


@app.route("/fire")
def fire_note():
	return render_template("fire.html")


if (__name__)=="__main__":
	app.run(debug = True)