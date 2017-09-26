from flask import render_template, session, redirect, url_for, flash
from . import shl
from flask_login import login_required
from ..models import User, Basket
from .forms import AddListForm, ModifyForm, AddItemForm, ModifyItemForm

basket = Basket()


# ROUTES
@shl.route('/', methods=['GET', 'POST'])
def index():
    # create list functionality
    add_list_form = AddListForm()
    modify_form = ModifyForm()

    if modify_form.validate_on_submit():
        name = modify_form.name.data
        old_name = modify_form.old_name.data
        try:
            basket.modify_list(name=old_name, new_name=name)
        except ValueError as error:
            flash(str(error), 'danger')
        return redirect(url_for('shl.index'))

    if add_list_form.validate_on_submit():
        name = add_list_form.name.data
        try:
            basket.create_list(name, author=session['user_id'])
        except ValueError as error:
            flash(str(error), 'danger')
            return redirect(url_for('shl.index'))
        return redirect(url_for('shl.index'))


    try:
        lists = []
        lists = basket.view_list()  # lists has a list of list objects
    except Exception as e:
        flash(str(e), 'danger')
    if not len(lists) and session.get('user_id'):
        flash("Seems like you currently have no lists, click on the add_list link to get started", 'info')
    return render_template('index.html', lists=lists, lists_len=len(lists), form=add_list_form, modif_form=modify_form)


@shl.route('/delete_list/<name>')
@login_required
def delete_list(name):
    """Here we will not use a form but rather a dynamic url that offers a parameter that
    we can use to identify a list-> like say the name of the list"""
    try:
        basket.delete_list(name)
    except ValueError as error:
        flash(str(error), 'danger')
    return redirect(url_for('shl.index'))


@shl.route('/contact')
def contact():
    """display contact details for shoppinglist co."""
    return render_template('info/contact.html')


@shl.route('/about')
def about():
    """display about shopping list with links to help material and documentation"""
    return render_template('info/about.html')


@shl.route('/list/<list_name>', methods=['GET', 'POST'])
@login_required
def view_items(list_name):
    """ Returns the single shopping list view"""
    form = AddItemForm()
    mod_form = ModifyItemForm()
    
    if mod_form.validate_on_submit():
        # we extract both the old and the new values, compare and if not same change them
        item_name = mod_form.name.data
        old_item_name = mod_form.old_name.data
        quantity = mod_form.quantity.data
        price = mod_form.price.data
        description = mod_form.description.data
        try:
            basket.modify_item(item_name=old_item_name, list_name=list_name, name=item_name, price=price,
                           description=description, quantity=quantity)
        except Exception as error:
            flash(str(error), 'danger')
            return redirect(url_for('shl.view_items', list_name=list_name))
        flash('item modified successfully', 'success')
        return redirect(url_for('shl.view_items', list_name=list_name))
    try:
        shl_list = basket.view_item(list_name=list_name)
    except Exception as e:
        flash(str(e), 'danger')
        return redirect(url_for('shl.view_items', list_name=list_name))
    try:
        lists = basket.view_list()
    except Exception as e:
        flash(str(e), 'danger')

    if form.validate_on_submit():
        # we add item with details from form
        item_name = form.name.data
        quantity = form.quantity.data
        price = form.price.data
        description = form.description.data
        try:
            basket.add_item(list_name, item_name, quantity, price, description, author=session['user_id'])
        except ValueError as error:
            flash(str(error), 'danger')
            return redirect(url_for('shl.view_items', list_name=list_name))
        flash('item added successfully', 'success')
        return redirect(url_for('shl.view_items', list_name=list_name))

    return render_template('each_list.html', shl_list=shl_list, lists=lists,
                           form=form, mod_form=mod_form, name=list_name)




@shl.route('/list/<list_name>')
@login_required
def edit_list():
    """ takes in a name list, retrieves the list and then passes it on to a form inside a popover"""
    return redirect(url_for('shl.view_items'))


@shl.route('/list/<list_name>/<item_name>')
@login_required
def delete_item(list_name, item_name):
    """ Extract the two names: list name and item_name
    delete the specified item"""
    try:
        basket.delete_item(item_name=item_name, list_name=list_name)
    except ValueError as error:
        flash(str(error), 'danger')
    return redirect(url_for('shl.view_items', list_name=list_name))

@shl.route('/terms')
def terms():
    return render_template('info/terms.html')