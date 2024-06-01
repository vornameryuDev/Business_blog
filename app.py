import os
from urllib.parse import urlencode
from flask import Flask, config, redirect, request, url_for, render_template
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flaskext.markdown import Markdown
import sqlalchemy

import config



#db 전역변수로 설정
db = SQLAlchemy()
migrate = Migrate()
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #https만 지원하는 기능 사용하기 위해

#에러났을때 호출되는 함수: 404나타내기
def page_not_found(e):
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    CORS(app) #보안등록

    #---------- 오류페이지
    app.register_error_handler(404, page_not_found)

    #---------- markdown
    # Markdown(app, extensions=['nl2br', 'fenced_code']) #줄바꿈변환, 코드표시기능

    #--------- CSRF
    # app.secret_key = config.secret_key

    #---------- config    
    # app.config.from_object(config)
    app.config.from_envvar('APP_CONFIG_FILE')

    #---------- db, mirate init
    db.init_app(app)
    migrate.init_app(app, db)
    from models.comment_model import Comment
    from models.answer_model import Answer
    from models.question_model import Question
    from models.notice_model import Notice
    from models.user_model import User

    #---------- blueprint
    from views import user_views, notice_views, question_views, answer_views, comment_views, main_views
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(notice_views.bp)
    app.register_blueprint(user_views.bp)
    app.register_blueprint(main_views.bp)

    #---------- login support
    login_manager = LoginManager()
    login_manager.init_app(app) #app등록
    login_manager.session_protection = 'strong'

    @login_manager.user_loader #세션저장
    def load_user(user_id):
        return User.get(user_id)
    
    @login_manager.unauthorized_handler #로그인 안하고 접근시
    def unauthorized_callback():
        print(request.path)
        print(urlencode(request.args))
        return redirect(url_for('user.login'))    

    #---------- filters
    import filters
    app.jinja_env.filters['datetime'] = filters.datetime_format

        
    return app