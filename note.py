from flask import Flask, request, render_template, redirect
import quake

app = Flask(__name__)

@app.route("/")
def note():
	get_quake():
	return render_template("home.html", title=title)


if (__name__)=="__main__":
	app.run()