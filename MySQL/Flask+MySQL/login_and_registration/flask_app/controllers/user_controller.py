from flask_app import app
from flask_app.models.user_model import User
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def loginPage():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    hash = bcrypt.generate_password_hash(request.form['password'])

    if not User.validate_user(request.form):
        return redirect('/')

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hash,
    }
    User.create_user(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():

    if not User.validate_login(request.form):
        return redirect('/')

    found_user =  User.get_email(request.form)
    session['uid'] = found_user.id
    session['first_name'] = found_user.first_name

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not 'uid' in session:
        return redirect('/')
    
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')