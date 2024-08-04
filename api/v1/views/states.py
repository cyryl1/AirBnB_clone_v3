#!/usr/bin/python3
"""
Create a new view for State objects 
that handles all default RESTFul API actions
"""

from flask import jsonify
from api.v1.views import app_views
from model import storage

@app_views.route('/states')
def all_objects():
    """
    retrieves the list of all state objects.
    """
    obj = storage.all(cls='State')
    obj_list = [item for item in obj]
    return (obj_list)

@app_views.route('/states/<state_id>')
def state_objects(state_id):
    """
    retrieves State object
    """
    if (state_id):
        obj = storage.all(cls='State')
        obj_list = [item for item in obj if state_id == item.id]
        return (obj_list[0])
    else:
        return (jsonify({
            "error": "Not Found"
            }))

@app_views.route('/states/<state_id>', method=['DELETE'])
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

@app_views.route('/states', method=['POST'])
def create_state():
    """
    Creates a new state
    """
    if request.is_json:
        data = request.get_json
        state_id = data['id']
        if 'name' in data.keys():
            storage.new(data)
            state_obj = state_objects(state_id)
            return (jsonify(state_obj), 201)
        else:
            return (jsonify({"error": "Missing name"}), 400)
    else:
        return (jsonify({
            "error": "Not a JSON"
            }), 400)


@app_views.route('states/<state_id>', method=['PUT'])
def update_states(state_id):
    """
    Updates the states obj
    """
    if request.is_json:
        data = request.get_json
        for obj in storage.__objects:
            if state_id == obj.id:
                obj['name'] = data['name']
                state_obj = state_objects(state_id)
                return (jsonify(state_obj), 200)
            else:
                return (jsonify({"error": "Not Found"}))
    else:
        return (jsonify({"error": "Not a json"}), 404)
