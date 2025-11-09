class UserDTO:
    @staticmethod
    def to_dict_public(user):
        return {
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
        }