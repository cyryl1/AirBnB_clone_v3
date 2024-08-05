#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.city import City
import json

#print("All objects: {}".format(storage.count()))
#print("State objects: {}".format(storage.count(State)))

#first_state_id = list(storage.all(State).values())[0].id
#print("First state: {}".format(storage.get(State, first_state_id)))

print(f"\nALL CITY Objects\n {[i.to_dict() for i in storage.all(City).values()]}")
