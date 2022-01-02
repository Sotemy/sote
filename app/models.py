from datetime import datetime
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash
import jwt
from time import time

from app import db, login_manager, app

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(128), nullable=False)
    text=db.Column(db.Text, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow())
    user_name = db.Column(db.Integer, db.ForeignKey('user.login'))
    
class Role(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64), nullable=False, unique=True)
    desc=db.Column(db.String(120), nullable=False)
    users = db.relationship("User", backref="roles")
    # users = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    login=db.Column(db.String(64), nullable=False)
    active=db.Column(db.Boolean, nullable=False)
    last_seen=db.Column(db.DateTime, nullable=False)
    email=db.Column(db.String(120), nullable=False)
    password=db.Column(db.String(256), nullable=False)
    date_reg=db.Column(db.DateTime, default=datetime.utcnow())
    # role = db.relationship("Role", backref="users")
    role = db.Column(db.Integer, db.ForeignKey('role.name'))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, login, password, email):
        self.password=generate_password_hash(password)
        self.email=email
        self.login=login
        self.active=False
        self.last_seen=datetime.utcnow()

    def toggle_active(self):
        user=User.query.filter_by(id=self.id).first()
        if user:
            if user.active == True:
                print(user.last_seen)
                user.active = False
            elif user.active ==False:
                user.active=True
            print(user.last_seen)
            user.last_seen=datetime.utcnow()
            db.session.commit()
            return True
        return False


    def set_role(self, role):
        rl=Role.query.filter_by(name=role).first()
        if rl:
            self.role=role
            return True
        return False

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
            print(id)
        except:
            return print('failed')
        return User.query.get(id)

def check_val(login, password):
    if len(login) < 5:
        return False
            
    if len(password) < 8:
        return False
    
    return True

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)