from backend.models import Userstb

class UserDTO:
    @staticmethod
    def to_dict_public(user):
        return {
            "userid": user.userid,
            "username": user.username,
            "email": user.email,
        }