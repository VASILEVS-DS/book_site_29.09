from reader import app
from reader.models import Book
from flask import render_template, send_from_directory


@app.route('/')
def index():
    films = Book.query.all()
    return render_template('index.html', films=films)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)