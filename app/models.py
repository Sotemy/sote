from datetime import datetime
from enum import unique
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
import jwt
from time import time

from app import db, login_manager, app

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    item=db.Column(db.String(140), db.ForeignKey('post.id'))
    sent_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True, unique=True)
    title=db.Column(db.String(128), nullable=False)
    text=db.Column(db.Text, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow())
    user_name = db.Column(db.String(64), db.ForeignKey('user.login'))
    tags = db.Column(db.String(140), db.ForeignKey('tag.name'))
    category= db.Column(db.String(140), db.ForeignKey('category.name'))

    def set_tag(self, tag):
        new_tag=Tag.query.filter_by(name=tag).first()
        if new_tag:
            self.tags.append(new_tag)
            db.session.commit()
            return True
        return False

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), unique=True)
    cats = db.Column(db.String, db.ForeignKey('category.name'))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), unique=True)
    tags=db.relationship("Tag", backref="categories")


class Role(db.Model):
    id=db.Column(db.Integer, primary_key=True, unique=True)
    name=db.Column(db.String(64), nullable=False, unique=True)
    desc=db.Column(db.String(120), nullable=False)
    users = db.relationship("User", backref="roles")
    # users = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True, unique=True)
    login=db.Column(db.String(64), nullable=False)
    active=db.Column(db.Boolean, nullable=False)
    last_seen=db.Column(db.DateTime, nullable=False)
    email=db.Column(db.String(120), nullable=False)
    password=db.Column(db.String(256), nullable=False)
    date_reg=db.Column(db.DateTime, default=datetime.utcnow())
    role = db.Column(db.String, db.ForeignKey('role.name'))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)

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

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

def check_val(login, password):
    if len(login) < 5:
        return False
            
    if len(password) < 5:
        return False
   
    return True

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)