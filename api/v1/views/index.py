#!/usr/bin/python3
"""
A flask app
"""

from flask import jsonify
import api.v1.views as view
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User


app_views = view.app_views

@app_views.route("/status")
def return_status():
    """
    returns status of api
    """
    return jsonify({
        "status": "OK"
        })


@app_views.route("/stats")
def stats():
    """
    Returns the number of each objects
    by type
    """

    return (jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
        }))
