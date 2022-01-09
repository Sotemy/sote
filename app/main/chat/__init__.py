from flask import Blueprint

userchat=Blueprint('chat', __name__, url_prefix='/chat')

from app.main.chat import views