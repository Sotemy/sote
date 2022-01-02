from functools import wraps
from flask_login import current_user
from flask import abort, Response

from app.models import User


#############################       LOGIN UTILS     #####################

def get_role():
    return current_user.role

def admin_required(f):
    @wraps(f)
    def admin_wrap(*args, **kwargs):
        role=get_role()
        if role == 'admin':
            return f(*args, **kwargs)
        return abort(401)
    return admin_wrap

def user_required(f):
    @wraps(f)
    def user_wrap(*args, **kwargs):
        role=get_role()
        if role in ['user', 'admin']:
            return f(*args, **kwargs)
        return abort(401)
    return user_wrap