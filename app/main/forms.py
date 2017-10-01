from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField, BooleanField
from wtforms.validators import DataRequired, input_required


class AddListForm(FlaskForm):
    """ Used to model the registration form"""
    name = StringField('', validators=[input_required(), DataRequired()])
    public = BooleanField('Make me public')
    add = SubmitField('add list')


class ModifyForm(FlaskForm):
    """ Used to model the registration form"""
    name = StringField('', validators=[input_required(), DataRequired()])
    old_name = StringField('', validators=[input_required(), DataRequired()])
    public = BooleanField('Make me public')
    add = SubmitField('modify_list')


class AddItemForm(FlaskForm):
    """ folllows an almost similar layout as add list form. it will be used to add items to list"""
    list_name = StringField('', validators=[input_required(), DataRequired()])
    name = StringField('', validators=[input_required(), DataRequired()])
    quantity = StringField('', validators=[input_required(), DataRequired()])
    price = FloatField('', validators=[input_required(), DataRequired()])
    description = StringField('', validators=[input_required(), DataRequired()])
    add = SubmitField('add_item')


class ModifyItemForm(FlaskForm):
    list_name = StringField('', validators=[input_required(), DataRequired()])
    old_name = StringField('', validators=[input_required(), DataRequired()])
    old_quantity = StringField('', validators=[input_required(), DataRequired()])
    old_price = FloatField('', validators=[input_required(), DataRequired()])
    old_description = StringField('', validators=[input_required(), DataRequired()])
    name = StringField('', validators=[input_required(), DataRequired()])
    quantity = StringField('', validators=[input_required(), DataRequired()])
    price = FloatField('', validators=[input_required(), DataRequired()])
    description = StringField('', validators=[input_required(), DataRequired()])
    add = SubmitField('modify_item')