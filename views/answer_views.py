
from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import true

from app import db
from forms.answer_form import AnswerCreateForm, AnswerUpdateForm
from models.answer_model import Answer
from models.question_model import Question
from models.comment_model import Comment


bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/comment/<int:answer_id>', methods=["POST"])
@login_required
def comment(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if request.method == 'POST':
        newComment = request.form['answer-comment']
        print(newComment)
        answer_comment = Comment(
            user = current_user,
            answer = answer,
            content = newComment,
            created_at = datetime.now()
        )
        db.session.add(answer_comment)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=answer.question_id))

@bp.route('/vote/<int:answer_id>')
@login_required
def vote(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if answer.user.nickname == current_user.nickname:
        flash("본인의 답변은 추천할 수 없습니다")
    else:
        try:
            answer.voter.append(current_user)            
            db.session.commit()
        except Exception as e:
            print(f"error: {e}")
            db.session.rollback() #commit을 해줬었기 때문에 rollback해줘야 함
    return redirect(f"{url_for('question.detail', question_id=answer.question_id)}#answer_{answer.id}")


@bp.route('/delete/<int:answer_id>')
def delete(answer_id):    
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if current_user.nickname != answer.user.nickname:
        return jsonify(grant=False)
    db.session.delete(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))


@bp.route('/update/<int:answer_id>', methods=["GET", "POST"])
def update(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    form = AnswerUpdateForm(obj=answer) #원래 내용 가져오기
    #post and validate
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(answer)
        db.session.commit() #db저장
        return redirect(f"{url_for('question.detail', question_id=answer.question.id)}#answer_{answer.id}")
    #get
    if current_user.nickname != answer.user.nickname: #권한있는 사람만 url로 접근가능
        return jsonify(grant=False)
    return render_template('answer/update.html', form=form)


@bp.route('/create/<int:question_id>', methods=["POST"])
@login_required
def create(question_id):
    form = AnswerCreateForm()
    question = Question.query.get(question_id)        
    if request.method == "POST" and form.validate_on_submit():
        answer = Answer(
            content = form.content.data,
            user = current_user,
            created_at = datetime.now()
        ) #answer정의
        question.answer_set.append(answer) #답변저장
        db.session.commit() #커밋
        return redirect(f"{url_for('question.detail', question_id=question_id)}#answer_{answer.id}")
    #get접근
    return jsonify(grant=False)
    