from flask import Flask
from .config import  project_config
from Flask_Mvt.models import  db
from flask_migrate import Migrate

def create_app(config_name):
    app = Flask(__name__)
    app_config = project_config[config_name] 
    
    app.config["SQLALCHEMY_DATABASE_URI"]=app_config.SQLALCHEMY_DATABASE_URI

    app.config.from_object(app_config)
    db.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)

    from Flask_Mvt.posts.postblueprints import post_blueprint
    app.register_blueprint(post_blueprint)

    return app