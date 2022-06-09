from tkinter import image_names
from flask import Blueprint, Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
    """
    Create Flask App
    """
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'aR"v[-Um>?2Rp1n(QV@@U(6dqN713Y'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app