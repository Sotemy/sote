from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app.main.post_mod import post_mod
from app.main.post_mod.forms import NewPostForm
from app.models import Post, User
from app import db

@post_mod.route('/add', methods=['GET', 'POST'])
@login_required
def addPost():
    form=NewPostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data, text=form.text.data, author=current_user.id)
        print(current_user)
        try:
            db.session.add(post)
            db.session.commit()
            post=Post.query.filter_by(author=current_user.id).order_by(Post.id.desc()).first()
            return redirect(url_for('main.post_mod.postId', id=post.id))
        except Exception as e:
            return f'error {e}'
    return render_template('main/post_mod/addPost.html', form=form)

@post_mod.route('/<id>')
def postId(id):
    post=Post.query.filter_by(id=id).first_or_404()
    user=User.query.filter_by(id=post.author).first()
    return render_template('main/post_mod/postId.html', post=post, user=user)
