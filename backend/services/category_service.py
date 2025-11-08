from backend.connection import db
from backend.models import Categories

class CategoryService:
    @staticmethod
    def create_category(title):
        category = Categories(title=title)

        db.session.add(category)
        db.session.commit()

        return category

    @staticmethod
    def edit_category(id, title):
        category = Categories.query.get(id)

        if category:
            category.title = title
            db.session.commit()
            return category
        
        return None
    
    @staticmethod
    def get_category_by_title(title):
        category = db.session.query(Categories).filter_by(title=title).first()
        if category:
            return category
        
        return None
    
    @staticmethod
    def get_category_by_id(id):
        category = db.session.query(Categories).filter_by(category_id=id).first()
        if category:
            return category
        
        return None
