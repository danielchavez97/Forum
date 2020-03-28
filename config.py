import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Na7LYg'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'False')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'True')
    MAIL_USERNAME = os.environ.get('daniel.chavez9797@gmail.com')
    MAIL_PASSWORD = os.environ.get('Realmadrid97')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Groove Spot]'
    FLASKY_MAIL_SENDER = 'daniel.chavez9797@gmail.com'
    FLASKY_ADMIN = 'daniel.chavez9797@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig

}

