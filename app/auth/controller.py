from flask import redirect, render_template, flash, url_for
from flask_login import current_user, login_user, logout_user

from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from app.models import Role, User
from app import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        print(form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Sign In', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            user=User.query.filter_by(username=form.username.data).first()
            role=Role(user_id=user.id)
            db.session.add(role)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('auth.login'))
        except Exception as e:
            return e
    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))