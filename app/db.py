from models import Role, User, roles_users
from app import db

try:
    role=Role(name='admin', description='admin')
    db.session.add(role)
    db.session.commit()
    p='pbkdf2:sha256:260000$3zBdX7KPYYWW3t6X$31468f39f7d307d0cdadc1e8c8bdf091301a7b07fea20f9d2806ef3d7cdc99cf'
    user = User(login='aboba', password=p, email='dmitrii@lechenko.me')
    user.set_role('admin')
    db.session.add(user)
    db.session.commit()
except Exception as e:
    print(e)