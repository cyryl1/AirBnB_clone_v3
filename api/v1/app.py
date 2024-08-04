#!/usr/bin/python3
"""
A Flask applicaton
"""

from flask import Flask, jsonify
import storage
import models
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def storage_close():
    """
    calls the storage.calls method
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
