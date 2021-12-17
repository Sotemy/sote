class Config(object):
    SQLALCHEMY_DATABASE_URI='sqlite:///tmp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Development(Config):
    SECRET_KEY='KDKASsldksad2138293/('
    DEBUG=True

class Production(Config):
    DEBUG=False