import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Base(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Base):
    DEBUG_TB_INTERCEPT_REDIRECTS=False
    DEBUG=True
    TESTING=True
    PERMANENT_SESSION_LIFETIME=timedelta(days=1)

    MAIL_SERVER='localhost'
    MAIL_PORT=8025
    

class ProductionConfig(Base):
    DEBUG=True
    TESTING=True
    PERMANENT_SESSION_LIFETIME=timedelta(days=1)