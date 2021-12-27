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

class Development(Config):
    SECRET_KEY='KDKASsldksad2138293/('
    DEBUG=True
    TESTING=True

class Production(Config):
    DEBUG=False