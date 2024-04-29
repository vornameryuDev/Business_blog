from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from forms.answer_form import AnswerCreateForm
from forms.question_form import QuestionCreateForm, QuestionUpdateForm
from models.question_model import Question
from app import db


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/vote/<int:question_id>')
@login_required
def vote(question_id):
    question = Question.query.get_or_404(question_id)
    if question.user.nickname == current_user.nickname:
        flash('본인의 글은 추천하지 못합니다')
    else:
        question.voter.append(current_user) #추천정보 db 저장
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))


@bp.route('/delete/<int:question_id>')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id) #객체검색
    if current_user.nickname == question.user.nickname:
        db.session.delete(question)
        db.session.commit() #db에서 삭제
        return redirect(url_for('question.list'))
    else:
        return jsonify(grant=False)


@bp.route('/update/<int:question_id>', methods=["GET", "POST"])
@login_required
def update(question_id):
    question = Question.query.get_or_404(question_id) #객체 가져오기
    form = QuestionUpdateForm(obj=question) #원래거 가져와서 form에 넣기
    if request.method == "POST" and form.validate_on_submit():
        form.populate_obj(question) #폼에 입력된것 notice에 update
        question.modified_at = datetime.now()
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    #get
    if current_user.nickname != question.user.nickname:
        return jsonify(grant=False)
    return render_template('question/update.html', form=form)


@bp.route('/detail/<int:question_id>')
@login_required
def detail(question_id):
    form = AnswerCreateForm()
    question = Question.query.get_or_404(question_id)
    answer_list = question.answer_set
    return render_template('question/detail.html', question=question, form=form, answer_list=answer_list)


@bp.route('/create', methods=["GET", "POST"])
@login_required
def create():
    form = QuestionCreateForm()    
    if request.method=="POST" and form.validate_on_submit():
        question = Question(
            user = current_user,
            subject = form.subject.data,
            content = form.content.data,
            created_at = datetime.now()
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question.list'))    
    return render_template('question/create.html', form=form)


@bp.route('/list')
def list():
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.created_at.desc())    
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/list.html', question_list=question_list)