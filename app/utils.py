from functools import wraps
from flask_login import current_user
from flask import abort, Response

from app.models import User


#############################       LOGIN UTILS     #####################

def get_role():
    return current_user.role

def admin_required(f):
    @wraps(f)
    def role_wrap(*args, **kwargs):
        role=get_role()
        if role == 'admin':
            return f(*args, **kwargs)
        return abort(Response('Hello World'), 401)
    return role_wrap