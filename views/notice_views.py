from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from forms.notice_form import NoticeCreateForm, NoticeUpdateForm
from models.notice_model import Notice
from models.user_model import User
from app import db


bp = Blueprint('notice', __name__, url_prefix='/notice')


@bp.route('/delete/<int:notice_id>')
@login_required
def delete(notice_id):
    notice = Notice.query.get_or_404(notice_id) #객체검색
    if current_user.username != "유민수":
        return jsonify(grant=False)
    db.session.delete(notice)
    db.session.commit() #db에서 삭제
    return redirect(url_for('notice.list'))


@bp.route('/update/<int:notice_id>', methods=["GET", "POST"])
@login_required
def update(notice_id):
    notice = Notice.query.get_or_404(notice_id) #객체 가져오기
    form = NoticeUpdateForm(obj=notice) #원래거 가져와서 form에 넣기
    if request.method == "POST" and form.validate_on_submit():
        form.populate_obj(notice) #폼에 입력된것 notice에 update
        db.session.commit()
        return redirect(url_for('notice.detail', notice_id=notice_id))
    #get
    if current_user.username != "유민수":
        return jsonify(grant=False)
    return render_template('notice/update.html', form=form)


@bp.route('/detail/<int:notice_id>')
def detail(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    return render_template('notice/detail.html', notice=notice)


@bp.route('/create', methods=["GET", "POST"])
@login_required
def create():
    form = NoticeCreateForm()
    user = current_user
    if request.method=="POST" and form.validate_on_submit():
        notice = Notice(
            user = user,
            subject = form.subject.data,
            content = form.content.data,
            created_at = datetime.now()
        )
        db.session.add(notice)
        db.session.commit()
        return redirect(url_for('notice.list'))
    if current_user.username != "유민수":
        return jsonify(grant=False)
    return render_template('notice/create.html', form=form)


@bp.route('/list')
def list():    
    page = request.args.get('page', type=int, default=1) #페이지 가져오기
    notice_list = Notice.query.order_by(Notice.created_at.desc()) #공지사항 전부 가져오기
    notice_list = notice_list.paginate(page=page, per_page=10) #페이지적용
    return render_template('notice/list.html', notice_list=notice_list)