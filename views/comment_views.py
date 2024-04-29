import datetime
from flask_login import current_user, login_required
from models.comment_model import Comment
from flask import Blueprint, jsonify, request

from models.question_model import Question
from app import db


bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:question_id>', methods=['POST'])
@login_required
def create(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method=='POST':
        comment = request.form['comment']        
        comment = Comment(
            user = current_user,
            question = question,
            content = comment,
            created_at = datetime.datetime.now()
        )
        db.session.add(comment)
        db.session.commit()
    return jsonify(success=True)
