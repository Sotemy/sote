from flask_login import current_user
from flask import render_template
from flask_login.utils import login_required

from app.main.profile import profile
from app.models import Post, User


@profile.route('/')
@login_required
def showYourProfile():
    user=User.query.filter_by(id=current_user.id).first()
    posts=Post.query.filter_by(author=user.id).order_by(Post.time.desc()).all()

    return render_template('main/profile/yourProfile.html', user=user, posts=posts)