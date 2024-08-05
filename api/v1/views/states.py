#!/usr/bin/python3
"""
Create a new view for State objects
that handles all default RESTFul API actions
"""

from flask import jsonify, redirect, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states')
def all_objects():
    """
    retrieves the list of all state objects.
    """
    obj = storage.all(cls='State')
    obj_list = [item.to_dict() for item in obj]
    return (obj_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def state_objects(state_id):
    """
    retrieves State object
    """
    if (state_id):
        obj = storage.all(cls='State')
        obj_list = [item for i7tem in obj if state_id == item.id]
        return (obj_list[0])
    else:
        return (redirect("/api/v1/nop"))


@app_views.route('/states/<state_id>', methods=['DELETE'])
def handle_delete(state_id):
    """
    deletes an object
    """
    if (state_id):
        obj = state_objects(state_id)
        storage.delete(obj)
        result = {}
#        result.status_code = 200
        return (result)
    else:
        return (jsonify({"error": "Not Found"}), 200)


@app_views.route('/states', methods=['POST'])
def create_state():
    """
    Creates a new state
    """
    if data.is_json:
        data = request.get_json()
        state_id = data['id']
        if 'name' in data.keys():
            model = State(data)
            model.save()

#            storage.new(data)
#            state_obj = state_objects(state_id)
            return (jsonify(model.to_dict()), 201)
        else:
            return (jsonify({"error": "Missing name"}), 400)
    return (jsonify({
            "error": "Not a JSON"
            }), 400)


@app_views.route('states/<state_id>', methods=['PUT'])
def update_states(state_id):
    """
    Updates the states obj
    """
    if data.is_json:
        data = request.get_json()
        state = storage.get(State, state_id).to_dict()
        if state is None:
            return (redirect("/api/v1/nop"))
        state['name'] = data['name']
        return (jsonify(state), 200)
    else:
        return (jsonify({"error": "Not a JSON"}), 400)
