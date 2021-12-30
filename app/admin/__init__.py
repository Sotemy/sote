from flask import Blueprint

adm=Blueprint('admin', __name__, url_prefix='/admin')

from app.admin import views