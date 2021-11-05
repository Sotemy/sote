from flask import Blueprint

main=Blueprint('main', __name__, url_prefix='/')

from app.main import controller

from app.main.post_mod import post_mod

main.register_blueprint(post_mod)

from app.main.profile import profile as profile_mod

main.register_blueprint(profile_mod)
