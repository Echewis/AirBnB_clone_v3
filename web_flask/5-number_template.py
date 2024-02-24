#!/usr/bin/python3
"""This script will start a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import render_template

application = Flask(__name__)


@application.route("/", strict_slashes=False)
def hello_hbnb():
    """This will display 'Hello HBNB!'"""
    return "Hello HBNB!"


@application.route("/hbnb", strict_slashes=False)
def hbnb():
    """This will display 'HBNB'"""
    return "HBNB"


@application.route("/c/<text>", strict_slashes=False)
def c(text):
    """This will display 'C'and followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@application.route("/python", strict_slashes=False)
@application.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """This will display 'Python' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@application.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """This will display 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@application.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """This will display an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    application.run(host="0.0.0.0")
