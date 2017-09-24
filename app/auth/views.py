from flask import render_template, session, redirect, url_for, request, flash
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User, Gears
from flask_login import login_user, login_required, logout_user, current_user


gear = Gears()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # get user by email -> tricky
        email = login_form.email.data
        user = gear.get_user_by_email(email)
        passcode = login_form.passcode.data
        if user and user.check_password(passcode):
            logging_in_user = user
            login_user(logging_in_user)
            return redirect(url_for('shl.index') or request.args.get('next'))
        else:
            flash('invalid email or password')
    return render_template('login.html', form=login_form)


@auth.route('/log_out')
@login_required
def logout():
    logout_user()  # removes and resets a user session
    flash('GOODBYE')
    return redirect(url_for('shl.index'))


@auth.route('/register', methods=['POST', 'GET'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        email = reg_form.email.data
        user_name = str(reg_form.user_name.data).strip()
        passcode = reg_form.passcode.data
        name = reg_form.name.data
        try:
            gear.add_user(email=email, password=passcode, name=name, user_name=user_name)
        except Exception as error:
            flash('{}'. format(error))
            return render_template('register.html', form=reg_form)
        flash('You have been successfully registered')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=reg_form)