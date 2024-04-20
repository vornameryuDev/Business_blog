from flask import Blueprint, render_template


bp = Blueprint('home', __name__, '/')

@bp.route('/')
def test():
    return render_template('test.html')