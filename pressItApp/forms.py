from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CrawlForm(FlaskForm):
    ip_address = StringField('IP Addresss', validators=[DataRequired()])
    ip_range = StringField('Range', validators=[DataRequired()])
    submit = SubmitField('Go!')



