from flask import Blueprint, jsonify, request
from backend.services.image_service import ImageService
from flask_jwt_extended import jwt_required

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/image', methods=['POST'])
@jwt_required()
def upload_image():
    file = request.files['file']
    if not file:
        return jsonify({"Error": "File path is empty"}), 400

    status, result = ImageService.upload_a_blob(file)

    if status == 'Success':
        return jsonify({"Success": "Image succesfully uploaded!", "URL": result}), 200
    elif result == "Invalid filetype":
        return jsonify({"Error": "Invalid filetype"}), 403
    else:
        return jsonify({"Error": "An error occured"}), 500

@image_bp.route('/image', methods=['DELETE'])
@jwt_required()
def delete_image():
    file = request.get_json()
    image = file.get('path')

    if not image:
        return jsonify({"Error": "File path is empty"}), 400

    status, _ = ImageService.delete_blob(image)

    if status == 'Success':
        return jsonify({"Success": f"Image succesfully deleted!"}), 200
    else:
        return jsonify({"Error": "An error occured"}), 500