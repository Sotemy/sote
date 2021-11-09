from flask import render_template

from app.models import Post
from app.main import main

@main.route('/')
def index():
    result=Post.query.order_by(Post.time.desc()).all()
    
    return render_template('main/index.html', result=result)
