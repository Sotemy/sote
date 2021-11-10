from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail

from config import  DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db=SQLAlchemy(app)
migrate = Migrate(app)
mail = Mail(app)
login_manager=LoginManager(app)

login_manager.login_view = 'auth.login'

toolbar = DebugToolbarExtension(app)

#########################################   MODULES    #########################################

from app.auth import auth
from app.main import main
from app.errors import error as error_mod
from app.chat import chat

app.register_blueprint(auth)

app.register_blueprint(main)

app.register_blueprint(error_mod)

app.register_blueprint(chat)

db.create_all()