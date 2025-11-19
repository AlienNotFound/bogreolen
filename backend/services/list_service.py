from backend.connection import db
from backend.models.list_model import Lists
from backend.services.base_service import BaseService
from backend.services.validators.list_validator import ListValidator

class ListService(BaseService):
    @staticmethod
    def add_to_list (user_id, book_id, listname):
        list = Lists(user_id=user_id, book_id=book_id, listname=listname)
        db.session.add(list)

        success, result = BaseService.commit_session(list)

        return success, result
        
    @staticmethod
    def move_to_list(user_id, book_id, listname):
        if ListValidator.validate_listname(listname) == None:
            return f'{listname} is not a valid list name.'
        
        list = ListService.get_list_by_user_and_book(user_id=user_id, book_id=book_id)

        if list == None:
            return 'List entry not found'

        list.listname = listname

        _, result = BaseService.commit_session(list)

        return result
    
    @staticmethod
    def delete_book_from_lists(user_id, book_id):
        success, result = BaseService.delete_by_composite(Lists, {"user_id": user_id, "book_id": book_id})

        return result if not success else None

    @staticmethod
    def get_list_by_user_and_book(user_id, book_id):
        return db.session.get(Lists, {"user_id": user_id, "book_id": book_id})
    
    @staticmethod
    def get_lists_by_user(user_id):
        return BaseService.get_all_by_id(Lists, Lists.user_id, user_id)
    
    @staticmethod
    def get_book_status(user_id, book_id):
        return BaseService.get_by_composite(Lists, {"user_id": user_id, "book_id": book_id})