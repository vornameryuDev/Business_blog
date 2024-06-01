from flask import Blueprint, current_app, redirect, url_for


bp = Blueprint('home', __name__, url_prefix="/")

@bp.route('/')
def home():
    current_app.logger.info("info레벨로 출력")
    return redirect(url_for('notice.list'))