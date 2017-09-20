from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from config import config



login_manager = LoginManager()
mail = Mail()
moment = Moment()


login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


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
    from .main import shl
    app.register_blueprint(shl)
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
