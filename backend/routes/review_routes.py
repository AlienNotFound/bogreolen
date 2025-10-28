from flask import Blueprint, jsonify, request
from backend.models import Reviewstb
from backend.services.review_service import ReviewService
from backend.DTOs.review_dto import ReviewDTO

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['GET'])
def get_all_reviews():
    reviews = ReviewService.get_all_reviews()

    if reviews:
        return jsonify([ReviewDTO.to_dict(r) for r in reviews]), 200
    else:
        return jsonify({"Error": "Reviews not found!"}), 400
    
@review_bp.route('/review/<id>', methods=['GET'])
def get_review_by_id(id):
    review = ReviewService.get_review_by_id(id)

    if review:
        return jsonify(ReviewDTO.to_dict(review)), 200
    else:
        return jsonify({"Error": "Review not found!"}), 400

@review_bp.route('/reviews/book/<id>', methods=['GET'])
def get_reviews_based_on_user_list(id):
    reviews = ReviewService.get_reviews_based_on_user_list(id)

    if reviews:
        return jsonify([review for review in reviews]), 200
    else:
        return jsonify({"Error": "Reviews not found!"}), 400
    
@review_bp.route('/review', methods=['POST'])
def create_review():
    data = request.get_json()

    bookid = data.get('bookid')
    userid = data.get('userid')
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
    else:
        return jsonify({"Error": "An error occured"}), 500
    
@review_bp.route('/review/<id>', methods=['PUT'])
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
def delete_review(id):
    if ReviewService.get_review_by_id(id) == None:
        return jsonify({"Error": "Review does not exist."}), 404
    
    review = ReviewService.delete_review(id)

    if review == None:
        return jsonify({"Success": "Review succesfully deleted!"}), 200
    else:
        return jsonify({"Error": "Could not delete review."}), 500