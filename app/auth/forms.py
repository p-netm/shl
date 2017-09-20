from flask_wtf import Form
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email


class RegistrationForm(Form):
    """ Used to model the registation form"""
    name = StringField('', validators=[DataRequired()])
    user_name = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired(), Email()])
    passcode = PasswordField('')
    C_passcode = PasswordField('')
    sign_up = SubmitField('Sign up')


class LoginForm(Form):
    """ used to model the login form"""
    email = StringField('', validators=[DataRequired(), Email()])
    passcode = PasswordField('', validators=[DataRequired()])
    sign_in = SubmitField('Log in')

