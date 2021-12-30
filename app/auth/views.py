from flask import request, jsonify, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.auth import auth
from app.models import User, check_val
from app.auth.email import send_password_reset_email

@auth.route('/login', methods=['POST'])
def loginpage():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                user.toggle_active()
                return jsonify({'result':'success', 'role':user.role})
            
            return jsonify({'result':'error', 'text':'wrong password', 'user':[user.login, user.password], 'password':generate_password_hash(password)})
        return jsonify({'result':'error', 'text':'uregistered'})

@auth.route('/register', methods=['POST'])
def registerpage():
    if request.method == 'POST':
        login=request.form['login']
        email=request.form['email']
        password=request.form['password']
        password2=request.form['password2']
        user=User.query.filter_by(login=login).first()

        if user:
            return jsonify({'result':'error', 'text':'exists'})

        if password!=password2:
            return jsonify({'result':'error', 'text':'unequal pass'})

        if check_val(login, password)==False:
            return jsonify({'result':'error', 'text':'password or login problem'})

        user=User(login=login, password=password, email=email)
        if user.set_role('admin'):
            try:
                db.session.add(user)
                db.session.commit()
                return jsonify({'result':'success'})
            except Exception as e:
                print(e)
                return jsonify({'result':'error', 'text':'e'}) 
        return 'error'

@auth.route('/reset-password', methods=['GET', 'POST'])
def resetpage():
    if request.method == 'POST':
        email=request.form['email']
        user=User.query.filter_by(email=email).first()
        if user:
            send_password_reset_email(user)
            return jsonify({'result':'success', 'text':'Link'})
        return jsonify({'result':'error'})

@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        user = User.verify_reset_password_token(token)
        if not user:
            return redirect(url_for('main.index'))
        password=request.form['password']
        user.set_password(password)
        db.session.commit()
        print('Your password has been reset.')
        return redirect('/')
        
    return render_template('auth/reset_password.html')

@auth.route('/logout', methods=['get','post'])
def logoutUser():
    logout_user()
    return redirect('/')
