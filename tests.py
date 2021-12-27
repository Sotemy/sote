import os
import unittest
from werkzeug.security import check_password_hash

from app import app, db
from app.models import User, check_val
from app.auth.email import send_password_reset_email


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_table(self):
        user=User(login='123123', password='121313', email='sadsada@ldsa.com')
        assert check_val(user.login, user.password) == True
        print(check_val(user.login, user.password))

        db.session.add(user)
        db.session.commit()
        user=User.query.filter_by(login='123123').first()
        assert check_val(user.login, user.password) == True
        assert user.login == '123123'
        print(check_val(user.login, user.password))

        user=User(login='hi', password='', email='sadsada@ldsiiiiia.com')
        db.session.add(user)
        db.session.commit()
        user=User.query.filter_by(login='hi').first()
        assert user.login == 'hi'
        assert check_val(user.login, user.password) == False
        u=User.query.all()
        for i in u:
            print(i.email)

    def test_login(self):
        
        user=User(login='aboba', password='121313', email='sadsada@ldsasda.com')
        db.session.add(user)
        db.session.commit()
        email='sadsada@ldsasda.com'
        user=User.query.filter_by(email=email).first()
        print(user)
        assert email==user.email
    
    def test_reset(self):
        user=User(login='aboadasba', password='121313', email='saadsada@ldsasda.com')
        db.session.add(user)
        db.session.commit()
        email='saadsada@ldsasda.com'
        user=User.query.filter_by(email=email).first()
        print(user)
        send_password_reset_email(user)


if __name__ == '__main__':
    unittest.main()