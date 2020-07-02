from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo
from wtforms import StringField, PasswordField , validators
from wtforms.fields.html5 import EmailField


class Join_form(FlaskForm):
    user_id = EmailField('user_id', validators=[DataRequired()])
    user_nick = StringField('user_nick', validators=[DataRequired()])
    user_pw = PasswordField('user_pw', validators=[DataRequired(), EqualTo('user_cpw')])
    user_cpw = PasswordField('user_cpw' , validators=[DataRequired()])
