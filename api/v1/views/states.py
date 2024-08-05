#!/usr/bin/python3
"""
Create a new view for State objects 
that handles all default RESTFul API actions
"""

from flask import jsonify
from api.v1.views import app_views

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
        return jsonify({
            "error": "Not Found"
            })

@app_views.route('/states/<state_id>', method=['DELETE'])
def handle_delete(state_id):
    """
    deletes an object
    """
    if (state_id):
        obj = state_objects(state_id)
        storage.delete(obj)
        result = {}
        result.status_code = 200
        return (result)
    else:
        return jsonify({"error": "Not Found"})

@app_views.route('/states', method=['POST'])
def create_state():
    request_data = request.get_json


