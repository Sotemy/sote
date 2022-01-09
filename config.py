import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI='sqlite:///tmp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ADMINS='sote.mail.agent@gmail.com'
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    MAIL_ASCII_ATTACHMENTS =False
    MAIL_DEFAULT_SENDER='sote.mail.agent@gmail.com'
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USE_SSL= False
    MAIL_USERNAME='sote.mail.agent@gmail.com'
    MAIL_PASSWORD='sotetopchik'
    POSTS_PER_PAGE = 5

class Development(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///tmp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ADMINS='sote.mail.agent@gmail.com'
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    MAIL_ASCII_ATTACHMENTS =False

    MAIL_DEFAULT_SENDER='sote.mail.agent@gmail.com'
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USE_SSL= False
    MAIL_USERNAME='sote.mail.agent@gmail.com'
    MAIL_PASSWORD='sotetopchik'
    SECRET_KEY='KDKASsldksad2138293/('
    DEBUG=True
    TESTING=True

class Production(Config):
    DEBUG=os.environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('TRACK_MOD')
    ADMINS=os.environ.get('ADMINS')
    MAIL_DEBUG=os.environ.get('MAIL_DEBUG')
    MAIL_SUPPRESS_SEND = os.environ.get('MAIL_SUPPRESS_SEND')
    TESTING = os.environ.get('TESTING')
    MAIL_ASCII_ATTACHMENTS =os.environ.get('ATTACH')

    
    MAIL_DEFAULT_SENDER=os.environ.get('SENDER')
    MAIL_SERVER= os.environ.get('SERVER')
    MAIL_PORT= int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS= os.environ.get('TLS')
    MAIL_USE_SSL= os.environ.get('SSL')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASS')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    POSTS_PER_PAGE = 25