import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

db = SQLAlchemy()

def create_app(test_config = None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL


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
    from backend.routes.comment_routes import comment_bp
    from backend.routes.category_routes import category_bp
    
    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(list_bp)
    app.register_blueprint(track_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(category_bp)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_COOKIE_SECURE"] = os.getenv("JWT_COOKIE_SECURE")
    app.config["JWT_COOKIE_SAMESITE"] = os.getenv("JWT_COOKIE_SAMESITE")
    app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"] 
    app.config["JWT_ACCESS_COOKIE_NAME"] = 'access_token'
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

    JWTManager(app)

    CORS(app, origins=[os.getenv("CORS_ORIGIN")],
     supports_credentials=True,
     allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'DELETE', 'OPTIONS', 'PUT'])

    return app