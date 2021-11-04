from flask import Blueprint

post_mod=Blueprint('post_mod', __name__, url_prefix='/post')

from app.main.post_mod import controller