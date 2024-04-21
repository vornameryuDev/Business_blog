from datetime import datetime
from flask import Blueprint, jsonify, redirect, request, url_for
from flask_login import current_user, login_required

from app import db
from forms.answer_form import AnswerCreateForm
from models.answer_model import Answer
from models.question_model import Question


bp = Blueprint('answer', __name__, url_prefix='/answer')


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
        return redirect(url_for('question.detail', question_id=question_id))
    #get접근
    return jsonify(grant=False)
    