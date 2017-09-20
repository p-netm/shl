from flask import Flask
import os
from flask_mail import Mail
from flask_moment import Moment
from shl.config import config
from shl.app.main import shl
from flask_login import LoginManager
from shl.app.auth import auth

login_manager = LoginManager()
mail = Mail()
moment = Moment()


def create_app(configuration_name='default'):
    """ factory function: used to delay the creation of the application instance
    so that configuration details can be selected"""
    app = Flask(__name__)
    # make sure configuration is valid
    configuration_list = ['development', 'testing', 'production', 'default']
    if configuration_name not in configuration_list:
        raise ValueError('Unknown configuration argument')
    app.config.from_object(config[configuration_name])
    config[configuration_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    # register the shl blueprint: comes alive with the application instance
    app.register_blueprint(shl)
    app.register_blueprint(auth)

    return app
