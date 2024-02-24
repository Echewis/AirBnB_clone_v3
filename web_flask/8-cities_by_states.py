#!/usr/bin/python3
"""This script will Start a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """This will display an HTML page with a list of all states and related cities.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@application.teardown_appcontext
def teardown(exc):
    """This will remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    application.run(host="0.0.0.0")
