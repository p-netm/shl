from flask_script import Manager, Shell
from app.models import User, ShoppingList
from app import create_app
import os


app = create_app(os.environ.get('CONFIGURATION'))
manager = Manager(app=app)



if __name__ == '__main__':
    app.run()