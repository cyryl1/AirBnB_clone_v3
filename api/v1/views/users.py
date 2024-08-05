#!/usr/bin/python3
"""API routes for the User component
"""

from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request


@app_views_route("/api/v1/users",
                 methods=["GET"])
def get_users():
    """Returns all Users"""

    users = [i.to_dict() for i in storage.all(User).values()]
    return (jsonify(users))


@app_views.route("/api/v1/users/<user_id>",
                 methods=["GET"])
def get_user(user_id):
    """Returns a user with the
    specified user_id"""

    user = storage.get(User, user_id)
    if user is None:
        return (redirect("/api/v1/nop"))
    return (jsonify(user.to_dict()))


@app_views.route("/api/v1/users/<user_id>",
                 methods=["DELETE"])
def delete_user(user_id):
    """Delete the User objevt with
    the specified user_id"""

    user = storage.get(User, user_id)
    if user is None:
        return (redirect("/api/v1/nop"))
    storage.delete(user)
    return ({}, 200)


@app_views.route("/api/v1/users",
                 methods=["POST"])
def create_user():
    """Creates a new User object from
    the request body"""

    data = request.get_json()
    if not data.is_json():
        return (jsonify({
            "error": "Not a JSON"
            }), 400)
    if "email" not in data.keys():
        return(jsonify({
            "error": "Missing email"
            }), 400)
    if "password" not in data.keys():
        return(jsonify({
            "error": "Missing password"
            }), 400)
    model = User(data)
    model.save()
    return (jsonify(model.to_dict()), 200)


@app_views.route("/api/v1/users/<user_id>",
                 methods=["PUT"])
def update_user(user_id):
    """Update the User object with the
    specified user_id"""

    user = storage.get(User, user_id)
    if user is None:
        return (redirect("/api/v1/nop"))
    data = request.get_json()
    if not data.is_json():
        return (jsonify({
            "error": "Not a JSON"
            }))
    ignore = ["id", "email", "created_at", "updated_at"]
    for key, val in data:
        if key not in ignore:
            setattr(user, key, val)
    user.save()
    return (jsonify(user.to_dict()))
