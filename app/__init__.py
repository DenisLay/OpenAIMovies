from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_filename='config.py'):
    app = Flask(__name__)
    #app.config.from_object(config_filename)

    #db.init_app(app)
    ma.init_app(app)

    from .routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app