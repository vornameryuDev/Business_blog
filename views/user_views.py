from flask import Blueprint, jsonify


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
def login():
    return jsonify(success=True)

@bp.route('/create')
def create():
    return jsonify(success=True)