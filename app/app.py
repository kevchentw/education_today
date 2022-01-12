from flask import Flask
import models

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"