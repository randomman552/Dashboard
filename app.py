import os
from werkzeug.exceptions import NotFound
from flask import Flask, render_template, send_from_directory

from util import get_config


# Set static_folder to None so we can register our own handler
app = Flask(__name__, static_folder=None)
app.config["DASHBOARD_DATA_PATH"] = os.path.join(os.getcwd(), "data")


@app.route("/static/<path:filename>")
def static(filename):
    """
    Custom static file handler.
    We use this to first query the data directory, 
    then fall back to the static directory if it is not found
    """
    try:
        data_path = app.config.get("DASHBOARD_DATA_PATH")
        return send_from_directory(data_path, filename)
    except NotFound:
        return send_from_directory("static", filename)


@app.route("/")
def dashboard():
    """Dashboard rendering function"""
    config = get_config()
    return render_template("dashboard.html", config=config)
