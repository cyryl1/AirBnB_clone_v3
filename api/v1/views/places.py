#!/usr/bin/python3
"""RESTful endpoint for place model"""

from models import storage
from models.place import Place
from flask import jsonify, request, abort
from api.v1.views import app_views


@app_views.route("/cities/<city_id>/places", methods=['GET'])
def places(city_id):
    """
    Returnns all places with the specified
    city_id"""
    obj = storage.all(cls="Place").values()
    places = [item.to_dict() for item in obj 
              if item.to_dict['city_id'] == city_id]
    
    if len(places) < 1:
        return(abort(404))
    return (jsonify(places))


@app_views.route("/places/<place_id>", methods=['GET'])
def place(place_id):
    """
    Return the place with the specified id
    """
    place = storage.get(Place, place_id)
    if place is None:
        return (abort(404))
    return (jsonify(place.to_dict()))


@app_views.route("/places/<place_id>", methods=['DELETE'])
def delete_place(place_id):
    """
    deletes place with the id place_id
    """
    place = storage.get(Place, place_id)
    if place is None:
        return (abort(404))
    for k, v in storage.all(Place).items():
        if v == place:
            storage.delete(place)
            storage.save()
    return({}, 200)


@app_views.route("/cities/<city_id>/places", methods=['POST'])
def create_place(city_id):
    """
    Creates a new place
    """
    if request.is_json:
        new_place = request.get_json()
        city = storage.get(City, city_id)
        if city is None:
            return (abort(404))
        if 'user_id' not in new_place.keys():
            return (jsonify({"error": "Missing user_id"}), 400)
        user = storage.get(User, new_place['user_id'])
        if user is None:
            return (abort(404))
        if 'name' not in new_place.keys():
            return (jsonify({"error": "Missing name"}), 400)
        
        new_place["city_id"] = city_id
        model = Place(**new_place)
        model.save()
        return (jsonify(model), 201)
    return (jsonify({"error": "Not a JSON"}), 400)


@app_views.route("/places/<place_id>", methods=['PUT'])
def update_place(place_id):
    """
    Updates the place
    """
    if request.is_json():
        update_place = request.get_json()
        place = storage.get(Place, place_id)
        if place is None:
            return (abort(404))

        setattr(place, "name", update_place['name'])
        place.save()
        return (jsonify(place.to_dict()), 200)
    return (jsonify({"error": "Not a JSON"}), 400)
