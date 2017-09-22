from flask_wtf import Form
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, input_required


class AddListForm(Form):
    """ Used to model the registration form"""
    name = StringField('', validators=[input_required(), DataRequired()])
    add = SubmitField('add_list')