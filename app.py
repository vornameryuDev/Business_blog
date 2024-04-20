from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)

    #---------- config    
    app.config.from_object(config)

    #---------- db, mirate init
    db.init_app(app)
    migrate.init_app(app, db)
    

    #---------- blueprint
    from views import question_views, user_views
    app.register_blueprint(question_views.bp)
    app.register_blueprint(user_views.bp)
        
    return app