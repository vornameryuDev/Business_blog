from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from forms.user_forms import UserCreateForm, UserLoginForm
from models.user_model import User
from app import db


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/logout')
def logout():
    logout_user() #세션삭제    
    return redirect(url_for('question.list'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    #post
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter(User.nickname == form.nickname.data).first() #db에서 user 찾기
        print(user.username)
        if not user: #user 없음
            error = "존재하지 않는 ID입니다."
        elif not check_password_hash(user.password, form.password.data): #비밀번호 안맞음
            error = "비밀번호가 틀렸습니다."
        if error is None: #둘다 맞으면
            login_user(user) #session 저장            
            return redirect(url_for('question.list')) #홈으로 이동
        flash(error) #에러송출
    #get
    if current_user.is_authenticated:
        return redirect(url_for('question.list'))
    return render_template('user/login.html', form=form)


@bp.route('/create', methods=["GET", "POST"])
def create():
    form = UserCreateForm()    
    #post
    if request.method == "POST" and form.validate_on_submit():
        #정상입력되면 <-> 안되면 error생성됨(자동)
        user = User.query.filter(
            (User.nickname == form.nickname.data) |
            (User.phone == form.phone.data) |
            (User.email == form.email.data)
            ).first() #입력값 으로 user객체 만들기        
        if not user: #user없으면(db에 없으면)
            user = User(
                username=form.username.data,
                nickname=form.nickname.data,
                password=generate_password_hash(form.password1.data),
                phone=form.phone.data,
                email=form.email.data,
                address=form.address.data,
                created_at=datetime.now()
            )
            db.session.add(user)
            db.session.commit() #db에 저장
            return redirect(url_for('question.list'))
        else: #db에 있으면
            flash("이미 가입되어 있습니다.")
    #get
    if current_user.is_authenticated:
        return redirect(url_for('question.list'))
    return render_template('user/create.html', form=form)
