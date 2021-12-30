from functools import wraps
from flask_login import current_user
from flask import abort, Response

from app.models import User


#############################       LOGIN UTILS     #####################


def admin_required(f):
    @wraps(f)
    def role_wrap(*args, **kwargs):
        role=(User.query.filter_by(id=current_user.id).first()).get_role()
        if role == 'admin':
            return f(*args, **kwargs)
        return abort(Response('Hello World'), 403)
    return role_wrap