from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app import db
from forms.question_form import QuestionCreateForm, QuestionUpdateForm
from forms.user_forms import UserCreateForm, UserLoginForm
from models.question_model import Question
from models.user_model import User


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/update/<int:question_id>', methods=["GET", "POST"])
@login_required
def update(question_id):
    question = Question.query.get_or_404(question_id) #객체 가져오기
    form = QuestionUpdateForm(obj=question) #원래거 가져와서 form에 넣기
    if request.method == "POST" and form.validate_on_submit():
        form.populate_obj(question) #폼에 입력된것 question에 update
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    #get
    if current_user.username != "유민수":
        return jsonify(grant=False)
    return render_template('questions/update.html', form=form)


@bp.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('questions/detail.html', question=question)

@bp.route('/create', methods=["GET", "POST"])
@login_required
def create():
    form = QuestionCreateForm()
    user = current_user
    if request.method=="POST" and form.validate_on_submit():
        question = Question(
            user = user,
            subject = form.subject.data,
            content = form.content.data,
            created_at = datetime.now()
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question.list'))
    if current_user.username != "유민수":
        return jsonify(grant=False)
    return render_template('questions/create.html', form=form)

@bp.route('/list')
def list():
    question_list = Question.query.all()
    return render_template('questions/list.html', question_list=question_list)