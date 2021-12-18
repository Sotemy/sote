from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Development

app=Flask(__name__)
app.config.from_object(Development)
db=SQLAlchemy(app)
login_manager = LoginManager(app)

from app.main import main
from app.auth import auth

app.register_blueprint(auth)
app.register_blueprint(main)

db.create_all()


from app.models import User