from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class AddTask(FlaskForm):
    description = StringField(
            'Description',
            [DataRequired()]
            )
    project = StringField(
            'Project',
            []
            )
    due = StringField(
            'Due date',
            []
            )
    submit = SubmitField('Submit')
