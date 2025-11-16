from re import match

class UserValidator:        
    @staticmethod
    def validate_email(email):
        EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not match(EMAIL_REGEX, email):
            return False
        else:
            return True
        
    @staticmethod
    def validate_password(password, password_again):
        if password == password_again:
            return True
        else:
            return False
