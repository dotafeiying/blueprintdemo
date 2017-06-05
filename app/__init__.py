# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='main.login'
# login_manager.login_message = "Bonvolu ensaluti por uzi tio paĝo."
login_manager.init_app(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# from app import views, models