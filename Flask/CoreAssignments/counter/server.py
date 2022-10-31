
from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key ='gh1232jh^%#nsch78yt2811cxn#$bhashd19084578ads!^&a'

@app.route('/')
def welcome():
    counter = 1

    if 'counter' in session:
        counter += 1
    
    session['counter'] = counter

    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect()


if __name__=="__main__":
    app.run(debug=True)