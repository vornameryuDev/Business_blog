import os
from urllib.parse import urlencode
from flask import Flask, config, redirect, request, url_for
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

import config



#db 전역변수로 설정
db = SQLAlchemy()
migrate = Migrate()
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #https만 지원하는 기능 사용하기 위해

def create_app():
    app = Flask(__name__)
    CORS(app) #보안등록

    #--------- CSRF
    app.secret_key = config.secret_key

    #---------- config    
    app.config.from_object(config)

    #---------- db, mirate init
    db.init_app(app)
    migrate.init_app(app, db)
    from models.answer_model import Answer
    from models.question_model import Question
    from models.notice_model import Notice
    from models.user_model import User

    #---------- blueprint
    from views import user_views, notice_views, question_views, answer_views
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(notice_views.bp)
    app.register_blueprint(user_views.bp)

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