#!/usr/bin/python3
"""This script will start a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask
from flask import abort

application = Flask(__name__)


@application.route("/", strict_slashes=False)
def hello_hbnb():
    """This will display 'Hello HBNB!'."""
    return "Hello HBNB!"


@application.route("/hbnb", strict_slashes=False)
def hbnb():
    """This will display 'HBNB'."""
    return "HBNB"


@application.route("/c/<text>", strict_slashes=False)
def c(text):
    """This displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@application.route("/python", strict_slashes=False)
@application.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """This will displays 'Python' followed by the value of <text>.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@application.route("/number/<int:num>", strict_slashes=False)
def number(num):
    """This will display 'num is a number' only if num is an integer."""
    return "{} is a number".format(num)


if __name__ == "__main__":
    application.run(host="0.0.0.0")
