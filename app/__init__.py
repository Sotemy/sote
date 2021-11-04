from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager=LoginManager(app)
login_manager.login_view = 'login'

toolbar = DebugToolbarExtension(app)

from app.auth import auth

app.register_blueprint(auth)

from app.main import main

app.register_blueprint(main)

db.create_all()