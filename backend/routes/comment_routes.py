from flask import Blueprint, jsonify, request
from backend.services.comment_service import CommentService
from flask_jwt_extended import jwt_required, get_jwt_identity

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/comment', methods=['POST'])
@jwt_required()
def create_comment():
    data = request.get_json()
    
    user_id = get_jwt_identity()

    review_id = data.get('review_id')
    comment_text = data.get('comment_text')

    result, message = CommentService.create_comment(
        user_id=user_id,
        review_id=review_id,
        comment_text=comment_text
    )

    if result:
        return jsonify({'Success': 'Comment created!'}), 200
    else:
        return jsonify({'Error': f'{message}'}), 500

@comment_bp.route('/comment/<id>', methods=['PUT'])
@jwt_required()
def edit_comment(id):
    data = request.get_json()

    comment_text = data.get('comment_text')

    result, message = CommentService.edit_comment(
        id=id,
        comment_text=comment_text
    )

    if result:
        return jsonify({"Success": "Comment editted."}), 200
    elif message == 'Comment does not exist.':
        return jsonify({"Error": f'{message}'}), 404
    else:
        return jsonify({"Error": 'An error occured'}), 500

@comment_bp.route('/comment/<id>', methods=['DELETE'])
@jwt_required()
def delete_comment(id):
    result, message = CommentService.delete_comment(id=id)

    if result:
        return jsonify({"Success": f'{message}'})
    elif message == 'Comment does not exist.':
        return jsonify({"Error": f'{message}'})
    else:
        return jsonify({"Error": 'An error occured'})
