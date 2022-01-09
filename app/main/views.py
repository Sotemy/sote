from flask import render_template, request, redirect, jsonify, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from app.models import Category, Post, User, Role
from app import db, app
from app.main import main

@main.route('/')
def index():
    # role = Role(name='user', desc='user')
    # db.session.add(role)
    # db.session.commit()
    # admin=User(login='sotemy', email='dmitrii@lechenko.me', password='sotemy1337')
    # admin.set_role('admin')
    # db.session.add(admin)
    # db.session.commit()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    return render_template("main/index.html", posts=posts.items, pages=posts)



@main.route('/post/<id>')
def showPost(id):
    post=Post.query.filter_by(id=id).first_or_404()
    return render_template('main/postForm.html', post=post)

@main.route('/post/add', methods=['GET','POST'])
@login_required
def createPost():
    if request.method=='POST':
        title=request.form['title']
        text=request.form['text']
        if len(title)<=2:
            return jsonify({'result':'erroe', 'text':'short title'})
        post=Post(title=title, text=text, author=current_user)
        try:
            db.session.add(post)
            db.session.commit()
            # jsonify({'result':'succes', 'text':'added'})
            post=Post.query.filter_by(user_name=current_user.login).order_by(Post.id.desc()).first()
            return redirect(url_for('main.showPost', id=post.id))
        except Exception as e:
            print(e)
            return jsonify({'result':'error', 'text':'e'})
    cats=Category.query.all()
    return render_template('main/addPost.html', cats=cats)