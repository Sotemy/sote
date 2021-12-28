from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
import jwt
from time import time

from app import db, login_manager, app

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    users = db.relationship('User', secondary=roles_users,
                            backref=db.backref('roles', lazy='dynamic'))


class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    login=db.Column(db.String(64), nullable=False)
    email=db.Column(db.String(120), nullable=False)
    password=db.Column(db.String(256), nullable=False)
    date_reg=db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, login, password, email):
        self.password=generate_password_hash(password)
        self.email=email
        self.roles.append('user')
        self.login=login
    
    def set_role(self, role):
        role=Role.query.filter_by(name=role).first()
        if role:
            self.roles.append(role)
            return True
        return False
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

def check_val(login, password):
    if len(login) < 5:
        return False
            
    if len(password) < 8:
        return False
    
    return True

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)