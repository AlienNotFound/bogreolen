from sqlalchemy.exc import IntegrityError
from backend.connection import db
from backend.models import Userstb
from backend.services.base_service import BaseService
from backend.services.validators.uservalidator import UserValidator
from werkzeug.security import generate_password_hash

class UserService(BaseService):
    @staticmethod
    def create_user(username, email, password, password_again):

        if not UserValidator.validate_password(password, password_again):
            return -1
        
        if not UserValidator.validate_email(email):
            return -2

        hashed_password = generate_password_hash(password)

        user = Userstb(username=username, email=email, passwordhash=hashed_password)
        db.session.add(user)

        success, result = BaseService.commit_session(user)

        if not success:
            return UserValidator.check_for_duplicate(result)

        return result
        
    @staticmethod
    def edit_user(id, username, email, password, password_again):
        user = Userstb.query.get(id)

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

        success, result = BaseService.commit_session(user)

        if not success:
            return UserValidator.check_for_duplicate(result)
        
        return result
    
    @staticmethod
    def get_user_by_id(id):
        return BaseService.get_by_id(Userstb, Userstb.userid, id)
    
    @staticmethod
    def get_user_by_username(username):
        return BaseService.get_by_id(Userstb, Userstb.username, username)
    
    @staticmethod
    def get_all_users():
        return BaseService.get_all(Userstb)
    
    @staticmethod
    def delete_user(id):
        return BaseService.delete(Userstb, Userstb.userid, id)