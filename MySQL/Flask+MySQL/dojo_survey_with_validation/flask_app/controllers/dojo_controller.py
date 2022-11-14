from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask import render_template, session, request, redirect

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['language']
        }

    Dojo.add_dojos(data)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')