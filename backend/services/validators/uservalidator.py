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

    @staticmethod
    def validate_password_regex(password):
        errors = []

        if len(password) < 8:
            errors.append("at least 8 characters")
        if not any(c.isupper() for c in password):
            errors.append("an uppercase letter")
        if not any(c.islower() for c in password):
            errors.append("a lowercase letter")
        if not any(c.isdigit() for c in password):
            errors.append("a number")
        if not any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
            errors.append("a special character")

        if not errors:
            return True, ""

        error_string = ""
        for index, item in enumerate(errors):
            if index == 0:
                error_string += item
            elif index == len(errors) - 1:
                error_string += " and " + item
            else:
                error_string += ", " + item

        return False, error_string
