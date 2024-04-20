from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        user = User.query.get(user_id)
        return user
    
    