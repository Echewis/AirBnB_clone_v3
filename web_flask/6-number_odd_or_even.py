#!/usr/bin/python3
"""This script will start a Flask web application.
The application will listen on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template

application = Flask(__name__)
application.jinja_env.trim_blocks = True
application.jinja_env.lstrip_blocks = True


@application.route("/", strict_slashes=False)
def hello_hbnb():
    """This function will display 'Hello HBNB!'"""
    return "Hello HBNB!"


@application.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function will display 'HBNB'"""
    return "HBNB"


@application.route("/c/<text>", strict_slashes=False)
def c(text):
    """This function will display 'C' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@application.route("/python", strict_slashes=False)
@application.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """This function will display 'Python' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@application.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """This function will display 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@application.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """This function will display an HTML page only if <n> is an integer.
    This function will display the value of <n> in the body.
    """
    return render_template("5-number.html", n=n)


@application.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """This function will display an HTML page only if <n> is an integer.
    States whether <n> is odd or even in the body.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    application.run(host="0.0.0.0")
