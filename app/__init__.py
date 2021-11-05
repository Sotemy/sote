from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

from config import  DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db=SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager=LoginManager(app)
login_manager.login_view = 'auth.login'

toolbar = DebugToolbarExtension(app)

from app.auth import auth

app.register_blueprint(auth)

from app.main import main

app.register_blueprint(main)

from app.errors import error as error_mod

app.register_blueprint(error_mod)

db.create_all()