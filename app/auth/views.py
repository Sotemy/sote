from flask import request, jsonify
from flask_login.utils import login_user, logout_user
from werkzeug.security import check_password_hash

from app import db, app
from app.auth import auth
from app.models import User, check_val

@auth.route('/login', methods=['POST'])
def loginpage():
    if request.method == 'POST':
        login=request.form['login']
        password=request.form['password']
        user=User.query.filter_by(login=login).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return jsonify({'result':'success'})
            return jsonify({'result':'error'})
        return jsonify({'result':'error'})

@auth.route('/register', methods=['POST'])
def registerpage():
    if request.method == 'POST':
        login=request.form['login']
        password=request.form['password']
        password2=request.form['password2']
        user=User.query.filter_by(login=login).first()

        if user:
            return jsonify({'result':'error'})

        if password!=password2:
            return jsonify({'result':'error'})

        if check_val(login, password)==False:
            return jsonify({'result':'error'})

        user=User(login=login, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({'result':'success'})
        except Exception as e:
            return jsonify({'result':'error'}) 

@auth.route('/reset-password', methods=['POST'])
def resetpage():
    if request.method == 'POST':
        login=request.form['login']
        user=User.query.filter_by(login=login).first()
        if user:
            if len(user.secret_phrase)>0:
                
                return jsonify({'':''})


@auth.route('/get-key')
def requestKey():
    return jsonify({'result':'key',
    'key':'adasdQWEQW'})

@auth.route('/logout')
def logoutUser():
    logout_user()
    return jsonify({'result':'success'})