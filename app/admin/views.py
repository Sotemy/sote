from flask import render_template, request
from flask.json import jsonify
from flask_login import current_user, login_required
import os

from app import db
from app.admin import adm
from app.models import Category, Role, Tag, User
from app.utils import admin_required


@adm.route('/')
@login_required
@admin_required
def index():
    print(current_user.role)
    return render_template('admin/index.html')

@adm.route('/add', methods=['POST'])
def addTag():
    name=request.form["name"]
    context=request.form["context"]
    if context == 'add_tag':
        if Tag.query.filter_by(name=name).first():
            return jsonify({'result':'error', 'text':'Tag already exists'})
        tag=Tag(name=name)
        db.session.add(tag)
        db.session.commit()
        return jsonify({'result':"success"})

    if context == 'add_cat':
        if Category.query.filter_by(name=name).first():
            return jsonify({'result':'error', 'text':'Tag already exists'})
        tag=Category(name=name)
        db.session.add(tag)
        db.session.commit()
        return jsonify({'result':"success"})
    



@adm.route('/tables')
@login_required
@admin_required
def tablesPage():
    roles=Role.query.all()
    # , roles=roles
    users=User.query.all()
    tags=Tag.query.all()
    categories=Category.query.all()
    return render_template('admin/tables.html', users=users, roles=roles,
    tags=tags, categories=categories)

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

@adm.route('/config')
@login_required
@admin_required
def checkConfig():
    env=os.environ.get('DATABASE_URL')
    return env

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

@adm.route('/start')
def startLogin():
    if Role.query.filter_by(name='admin').first() == None:
        role=Role(name='admin', desc='admin')
        db.session.add(role)
        db.session.commit()

    if User.query.filter_by(role='admin').first() == None:
        user=User(login='admin', password='123456', email='dmitrii@lechenko.me')
        user.set_role('admin')
        db.session.add(user)
        db.session.commit()

    if Role.query.filter_by(name='user').first() == None:
        role=Role(name='user', desc='user')
        db.session.add(role)
        db.session.commit()
    return 'done'