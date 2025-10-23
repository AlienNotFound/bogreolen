from backend.connection import db
from backend.models import Categoriestb

class CategoryService:
    @staticmethod
    def create_category(title):
        category = Categoriestb(title=title)

        db.session.add(category)
        db.session.commit()

        return category

    @staticmethod
    def edit_category(id, title):
        category = Categoriestb.query.get(id)

        if category:
            category.title = title
            db.session.commit()
            return category
        
        return None
    
    @staticmethod
    def get_category_by_title(title):
        category = db.session.query(Categoriestb).filter_by(title=title).first()
        if category:
            return category
        
        return None
    
    @staticmethod
    def get_category_by_id(id):
        category = db.session.query(Categoriestb).filter_by(categoryid=id).first()
        if category:
            return category
        
        return None
