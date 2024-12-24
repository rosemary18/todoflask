from flask import Flask

from app.models import db
from .routes import register_blueprints

def create_app():
    
    app = Flask(
        __name__,
        template_folder="views",
        static_folder="public",
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'production'

    db.init_app(app)
    
    register_blueprints(app)
    
    with app.app_context():
        db.create_all()
        
    return app