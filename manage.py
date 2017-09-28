from flask_script import Manager, Shell
from app.models import User, ShoppingList, Basket
from app import create_app
import os


app = create_app('default' or os.environ.get('CONFIGURATION'))
manager = Manager(app=app)


def make_shell_context():
    return dict(app=app, User=User, Shoppinglist=ShoppingList)

manager.add_command('shell', Shell(make_context=make_shell_context()))


@manager.command
def start():
    """deploy"""


if __name__ == '__main__':
    manager.run()