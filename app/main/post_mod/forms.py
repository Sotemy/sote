from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

class NewPostForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    text=TextAreaField('Text', validators=[DataRequired()])