#!/usr/bin/python3
"""This script will start a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route("/states", strict_slashes=False)
def states():
    """This will display an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@application.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """This will display an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@application.teardown_appcontext
def teardown(exc):
    """This will remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    application.run(host="0.0.0.0")
