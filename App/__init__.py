from flask import Flask,Blueprint 
from .routes import wine_bp,house_bp,home_bp

def create_flask_app():

    app = Flask(__name__)

    app.register_blueprint(wine_bp,url_prefix="/wine")
    app.register_blueprint(house_bp,url_prefix="/house")
    app.register_blueprint(home_bp,url_prefix="/")

    return app