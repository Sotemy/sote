from flask import render_template
from flask_login import login_required, current_user
from werkzeug.exceptions import abort

from app.chat import chat as chat_mod
from app.models import Post

@chat_mod.route('/')
def index():
    return render_template('chat/index.html')

@chat_mod.route('/<post_id>')
@login_required
def showChatByPost(post_id):
    chat_user=Post.query.filter_by(id=post_id).first()

    if chat_user.author!=current_user.id:
        abort(404)
    
    return 'it works'