from flask_app import app
from flask_app.models.dojo import Dojo 
from flask import render_template, redirect, request

#root route directs to the /dojos page
@app.route('/')
def home_route():
    return redirect('/dojos')

#main page displays the full list of dojos and has the ability to add a new dojo
@app.route('/dojos')
def all_dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

#add a new dojo to database when create button is pressed on /dojo route
@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    data = {'name': request.form['name']}
    Dojo.add_dojo(data)
    return redirect('/dojos')

#dojo show page; displays all ninjas in the dojo
@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {'id':dojo_id}
    return render_template('dojo_show.html', dojo = Dojo.get_dojo_with_ninjas(data))
