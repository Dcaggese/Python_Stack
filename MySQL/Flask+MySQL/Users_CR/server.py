from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)

#root route redirects to /users
@app.route('/')
def direct_users():
    return redirect('/users')

#brings user to the main page, showing all users
@app.route('/users')
def show_users():
    users = User.get_all()
    return render_template('Read(All).html', users = users)

#brings user to the create user form
@app.route('/create_user')
def show_form():
    return render_template('Create.html')

#submits create form and posts data to server
@app.route('/submit_user', methods=["POST"])
def create_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users')

#shows user data based on id
@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {'id': user_id}
    user = User.get_user(data)
    return render_template('show.html', user = user[0])

#brings user to edit form
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    data = {'id' : user_id}
    user = User.get_user(data)
    return render_template('edit.html', user = user[0])

#takes new user data and posts to server
@app.route('/edit_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'updated_at': 'NOW()'
    }
    User.edit_user(data)
    return redirect('/users')


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {'id': user_id}
    User.delete_user(data)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)