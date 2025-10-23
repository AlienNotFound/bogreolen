from sqlalchemy.exc import IntegrityError
from backend.connection import db

class BaseService:
    @staticmethod
    def get_by_id(model, id_column, id):
        return db.session.query(model).filter(id_column == id).first()

    @staticmethod
    def get_all(model):
        return db.session.query(model).all()
    
    @staticmethod
    def delete(model, id_column, id):
        db.session.query(model).filter(id_column == id).delete()
        BaseService.commit_session()

    @staticmethod
    def commit_session(instance=None):
        try:
            db.session.commit()
            
            return True, instance
        except IntegrityError as e:
            db.session.rollback()
            
            return False, str(e.orig)