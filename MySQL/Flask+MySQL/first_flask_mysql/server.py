from flask import Flask, render_template, request, redirect
# import the class from friends.py
from friends import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html",friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    #dicitionary used to store the data
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    #calling the Friend classmethod save to insert the data
    Friend.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

