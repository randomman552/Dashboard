from io import FileIO
import json
import os
from flask import current_app as app


def get_file(path: str, mode: str="r") -> FileIO:
    """
    Utility function to retrieve a file from application storage.
    First checks "DASHBOARD_DATA_PATH", if the file is not found
    then the function will fall back to static.
    If the file isn't present in either, will raise FileNotFoundError.
    """
    try:
        data_path = app.config.get("DASHBOARD_DATA_PATH")
        return open(os.path.join(data_path, path), mode)
    except FileNotFoundError:
        return open(os.path.join("static", path))


def get_config() -> dict:
    """
    Utility method to get config file and convert it to a dict.
    """
    try:
        with get_file("config.json") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config.json is not present.")
        return dict()