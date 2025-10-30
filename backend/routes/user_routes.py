from flask import Blueprint, jsonify, request
from backend.models import Userstb
from backend.services.user_service import UserService
from backend.DTOs.user_dto import UserDTO
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import check_password_hash

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = UserService.get_all_users()

    if users:
        return jsonify([UserDTO.to_dict_public(u) for u in users]), 200
    else:
        return jsonify({"Error": "Users not found!"}), 400
    
@user_bp.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    user = UserService.get_user_by_id(id)

    if user:
        return jsonify(UserDTO.to_dict_public(user)), 200
    else:
        return jsonify({"Error": "User not found!"}), 400
    
@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password_again = data.get('password_again')

    result = UserService.create_user(
        username=username,
        email=email,
        password=password,
        password_again=password_again
    )

    if isinstance(result, Userstb):
        return jsonify({"Success": "User created!"}), 200
    elif result == -1:
        return jsonify({"Error": "Password must be the same."}), 409
    elif result == -2:
        return jsonify({"Error": "Invaled email format."}), 403
    elif 'USERNAME_EXISTS' in result:
        return jsonify({"Error": "Username already exists."}), 409
    elif 'EMAIL_EXISTS' in result:
        return jsonify({"Error": "Email already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
    
@user_bp.route('/user/<id>', methods=['PUT'])
def edit_user(id):
    if UserService.get_user_by_id(id) == None:
        return jsonify({"Error": "User does not exist."}), 404
    
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password_again = data.get('password_again')

    result = UserService.edit_user(
        id=id,
        username=username,
        email=email,
        password=password,
        password_again=password_again
    )

    if isinstance(result, Userstb):
        return jsonify({"Success": f"User updated!"}), 200
    elif result == -1:
        return jsonify({"Error": "Password must be the same."}), 409
    elif result == -2:
        return jsonify({"Error": "Invaled email format."}), 403
    elif result == 'USERNAME_EXISTS':
        return jsonify({"Error": "Username already exists."}), 409
    elif result == 'EMAIL_EXISTS':
        return jsonify({"Error": "Email already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500

@user_bp.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if UserService.get_user_by_id(id) == None:
        return jsonify({"Error": "User does not exist."}), 404
    
    user = UserService.delete_user(id)

    if user == None:
        return jsonify({"Success": "User succesfully deleted!"}), 200
    else:
        return jsonify({"Error": "Could not delete user."}), 500
    
@user_bp.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = UserService.get_user_by_username(username)

    if not user:
        return jsonify({'Error': 'User not found.'}), 404
    
    if not user or not check_password_hash(user.passwordhash, password):
        return jsonify({'error': f'Wrong username or password'}), 401

    access_token = create_access_token(identity = username)

    return jsonify({'access_token': access_token})