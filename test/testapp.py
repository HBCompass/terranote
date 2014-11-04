from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def note():
	return render_template(".html")





if (__name__)=="__main__":
	app.run