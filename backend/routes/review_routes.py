from flask import Blueprint, jsonify, request
from backend.models import Reviewstb
from backend.services.review_service import ReviewService
from backend.DTOs.review_dto import ReviewDTO
from flask_jwt_extended import jwt_required, get_jwt_identity

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['GET'])
@jwt_required()
def get_all_reviews():
    reviews = ReviewService.get_all_reviews()

    if reviews:
        return jsonify([ReviewDTO.to_dict(r) for r in reviews]), 200
    else:
        return jsonify({"Error": "Reviews not found!"}), 400
    
@review_bp.route('/review/<id>', methods=['GET'])
@jwt_required()
def get_review_by_id(id):
    review = ReviewService.get_review_by_id(id)

    if review:
        return jsonify(ReviewDTO.to_dict(review)), 200
    else:
        return jsonify({"Error": f"Review not found!"}), 400

@review_bp.route('/reviews/user', methods=['GET'])
@jwt_required()
def get_reviews_based_on_user_list():
    user_id = get_jwt_identity()
    reviews = ReviewService.get_reviews_based_on_user_list(user_id)

    if reviews:
        return jsonify([review for review in reviews]), 200
    else:
        return jsonify({"Error": "Reviews not found!"}), 400
    
@review_bp.route('/review', methods=['POST'])
@jwt_required()
def create_review():
    data = request.get_json()

    bookid = data.get('bookid')
    userid = get_jwt_identity()
    rating = data.get('rating')
    reviewtext = data.get('reviewtext')

    result = ReviewService.create_review(
        bookid=bookid,
        userid=userid,
        rating=rating,
        reviewtext=reviewtext
    )

    if isinstance(result, Reviewstb):
        return jsonify({"Success": "Review created!"}), 200
    if result == 'You\'ve already reviewed this book':
        return jsonify({"Error": f"{result}"}), 409
    else:
        return jsonify({"Error": f"{result}An error occured"}), 500
    
@review_bp.route('/review/<id>', methods=['PUT'])
@jwt_required()
def edit_review(id):
    if ReviewService.get_review_by_id(id) == None:
        return jsonify({"Error": "Review does not exist."}), 404
    
    data = request.get_json()

    rating = data.get('rating')
    reviewtext = data.get('reviewtext')

    result = ReviewService.edit_review(
        id=id,
        rating=rating,
        reviewtext=reviewtext
    )

    if isinstance(result, Reviewstb):
        return jsonify({"Success": f"Review updated!"}), 200
    else:
        return jsonify({"Error": "An error occured"}), 500

@review_bp.route('/review/<id>', methods=['DELETE'])
@jwt_required()
def delete_review(id):
    if ReviewService.get_review_by_id(id) == None:
        return jsonify({"Error": "Review does not exist."}), 404
    
    review = ReviewService.delete_review(id)

    if review == None:
        return jsonify({"Success": "Review succesfully deleted!"}), 200
    else:
        return jsonify({"Error": "Could not delete review."}), 500