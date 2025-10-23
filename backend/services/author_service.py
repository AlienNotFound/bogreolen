from backend.connection import db
from backend.models import Authorstb

class AuthorService:
    @staticmethod
    def create_author(name):
        author = Authorstb(name=name)

        db.session.add(author)
        db.session.commit()

        return author

    @staticmethod
    def edit_author(id, name):
        author = Authorstb.query.get(id)

        if author:
            author.name = name
            db.session.commit()
            return author
        
        return None
    
    @staticmethod
    def get_author_by_name(name):
        author = db.session.query(Authorstb).filter_by(name=name).first()
        if author:
            return author
        
        return None
    
    @staticmethod
    def get_author_by_id(id):
        author = db.session.query(Authorstb).filter_by(authorid=id).first()
        if author:
            return author
        
        return None
