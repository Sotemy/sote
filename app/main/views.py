from flask.templating import render_template

from app.models import Role
from app import db
from app.main import main

@main.route('/')
def index():
    # role = Role(name='admin', desc='admin')
    # db.session.add(role)
    # db.session.commit()
    
    return render_template('main/index.html')