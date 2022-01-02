from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail 
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
from OpenSSL import SSL

from config import Development

# context=SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_certificate_file('docs/cert.pem')
# context.use_privatekey_file('docs/key.pem')

app=Flask(__name__)
app.config.from_object(Development)
db=SQLAlchemy(app)
login_manager=LoginManager(app)
mail=Mail(app)
migrate = Migrate(app, db, render_as_batch=True)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from app.main import main
from app.auth import auth
from app.admin import adm as admin

app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(admin)

db.create_all()

print(app.url_map)

from app.models import User