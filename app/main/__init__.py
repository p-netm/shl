from flask import Blueprint
from shl.app.main import views, errors, forms

shl = Blueprint('shl', __name__)