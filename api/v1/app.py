#!/usr/bin/python3
"""
A Flask applicaton
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception=None):
    """
    calls the storage.close method
    """
    storage.close()


@app.errorhandler(404)
def _handle_api_error(error):
    """
    Returns a JSON-formatted 404 status code response
    """
    error = {
            "error": "Not found"
            }
    return (jsonify(error), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, threaded=True)
