from flask_cors import CORS
from flask import Flask
from config import config
from modules.db_model import db
from modules.sample.sample_controller import sample_api

def create_app(app_name, config_name):
    app = Flask(app_name, static_url_path='')
    app.config.from_object(config[config_name])
    CORS(app)
    init_db(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(sample_api)

def init_db(app):
    db.init_app(app)
    app.db = db
