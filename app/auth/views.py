from flask import request, jsonify
from flask_login.utils import login_user
from werkzeug.security import check_password_hash

from app.auth import auth
from app.models import User

@auth.route('/login', methods=['POST'])
def loginpage():
    if request.method == 'POST':
        login=request.form['login']
        password=request.form['password']
        user=User.query.filter_by(login=login).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return jsonify({'result':'Success'})
            return jsonify({'result':'Wrong password'})
        return jsonify({'result':'Wrong username'})

@auth.route('/register', methods=['POST'])
def registerpage():
    if request.method == 'POST':
        login=request.form['login']
        password=request.form['password']
        password2=request.form['password2']
