from flask import request, jsonify
from flask_login.utils import login_user
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
                return jsonify({'result':'Success'})
            return jsonify({'result':'Wrong password'})
        return jsonify({'result':'Wrong username'})

@auth.route('/register', methods=['POST'])
def registerpage():
    if request.method == 'POST':
        login=request.form['login']
        password=request.form['password']
        password2=request.form['password2']
        user=User.query.filter_by(login=login).first()

        if user:
            return jsonify({'result':'Login in use'})

        if password!=password2:
            return jsonify({'result':'Unequal passwords'})

        if check_val(login, password):
            return jsonify({'result':'Too short'})

        user=User(login=login, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({'result':'success'})
        except Exception as e:
            return jsonify({'result':e}) 

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
    return jsonify({'result':app.config['SECRET_KEY']})
