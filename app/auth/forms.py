from flask_wtf import Form
from wtforms import PasswordField, SubmitField, StringField, ValidationError
from wtforms.validators import DataRequired, Email, length, Regexp, EqualTo, input_required
from ..models import User, Gears


class RegistrationForm(Form):
    """ Used to model the registration form"""
    name = StringField('', validators=[input_required(), DataRequired(), length(1, 64),
                                       Regexp('^[A-Za-z][A-Za-z0-9_ ]*$', 0,
                                              'Name can only contain numbers, space or underscores')])
    user_name = StringField('', validators=[input_required(),
                                            DataRequired(), length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_]*$',
                                                                                  0, 'Name can only contain numbers,'
                                                                                     ' space or underscores')])
    email = StringField('', validators=[input_required(), DataRequired(), Email()])
    passcode = PasswordField('', validators=[input_required(), DataRequired(), EqualTo('C_passcode',
                                                                                       message='Passwords must match')])
    C_passcode = PasswordField('', validators=[input_required(), DataRequired()])
    sign_up = SubmitField('Sign up')


class LoginForm(Form):
    """ used to model the login form"""
    email = StringField('', validators=[DataRequired(), Email(), input_required()])
    passcode = PasswordField('', validators=[DataRequired(), input_required()])
    sign_in = SubmitField('Log in')