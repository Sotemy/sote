from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app import login_manager

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role=db.relationship('Role', backref='user', lazy='dynamic')
    posts=db.relationship('Post', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(140), default='user')
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    privelegy=db.Column(db.String(140), default='r')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Role {}>'.format(self.role)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String)
    text=db.Column(db.Text)
    time=db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author=db.Column(db.Integer, db.ForeignKey('user.id'))