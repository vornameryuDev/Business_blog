from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class AnswerCreateForm(FlaskForm):
    content = TextAreaField("답변내용", validators=[DataRequired()])