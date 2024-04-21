from app import db
from models.user_model import User


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('answer_set'))
    question = db.relationship('Question', backref=db.backref('answer_set', order_by='Answer.created_at.desc()'))
