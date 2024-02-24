#!/usr/bin/python3
"""This script start a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route("/hbnb", strict_slashes=False)
def hbnb():
    """This will display the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@application.teardown_appcontext
def teardown(exc):
    """This will remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    application.run(host="0.0.0.0")
