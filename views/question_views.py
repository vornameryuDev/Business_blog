from flask import Blueprint, jsonify


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list')
def list():
    return jsonify(success=True)