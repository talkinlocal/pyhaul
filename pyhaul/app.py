from flask import Flask
from flask_wtf import CsrfProtect

def create_app():
    """
    Build the Flask application.
    :return: the application.
    """
    app = Flask(__name__)

    CsrfProtect(app)

    import settings

    app.config.from_object('settings.Config')
    
    return app
