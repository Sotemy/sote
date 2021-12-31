from flask.json import jsonify
from flask_login import login_required, current_user
from flask import render_template, request
from werkzeug.security import generate_password_hash

from app import db
from app.admin import adm
from app.models import Role, User
from app.utils import admin_required

@adm.route('/')
@login_required
@admin_required
def index():
    print(current_user.role)
    return render_template('admin/index.html')

@adm.route('/tables')
@login_required
@admin_required
def tablesPage():
    roles=Role.query.all()
    # , roles=roles
    users=User.query.all()
    return render_template('admin/tables.html', users=users, roles=roles)

@adm.route('/create-role', methods=['post'])
@login_required
@admin_required
def createRole():
    name=request.form['name']
    desc=request.form['desk']
    cr=Role.query.filter_by(name='name').first()
    if cr:
        return jsonify({'result':'error', 'text':'role exists'})
    role=Role(name=name, desc=desc)
    try:
        db.session.add(role)
        db.session.commit()
        return jsonify({'result':'success', 'text':'role added'})
    except Exception as e:
        return jsonify({'result':'error', 'text':e})

@adm.route('/reg')
def reg():
    # role=Role(name='user', desc='user')
    # db.session.add(role)
    # db.session.commit()
    # user1=User(login='testuser1', password=generate_password_hash('testuser1'), 
    # email='dmitrii@lechenko.me')

    # user2=User(login='testuser2', password=generate_password_hash('testuser2'), 
    # email='tester@lechenko.me')

    # user3=User(login='testuser3', password=generate_password_hash('testuser3'), 
    # email='dmitrii@test.me')

    # user4=User(login='testuser4', password=generate_password_hash('testuser4'), 
    # email='test@test.me')

    # user1.set_role('user')
    # user2.set_role('user')
    # user3.set_role('user')
    # user4.set_role('user')

    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.add(user3)
    # db.session.add(user4)
    # db.session.commit()
    return 'done'