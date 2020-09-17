from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/super_simple')
def super_simple():
    return "<h1>This is Super Simple boo</h1>"
