from flask_wtf import Form
from wtforms import PasswordField, SubmitField, StringField, ValidationError
from wtforms.validators import DataRequired, Email, length, Regexp, EqualTo
from ..models import User, Gears

gear = Gears()


class RegistrationForm(Form):
    """ Used to model the registration form"""
    name = StringField('', validators=[DataRequired(), length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_ ]*$',
                                                                             0, 'Name can only contain numbers, '
                                                                                'space or underscores')])
    user_name = StringField('', validators=[DataRequired(),
                                            length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                                  0, 'Name can only contain numbers, '
                                                                     'dots or underscores')])
    email = StringField('', validators=[DataRequired(), Email(), length(1, 64)])
    passcode = PasswordField('', validators=[DataRequired()])
    C_passcode = PasswordField('', validators=[DataRequired(), EqualTo(passcode, 'Password do not match')])
    sign_up = SubmitField('Sign up')

    def validate_email(self, field):
        email = field.data
        """custom validation that checks if a user details are already being used"""
        # if email in user.emails then raise a validation error
        try:
            gear.validate_email(email)
        except Exception:
            raise ValidationError

    def validate_username(self, field):
        """ validates that the username is unique to the system"""
        user_name = field.data
        # if user_name in user.usernames then raise a validationerror
        try:
            gear.validate_user_name(user_name)
        except Exception:
            raise ValidationError


class LoginForm(Form):
    """ used to model the login form"""
    email = StringField('', validators=[DataRequired(), Email()])
    passcode = PasswordField('', validators=[DataRequired()])
    sign_in = SubmitField('Log in')

