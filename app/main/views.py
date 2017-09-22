from flask import render_template, session, redirect, url_for
from . import shl
from flask_login import login_required
from ..models import User, Basket
from .forms import AddListForm

basket = Basket()


# ROUTES
@shl.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # create list functionality
    add_list_form = AddListForm()
    if add_list_form.validate_on_submit():
        name = add_list_form.name.data
        basket.create_list(name)
        lists = basket.view_list()
        return render_template('index.html', lists=lists, lists_len=len(lists), form=add_list_form)
    lists = basket.view_list()  # lists has a list of list objects
    return render_template('index.html', lists=lists, lists_len=len(lists), form=add_list_form)


@shl.route('/delete_list/<name>')
@login_required
def delete_list(name):
    """Here we will not use a form but rather a dynamic url that offers a parameter that
    we can use to identify a list-> like say the name of the list"""
    basket.delete_list(name)
    return url_for('shl.index')


@shl.route('/contact')
def contact():
    """display contact details for shoppinglist co."""
    return render_template('contact.html')


@shl.route('/about')
def about():
    """display about shopping list with links to help material and documentation"""
    return render_template('about.html')


@shl.route('/list/<name>')
def view_items(name):
    """ Returns the single shopping list view"""
    return render_template('each_list.html', shl=basket.view_item(name))

@shl.route('/list/<name>')
def edit_list():
    """ takes in a name list, retrives the list and then passe it on to a f"""
    return '<br>'