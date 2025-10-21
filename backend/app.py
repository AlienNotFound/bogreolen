from backend.connection import create_app, db
from backend.models import *

app = create_app()

with app.app_context():
    db.create_all()

Bookstb.create_book()