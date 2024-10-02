from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/juan")
def hello_juan():
    return "<p>Hello, juan!</p>"