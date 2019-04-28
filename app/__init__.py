from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # ....

    # initializing flask extensions
    # config_options[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    return app