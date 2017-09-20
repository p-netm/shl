from flask_script import Manager, Shell
from shl.app.models import User, ShoppingList
from shl.app import create_app
import os


app = create_app(os.getenv('COFIGURATION'))
manager = Manager(app=app)


@manager.shell
def make_shell_context():
    return dict(app=app, User=User, ShoppingList=ShoppingList)


if __name__ == '__main__':
    manager.run()