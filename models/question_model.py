from sqlalchemy import ForeignKey
from app import db


question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    modified_at = db.Column(db.DateTime(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('question_set'))
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))
