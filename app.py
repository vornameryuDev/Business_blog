import os
from flask import Flask, config
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

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
    from models.user_model import User

    #---------- blueprint
    from views import question_views, user_views
    app.register_blueprint(question_views.bp)
    app.register_blueprint(user_views.bp)

    #---------- login support
    login_manager = LoginManager()
    login_manager.init_app(app) #app등록
    login_manager.session_protection = 'strong'

    @login_manager.user_loader #세션저장
    def load_user(user_id):
        return User.get(user_id)

        
    return app