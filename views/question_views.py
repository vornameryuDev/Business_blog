from flask import Blueprint, render_template


bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/')
def list():
    return render_template('questions/list.html')