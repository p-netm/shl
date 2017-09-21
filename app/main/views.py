from flask import render_template, session, redirect, url_for
from . import shl
from flask_login import login_required
from ..models import User, Basket

basket = Basket()
# ROUTES
@shl.route('/')
@login_required
def index():
    # create list functionality

    return render_template('index.html', lists=basket.view_list())


@shl.route('/add_list')
@login_required
def add_list():
    """ renders a biult list form from which users can fill in their details"""
    # then returns the index page

    return render_template('index.html', list=basket.view_list())


@shl.route('/delete_list')
@login_required
def delete_list():
    """Here we will not use a form but rather a dynamic url that offers a parameter that
    we can use to indentify a list-> like say the name of the list"""

    return render_template('index.html', list=basket.view_list())