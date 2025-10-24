from flask import Blueprint, jsonify, request
from backend.models import Trackstb
from backend.services.track_service import TrackService
from backend.DTOs.track_dto import TrackDTO

track_bp = Blueprint('track_bp', __name__)

@track_bp.route('/track', methods=['POST'])
def track_book():
    data = request.get_json()

    user_id = 1
    book_id = 1

    read_today = data.get('read_today')
    current_page = data.get('current_page')
    last_page = data.get('last_page')

    result = TrackService.track_book(
        user_id=user_id,
        book_id=book_id,
        read_today=read_today,
        current_page=current_page,
        last_page=last_page
    )

    if isinstance(result, Trackstb):
        return jsonify({"Success": "Book tracked!"}), 200
    else:
        return jsonify({"Error": f"{result}An error occured"}), 500
    
@track_bp.route('/track/<id>', methods=['PUT'])
def edit_track(id):
    if TrackService.get_track_by_id(id) == None:
        return jsonify({"Error": "Track does not exist."}), 404
    
    data = request.get_json()

    current_page = data.get('current_page')
    last_page = data.get('last_page')

    result = TrackService.edit_track(
        track_id=id, 
        current_page=current_page,
        last_page=last_page
    )

    if isinstance(result, Trackstb):
        return jsonify({"Success": f"Track updated!"}), 200
    else:
        return jsonify({"Error": f"{result} An error occured"}), 500
    
@track_bp.route('/track/<id>', methods=['DELETE'])
def delete_track(id):
    if TrackService.get_track_by_id(id) == None:
        return jsonify({"Error": "Track does not exist."}), 404
    
    track = TrackService.delete_track(id)

    if track == None:
        return jsonify({"Success": "Track succesfully deleted!"}), 200
    else:
        return jsonify({"Error": "Could not delete review."}), 500
    
@track_bp.route('/track/<id>', methods=['GET'])
def get_track_by_id(id):
    track = TrackService.get_track_by_id(id)

    if track:
        return jsonify(TrackDTO.to_dict(track)), 200
    else:
        return jsonify({"Error": "Track not found!"}), 400