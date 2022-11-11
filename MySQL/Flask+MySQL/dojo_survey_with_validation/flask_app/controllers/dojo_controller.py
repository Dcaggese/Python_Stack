from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask import render_template, session, request, redirect

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = {}

    Dojo.add_dojos(data)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')