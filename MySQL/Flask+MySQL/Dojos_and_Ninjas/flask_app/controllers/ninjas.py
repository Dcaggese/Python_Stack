from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request, url_for

#renders the add ninja form
@app.route('/new_ninja')
def new_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

#adds ninja to database with a POST route
@app.route('/add_ninja', methods=["POST"])
def add_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/dojos')

