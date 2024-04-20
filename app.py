from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    #---------- blueprint
    from views import home_view
    app.register_blueprint(home_view.bp)
    
    
    return app