from flask import Flask
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    
    # Login setup
    login_manager = LoginManager()
    login_manager.login_view = 'products.index'
    login_manager.init_app(app)

    from app.routes.products import products_bp
    from app.routes.stock import stock_bp
    app.register_blueprint(products_bp)
    app.register_blueprint(stock_bp)

    return app
