#!/usr/bin/python3
"""
A Flask applicaton
"""

from flask import Flask, jsonify
from models import storage
import api.v1.views as view

app = Flask(__name__)
app.register_blueprint(view.app_views)


@app.teardown_appcontext
def close_storage():
    """
    calls the storage.close method
    """
    storage.close()


@app.errorhandler(404)
def _handle_api_error():
    """
    Returns a JSON-formatted 404 status code response
    """
    error = {
            "error": "Not found"
            }
    return jsonify(error)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
