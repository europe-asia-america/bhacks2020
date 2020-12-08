from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length

class TaskFeedbackForm(FlaskForm):
    hidden_id = HiddenField('ID')
    skip = SubmitField('Skip')
    progress = SubmitField('Progress')
    done = SubmitField('Done')
    delete = SubmitField('Delete')
