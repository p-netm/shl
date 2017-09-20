__author__ = 'Sudo Pnet'
from flask_wtf import Form
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired


class RegistrationForm(Form):

    name = StringField('', validators=[DataRequired()])
    user_name = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired])
    passcode = PasswordField('')
    C_passcode = PasswordField('')
    sign_up = SubmitField('Sign up')


class LoginForm(Form):

    email = StringField('', validators=[DataRequired()])
    passcode = PasswordField('', validators=[DataRequired()])
    sign_in = SubmitField('Log in')

