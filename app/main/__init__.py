from flask import Blueprint


shl = Blueprint('shl', __name__)


from . import views, errors