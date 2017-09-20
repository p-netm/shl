from flask import render_template, session, redirect, url_for, request, flash
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from flask_login import login_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # get user by email
        email = login_form.email.data
        user = User.get_user_by_email(email)
        passcode = login_form.passcode.data
        if user and user.check_password(passcode):
            login_user(user)
            return redirect(url_for('shl.index') or request.args.get('next'))
        else:
            flash('invalid email or password')
    return render_template('login.html', form=login_form)