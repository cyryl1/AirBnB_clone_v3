#!/usr/bin/python3
"""
A flask app
"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status")
def return_status():
    """
    returns status of api
    """
    return jsonify({
        "status": "OK"
        })
