#!/usr/bin/python3
"""RESTFUL API view for Amenity component
"""

from models import storage
from models.amenity import Amenity
from flask import jsonify, request, abort
from api.v1.views import app_views


@app_views.route("/amenities",
                 methods=["GET"])
def get_amenities():
    """Return all Amenities Objects"""

    amenities = [i.to_dict() for i in storage.all(Amenity).values()]
    return (jsonify(amenities))


@app_views.route("/amenities/<amenity_id>",
                methods=["GET"])
def get_amenity(amenity_id):
    """Return the amenity with the
    specified amenity_id"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return (abort(404))
    return (jsonify(amenity.to_dict()))


@app_views.route("/amenities/<amenity_id>",
                methods=["DELETE"])
def delete_amenity(amenity_id):
    """Delete the Amenity with the
    specified amenity_id"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return (abort(404))
    for k, v in storage.all(Amenity).items():
        if v == amenity:
            storage.delete(amenity)
            storage.save()
    return ({}, 200)


@app_views.route("/amenities",
                 methods=["POST"])
def create_amenity():
    """Creates a new amenity with the
    details in the request body"""

    if not request.is_json:
        return (jsonify({
            "error": "Not a JSON"
            }), 400)

    data = request.get_json()
    if "name" not in data.key():
        return (jsonify({
            "error": "Missing name"
            }), 400)
    model = Amenity(**data)
    model.save()
    return (jsonify(model.to_dict()), 201)


@app_views.route("/amenities/<amenity_id>",
                 methods=["PUT"])
def update_amenity(amenity_id):
    """Update an Amenity with the specfied
    amenity_id and request body"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return (abort(404))
    if not request.is_json:
        return (jsonify({
            "error": "Nota a JSON"
            }), 400)

    data = request.get_json()
    setattr(amenity, "name", data["name"])
    amenity.save()
    return (jsonify(amenity.to_dict), 200)
