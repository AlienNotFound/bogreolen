from sqlalchemy.exc import IntegrityError
from backend.connection import db

class BaseService:
    @staticmethod
    def get_by_latest(model, id_column):
        return db.session.query(model).order_by(id_column.desc()).first()

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
    def delete_by_composite(model, filters: dict):
        db.session.query(model).filter_by(**filters).delete()
        return BaseService.commit_session()

    @staticmethod
    def commit_session(instance=None):
        try:
            db.session.commit()
            
            return True, instance
        except IntegrityError as e:
            db.session.rollback()
            
            return False, str(e.orig)
        
    @staticmethod
    def search_for(model, search_column, search_query):
        return db.session.query(model).filter(search_column.like(f'%{search_query}%')).all()