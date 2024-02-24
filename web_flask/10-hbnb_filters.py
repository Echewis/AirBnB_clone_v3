#!/usr/bin/python3
"""This script will start a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """This will display the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@application.teardown_appcontext
def teardown(exc):
    """This will remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    application.run(host="0.0.0.0")
