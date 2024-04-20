from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def test():
        return render_template('test.html')
    
    return app