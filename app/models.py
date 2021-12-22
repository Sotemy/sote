from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from app import db, login_manager

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    login=db.Column(db.String(64), nullable=False)
    password=db.Column(db.String(256), nullable=False)
    date_reg=db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, login, password):
        self.password=generate_password_hash(password)

        self.login=login

def check_val(login, password):
    if len(login) < 5:
        return False
            
    if len(password) < 8:
        return False
    
    return True

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)