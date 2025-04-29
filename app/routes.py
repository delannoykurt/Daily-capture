from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')

@main.route('/')
def index():
    photos = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', photos=photos)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('main.index'))
    return render_template('upload.html')
