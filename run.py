from flask import Flask
from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(app_config[config_filename])
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)
    migrate = Migrate(app, db)

    from models import department, employee

    return app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == "__main__":
    app.run(port='5002')