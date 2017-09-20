from flask import render_template, session, redirect, url_for
from shl.app.main import shl
# forms

from shl.app.models import User


# ROUTES
@shl.route('/')
def index():
    return render_template('login.html')