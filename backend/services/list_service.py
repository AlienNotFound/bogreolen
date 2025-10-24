from backend.connection import db
from backend.models.list_model import Liststb
from backend.services.base_service import BaseService
from backend.services.validators.list_validator import ListValidator

class ListService(BaseService):
    @staticmethod
    def add_book(userid, bookid, listname):
        list = Liststb(userid=userid, bookid=bookid, listname=listname)
        db.session.add(list)

        _, result = BaseService.commit_session(list)

        return result
        
    @staticmethod
    def move_to_list(userid, bookid, listname):
        if ListValidator.validate_listname(listname) == None:
            return f'{listname} is not a valid list name.'
        
        list = ListService.get_list_by_user_and_book(userid=userid, bookid=bookid)

        if list == None:
            return 'List entry not found'

        list.listname = listname

        _, result = BaseService.commit_session(list)

        return result
    
    @staticmethod
    def delete_book_from_lists(bookid, userid):
        success, result = BaseService.delete_by_composite(Liststb, {"userid": userid, "bookid": bookid})

        return result if not success else None

    @staticmethod
    def get_list_by_user_and_book(userid, bookid):
        return db.session.get(Liststb, {"userid": userid, "bookid": bookid})