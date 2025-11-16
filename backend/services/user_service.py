from backend.connection import db
from backend.models import Users
from backend.services.base_service import BaseService
from backend.services.validators.uservalidator import UserValidator
from werkzeug.security import generate_password_hash

class UserService(BaseService):
    @staticmethod
    def create_user(username, email, password, password_again):

        if not UserValidator.validate_password(password, password_again):
            return 'INVALID_PASSWORD'
        
        if not UserValidator.validate_email(email):
            return 'INVALID_EMAIL'

        hashed_password = generate_password_hash(password)

        if UserService.get_user_by_username(username):
            return False, 'USERNAME_EXISTS'
        
        if UserService.get_user_by_email(email):
            return False, 'EMAIL_EXISTS'
        
        user = Users(username=username, email=email, passwordhash=hashed_password)

        success, result = BaseService.add_entry(user)

        return success, result
        
    @staticmethod
    def edit_user(id, username, email, password, password_again):
        user = Users.query.get(id)

        if (password and password_again):
            if not UserValidator.validate_password(password, password_again):
                return -1
            
        if not UserValidator.validate_email(email):
            return -2
        
        hashed_password = generate_password_hash(password)
        
        user.username = username
        user.email = email
        
        if (password and password_again):
            user.passwordhash = hashed_password

        _, result = BaseService.commit_session(user)

        return result
    
    @staticmethod
    def get_user_by_id(id):
        return BaseService.get_by_id(Users, Users.user_id, id)
    
    @staticmethod
    def get_user_by_username(username):
        return BaseService.get_by_id(Users, Users.username, username)

    @staticmethod
    def get_user_by_email(email):
        return BaseService.get_by_id(Users, Users.email, email)
    
    @staticmethod
    def get_all_users():
        return BaseService.get_all(Users)
    
    @staticmethod
    def delete_user(id):
        return BaseService.delete(Users, Users.user_id, id)