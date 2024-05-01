import datetime
from flask_login import current_user, login_required
from models.comment_model import Comment
from flask import Blueprint, jsonify, redirect, request, url_for

from models.question_model import Question
from app import db


bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/delete/<int:comment_id>')
def delete(comment_id):
    return jsonify(delete=True)

@bp.route('/update/<int:comment_id>', methods=["POST"])
def update(comment_id):
    comment = Comment.query.get_or_404(comment_id)    
    if request.method == "POST":
        update_comment = request.form['comment']
        print(update_comment)
        comment.content = update_comment
        comment.modified_at = datetime.datetime.now()
        db.session.commit()
        return redirect(url_for('question.detail', question_id=comment.question_id))
    

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
    return redirect(url_for('question.detail', question_id=question_id))
