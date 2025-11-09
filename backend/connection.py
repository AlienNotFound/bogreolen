import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

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
    from backend.routes.list_routes import list_bp
    from backend.routes.track_routes import track_bp
    from backend.routes.image_route import image_bp
    from backend.routes.author_routes import author_bp
    
    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(list_bp)
    app.register_blueprint(track_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(author_bp)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_COOKIE_SAMESITE"] = "Lax"
    app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"] 
    app.config["JWT_ACCESS_COOKIE_NAME"] = 'access_token'
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

    JWTManager(app)

    CORS(app, origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
     supports_credentials=True,
     allow_headers=['Content-Type'],
     methods=['GET', 'POST', 'DELETE', 'PUT'])

    return app