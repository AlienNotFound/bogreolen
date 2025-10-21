import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

load_dotenv()

MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
MYSQL_DATABASE= os.getenv('MYSQL_DATABASE')


def create_app(test_config = None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:' + MYSQL_ROOT_PASSWORD + '@localhost:3306/' + MYSQL_DATABASE

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    return app

create_app()