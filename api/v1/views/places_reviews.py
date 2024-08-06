#!/usr/bin/python3
"""RESTful endpoint for review model"""

from models import storage
from models.review import Review
from flask import jsonify, request, redirect
from api.v1.views import app_views


@app_views.route("/places/<place_id>/reviews", methods=['GET'])
def reviews(place_id):
    """
    Returnns all reviews with the specified
    place_id
    """
    obj = storage.all(Review).values()
    reviews = [item.to_dict() for item in obj
               if item.to_dict['place_id'] == place_id]

    if len(review) < 1:
        return(abort(404))
    return (jsonify(reviews))


@app_views.route("/reviews/<review_id>", methods=['GET'])
def review(review_id):
    """
    Return the review with the specified id
    """
    review = storage.get(Review, review_id)
    if review is None:
        return (abort(404))
    return (jsonify(review.to_dict()))


@app_views.route("/reviews/<review_id>", methods=['DELETE'])
def delete_review(review_id):
    """
    deletes review with the review_id
    """
    review = storage.get(Place, review_id)
    if review is None:
        return (abort(404))
    for k, v in storage.all(Review).items():
        if v == review:
            storage.delete(review)
            storage.save()
    return({}, 200)


@app_views.route("/places/<place_id>/reviews", methods=['POST'])
def create_review(place_id):
    """
    Creates a new review
    """
    if request.is_json:
        new_review = request.get_json()
        place = storage.get(Place, place_id)
        if place is None:
            return (abort(404))
        if 'user_id' not in new_review.keys():
            return (jsonify({"error": "Missing user_id"}), 400)
        user = storage.get(User, new_place['user_id'])
        if user is None:
            return (abort(404))
        if 'text' not in new_place.keys():
            return (jsonify({"error": "Missing text"}), 400)

        new_review["place_id"] = place_id
        model = Review(**new_review)
        model.save()
        return (jsonify(model), 201)
    return (jsonify({"error": "Not a JSON"}), 400)


@app_views.route("/reviews/<review_id>", methods=['PUT'])
def update_review(review_id):
    """
    Updates the review
    """
    if request.is_json:
        update_review = request.get_json()
        review = storage.get(Review, review_id)
        if review is None:
            return (abort(404))

        setattr(review, "name", update_review['name'])
        review.save()
        return (jsonify(review.to_dict()), 200)
    return (jsonify({"error": "Not a JSON"}), 400)
