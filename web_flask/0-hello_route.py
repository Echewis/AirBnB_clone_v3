#!/usr/bin/python3
""" This script will Start a Flask web application.
and the  application will listen on 0.0.0.0, port 5000.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """The mwessage display will be 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
