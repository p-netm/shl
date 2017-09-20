from flask import Blueprint
from shl.app.auth import views, forms

auth = Blueprint('auth', __name__)
