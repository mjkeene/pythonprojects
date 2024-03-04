from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def index():
	return "<h3>This line should display on the webpage!</h3>"


app.run(host="0.0.0.0", port=80)
