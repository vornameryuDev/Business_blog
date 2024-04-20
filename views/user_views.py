from datetime import datetime
import email
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from forms.user_forms import UserCreateForm
from models.user_model import User
from app import db


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
def login():
    return jsonify(success=True)


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
    return render_template('user/create.html', form=form)
