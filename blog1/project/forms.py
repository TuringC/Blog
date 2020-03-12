from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class ArticleInput(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(1, 30)])
    body = TextAreaField('Article', validators=[DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 16)])
    submit = SubmitField()

class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')