
from backend.models.list_model import ListName

class ListValidator:
    @staticmethod
    def validate_listname(listname):
        try:
            return ListName(listname)
        except ValueError:
            return None