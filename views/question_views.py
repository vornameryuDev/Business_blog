from flask import Blueprint, jsonify, render_template

from forms.user_forms import UserCreateForm, UserLoginForm


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/detail/<int:question_id>')
def detail(question_id):
    return jsonify(success=True)

@bp.route('/create')
def create():
    return jsonify(success=True)

@bp.route('/list')
def list():    
    return render_template('questions/list.html')