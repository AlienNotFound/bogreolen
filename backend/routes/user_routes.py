from flask import Blueprint, jsonify, request
from backend.models import Users
from backend.services.user_service import UserService
from backend.services.validators.general_validators import GeneralValidator
from backend.services.validators.uservalidator import UserValidator
from backend.DTOs.user_dto import UserDTO
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity, get_jwt
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
@jwt_required()
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

    required_fields = ['username', 'email', 'password', 'password_again']

    no_empty_fields, empty_fields = GeneralValidator.validate_required_fields(required_fields, data)
    
    valid, message = UserValidator.validate_password_regex(password)

    if not valid:
        return jsonify({"error": f"Password must contain {message}"}), 400
    if not no_empty_fields:
        return jsonify({'error': f'{empty_fields} cannot be empty.' }), 404
    
    success, result = UserService.create_user(
        username=username,
        email=email,
        password=password,
        password_again=password_again
    )

    if success:
        return jsonify({'message': 'User created!'}), 200
    elif result == 'INVALID_PASSWORD':
        return jsonify({'error': 'Password must be the same.'}), 403
    elif result == 'INVALID_EMAIL':
        return jsonify({'error': 'Invalid email format.'}), 403
    elif result == 'USERNAME_EXISTS':
        return jsonify({'error': 'Username already exists.'}), 409
    elif result == 'EMAIL_EXISTS':
        return jsonify({'error': 'Email already exists.'}), 409
    else:
        return jsonify({'error': 'An error occured'}), 500
    
@user_bp.route('/user/<id>', methods=['PUT'])
@jwt_required()
def edit_user(id):

    user = UserService.get_user_by_id(id)
    if user == None:
        return jsonify({"error": "User does not exist."}), 404
    
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    current_password = data.get('current_password')
    password = data.get('password')
    password_again = data.get('password_again')

    if current_password and not check_password_hash(user.passwordhash, current_password):
        return jsonify({"error": "Current password is invalid."}), 403
    
    valid, message = UserValidator.validate_password_regex(password)

    if not valid:
        return jsonify({"error": f"Password must contain {message}"}), 400

    success, message = UserService.edit_user(
        id=id,
        username=username,
        email=email,
        password=password,
        password_again=password_again
    )

    if success:
        return jsonify({"message": "User updated."}), 200
    elif message == 'INVALID_PASSWORD':
        return jsonify({"error": "Password must be the same."}), 403
    elif message == 'INVALID_EMAIL':
        return jsonify({"error": "Invalid email format."}), 403
    elif message == 'USERNAME_EXISTS':
        return jsonify({"error": "Username already exists."}), 409
    elif message == 'EMAIL_EXISTS':
        return jsonify({"error": "Email already exists."}), 409
    else:
        return jsonify({"error": f"An error occured"}), 500

@user_bp.route('/user/<id>', methods=['DELETE'])
@jwt_required()
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

    required_fields = ['username', 'password']

    no_empty_fields, empty_fields = GeneralValidator.validate_required_fields(required_fields, data)

    if not no_empty_fields:
        return jsonify({'error': f'{empty_fields} cannot be empty.' }), 404

    user = UserService.get_user_by_username(username)

    if not user:
        return jsonify({'error': 'User doesn\'t exist.'}), 404
    
    if not user or not check_password_hash(user.passwordhash, password):
        return jsonify({'error': f'Wrong username or password'}), 401

    access_token = create_access_token(identity = str(user.user_id), fresh = True)
    refresh_token = create_refresh_token(str(user.user_id))

    return jsonify({'access_token': access_token,
                    'refresh_token': refresh_token}), 200

@user_bp.route('/refreshtoken', methods=['POST'])
@jwt_required(refresh = True)
def refreshtoken():
    user_id = get_jwt_identity()
    new_token = create_access_token(identity = user_id, fresh = False)

    return {"access_token": new_token}, 200