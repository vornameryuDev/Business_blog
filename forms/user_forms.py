import datetime
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserLoginForm(FlaskForm):
    nickname = StringField('ID', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    nickname = StringField('로그인ID', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    phone = StringField('핸드폰 번호', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    address = StringField('주소', validators=[DataRequired()])
