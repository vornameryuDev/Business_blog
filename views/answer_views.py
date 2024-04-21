from flask import Blueprint, jsonify


bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/list')
def list():
    return jsonify(success=True)