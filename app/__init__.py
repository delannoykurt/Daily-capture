from flask import Flask
from .routes import main
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join('app', 'static', 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max par fichier
    app.secret_key = "super_secret_key"  # A changer dans le .env plus tard

    app.register_blueprint(main)

    return app
