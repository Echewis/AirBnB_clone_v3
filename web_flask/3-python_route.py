#!/usr/bin/python3
"""This script will starts a Flask web application.
The application listens on 0.0.0.0, port 5000..
"""
from flask import Flask

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
    """Displays 'C' followed by the value of <text>.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@application.route("/python", strict_slashes=False)
@application.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """This will display 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    application.run(host="0.0.0.0")
