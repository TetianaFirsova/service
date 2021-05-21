from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)
    migrate = Migrate(app, db)

    from models import department, employee

    return app

app = create_app('config')

if __name__ == "__main__":
    app.run(debug=True, port='5002')