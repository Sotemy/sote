from flask import Blueprint

profile=Blueprint('profile', __name__, url_prefix='/profile')

from app.main.profile import controller