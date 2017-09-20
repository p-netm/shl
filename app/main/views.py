from flask import render_template, session, redirect, url_for
from . import shl
from flask_login import login_required
from ..models import User


# ROUTES
@shl.route('/')
@login_required
def index():
    return render_template('index.html')