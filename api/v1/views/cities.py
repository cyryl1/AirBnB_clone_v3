#!/usr/bin/python3
""" RESTFUL API view for cities model """

from models import storage
from models.city import City
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route("/api/v1/states/<state_id>/cities",
                 methods=["GET"])
def all_cities(state_id):
    """Returns all Cities with
    the specified state_id"""

    cities = [i.to_dict for i in storage.all(City).values()
              if i.to_dict["state_id"] == state_id]
    if len(cities) < 1:
        return (redirect("/api/v1/nop"))
    return (jsonify(cities))


@app_views.route("/api/v1/cities/<city_id>",
                 methods=["GET"])
def get_city(city_id):
    """Return a City object with the specified id"""

    city = storage.get(City, city_id)
    if city is None:
        return (redirect("/api/v1/nop"))
    return (jsonify(city.to_dict()))


@app_views.route("/api/v1/cities/<city_id>",
                 methods=["DELETE"])
def delete_city(city_id):
    """ Deletes the city object
    with the specified ID"""

    city = storage.get(City, city_id)
    if city is None:
        return (redirect("/api/v1/nop"))
    storage.delete(city)
    return ({}, 200)


@app_views.route("/api/v1/states/<state_id>/cities",
                 methods=["POST"])
def create_city(state_id):
    """Creates a new City object based on
    the specified state_id"""

    if storage.get('State', state_id) is None:
        return (redirect("/api/v1/nop"))
    data = request.get_json()
    if not data.is_json():
        return (jsonify({
            "error": "Not a JSON"
            }), 400)
    if "name" not in data.keys():
        return (jsonify({
            "error": "Missing name"
            }), 400)
    model = City(data)
    model.save()
    return (jsonify(model.to_dict()))


@app_views.route("/api/v1/cities/<city_id>",
                 methods=["PUT"])
def update_city(city_id):
    """Update the City object with the
    specified ID"""

    city = storage.get(City, city_id)
    if city is None:
        return (redirect("/api/v1/nop"))
    data = request.get_json()
    if not data.is_json():
        return (jsonify({
            "error": "Not a JSON"
            }), 400)
    setattr(city, data["name"])
    city.save()
    return (jsonify(city.to_dict()))
