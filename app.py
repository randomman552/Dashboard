import json
import os
from flask import Flask, render_template


app = Flask(__name__)
app.config["DASHBOARD_DATA_PATH"] = os.path.join(os.getcwd(), "data")


def get_config() -> dict:
    """Function to get config or return default config"""
    data_path = app.config.get("DASHBOARD_DATA_PATH")
    config_path = os.path.join(data_path, "config.json")
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("")
        return dict()


@app.route("/")
def dashboard():
    """Dashboard rendering function"""
    config = get_config()
    print(f"Rendering dashboard with config: {config}")
    return render_template("dashboard.html", config=config)
