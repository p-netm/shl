from flask_script import Manager, Shell
from app.models import User, ShoppingList
from app import create_app
import os


app = create_app('default')
manager = Manager(app=app)


@manager.shell
def make_shell_context():
    return dict(app=app, User=User, ShoppingList=ShoppingList)


if __name__ == '__main__':
    manager.run()