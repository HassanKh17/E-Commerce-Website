from flask_wtf import FlaskForm
from wtforms import FileField, DecimalField, SubmitField
from wtforms import PasswordField, validators, IntegerField
from wtforms import TextAreaField, StringField, SelectField
from wtforms.validators import DataRequired, EqualTo

# User Registration Form


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Product Creation Form


class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[validators.InputRequired(
        message="Price is required"), validators.NumberRange(
            min=1, max=10000,
            message="Price must be between 0 and 1,000,000")])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    category = SelectField(
        'Category', choices=[('bat', 'Bat'), ('helmet', 'Helmet'), (
            'gloves', 'Gloves'), ('bags', 'Bags'),
            ('shoes', 'Shoes')], validators=[DataRequired()])
    submit = SubmitField('Add Product')
