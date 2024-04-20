from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    #---------- blueprint
    from views import question_view
    app.register_blueprint(question_view.bp)
        
    return app