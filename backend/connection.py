import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.getenv('MYSQL_HOST', 'db')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
MYSQL_DATABASE= os.getenv('MYSQL_DATABASE')

db = SQLAlchemy()

def create_app(test_config = None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:' + MYSQL_ROOT_PASSWORD + '@' + MYSQL_HOST + ':3306/' + MYSQL_DATABASE

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    
    from backend.routes.book_routes import book_bp
    from backend.routes.user_routes import user_bp
    from backend.routes.review_routes import review_bp
    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(review_bp)

    return app