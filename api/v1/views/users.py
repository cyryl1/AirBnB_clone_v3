#!/usr/bin/python3
"""API routes for the User component
"""

from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request, abort


@app_views.route("/users",
                 methods=["GET"])
def get_users():
    """Returns all Users"""

    users = [i.to_dict() for i in storage.all(User).values()]
    return (jsonify(users))


@app_views.route("/users/<user_id>",
                 methods=["GET"])
def get_user(user_id):
    """Returns a user with the
    specified user_id"""

    user = storage.get(User, user_id)
    if user is None:
        return (abort(404))
    return (jsonify(user.to_dict()))


@app_views.route("/users/<user_id>",
                 methods=["DELETE"])
def delete_user(user_id):
    """Delete the User object with
    the specified user_id"""

    user = storage.get(User, user_id)
    if user is None:
        return (abort(404))
    for k, v in storage.all(User).items():
        if v == user:
            storage.delete(user)
            storage.save()
    return ({}, 200)


@app_views.route("/users",
                 methods=["POST"])
def create_user():
    """Creates a new User object from
    the request body"""

    if not request.is_json:
        return (jsonify({
            "error": "Not a JSON"
            }), 400)
    data = request.get_json()
    if "email" not in data.keys():
        return(jsonify({
            "error": "Missing email"
            }), 400)
    if "password" not in data.keys():
        return(jsonify({
            "error": "Missing password"
            }), 400)
    model = User(**data)
    model.save()
    return (jsonify(model.to_dict()), 201)


@app_views.route("/users/<user_id>",
                 methods=["PUT"])
def update_user(user_id):
    """Update the User object with the
    specified user_id"""

    user = storage.get(User, user_id)
    if user is None:
        return (abort(404))

    if not request.is_json:
        return (jsonify({
            "error": "Not a JSON"
            }))
    ignore = ["id", "email", "created_at", "updated_at"]
    for key, val in data:
        if key not in ignore:
            setattr(user, key, val)
    user.save()
    return (jsonify(user.to_dict()), 200)
