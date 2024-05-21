from app import db


comment_voter = db.Table(
    'comment_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('comment_id', db.Integer, db.ForeignKey('comment.id', ondelete='CASCADE'), primary_key=True)
)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'))
    answer = db.relationship('Answer', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    modified_at = db.Column(db.DateTime())
    voter = db.relationship('User', secondary=comment_voter, backref=db.backref('comment_voter_set'))