#!/usr/bin/python3
"""RESTFUL API view for Amenity component
"""

from models import storage
from models.amenity import Amenity
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route("/api/v1/ameniities",
                 methods=["GET"])
def get_amenities():
    """Return all Amenities Objects"""

    amenities = [i.to_dict() for i in storage.all(Amenity).values()]
    return (jsonify(amenities))


@app_view.route("/api/v1/amenities/<amenity_id>",
                methods=["GET"])
def get_amenity(amenity_id):
    """Return the amenity with the
    specified amenity_id"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return (redirect("/api/v1/nop"))
    return (jsonify(amenity.to_dict()))


@app_view.route("/api/v1/amenities/<amenity_id>",
                methods=["DELETE"])
def delete_amenity(amenity_id):
    """Delete the Amenity with the
    specified amenity_id"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return (redirect("/api/v1/nop"))
    storage.delete(amenity)
    return ({}, 200)


@app_views.route("/api/v1/amenities",
                 methods=["POST"])
def create_amenity():
    """Creates a new amenity with the
    details in the request body"""

    data = request.get_json()
    if not data.is_json():
        return (jsonify({
            "error": "Not a JSON"
            }), 400)
    if "name" not in data.key():
        return (jsonify({
            "error": "Missing name"
            }), 400)
    model = Amenity(data)
    model.save()
    return (jsonify(model.to_dict()))


@app_views.route("/api/v1/amenities/<amenity_id>",
                 methods=["PUT"])
def update_amenity(amenity_id):
    """Update an Amenity with the specfied
    amenity_id and request body"""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return (redirect("/api/v1/nop"))
    data = request.get_json()
    if not data.is_json():
        return (jsonify({
            "error": "Nota a JSON"
            }), 400)
    setattr(amenity, data["name"])
    amenity.save()
    return (jsonify(amenity.to_dict), 200)
