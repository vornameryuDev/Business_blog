from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from app import db
from forms.question_form import QuestionCreateForm
from forms.user_forms import UserCreateForm, UserLoginForm
from models.question_model import Question
from models.user_model import User


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('questions/detail.html', question=question)

@bp.route('/create', methods=["GET", "POST"])
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
    else:
        flash('안된다')
    return render_template('questions/create.html', form=form)

@bp.route('/list')
def list():
    question_list = Question.query.all()
    return render_template('questions/list.html', question_list=question_list)