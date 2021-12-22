import os
import unittest

from app import app, db
from app.models import User, check_val

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_table(self):
        user=User(login='123123', password='121313')
        assert check_val(user.login, user.password) == True
        print(check_val(user.login, user.password))

        db.session.add(user)
        db.session.commit()
        user=User.query.filter_by(login='123123').first()
        assert check_val(user.login, user.password) == True
        assert user.login == '123123'
        print(check_val(user.login, user.password))

        user=User(login='hi', password='')
        db.session.add(user)
        db.session.commit()
        user=User.query.filter_by(login='hi').first()
        assert user.login == 'hi'
        assert check_val(user.login, user.password) == False

if __name__ == '__main__':
    unittest.main()