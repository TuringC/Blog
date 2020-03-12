from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import ext
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask('project')

app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.session_protection = "strong"
def inin_ext(app):
    login_manager.init_app(app)
inin_ext(app)

from project import views, errors, commands