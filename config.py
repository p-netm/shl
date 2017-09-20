__author__ = 'Sudo Pnet'
import os


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'adau fagkfa821b 32bdc^!$@sad'
    FLASKY_MAIL_SUBJECT_PREFIX = "SHOPPING LIST.COM"
    FLASKY_MAIL_SENDER = ''

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfiguration(Configuration):
    DEBUG = True
    MAIL_SERVER = ''
    MAIL_PORT = ''
    MAIL_USE_TLS = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class TestingConfiguration(Configuration):
    TESTING = True


class ProductionConfiguration(Configuration):
    pass


config = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
    'default' : DevelopmentConfiguration
}